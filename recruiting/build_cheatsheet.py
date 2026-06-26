import base64, os
HERE = os.path.expanduser("~/GitHub Projects/video-strategy-to-grow-dj-brand/recruiting")
logo = base64.b64encode(open(os.path.join(HERE,"kale_white_logo.png"),"rb").read()).decode()

html = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<style>
  @page { size: Letter; margin: 0; }
  * { box-sizing: border-box; margin:0; padding:0; }
  body { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; color:#262b28; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .page { width:8.5in; height:11in; padding:0; position:relative; }
  /* Header band */
  .hdr { background:#303328; color:#fff; padding:26px 40px 22px; }
  .hdr .logo { height:30px; margin-bottom:14px; }
  .hdr h1 { font-size:30px; line-height:1.05; letter-spacing:-0.4px; }
  .hdr .kicker { color:#f46942; font-weight:700; font-size:13px; letter-spacing:1.2px; text-transform:uppercase; margin-bottom:8px; }
  .hdr .sub { color:#dfe1da; font-size:13.5px; margin-top:10px; max-width:6.6in; line-height:1.45; }
  /* Body */
  .body { padding:20px 40px 0; }
  .sec { margin-bottom:13px; }
  .sec h2 { font-size:15px; color:#002f66; display:flex; align-items:baseline; gap:9px; margin-bottom:4px; }
  .num { display:inline-flex; align-items:center; justify-content:center; min-width:21px; height:21px; background:#f46942; color:#fff; border-radius:50%; font-size:12.5px; font-weight:800; flex:none; transform:translateY(2px); }
  .sec .note { font-size:11.5px; color:#5b6159; font-style:italic; margin:0 0 5px 30px; }
  ul { list-style:none; margin:2px 0 0 30px; }
  li { font-size:12px; line-height:1.5; padding-left:15px; position:relative; margin-bottom:2px; }
  li:before { content:""; position:absolute; left:0; top:7px; width:6px; height:6px; background:#bec1b6; border-radius:50%; }
  b, strong { color:#303328; }
  .pill { margin:6px 0 0 30px; background:#f5f5f5; border-left:3px solid #f46942; padding:7px 12px; font-size:11.5px; font-weight:600; color:#303328; border-radius:3px; }
  /* Two-col share */
  .cols { display:flex; gap:16px; margin:4px 0 0 30px; }
  .col { flex:1; background:#f5f5f5; border-radius:7px; padding:11px 14px; }
  .col h3 { font-size:12.5px; color:#002f66; margin-bottom:5px; }
  .col ol { margin-left:16px; }
  .col li { padding-left:4px; font-size:11px; line-height:1.45; }
  .col li:before { display:none; }
  .col ol { list-style:decimal; }
  /* CTA */
  .cta { margin:14px 40px 0; background:#f46942; color:#fff; border-radius:9px; padding:15px 22px; display:flex; align-items:center; justify-content:space-between; }
  .cta .l { font-size:14px; font-weight:600; }
  .cta .l span { display:block; font-size:11.5px; font-weight:400; opacity:.92; margin-top:3px; }
  .cta .ph { font-size:25px; font-weight:800; letter-spacing:0.5px; white-space:nowrap; }
</style></head>
<body><div class="page">
  <div class="hdr">
    <img class="logo" src="data:image/png;base64,{logo}">
    <div class="kicker">The Locker Room TRACK+</div>
    <h1>Record Your Win &mdash; Agent Cheat Sheet</h1>
    <div class="sub">You record a quick, raw clip. D.J. edits it into a polished video you can post to attract clients. That's the whole deal &mdash; about 5 minutes.</div>
  </div>
  <div class="body">

    <div class="sec">
      <h2><span class="num">1</span> Turn on highest quality FIRST</h2>
      <div class="note">The most important step. Film it low-res and it can't be fixed later.</div>
      <ul>
        <li><b>iPhone:</b> Settings &rarr; <b>Camera</b> &rarr; <b>Record Video</b> &rarr; choose <b>4K at 60 fps</b> (or 4K at 30).</li>
        <li><b>Android:</b> <b>Camera</b> app &rarr; <b>Settings</b> (gear) &rarr; <b>Video resolution</b> &rarr; set to the <b>highest</b> option (<b>4K / UHD</b>, or <b>FHD 1080p 60fps</b>). Set the front camera too.</li>
      </ul>
    </div>

    <div class="sec">
      <h2><span class="num">2</span> Set up your phone (30 seconds)</h2>
      <ul>
        <li><b>Go vertical.</b> Hold the phone up and down, not sideways.</li>
        <li><b>Eye level.</b> Prop it on a cup, laptop, or shelf so the camera is at eye height &mdash; not looking up your nose.</li>
        <li><b>Face a window or lamp.</b> Light in front of you, never behind you.</li>
        <li><b>Quiet room.</b> No TV, no music, no hallway noise. And <b>wipe the lens.</b></li>
      </ul>
    </div>

    <div class="sec">
      <h2><span class="num">3</span> Hit record and answer these (pick 2&ndash;3)</h2>
      <div class="note">Just talk like you're telling a friend. No script needed.</div>
      <ul>
        <li>What's working for you right now since joining TRACK+?</li>
        <li>What's one win or deal you're proud of lately?</li>
        <li>What's a habit or tip that's making you a better agent?</li>
        <li>How do you feel about your business today versus six months ago?</li>
      </ul>
      <div class="pill">Keep it under 60 seconds. One take is perfect. Mess-ups are fine &mdash; D.J. edits those out.</div>
    </div>

    <div class="sec">
      <h2><span class="num">4</span> Send it to D.J. &mdash; use a LINK (don't text the raw file)</h2>
      <div class="note">Texting the video shrinks the quality and wastes that 4K. A link keeps the original.</div>
      <div class="cols">
        <div class="col">
          <h3>iPhone &middot; Photos app</h3>
          <ol>
            <li>Open <b>Photos</b>, find your video.</li>
            <li>Tap the <b>Share</b> button (square with arrow &uarr;).</li>
            <li>Tap <b>&ldquo;Copy iCloud Link.&rdquo;</b> Wait a few seconds.</li>
            <li>Paste it in a text to D.J.</li>
          </ol>
        </div>
        <div class="col">
          <h3>Android &middot; Google Photos</h3>
          <ol>
            <li>Open <b>Google Photos</b>, tap your video.</li>
            <li>Tap <b>Share</b>.</li>
            <li>Tap <b>&ldquo;Create link.&rdquo;</b></li>
            <li>Tap <b>Copy</b>, paste it in a text to D.J.</li>
          </ol>
        </div>
      </div>
    </div>

  </div>
  <div class="cta">
    <div class="l">Text the link to D.J.<span>That's it. He'll turn it into something that makes you look like a star.</span></div>
    <div class="ph">(773) 354-6000</div>
  </div>
</div></body></html>"""

html = html.replace("{logo}", logo)
out = os.path.join(HERE, "Locker-Room-Record-Your-Win-Cheat-Sheet.html")
open(out,"w").write(html)
print("wrote", out)
