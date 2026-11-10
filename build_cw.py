"""Colour worlds layer (version 3 + menu B) on top of the Night Aurora build.
Run: python3 build_cw.py   (runs build.py first, then rewrites dist/na.js)"""
import re, json, os, subprocess, sys
subprocess.run([sys.executable, 'build.py'], check=True)
s = open('dist/na.js', encoding='utf-8').read()
def rep(a, b):
    global s
    assert a in s, 'MISSING: ' + a[:90]
    s = s.replace(a, b, 1)
rep("var MAP={'/':'home','/about-me':'about','/teaching-experience':'teach'};",
    "var MAP={'/':'home','/about-me':'about','/teaching-experience':'teach','/alta-flora':'alta','/balance':'balance'};")
rep("if(x==='alta'||x==='balance'){location.href=U[x];return}", "")
rep("teach:'Teaching | Freddie Grzybowski'}[x]", "teach:'Teaching | Freddie Grzybowski',alta:'Alta Flora Case Study | Freddie Grzybowski',balance:'Balance Case Study | Freddie Grzybowski'}[x]")
rep("var m={'/':'home','/about-me':'about','/teaching-experience':'teach'}[location.pathname", "var m={'/':'home','/about-me':'about','/teaching-experience':'teach','/alta-flora':'alta','/balance':'balance'}[location.pathname")
rep(";addEventListener('keydown',function(e){if(e.key==='Escape'&&S.mo)closeMenu()});addEventListener('popstate',function(){var m=", ";addEventListener('keydown',function(e){if(e.key==='Escape'&&window.__naEsc)window.__naEsc()});addEventListener('popstate',function(){var m=")
rep("if(m&&m!==S.p){S.p=m;closeMenu();mark();rv();window.scrollTo(0,0)}});", "if(m&&window.__naPop)window.__naPop(m)});")
rep("function setOrigin(){", "window.__naPop=function(m){if(m!==S.p){S.p=m;closeMenu();mark();rv();window.scrollTo(0,0)}};window.__naEsc=function(){if(S.mo)closeMenu()};\nfunction setOrigin(){")
rep("if(x===S.p){closeMenu();return}", "if(x===S.p){closeMenu();return}\n if(window.__pfWipe&&!go.__w&&U[x]){go.__w=1;window.__pfWipe(x,el,function(){try{go(x,el)}finally{go.__w=0}});return}")
rep("teach(c)+foot(c)+'</main>'", "teach(c)+(window.__pfPages?window.__pfPages():'')+foot(c)+'</main>'")
i = s.index('function build(){'); j = s.index('ready.then(lockW);', i) + len('ready.then(lockW);')
s = s[:j] + "if(window.__pfAfter)window.__pfAfter(site,NSR);" + s[j:]
i = s.index('function mark(){'); j = s.index("site.setAttribute('data-p',S.p);", i) + len("site.setAttribute('data-p',S.p);")
s = s[:j] + "if(window.__pfMark)window.__pfMark(S.p);" + s[j:]
rep("#site[data-p=teach] [data-pg=teach]{display:block", "#site[data-p=teach] [data-pg=teach],#site[data-p=alta] [data-pg=alta],#site[data-p=balance] [data-pg=balance]{display:block")

# ---- CSS: version prefixes + teaching colour layer (Colour worlds = warm sunrise) ----
css = open('cw/pf.css').read()
for k, v in [('VX ', '#site:not([data-ver="0"]) '), ('V1 ', '#site[data-ver="1"] '), ('V2 ', '#site[data-ver="2"] '), ('V3 ', '#site[data-ver="3"] ')]:
    css = re.sub(r'(?m)(^|\}|\{|,)' + k, lambda m: m.group(1) + v, css)
