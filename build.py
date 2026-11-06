"""Builds dist/na.js from the approved Night Aurora preview (preview/full2.html).

The preview is a self-contained app. We run it inside a Shadow DOM on the live
Webflow pages so its CSS and JS cannot clash with Webflow's own, and swap the
few preview-only bits (page switching, links, preview bar) for real site behaviour.
"""
import re, json, sys

src = open('preview/full2.html', encoding='utf-8').read()

css = ''.join(re.findall(r'<style>(.*?)</style>', src, re.S))
css = css.replace(':root{', ':host{', 1)
css = css.replace('body{margin:0;background:#fdfdf5;font-family:Montserrat,system-ui,sans-serif}',
                  ':host{display:block;margin:0;font-family:Montserrat,system-ui,sans-serif}', 1)

scripts = re.findall(r'<script>(.*?)</script>', src, re.S)
main = [s for s in scripts if 'function init()' in s][0]
patch = [s for s in scripts if 'function patch()' in s][0]
svg = re.search(r'<svg width="0" height="0" style="position:absolute" aria-hidden="true">.*?</svg>', src, re.S).group(0)

def must(old, new, count=1, text=None):
    global main
    t = main
    if old not in t:
        sys.exit('PATCH MISS: ' + old[:80])
    main = t.replace(old, new) if count == 0 else t.replace(old, new, count)

# --- run inside the shadow root instead of the document ---
main = main.replace('document.getElementById(', 'NSR.getElementById(')
main = main.replace("document.querySelector('.pv-bar')", "NSR.querySelector('.pv-bar')")
main = main.replace('document.addEventListener(', 'NSR.addEventListener(')
main = main.replace('document.activeElement', '(NSR.activeElement||document.activeElement)')
main = main.replace("document.querySelectorAll('#site [data-go]')", "NSR.querySelectorAll('#site [data-go]')")
main = main.replace(',document)', ',NSR)')
# overlay effects that append to <body> must live in the shadow root to be styled
main = main.replace('document.body.appendChild(', 'NSR.appendChild(')

# --- real navigation instead of in-preview page switching ---
go_start = main.index('function go(x){')
go_end = main.index('function setOrigin()')
new_go = r"""function go(x,el){
 var U={home:'/',about:'/about-me',teach:'/teaching-experience',alta:'/alta-flora',balance:'/balance'};
 if(x==='x'){var t=el&&el.closest('[data-k]');var k=t?t.getAttribute('data-k'):'';x=(el&&/Balance/i.test(el.textContent))?'balance':(k==='b'?'balance':'alta')}
 if(x==='mail'){var tx=(el&&el.textContent||'').trim();
  if(/linkedin/i.test(tx))window.open('https://www.linkedin.com/in/freddiegrzybowski/','_blank','noopener');
  else if(/medium/i.test(tx))window.open('https://medium.com/@freddie.grzybowski','_blank','noopener');
  else location.href='mailto:Freddie.Grzybowski@gmail.com';return}
 if(x==='work'){var w=$('#work');if(w)window.scrollTo({top:w.getBoundingClientRect().top+scrollY-bar.offsetHeight-10,behavior:'smooth'});return}
 if(x==='alta'||x==='balance'){location.href=U[x];return}
 if(x===S.p){closeMenu();return}
 S.p=x;tlT=0;closeMenu();mark();rv();
 window.scrollTo({top:Math.max(0,site.getBoundingClientRect().top+scrollY-bar.offsetHeight+1),behavior:'auto'});
 try{history.pushState({p:x},'',U[x]);document.title={home:'Freddie Grzybowski | UX/UI Designer',about:'About me | Freddie Grzybowski',teach:'Teaching | Freddie Grzybowski'}[x]}catch(e){}
}
"""
main = main[:go_start] + new_go + main[go_end:]
must("go(g.dataset.go);return}", "go(g.dataset.go,g);return}")
must("go(its[ix].getAttribute('data-go'))", "go(its[ix].getAttribute('data-go'),its[ix])")
must("Item", "Item", 0) if False else None

# --- no hash routing, no auto-open, start on the page being visited ---
main = re.sub(r"try\{location\.hash=[^}]*\}catch\(e\)\{\}", "", main)
main = main.replace(
    "var h=(location.hash||'').slice(1).split('-');if(h[0]&&+h[0]>=1&&+h[0]<=10){S.c=+h[0];if(['home','about','teach'].indexOf(h[1])>-1)S.p=h[1]}",
    "var q=/[?&]menu=2/.test(location.search);S.c=q?2:1;S.p=window.__NA_PAGE||'home';")
main = main.replace("if(!/closed/.test(location.search))setTimeout(openMenu,700);", "")
if "__NA_PAGE" not in main:
    sys.exit('PATCH MISS: start state')

# the preview bar is hidden, drop its toast on links
main = main.replace("toast('Case study pages aren’t part of this preview')", "")

# Esc closes the menu even when focus is outside the shadow root
main += "\n;addEventListener('keydown',function(e){if(e.key==='Escape'&&S.mo)closeMenu()});addEventListener('popstate',function(){var m={'/':'home','/about-me':'about','/teaching-experience':'teach'}[location.pathname.replace(/\\/$/,'')||'/'];if(m&&m!==S.p){S.p=m;closeMenu();mark();rv();window.scrollTo(0,0)}});"

patch = patch.replace('document.getElementById(', 'NSR.getElementById(')

IIFE_TOP = r"""
(function(){
var P=location.pathname.replace(/\/$/,'')||'/';
var MAP={'/':'home','/about-me':'about','/teaching-experience':'teach'};
if(!MAP[P])return;
window.__NA_PAGE=MAP[P];
var host=document.createElement('div');host.id='na-host';
var NSR=host.attachShadow({mode:'open'});
NSR.innerHTML='<style>"""

js = IIFE_TOP + css.replace('\\', '\\\\').replace('`', '\\`') if False else None

# Build with JSON-escaped strings to avoid any quoting problems
out = []
out.append("(function(){\n")
out.append("var P=location.pathname.replace(/\\/$/,'')||'/';\n")
out.append("var MAP={'/':'home','/about-me':'about','/teaching-experience':'teach'};\n")
out.append("if(!MAP[P])return;\n")
out.append("window.__NA_PAGE=MAP[P];\n")
out.append("var CSS=%s;\nvar SVG=%s;\n" % (json.dumps(css), json.dumps(svg)))
out.append(r"""
function mount(){
 var host=document.createElement('div');host.id='na-host';
 var NSR=host.attachShadow({mode:'open'});
 NSR.innerHTML='<style>'+CSS+'</style>'+SVG+'<div class="pv-bar" id="pvb"></div><div class="pv-cap" id="hhc"></div><div id="site"></div><div class="pv-toast" id="pvt"></div>';
 document.body.insertBefore(host,document.body.firstChild);
 document.documentElement.classList.remove('na-pre');
 document.documentElement.classList.add('na-on');
 (function(NSR){
""")
out.append(main)
out.append("\n})(NSR);\n")
out.append("(function(NSR){\n" + patch + "\n})(NSR);\n")
out.append(r"""
}
if(document.body)mount();else document.addEventListener('DOMContentLoaded',mount);
})();
""")
import os
os.makedirs('dist', exist_ok=True)
open('dist/na.js', 'w', encoding='utf-8').write(''.join(out))
print('dist/na.js', len(''.join(out)))
