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

# --- layout fixes for wide screens: line the header and menu up with the page content column ---
css += """
#site .menu{-webkit-backdrop-filter:none!important;backdrop-filter:none!important;background:#03141a!important}
#site.mo>main,#site.mo>.scue{visibility:hidden;transition:visibility 0s linear .9s}
#site .menu .kzh{background-repeat:no-repeat;background-color:#03141a}
#site .menu:not([data-a]) .kzh0,#site .menu[data-a="0"] .kzh0,#site .menu[data-a="1"] .kzh1,#site .menu[data-a="2"] .kzh2,#site .menu[data-a="3"] .kzh3,#site .menu[data-a="4"] .kzh4,#site .menu[data-a="5"] .kzh5{--kr:14!important;-webkit-mask-image:none!important;mask-image:none!important}
#site .menu .kzh0,#site .menu .kzh3,#site .menu .kzh4{background-size:contain!important;background-position:center!important}
#site .menu .uug,#site .menu .kxgh{-webkit-backdrop-filter:none!important;backdrop-filter:none!important;background:linear-gradient(135deg,rgba(10,40,52,.92),rgba(5,24,32,.96))!important;border:1px solid rgba(127,243,228,.3)!important;animation:none!important}
#site .menu .uug .kgl,#site .menu .kwgl{display:none!important}
#site .menu .uug .kwt{text-shadow:none!important}
#site .stand img{-webkit-mask-image:linear-gradient(90deg,transparent,#000 26%,#000 74%,transparent),linear-gradient(180deg,transparent,#000 14%,#000 55%,rgba(0,0,0,.55) 74%,transparent 96%)!important;mask-image:linear-gradient(90deg,transparent,#000 26%,#000 74%,transparent),linear-gradient(180deg,transparent,#000 14%,#000 55%,rgba(0,0,0,.55) 74%,transparent 96%)!important}
#site .x-stp p{font:500 16px/1.6 var(--fb)!important;color:rgba(254,253,246,.92)!important;max-width:36ch!important}
#site .wi-c p{font:500 16px/1.6 var(--fb)!important;max-width:34ch!important;margin-top:16px!important}
#site .wi-c3 p{color:#fefdf6}
#site .x-bento .big img{transform:none!important;object-position:50% 22%!important}
/* lite mode: software rendering / no graphics acceleration */
:host(.lite) *{-webkit-backdrop-filter:none!important;backdrop-filter:none!important}
:host(.lite) .mcv,:host(.lite) .scue,:host(.lite) .bgfx::before,:host(.lite) .bgfx::after{display:none!important}
:host(.lite) .mbtn,:host(.lite) .mbtn *,:host(.lite) .kzh,:host(.lite) .kwf,:host(.lite) .tk,:host(.lite) .mq{animation:none!important}
:host(.lite) .x-g,:host(.lite) .x-stp,:host(.lite) .x-cat,:host(.lite) .x-tile,:host(.lite) .qs,:host(.lite) .tl-card{background:rgba(8,34,44,.88)!important;box-shadow:none!important}
:host(.lite) *{text-shadow:none!important;filter:none!important}
#site{--G:calc((100vw - min(100vw,1440px))/2 + 5vw)}
@media (min-width:1441px){
#site .nav{padding-left:var(--G)!important;padding-right:var(--G)!important}
#site .menu:is(.kxa,.kxb,.kxc,.kxd,.kua) .kwl{left:var(--G)!important}
#site .menu:is(.kxa,.kxb,.kxc,.kxd,.kua) .kwp{right:var(--G)!important}
#site .menu:is(.kxc,.kua) .ft{left:var(--G)!important}
}
/* unified glass for every card (matches the menu glass and the header pill) */
#site .x-g,#site .x-stp,#site .x-stp:nth-child(n),#site .x-cat,#site .x-tile{background:rgba(8,34,44,.55)!important;border:1px solid rgba(150,240,255,.22)!important;-webkit-backdrop-filter:blur(22px) saturate(1.3);backdrop-filter:blur(22px) saturate(1.3);border-radius:18px;box-shadow:0 0 40px rgba(127,243,228,.12),inset 0 1px 0 rgba(255,255,255,.08)!important}
#site .x-stp{padding:32px}
#site .x-cat{padding:28px 32px}
#site .x-cat li{display:flex;align-items:center}
#site .x-cat li+li::before{content:"";width:6px;height:6px;border-radius:50%;background:#7ff3e4;opacity:.7;margin-right:24px;flex:none}
#site .x-cat h4{color:#7ff3e4}
#site .x-stp:not(:last-child)::after{color:#7ff3e4}
#site .x-stp svg,#site .x-stp:nth-child(n) svg{stroke:#7ff3e4}
#site .x-loop{color:#7ff3e4;border-color:rgba(127,243,228,.4)}
#site .x-loop i{background:rgba(127,243,228,.3)}
#site .st b,#site .st>div:nth-child(n) b,#site .tw .ent .nm span,#site .tw .ent:nth-child(n) .nm span{background-image:linear-gradient(transparent 62%,rgba(110,230,255,.28) 62%)!important}
#site .qs{background:rgba(8,34,44,.55)!important;border:1px solid rgba(150,240,255,.22)!important;border-radius:32px!important;-webkit-backdrop-filter:blur(22px) saturate(1.3);backdrop-filter:blur(22px) saturate(1.3);box-shadow:0 0 40px rgba(127,243,228,.12),inset 0 1px 0 rgba(255,255,255,.08)}
#site .qs blockquote::before{color:#7ff3e4}
#site .tl-card{background:rgba(8,34,44,.55)!important;border:1px solid rgba(150,240,255,.22)!important;border-radius:18px!important;padding:32px!important;-webkit-backdrop-filter:blur(22px) saturate(1.3);backdrop-filter:blur(22px) saturate(1.3);box-shadow:0 0 40px rgba(127,243,228,.12),inset 0 1px 0 rgba(255,255,255,.08)!important}
#site .menu .kzh1{background-color:#000;background-repeat:no-repeat!important;background-size:auto 108%!important;background-position:78% 20%!important}
"""

