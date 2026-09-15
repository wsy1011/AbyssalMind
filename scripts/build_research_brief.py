"""Build the first Research Brief from Markdown and existing Zotero PDF Figure results."""
import hashlib
import json
import shutil
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'phased-fuel-transitions-for-asia-europe-corridor'
CACHE = Path.home() / 'Zotero/zotero-figure/results/1/NKT67I83'
OUT = ROOT / 'assets/articles/phased-fuel-transitions'
IDS = ['3-334kpd', '4-1gxi2q4', '5-pbxc2m', '6-gs9aig', '7-lkrio']
manifest = json.loads((CACHE / 'manifest.json').read_text(encoding='utf-8'))
records = {r['id']: r for r in manifest['results']}
provenance = []
for number, item_id in enumerate(IDS, 1):
    record = records[item_id]
    source = CACHE / record['imageFile']
    target = OUT / f'figure-{number}.png'
    shutil.copyfile(source, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    assert digest == hashlib.sha256(source.read_bytes()).hexdigest()
    provenance.append({
        'figure': number, 'pdfPage': record['pageIndex'] + 1,
        'journalPage': 1256 + record['pageIndex'], 'pluginResultId': item_id,
        'file': target.relative_to(ROOT).as_posix(), 'sha256': digest,
        'extraction': 'Existing Zotero PDF Figure cache, copied without image edits',
        'pluginCacheUpdatedAt': manifest['updatedAt'],
        'rect': record['rect'], 'sourceFingerprint': manifest['imageCache'][item_id]['sourceFingerprint'],
        'doi': '10.1038/s41893-026-01878-9',
        'license': 'https://creativecommons.org/licenses/by-nc-nd/4.0/',
    })
(OUT / 'provenance.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

source_md = ROOT / f'content/articles/{SLUG}.md'
soup = BeautifulSoup(markdown.markdown(source_md.read_text(encoding='utf-8-sig'), extensions=['tables']), 'html.parser')
for number, img in enumerate(soup.find_all('img'), 1):
    img['src'] = '../assets/articles/phased-fuel-transitions/' + Path(img['src']).name
    img['loading'] = 'lazy'
    parent = img.parent
    fig = soup.new_tag('figure', id=f'figure-{number}')
    link = soup.new_tag('a', href=img['src'], target='_blank')
    link['aria-label'] = f'打开论文图 {number} 完整图片'
    link.append(img.extract())
    fig.append(link)
    caption = soup.new_tag('figcaption')
    caption.string = f'原论文图 {number} · Li et al. (2026), Nature Sustainability · CC BY-NC-ND 4.0。点击图片查看完整尺寸。'
    fig.append(caption)
    parent.replace_with(fig)
toc = []
for i, heading in enumerate(soup.find_all('h2'), 1):
    heading['id'] = f'section-{i}'
    toc.append(f'<a href="#section-{i}">{heading.get_text()}</a>')
html = '''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>亚欧绿色航运走廊的燃料转型 | Abyssal Mind</title>
<link rel="stylesheet" href="../styles.css"><link rel="stylesheet" href="../brief.css"><link rel="stylesheet" href="../article-shell.css"></head><body>
<header class="site-header"><a class="brand" href="../index.html"><img src="../assets/brand/abyssal-mind-mark.png" alt="Abyssal Mind"><span>Abyssal Mind</span></a><nav><a href="../index.html#research">Research</a><a href="../index.html#industry">Industry</a><a href="../index.html#topics">Topics</a><a href="../index.html#resources">Resources</a><a href="../about.html">About</a></nav><button class="search" aria-label="搜索">⌕</button></header>
<div class="layout"><aside><p>RESEARCH BRIEF</p>''' + ''.join(toc) + '''</aside>
<main><div class="eyebrow">航运 / 能源 / 政策 · 研究解读草稿</div>''' + str(soup) + '''</main></div>
<footer><span>© 2026 Abyssal Mind</span><a href="../about.html">About Abyssal Mind</a><span>Research · Industry · Deep Insight</span></footer></body></html>'''
page = ROOT / f'articles/{SLUG}.html'
page.parent.mkdir(exist_ok=True)
page.write_text(html, encoding='utf-8')
assert len(soup.find_all('figure')) == 5
for img in soup.find_all('img'):
    assert (page.parent / img['src']).exists()
print(f'Built {page.name}: 5 plugin images, hashes and local links verified.')
