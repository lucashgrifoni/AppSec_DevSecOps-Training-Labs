"""Check the static catalog site and repository documentation without network calls."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "gitpage"


class SiteMarkup(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.targets: list[str] = []
        self.controls: list[str] = []
        self.html_lang = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.html_lang = bool(attributes.get("lang"))
        identifier = attributes.get("id")
        if identifier:
            if identifier in self.ids:
                raise ValueError(f"Duplicate HTML id: {identifier}")
            self.ids.add(identifier)
        for attribute in ("src", "href"):
            if attributes.get(attribute):
                self.targets.append(attributes[attribute])
        self.controls.extend((attributes.get("aria-controls") or "").split())


def local_target(source: Path, value: str, ids: set[str] | None = None) -> bool:
    target = urlsplit(value)
    if target.scheme or target.netloc:
        return False
    if not target.path:
        if target.fragment and ids is not None and unquote(target.fragment) not in ids:
            raise ValueError(f"Missing HTML anchor in {source.name}: {target.fragment}")
        return bool(target.fragment)
    resolved = (source.parent / unquote(target.path)).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError(f"Local link escapes repository: {source.relative_to(ROOT)}")
    if not resolved.exists():
        raise ValueError(f"Missing local target in {source.relative_to(ROOT)}: {target.path}")
    return True


def main() -> None:
    required = ["index.html", "css/main.css", "js/main.js", "images/favicon.svg"]
    for relative in required:
        if not (SITE / relative).is_file():
            raise ValueError(f"Required static asset missing: {relative}")
    markup = SiteMarkup()
    html = (SITE / "index.html").read_text(encoding="utf-8-sig")
    if not re.search(r"<!doctype\s+html\s*>", html, re.IGNORECASE):
        raise ValueError("Missing HTML5 doctype")
    markup.feed(html)
    markup.close()
    if not markup.html_lang or not markup.ids:
        raise ValueError("Site must have a document language and nonempty section IDs")
    for identifier in markup.controls:
        if identifier not in markup.ids:
            raise ValueError(f"aria-controls points to absent id: {identifier}")
    links = sum(local_target(SITE / "index.html", target, markup.ids) for target in markup.targets)
    javascript = (SITE / "js/main.js").read_text(encoding="utf-8-sig")
    dom_targets = re.findall(r'getElementById\(["\']([^"\']+)["\']\)', javascript)
    if not dom_targets:
        raise ValueError("No DOM bindings were checked")
    for identifier in dom_targets:
        if identifier not in markup.ids:
            raise ValueError(f"JavaScript refers to absent DOM id: {identifier}")
    css = (SITE / "css/main.css").read_text(encoding="utf-8-sig")
    for match in re.finditer(r"url\(\s*[\"\']?([^\)\"\']+)[\"\']?\s*\)", css):
        links += local_target(SITE / "css/main.css", match.group(1).strip())
    ElementTree.parse(SITE / "images/favicon.svg")
    documents = [ROOT / "README.md", SITE / "README.md", ROOT / "docs/openwiki.md"]
    for document in documents:
        text = document.read_text(encoding="utf-8-sig")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            links += local_target(document, target)
    print(json.dumps({"status": "PASS", "html_ids": len(markup.ids),
                      "dom_bindings": len(dom_targets), "local_links_and_assets": links,
                      "required_assets": len(required), "documents": len(documents),
                      "external_http_requests": 0}))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, ElementTree.ParseError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1) from error
