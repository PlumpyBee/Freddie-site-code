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
#site .hxp{display:none!important}
#site .te-img img{transform:rotate(-2deg) scale(1.25)!important;transform-origin:50% 50%;filter:drop-shadow(0 30px 40px rgba(0,0,0,.55))}
@media (min-width:1100px){#site .te-hero{grid-template-columns:1fr 1fr!important}#site .te-img{overflow:visible}#site .te-img img{width:185%!important;max-width:none!important;margin-left:-40%;transform:rotate(-2deg)!important}}
/* desktop: real nav bar instead of the Menu button, big statement hero (option A) */
@media (min-width:1100px){
#site .mbtn{display:none!important}
#site[data-nv] .nv,#site .nv{display:flex!important;background:none!important;border:0!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important;padding:0!important;gap:34px;align-items:center;box-shadow:none!important}
#site .nvi{display:none!important}
#site .nv a{padding:8px 0!important;font:600 12px var(--fb)!important;letter-spacing:.16em;text-transform:uppercase;border-radius:0!important;background:none!important;color:#fefdf6!important;transition:color .25s}
#site .nv li.on a,#site .nv a:hover{color:#7ff3e4!important;background:none!important}
#site .nv li[data-pp="mail"] a{padding:12px 22px!important;border:1px solid rgba(127,243,228,.55);border-radius:999px!important;background:rgba(8,34,44,.55)!important}
#site .nv li[data-pp="mail"] a:hover{background:#7ff3e4!important;color:#03141a!important}
#site .logo{border:0!important;background:none!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important;padding:0!important;font:500 24px var(--fd)!important;box-shadow:none!important}
#site .hero{display:flex!important;flex-direction:column;justify-content:flex-start;align-items:stretch;gap:clamp(40px,5vw,72px);min-height:0!important;padding-bottom:clamp(64px,7vw,110px)}
#site .hero .hh{gap:22px}
#site .hero h1.dk{font-size:min(15.2vw,29vh,218px);font-weight:300;line-height:.9;letter-spacing:-.01em}
#site .hero h1 .ln{display:inline!important}
#site .hero h1 .ln:first-child{display:block!important}
#site .hero h1.dk{white-space:nowrap}
#site .hero h1 .ln:nth-child(3){margin-left:.24em}
#site .hero .hr{flex-direction:row;justify-content:space-between;align-items:flex-end;width:100%;background:none!important;border:0!important;box-shadow:none!important;-webkit-backdrop-filter:none!important;backdrop-filter:none!important;padding:0!important}
#site .hero .hr .lead{max-width:560px;font-size:22px;line-height:1.55}
}

/* natural aurora behind the home hero */
#site .hero{isolation:isolate}
#site .hero .lead{text-shadow:0 2px 18px rgba(3,20,26,.9),0 0 6px rgba(3,20,26,.7)}
#site .aur{position:absolute;left:0;right:0;top:12%;width:100%;z-index:-1;pointer-events:none;-webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-image:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
#site .aur svg{display:block;width:100%;height:calc(var(--u,1px)*560)}
#site .aur .aug{position:absolute;left:0;right:0;top:48%;height:70%;background:radial-gradient(ellipse 50% 50% at 50% 30%,rgba(127,243,228,.22),rgba(127,243,228,0) 70%)}
@keyframes aurmv{0%,100%{opacity:.82}50%{opacity:1}}
@media (prefers-reduced-motion:reduce){#site .aur svg{animation:none}}
:host(.lite) .aur svg{animation:none;filter:none}

/* ===== Home hero: exactly the approved B5 layout (desktop) ===== */
@media (min-width:1100px){
#site{--u:min(calc(100vw/1440),calc(100vh/900),1.35px)}
#site .hero{max-width:none;min-height:calc(100vh - 90px)!important;justify-content:space-between;align-items:center;text-align:center;gap:0;padding:calc(var(--u)*44) 5vw calc(var(--u)*225)}
#site .hero .hh{align-items:center;gap:calc(var(--u)*22)}
#site .hero h1.dk{font-size:inherit;line-height:1;letter-spacing:0;text-transform:uppercase;display:flex;flex-direction:column;align-items:center;margin:0}
#site .hero h1 .ln{display:block!important;margin:0!important}
#site .hero h1 .ln:nth-child(1){font:200 calc(var(--u)*112)/1 var(--fd);letter-spacing:.06em}
#site .hero h1 .ln:nth-child(2){font:500 calc(var(--u)*262)/.84 var(--fd);letter-spacing:-.01em}
#site .hero h1 .ln:nth-child(3){font:300 calc(var(--u)*92)/1 var(--fd);letter-spacing:.34em;padding-left:.34em;margin-top:calc(var(--u)*6)!important}
#site .hero h1 .ln .hl{display:inline-block;background:none!important;color:inherit!important;filter:drop-shadow(0 0 calc(var(--u)*46) rgba(127,243,228,.45))}
#site .hero h1 .ln .hl .ch{background:linear-gradient(180deg,#fff 25%,#7ff3e4 100%);-webkit-background-clip:text;background-clip:text;color:transparent!important;-webkit-text-fill-color:transparent;text-shadow:none!important}
#site .hero .hr{flex-direction:column;align-items:center;justify-content:flex-end;width:100%}
#site .hero .hr .lead{max-width:600px;font-size:19px;line-height:1.55;text-align:center;margin:0}
#site .hero .hr .lk{display:none!important}
#site .aur{top:calc(47% - var(--u)*460)}
}

#site .hpl{position:absolute;inset:0;z-index:-1;pointer-events:none}
#site .hpl i{position:absolute;border-radius:50%;animation:hpld 12s ease-in-out infinite;transition:scale .6s,box-shadow .6s}
#site .hpl i.hot{box-shadow:0 0 calc(10px + var(--f,0)*20px) calc(1px + var(--f,0)*4px) var(--c);opacity:1!important;scale:calc(1 + var(--f,0)*.7)}
#site .ac{transform-box:fill-box;transform-origin:50% 100%}
#site .ac1{animation:acm1 11s ease-in-out infinite}
#site .ac2{animation:acm2 17s ease-in-out -5s infinite}
#site .ac3{animation:acm1 14s ease-in-out -9s infinite reverse}
#site .ac4{animation:acm3 9s ease-in-out infinite}
@keyframes acm1{0%,100%{transform:translateX(-30px) skewX(-1.6deg) scaleY(.94);opacity:.8}50%{transform:translateX(30px) skewX(1.8deg) scaleY(1.08);opacity:1}}
@keyframes acm2{0%,100%{transform:translateX(24px) skewX(1.4deg) scaleY(1.05);opacity:.75}50%{transform:translateX(-24px) skewX(-1.2deg) scaleY(.92);opacity:1}}
@keyframes acm3{0%,100%{opacity:.45;transform:translateX(-16px)}50%{opacity:1;transform:translateX(16px)}}
:host(.lite) .ac{animation:none}
@media (prefers-reduced-motion:reduce){#site .ac{animation:none}}
@keyframes hpld{0%,100%{transform:translate(0,0);opacity:.25}50%{transform:translate(var(--dx),var(--dy));opacity:.8}}
@media (prefers-reduced-motion:reduce){#site .hpl i{animation:none;opacity:.8}}
:host(.lite) .hpl i{animation:none!important;opacity:.6}:host(.lite) .hpl i:nth-child(n+26){display:none}
@media (min-width:1100px){
#site .hero .hh,#site .hero .hr{position:relative}
#site .hero .hr::before{content:'';position:absolute;left:50%;top:50%;width:min(760px,90%);height:230%;transform:translate(-50%,-50%);z-index:-1;background:radial-gradient(ellipse 50% 50% at 50% 50%,rgba(3,20,26,.85),rgba(3,20,26,.5) 60%,rgba(3,20,26,0) 100%);pointer-events:none}
#site .hero .hh::before{content:'';position:absolute;left:-8%;right:-8%;top:-6%;bottom:-4%;z-index:-1;background:radial-gradient(ellipse 52% 52% at 50% 52%,rgba(3,20,26,.8),rgba(3,20,26,.4) 55%,rgba(3,20,26,0) 78%);pointer-events:none}
#site .hero h1 .ln:nth-child(1),#site .hero h1 .ln:nth-child(3){filter:drop-shadow(0 0 calc(var(--u)*18) rgba(3,20,26,.9))}
#site .hero h1 .ln .hl{filter:drop-shadow(0 0 calc(var(--u)*26) rgba(3,20,26,.75)) drop-shadow(0 0 calc(var(--u)*46) rgba(127,243,228,.3))!important}
}
#site .bgfx{-webkit-mask-image:linear-gradient(#000 88%,transparent)!important;mask-image:linear-gradient(#000 88%,transparent)!important}

/* B3 soft-glow horizon (alternative to the aurora rays; add ?fx=rays to the URL to compare) */
#site .hfx{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden;-webkit-mask-image:linear-gradient(#000 84%,transparent 100%);mask-image:linear-gradient(#000 84%,transparent 100%)}
#site .hfx i{position:absolute;display:block}
#site .hfx .sk{inset:0;background:linear-gradient(180deg,rgba(2,16,26,0) 0%,rgba(4,32,42,.3) 45%,rgba(6,48,58,.45) 68%,rgba(10,74,80,.55) 84%,rgba(11,90,92,.6) 100%)}
#site .hfx .gw{left:50%;bottom:5%;width:132%;height:50%;margin-left:-66%;background:radial-gradient(ellipse 50% 50% at 50% 50%,rgba(127,243,228,.5),rgba(127,243,228,.16) 45%,rgba(127,243,228,0) 72%);filter:blur(26px)}
#site .hfx .bd{left:0;width:100%;bottom:0;height:46%;background:linear-gradient(180deg,rgba(3,20,26,0) 0%,rgba(3,20,26,.4) 45%,rgba(3,20,26,.9) 100%)}
#site .hfx .ms{border-radius:50%;background:rgba(200,255,250,.15);filter:blur(34px);height:12%;animation:b3ms 24s ease-in-out infinite}
#site .hfx .ms1{left:-20%;width:62%;bottom:19%}
#site .hfx .ms2{right:-16%;width:68%;bottom:15%;animation-duration:30s;animation-delay:-9s}
#site .hfx .pf{border-radius:50%;animation:b3pf 20s ease-in-out infinite;will-change:transform;mix-blend-mode:screen}
#site .hfx .pr{animation:b3pf 20s ease-in-out infinite;will-change:transform;mix-blend-mode:screen;-webkit-mask-image:radial-gradient(closest-side at 50% 80%,#000 10%,rgba(0,0,0,.5) 50%,transparent 100%),linear-gradient(0deg,#000 30%,transparent 100%);-webkit-mask-composite:source-in;mask-image:radial-gradient(closest-side at 50% 80%,#000 10%,rgba(0,0,0,.5) 50%,transparent 100%),linear-gradient(0deg,#000 30%,transparent 100%);mask-composite:intersect;opacity:.6}
@keyframes b3pf{0%,100%{transform:translate(0,0) scale(1) rotate(0deg);opacity:.65}50%{transform:translate(var(--tx),var(--ty)) scale(1.14) rotate(var(--rt));opacity:1}}
@keyframes b3sw{0%,100%{transform:translateX(-40px) skewX(-8deg);opacity:.55}50%{transform:translateX(40px) skewX(6deg);opacity:.9}}
@keyframes b3ms{0%,100%{transform:translateX(-60px);opacity:.5}50%{transform:translateX(60px);opacity:.9}}
@keyframes b3sh{0%,100%{opacity:.35;transform:scaleX(.92)}50%{opacity:.7;transform:scaleX(1.04)}}
:host(.lite) .hfx .pr,:host(.lite) .hfx .pf,:host(.lite) .hfx .ms{animation:none;filter:none;will-change:auto}
@media (prefers-reduced-motion:reduce){#site .hfx i{animation:none!important}}
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

AUR_JS = r'''

function aurRays(){var sd=0,R=function(){sd=(sd*1664525+1013904223)>>>0;return sd/4294967296};
function cur(base,amp,ph,hm,c0,c1,step,seed,op){sd=seed;var o='',x=-20;while(x<1460){var yb=base+amp*Math.sin(x/240+ph)+amp*.45*Math.sin(x/97+ph*2),env=.5+.5*Math.sin(x/310+ph*1.7)*Math.sin(x/130+ph),h=hm*Math.max(.3,env)*(.6+.4*R()),w=3+R()*6,ln=(R()*12-6)+(x-720)/720*-12,c=R()<.75?c0:c1,op2=Math.min(1,op*(.45+.55*R()));o+='<path d="M'+x.toFixed(0)+' '+yb.toFixed(0)+'L'+(x+ln).toFixed(0)+' '+(yb-h).toFixed(0)+'L'+(x+ln+w*.6).toFixed(0)+' '+(yb-h).toFixed(0)+'L'+(x+w).toFixed(0)+' '+yb.toFixed(0)+'Z" fill="url(#'+c+')" opacity="'+op2.toFixed(2)+'"/>';x+=step*(.6+.8*R())}return o}
var a1=cur(450,38,.5,400,'gT','gL',4.5,3,.95),a2=cur(490,30,2.1,330,'gL','gT',5.5,11,.75),a3=cur(410,26,4,270,'gG','gT',6.5,5,.6),p=[];for(var x=-20;x<=1460;x+=20)p.push(x+' '+(450+38*Math.sin(x/240+.5)+17*Math.sin(x/97+1)).toFixed(0));
var pk='';
return '<div class="hpl" aria-hidden="true">'+pk+'</div><div class="aur" aria-hidden="true"><i class="aug"></i><svg viewBox="0 0 1440 560" preserveAspectRatio="none"><defs><linearGradient id="gT" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#b8ffe6" stop-opacity=".95"/><stop offset=".25" stop-color="#4fe8b8" stop-opacity=".6"/><stop offset=".65" stop-color="#2fb7c8" stop-opacity=".22"/><stop offset="1" stop-color="#3a6fd8" stop-opacity="0"/></linearGradient><linearGradient id="gL" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffc6f0" stop-opacity=".85"/><stop offset=".3" stop-color="#b58cff" stop-opacity=".5"/><stop offset="1" stop-color="#6a5cff" stop-opacity="0"/></linearGradient><linearGradient id="gG" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e8ffb0" stop-opacity=".8"/><stop offset=".3" stop-color="#7ff3c4" stop-opacity=".5"/><stop offset="1" stop-color="#2fb7c8" stop-opacity="0"/></linearGradient><filter id="b1" x="-5%" y="-20%" width="110%" height="140%"><feGaussianBlur stdDeviation="1.8 3.6"/></filter><filter id="b2" x="-5%" y="-30%" width="110%" height="160%"><feGaussianBlur stdDeviation="22 30"/></filter><filter id="b3" x="-5%" y="-100%" width="110%" height="300%"><feGaussianBlur stdDeviation="8"/></filter></defs><g class="ac ac4"><g filter="url(#b2)" opacity=".55">'+a2+a1+'</g></g><g class="ac ac2"><g filter="url(#b1)">'+a2+'</g></g><g class="ac ac3"><g filter="url(#b1)">'+a3+'</g></g><g class="ac ac1"><g filter="url(#b1)">'+a1+'</g></g><path d="M'+p.join('L')+'" fill="none" stroke="#c8fff0" stroke-opacity=".5" stroke-width="12" filter="url(#b3)"/></svg></div>'}

function aurPuffs(){var sd=7,R=function(){sd=(sd*1664525+1013904223)>>>0;return sd/4294967296},P=[['120,255,190','100,210,255'],['127,243,228','160,140,255'],['100,210,255','255,150,225'],['160,140,255','127,243,228'],['235,239,160','120,255,190'],['255,150,225','160,140,255'],['127,243,228','120,255,190'],['120,255,190','160,140,255']],o='';for(var i=0;i<10;i++){var p=P[i%8],w=28+R()*22,h=40+R()*26,x=(i/10)*100-10+R()*10,y=4+R()*34,tx=Math.round((R()-.5)*180),ty=Math.round((R()-.5)*60),rt=((R()-.5)*12).toFixed(1),du=(14+R()*16).toFixed(1),dl=(R()*20).toFixed(1),per=11+Math.round(R()*14),a2=(.38+R()*.16).toFixed(2),st='left:'+x.toFixed(1)+'%;top:'+y.toFixed(1)+'%;width:'+w.toFixed(1)+'%;height:'+h.toFixed(1)+'%;--tx:'+tx+'px;--ty:'+ty+'px;--rt:'+rt+'deg;animation-duration:'+du+'s;animation-delay:-'+dl+'s';o+='<i class="pf" style="'+st+';background:radial-gradient(closest-side at 50% 78%,rgba('+p[0]+','+a2+'),rgba('+p[0]+','+(a2*.5).toFixed(2)+') 42%,rgba('+p[1]+','+(a2*.28).toFixed(2)+') 72%,rgba('+p[1]+',0) 100%)"></i><i class="pr" style="'+st+';background:repeating-linear-gradient(90deg,rgba('+p[0]+',0) 0,rgba('+p[0]+',.55) '+(per*.4).toFixed(1)+'px,rgba('+p[1]+',.15) '+(per*.7).toFixed(1)+'px,rgba('+p[1]+',0) '+per+'px)"></i>'}return o}
function aurB3(){return '<div class="hfx" aria-hidden="true"><i class="sk"></i>'+aurPuffs()+'<i class="gw"></i><i class="bd"></i><i class="ms ms1"></i><i class="ms ms2"></i></div>'}
function aurHtml(){return (/[?&]fx=rays/.test(location.search))?aurRays():aurB3()}

'''
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
must("function bgfx(c){","function bgfx(c){")
main = AUR_JS + main
must("<section class=\"hero\" data-l=\"Hero\"><div class=\"hh\">'","<section class=\"hero\" data-l=\"Hero\">'+aurHtml()+'<div class=\"hh\">'")
# --- original plankton: more of them, in swarms, drawn gently to the mouse trail ---
must("(.16+.1*Math.sin(ts/1200+p.ph)+p.b*.6)","(.24+.12*Math.sin(ts/1200+p.ph)+p.b*.6)")
must("n:80","n:(NSR.host.classList.contains('lite')?60:170)",0)

must("if(p.b>.06)glow(p.x,p.y,8+p.b*22,p.c,p.b*.4)","if(p.b>.06)glow(p.x,p.y,6+p.b*14,p.c,p.b*.28)")
must("P.forEach(function(p){if(!p.or){","for(var i9=0;i9<P.length;i9++){var a9=P[i9];for(var j9=i9+1;j9<P.length;j9++){var b9=P[j9],ux=a9.x-b9.x,uy=a9.y-b9.y;if(ux<62&&ux>-62&&uy<62&&uy>-62){var ud=Math.hypot(ux,uy)||.5;if(ud<62){var uf=(62-ud)/62*.0016;a9.vx+=ux/ud*uf;a9.vy+=uy/ud*uf;b9.vx-=ux/ud*uf;b9.vy-=uy/ud*uf}}}}\n  P.forEach(function(p){if(!p.or){p.hx=p.x;p.hy=p.y;")
must("if(d<360){var w=Math.pow(1-d/360,1.5),nx=dx/d,ny=dy/d;p.vx+=(-ny*p.dir*.022*p.sp+nx*(p.or-d)*.00035)*w;p.vy+=(nx*p.dir*.022*p.sp+ny*(p.or-d)*.00035)*w;p.tb=w*.32}else p.tb=0;","var hv=d<210?Math.pow(1-d/210,1.3):0;if(hv>0){p.vx+=dx/d*.016*hv;p.vy+=dy/d*.016*hv}p.vx+=(p.hx-p.x)*.00005+Math.cos(p.ph*3+ts/4000)*.0025;p.vy+=(p.hy-p.y)*.00005+Math.sin(p.ph*2+ts/5000)*.0025;p.tb=Math.max(p.pb||0,hv*.6);p.pb=(p.pb||0)*.992;")
must("if(mode=='biolum')RP.push({x:mx,y:my,r:0,a:1});","if(mode=='biolum'){RP.push({x:mx,y:my,r:0,a:1});P.forEach(function(p){var dx=p.x-mx,dy=p.y-my,d=Math.hypot(dx,dy)||1;if(d<320){var f=Math.pow(1-d/320,1.2);p.vx+=dx/d*f*2.4;p.vy+=dy/d*f*2.4;p.pb=Math.max(p.pb||0,.25+f*.65)}})}")
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
must('function hexburst(e){','function hexburst(e){return;')
main=main.replace('<img src="\'+IMG.h+\'" alt=""','<img src="'+_pics['h'].replace('-p-1080','-p-1600')+'" alt=""')
must("var L=[['Home','home'],['About','about'],['Teaching','teach']]","var L=[['Home','home'],['About','about'],['Teaching','teach'],['Alta Flora','alta'],['Balance','balance'],['Say hello','mail']]")
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
patch=_re.sub(r'var BEE="data:image/jpeg;base64,[^"]*"','var BEE="https://s3.amazonaws.com/webflow-prod-assets/65bcd665e34d787b54fdda73/6ad2055a3c648048bd0a675e_beekeeping.png"',patch)

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
