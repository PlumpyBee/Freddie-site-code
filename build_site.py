"""Self-hosted static site for freddieg.co.uk (GitHub Pages).
Run after build_cw.py:  python3 build_site.py  -> writes ./site
Each route gets its own HTML file (title, description, social tags) plus a plain readable
copy of the page for search engines and no-JS visitors; dist/na.js then draws the real site."""
import json, os, shutil, hashlib, html
DOMAIN = 'freddieg.co.uk'
ROOT = 'site'
CONTACT = json.load(open('site_contact.json'))  # mail + profile links, same as on the live site
PAGES = {
 '/': ('Freddie Grzybowski | UX/UI Designer', 'Portfolio of Freddie Grzybowski, a creative UX/UI designer and beekeeper based in the UK. Case studies in healthtech and mobile apps, plus UX design teaching experience.'),
 '/about-me': ('About | Freddie Grzybowski', 'UX/UI designer with a background in music, streaming and teaching. Learn about my design process, tools, and life outside of UX.'),
 '/teaching-experience': ('Teaching UX Design | Freddie Grzybowski', 'Four years teaching and mentoring aspiring UX designers online, across 14+ cohorts, with workshops, 1:1 mentoring and real-world projects.'),
 '/alta-flora': ('Alta Flora Case Study | Freddie Grzybowski', "UX case study: a three-week design sprint for Alta Flora's medical tracking app EVA, covering research, onboarding, personalisation and usability testing."),
 '/balance': ('Balance Case Study | Freddie Grzybowski', 'UX case study: a two-week design sprint for the meditation app Balance, exploring how EEG headband data could improve engagement and habit building.'),
}
H1 = {'/': 'I’m Freddie, UX/UI Designer', '/teaching-experience': 'Teaching UX Design'}
OG = 'https://s3.amazonaws.com/webflow-prod-assets/65bcd665e34d787b54fdda73/6adf7a067ac627eac5e39e01_alta-flora-hero-3-p-1080.png'
PRE = json.load(open(os.environ.get('PRERENDER', 'prerender.json')))
FAV = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#03141a"/>'
       '<path d="M22 46V18h22M22 32h17" fill="none" stroke="#7ff3e4" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
if os.path.isdir(ROOT): shutil.rmtree(ROOT)
os.makedirs(ROOT)
na = open('dist/na.js', 'rb').read(); ver = hashlib.sha1(na).hexdigest()[:10]
open(f'{ROOT}/na.js', 'wb').write(na)
open(f'{ROOT}/favicon.svg', 'w').write(FAV)
NAV = ''.join(f'<li><a href="{u}">{n}</a></li>' for u, n in [('/', 'Home'), ('/about-me', 'About'), ('/teaching-experience', 'Teaching'), ('/alta-flora', 'Alta Flora'), ('/balance', 'Balance')])
FOOT = (f'<p>Say hello: <a href="mailto:{CONTACT["mail"]}">{CONTACT["mail"]}</a> · '
        f'<a href="{CONTACT["linkedin"]}">LinkedIn</a> · <a href="{CONTACT["medium"]}">Medium</a></p>')

def page(path, title, desc, body, extra_script=''):
    url = f'https://{DOMAIN}{path if path == "/" else path + "/"}'
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{OG}"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#03141a">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300..700;1,400&family=Oswald:wght@200..700&display=swap" rel="stylesheet">
<style>html,body{{margin:0;background:#03141a;color:#fefdf6;font-family:Montserrat,system-ui,sans-serif}}
html.na-on body>*:not(#na-host):not(script):not(canvas){{display:none!important}}
.fb{{max-width:760px;margin:0 auto;padding:32px max(20px,env(safe-area-inset-left,0px));line-height:1.6}}
.fb nav ul{{display:flex;flex-wrap:wrap;gap:8px 20px;list-style:none;padding:0}}.fb a{{color:#7ff3e4}}
.fb h1,.fb h2,.fb h3{{font-family:Oswald,sans-serif;font-weight:400;text-transform:uppercase;line-height:1.1}}.fb img{{max-width:100%;height:auto;border-radius:12px}}</style>
<script>document.documentElement.classList.add('na-on')</script>
<noscript><style>html.na-on body>*{{display:block!important}}</style></noscript>
{extra_script}</head>
<body>
<div class="fb"><nav aria-label="Main"><ul>{NAV}</ul></nav><main>
{body}
</main><footer>{FOOT}</footer></div>
<script src="/na.js?v={ver}"></script>
</body>
</html>
'''

for path, (title, desc) in PAGES.items():
    body = PRE[path]
    if path in H1:
        lines = body.split('\n'); i = next(n for n, l in enumerate(lines) if l.startswith('<h1>'))
        lines[i] = '<h1>' + H1[path] + '</h1>'; body = '\n'.join(lines)
    d = ROOT if path == '/' else f'{ROOT}{path}'
    os.makedirs(d, exist_ok=True)
    open(f'{d}/index.html', 'w', encoding='utf-8').write(page(path, title, desc, body))

# unknown addresses go to the homepage
open(f'{ROOT}/404.html', 'w', encoding='utf-8').write(page('/', 'Page not found | Freddie Grzybowski', 'This page does not exist.',
     '<h1>Page not found</h1><p><a href="/">Go to the homepage</a></p>', '<script>location.replace("/")</script>\n'))
open(f'{ROOT}/CNAME', 'w').write(DOMAIN + '\n')
open(f'{ROOT}/robots.txt', 'w').write('User' + '-agent: *\nAllow: /\nSitemap: https://' + DOMAIN + '/sitemap.xml\n')
open(f'{ROOT}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'<url><loc>https://{DOMAIN}{p if p == "/" else p + "/"}</loc></url>\n' for p in PAGES) + '</urlset>\n')
open(f'{ROOT}/.nojekyll', 'w').write('')
print('site built', sorted(os.listdir(ROOT)))