def mk(c1,c2,c3,c4,gl=.2,extra='',hero=None):
    hc=hero or [c1,c1,c2,c2,c3,c3]
    L=''.join('#site .te-hero h1 .hl .ch:nth-child(%d){color:%s}'%(i+1,c) for i,c in enumerate(hc))
    def rg(c,a): return 'color-mix(in srgb,%s %d%%,transparent)'%(c,int(a*100))
    gcs=[c1,c2,c3,c4,c1,c2,c3]; gxs=[86,12,86,14,82,20,80]
    secs=''.join('#site [data-pg=teach]>section:nth-child(%d){--gc:%s;--gx:%d%%}'%(i+1,rg(gcs[i],gl),gxs[i]) for i in range(7))
    S="#site .st b,#site .st>div:nth-child(n) b,#site .tw .ent .nm span,#site .tw .ent:nth-child(n) .nm span"
    return ("""
#site [data-pg=teach]>section{position:relative;isolation:isolate}
#site [data-pg=teach]>section::before{content:"";position:absolute;inset:-14% -6%;z-index:-1;pointer-events:none;background:radial-gradient(38% 50% at var(--gx,85%) 45%,var(--gc),transparent 70%)}
"""+secs+"""
#site .te-hero h1 .hl,#site .te-hero h1 .hl *{background-image:none!important;background:none!important}
"""+L+S+"""{background-image:none!important}
#site .st>div{border-top:2px solid var(--c);padding-top:16px}
#site .st>div:nth-child(1){--c:%s}#site .st>div:nth-child(2){--c:%s}#site .st>div:nth-child(3){--c:%s}#site .st>div:nth-child(4){--c:%s}
#site .st>div b{color:var(--c)!important}
#site .tw .ent:nth-child(1) .nm span{color:%s!important}#site .tw .ent:nth-child(2) .nm span{color:%s!important}
#site .ent .mt{color:%s!important}
#site .tw .kk{color:%s!important}
#site .lrn .it:nth-child(1) h3,#site .lrn .it:nth-child(1) .no{color:%s}#site .lrn .it:nth-child(2) h3,#site .lrn .it:nth-child(2) .no{color:%s}#site .lrn .it:nth-child(3) h3,#site .lrn .it:nth-child(3) .no{color:%s}
#site [data-pg=teach] .sh .kk{color:%s!important}
#site .qs .sh2{color:%s!important}
#site .qs cite{color:%s!important}
#site .nx .kk{color:%s!important}
"""%(c1,c2,c3,c4,c2,c3,c1,c2,c1,c2,c4,c4,c2,c1,c1))+extra
T3 = mk('#ebefa0','#ffd29a','#7ff3e4','#ffb9a0',.24,"",hero=['#ebefa0','#ebefa0','#f5de9c','#ffd29a','#ffc49f','#ffb9a0'])
css = T3.replace('#site ', '#site[data-ver="3"] ') + css

# ---- case study pages with the real image files ----
os.environ['PF_IMG'] = os.path.abspath('cw/imgurls.json')
sys.path.insert(0, os.path.abspath('cw'))
import content
pages = [content.alta, content.balance]

layer = ('window.__pfLive=1;window.__pfCSS=' + json.dumps(css) + ';window.__pfHTML=' + json.dumps(pages) +
         ';window.__pfMenuCSS=' + json.dumps(open('cw/menu.css').read()) + ';\n' +
         open('cw/pf.js').read() + '\n' + open('cw/pfmenu.js').read() + '\n' + open('cw/plankton.js').read() +
         "\nwindow.__pfMail=function(){location.href='mailto:Freddie.Grzybowski@gmail.com'};\n")
# only run the layer on the site's own routes
layer = "(function(){var p=location.pathname.replace(/\\/$/,'')||'/';if(!{'/':1,'/about-me':1,'/teaching-experience':1,'/alta-flora':1,'/balance':1}[p])return;\n" + layer + "})();\n"
open('dist/na.js', 'w', encoding='utf-8').write(layer + s)
print('dist/na.js', len(layer + s))