scripts = re.findall(r'<script>(.*?)</script>', src, re.S)
main = [s for s in scripts if 'function init()' in s][0]
_pr=[("'Explore the problem, talk to users and define what really matters.'","'I start by talking to people and digging into the problem, so I know what really needs solving before I design anything.'"),
("'Turn insights into thoughtful ideas, wireframes and intuitive experiences.'","'I turn what I learn into wireframes and prototypes that are simple to use and easy to follow.'"),
("'Test, learn and improve, always looking for ways to make things clearer, simpler and more accessible.'","'I test with real users, fix what is confusing, and keep improving until it is clear, simple and accessible.'")]
for _a,_b in _pr:
    assert _a in main,'PATCH MISS process'
    main=main.replace(_a.strip("'"),_b.strip("'"))
# --- menu preview cards: real pictures for About and Say hello instead of plain gradients ---
_imgs = json.load(open('assets/imgs.json'))
main = main.replace('var IMG={', 'var IMG={ab:%s,pt:%s,' % (json.dumps(_imgs['hero']), json.dumps(_imgs['portrait'])), 1)
_old = "'linear-gradient(135deg,#e6e0ff,#7a6af0)','url('+IMG.t+')'"
assert _old in main, 'PATCH MISS: PVB about'
main = main.replace(_old, "'url('+IMG.pt+')','url('+IMG.t+')'", 1)
_old = ",'linear-gradient(135deg,#ffc929,#ebefa0)'][i]}"
assert _old in main, 'PATCH MISS: PVB hello'
main = main.replace(_old, ",'linear-gradient(135deg,#0f5f66,#7ff3e4 48%,#e6e0ff)'][i]}", 1)
_B='https://s3.amazonaws.com/webflow-prod-assets/65bcd665e34d787b54fdda73/'
_pics={'h':_B+'6ad5f64b1b6de57eb41ad39f_heromashup2-p-1080.png','t':_B+'6ad3735e08484eaec7f80c11_Screenshot%202023-03-22%20at%2016.57%202-p-1600.png','a':_B+'6adf7a067ac627eac5e39e01_alta-flora-hero-3-p-1080.png','b':_B+'6adf79e0eb7f85baae64703c_balance-hero-p-1080.png'}
for _k,_u in _pics.items():
    _o="'url('+IMG.%s+')'"%_k
    assert _o in main,'PATCH MISS pic '+_k
    main=main.replace(_o,"'url(%s)'"%_u,1)
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

must('i<70','i<(NSR.host.classList.contains("lite")?18:70)')
# the preview bar is hidden, drop its toast on links
main = main.replace("toast('Case study pages aren’t part of this preview')", "")

# Esc closes the menu even when focus is outside the shadow root
main += "\n;addEventListener('keydown',function(e){if(e.key==='Escape'&&S.mo)closeMenu()});addEventListener('popstate',function(){var m={'/':'home','/about-me':'about','/teaching-experience':'teach'}[location.pathname.replace(/\\/$/,'')||'/'];if(m&&m!==S.p){S.p=m;closeMenu();mark();rv();window.scrollTo(0,0)}});"

patch = patch.replace('document.getElementById(', 'NSR.getElementById(')
for _a,_b in _pr:
    _a=_a.strip("'");_b=_b.strip("'")
    assert _a in patch,'PATCH MISS process in patch'
    patch=patch.replace(_a,_b)
import re as _re
_n=len(_re.findall(r'var BEE="data:image/jpeg;base64,[^"]*"', patch))
assert _n==1,'PATCH MISS BEE photo'
patch=_re.sub(r'var BEE="data:image/jpeg;base64,[^"]*"','var BEE="https://s3.amazonaws.com/webflow-prod-assets/65bcd665e34d787b54fdda73/6ad35c518c6b81db3436e306_229614763_534730867766597_9168841667037193452_n-p-1080.jpeg"',patch)

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
 try{var gc=document.createElement('canvas'),gl=gc.getContext('webgl')||gc.getContext('experimental-webgl'),lite=!gl;
  if(gl){var ex=gl.getExtension('WEBGL_debug_renderer_info');var rn=ex?gl.getParameter(ex.UNMASKED_RENDERER_WEBGL):'';if(/swiftshader|llvmpipe|software|basic render|microsoft basic/i.test(rn))lite=true}
  if(lite||/[?&]lite=1/.test(location.search))host.classList.add('lite')}catch(e){}
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
