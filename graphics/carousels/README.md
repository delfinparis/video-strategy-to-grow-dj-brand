# Rendered carousel slides

Generated output. Do not hand-edit anything in here.

Every folder matches a file in [`scripts/carousels/`](../../scripts/carousels/) and is rebuilt by:

```bash
python3 scripts/render_carousel.py scripts/carousels/<name>.md
python3 scripts/render_carousel.py "scripts/carousels/*.md"    # rebuild everything
```

To change a slide, edit the markdown and re-run. The markdown is the source of truth.

## What's in each folder

| File | Use |
|---|---|
| `01.png` ... `NN.png` | The slides at 1080x1350 (4:5). Upload to Instagram and LinkedIn in filename order |
| `preview.html` | Contact sheet. Open in a browser to read the whole deck before posting |
| `<slug>.pdf` | Only when built with `--pdf`. The LinkedIn document carousel |

## Posting notes

- **Instagram:** upload the PNGs as a carousel post, in order. 1080x1350 is the native 4:5 crop, so nothing gets cut.
- **LinkedIn:** either upload the PNGs as an image carousel, or upload the `--pdf` file as a document post. Documents out-engage images on LinkedIn, so prefer the PDF when there is one.
- **Facebook:** same PNGs, same order.

Format spec and the rules behind the design: [`docs/series/carousel-standard.md`](../../docs/series/carousel-standard.md).
Color tokens are shared with the video graphics in [`../insider-news-merger-take/README.md`](../insider-news-merger-take/README.md).
