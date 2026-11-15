/**
 * Control panel heartbeat. Paste this whole file into any Apps Script project
 * you want the panel to watch, then wrap the function its trigger calls:
 *
 *   function sendDailyBillingReminders() {
 *     return panelWatch_('hc-billing-reminders', function () {
 *       ...the code that was already here...
 *     });
 *   }
 *
 * The id must match an "id" under appsScripts in panel.config.json.
 * Set the two values once: Project Settings > Script properties >
 *   PANEL_HUB_URL = the hub web app URL
 *   PANEL_HUB_KEY = the check-in key (hb_..., from hub/Secrets.gs)
 *
 * It can never break your script: every network call is wrapped, and the
 * original error is always re-thrown so your existing failure emails still fire.
 * Successes are reported at most once an hour; failures are reported every time.
 */
function panelWatch_(id, fn) {
  try {
    var result = fn();
    panelPing_(id, true, typeof result === 'string' ? result : '');
    return result;
  } catch (err) {
    panelPing_(id, false, (err && err.message) || String(err));
    throw err;
  }
}

function panelPing_(id, ok, message) {
  try {
    var p = PropertiesService.getScriptProperties();
    var url = p.getProperty('PANEL_HUB_URL'), key = p.getProperty('PANEL_HUB_KEY');
    if (!url || !key) return;
    var cache = CacheService.getScriptCache();
    if (ok && cache.get('panel_' + id)) return;
    UrlFetchApp.fetch(url, {
      method: 'post', contentType: 'application/json', muteHttpExceptions: true,
      payload: JSON.stringify({ key: key, type: 'heartbeat', id: id, ok: ok, message: String(message || '').slice(0, 300) })
    });
    if (ok) cache.put('panel_' + id, '1', 3300);
  } catch (e) { /* the panel is never allowed to break the real job */ }
}
