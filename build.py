"""Build the GitHub version of the pages.

The files in src/ are the sources of the published Claude artifacts. Those have
no <!doctype>, <head> or <body>, because the artifact host adds them. This
script wraps each one into a complete page at the repo root, points the links
between pages at the local files, and adds a link back to the landing page.

Run it after changing anything in src/:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ["index.html", "hanna-island.html", "carbon-mui.html"]
ARTIFACT_LINKS = {
    "https://claude.ai/artifact/RtgWNjPbuZ2s5EMfsuiGgu": "hanna-island.html",
    "https://claude.ai/artifact/F4yvWjkK6TrBRzygYGq7LM": "carbon-mui.html",
}

# The same small reset the artifact host puts in front of every page.
HEAD_START = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    "<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}"
    "body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}"
    "img{max-width:100%}[hidden]{display:none!important}"
    ".home-link{font-size:.9rem;font-weight:600;color:var(--ink);text-decoration:none;margin-right:8px}"
    ".home-link:hover{text-decoration:underline}</style>\n"
)

HOME_LINK = '<a class="home-link" href="index.html">← All pages</a>\n    '


def build(name: str) -> None:
    src = (ROOT / "src" / name).read_text(encoding="utf8")
    for url, local in ARTIFACT_LINKS.items():
        src = src.replace(f'href="{url}" target="_blank" rel="noopener"', f'href="{local}"')
        src = src.replace(f'href="{url}"', f'href="{local}"')
    if name != "index.html":
        src = src.replace('<div class="ds-inner">\n    ', '<div class="ds-inner">\n    ' + HOME_LINK, 1)
    split = src.index("\n<div")
    head, body = src[:split], src[split:]
    page = HEAD_START + head.strip() + "\n</head>\n<body>" + body.rstrip() + "\n</body>\n</html>\n"
    (ROOT / name).write_text(page, encoding="utf8")
    print(f"built {name}")


if __name__ == "__main__":
    for page in PAGES:
        build(page)
