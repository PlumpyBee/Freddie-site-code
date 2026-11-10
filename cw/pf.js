(function(){
var VER=1,site,R,io,io2,RM=false,lastXY=[innerWidth/2,innerHeight/2];
try{RM=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}
try{var sv=localStorage.getItem('pfver');if(sv!=null&&/^[0-3]$/.test(sv))VER=+sv}catch(e){}
if(window.__pfLive)VER=3;
var NOTES=['Your site exactly as it is live today. Alta Flora and Balance are not built on the live site yet, so those two links show the Version 1 pages.',
'Same site, tidied. Hero text without the box plus a clear way down to the work. Case studies open on a dark hero, then turn into a paper page in the project colour.',
'Everything stays in Night Aurora. Each project keeps the dark look but gets its own glow colour. Work list shows the picture at your cursor on desktop.',
'Each project is its own place: yellow for Teaching, cream and mint for Alta Flora, deep indigo for Balance. The home page stacks them as big colour panels.'];
function $(s,r){return (r||site).querySelector(s)}
function $$(s,r){return [].slice.call((r||site).querySelectorAll(s))}
function setVer(n,quiet){VER=n;if(site)site.setAttribute('data-ver',n);
 [].forEach.call(document.querySelectorAll('.pfb button[data-v]'),function(b){b.setAttribute('aria-pressed',+b.dataset.v===n)});
 var nt=document.getElementById('pfnote');if(nt)nt.textContent=NOTES[n];
 try{localStorage.setItem('pfver',n)}catch(e){}
 if(site){navH();rail()}}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.pfb button');if(!b)return;
 if(b.dataset.v!=null)setVer(+b.dataset.v);
 else if(b.dataset.min!=null){var bar=document.querySelector('.pfb');var m=bar.classList.toggle('min');b.setAttribute('aria-expanded',!m);b.textContent=m?'Versions':'Hide'}});
document.addEventListener('pointerdown',function(e){lastXY=[e.clientX,e.clientY]},true);

window.__pfPages=function(){return (window.__pfHTML||[]).join('')};

function navH(){var n=$('.nav');if(n)site.style.setProperty('--navh',Math.round(n.getBoundingClientRect().height)+'px')}
function curPg(){var p=site.getAttribute('data-p');return $('[data-pg="'+p+'"]')}
var ticking=false;
function rail(){ticking=false;if(!site)return;var pg=curPg();if(!pg||!pg.classList.contains('cs'))return;
 var sh=$('.cs-sheet',pg),r=sh.getBoundingClientRect(),tot=Math.max(1,r.height-innerHeight*.6),pr=Math.min(1,Math.max(0,(120-r.top)/tot));
 var rl=$('.cs-rail',pg);rl.style.setProperty('--prog',pr.toFixed(4));
 var cur='',secs=$$('[data-sec]',pg);secs.forEach(function(s){if(s.getBoundingClientRect().top<innerHeight*.42)cur=s.getAttribute('data-sec')});
 if(rl._cur!==cur){rl._cur=cur;$$('button',rl).forEach(function(b){var on=b.dataset.to===cur;b.setAttribute('aria-current',on);
  if(on){var box=$('.in',rl);var t=b.offsetLeft-(box.clientWidth-b.offsetWidth)/2;if(box.scrollWidth>box.clientWidth)box.scrollTo({left:t,behavior:RM?'auto':'smooth'})}})}}
addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(rail)}},{passive:true});
addEventListener('resize',function(){if(site){navH();rail()}});

function observe(){
 if(!('IntersectionObserver' in window)||RM){$$('.cs-rv,.cs-grow,.cs-tasks').forEach(function(e){e.classList.add('in')});return}
 io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
 $$('.cs-rv').forEach(function(e){io.observe(e)});
 io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io2.unobserve(e.target);if(e.target._cu)e.target._cu()}})},{threshold:.45});
 $$('.cs-grow,.cs-tasks').forEach(function(e){io2.observe(e)});
}
function countUp(){$$('[data-pg=teach] .st b').forEach(function(b){var m=/^(\d+)(.*)$/.exec(b.textContent.trim());if(!m||b._cu)return;var n=+m[1],rest=m[2];
  b._cu=function(){if(site.getAttribute('data-ver')==='0'||RM)return;var t0=null,d=900+n*40;function f(ts){if(t0==null)t0=ts;var k=Math.min(1,(ts-t0)/d),e=1-Math.pow(1-k,3);b.textContent=Math.round(n*e)+rest;if(k<1)requestAnimationFrame(f)}requestAnimationFrame(f)};
  if(io2)io2.observe(b)})}
function notes(){var fine=false;try{fine=matchMedia('(hover:hover) and (pointer:fine)').matches}catch(e){}
 if(!fine)return;$$('.nt').forEach(function(n){var sx,sy,ox=0,oy=0,on=false;
  n.addEventListener('pointerdown',function(e){if(site.getAttribute('data-ver')==='0')return;on=true;sx=e.clientX-ox;sy=e.clientY-oy;n.classList.add('drag');try{n.setPointerCapture(e.pointerId)}catch(x){}});
  n.addEventListener('pointermove',function(e){if(!on)return;ox=Math.max(-260,Math.min(260,e.clientX-sx));oy=Math.max(-160,Math.min(160,e.clientY-sy));n.style.translate=ox+'px '+oy+'px'});
  function up(){on=false;n.classList.remove('drag')}n.addEventListener('pointerup',up);n.addEventListener('pointercancel',up)})}
function compare(){}
function extras(){
 var hero=$('[data-pg=home] .hero');
 if(hero&&!$('.pf-hx',hero)){var d=document.createElement('div');d.className='pf-hx';
  d.innerHTML='<a class="pf-cta1" data-go="work">See my work <i aria-hidden="true">↓</i></a>'
  +'<nav class="pf-dock" aria-label="Projects"><a data-go="teach" style="--c:#ebefa0"><b>01</b><span>UX Design Teaching</span></a><a data-go="alta" style="--c:#8fe8c0"><b>02</b><span>Alta Flora</span></a><a data-go="balance" style="--c:#c8b9ff"><b>03</b><span>Balance</span></a></nav>'
  +'<ul class="pf-facts"><li style="--c:#ebefa0"><b>4 years</b>teaching UX</li><li style="--c:#7ff3e4"><b>14+</b>cohorts taught</li><li style="--c:#c8b9ff"><b>8 years</b>keeping bees</li></ul>';
  hero.appendChild(d)}
 var work=$('#work');
 if(work&&!$('.pf-pan')){var go={t:'teach',a:'alta',b:'balance'},h='';
  $$('.wp',work).forEach(function(w,i){var k=w.getAttribute('data-k'),tags=$$('.tg span',w).map(function(s){return s.textContent}).slice(0,2).join(' · '),im=$('.wi img',w);
   h+='<a class="pf-pn" data-k="'+k+'" data-go="'+go[k]+'" style="--i:'+i+'"><div><span class="kk">0'+(i+1)+' · '+tags+'</span><h3>'+$('h3',w).textContent+'</h3><p>'+$('p',w).textContent+'</p><span class="go">View case study <span aria-hidden="true">→</span></span></div><div class="im"><img src="'+(im?im.src:'')+'" alt=""></div></a>'});
  var s=document.createElement('section');s.className='pf-pan';s.innerHTML=h;work.parentNode.insertBefore(s,work.nextSibling);
  var c=document.createElement('div');c.className='pf-cur';c.setAttribute('aria-hidden','true');
  c.innerHTML=$$('.wp',work).map(function(w){var im=$('.wi img',w);return '<img data-k="'+w.getAttribute('data-k')+'" src="'+(im?im.src:'')+'" alt="">'}).join('');site.appendChild(c);
  var tx=0,ty=0,x=0,y=0,run=false,rt=0;
  function loop(){x+=(tx-x)*.16;y+=(ty-y)*.16;rt+=((tx-x)*.05-rt)*.2;c.style.setProperty('--x',x.toFixed(1)+'px');c.style.setProperty('--y',y.toFixed(1)+'px');c.style.setProperty('--rt',Math.max(-9,Math.min(9,rt)).toFixed(2)+'deg');if(run)requestAnimationFrame(loop)}
  work.addEventListener('pointermove',function(e){var w=e.target.closest('.wp');tx=Math.min(innerWidth-200,Math.max(e.clientX+240,innerWidth*.64));ty=e.clientY;
   if(w){var k=w.getAttribute('data-k');$$('img',c).forEach(function(i){i.classList.toggle('on',i.getAttribute('data-k')===k)});if(!c.classList.contains('on')){x=tx;y=ty;c.classList.add('on')}if(!run){run=true;requestAnimationFrame(loop)}}else{c.classList.remove('on')}});
  work.addEventListener('pointerleave',function(){c.classList.remove('on');run=false})}
 if(!$('.pf-wipe')){var w=document.createElement('i');w.className='pf-wipe';w.setAttribute('aria-hidden','true');site.appendChild(w)}
}
window.__pfAfter=function(s,nsr){site=s;R=nsr;
 if(!R.getElementById('pfcss')){var st=document.createElement('style');st.id='pfcss';st.textContent=window.__pfCSS;R.appendChild(st)}
 site.classList.add('pfjs');setVer(VER,true);extras();observe();countUp();notes();compare();navH();
 site.addEventListener('click',function(e){var b=e.target.closest('.cs-rail button');if(!b)return;var pg=curPg(),t=$('[data-sec="'+b.dataset.to+'"]',pg);if(!t)return;
  var nh=parseFloat(site.style.getPropertyValue('--navh'))||66;window.scrollTo({top:t.getBoundingClientRect().top+scrollY-nh-70,behavior:RM?'auto':'smooth'})});
 setTimeout(function(){navH();rail()},300)};
window.__pfMark=function(p){if(!site)return;requestAnimationFrame(function(){navH();rail()})};
var WC={home:['#03141a','linear-gradient(180deg,#0b3a44,#03141a)'],about:['#0a332b','linear-gradient(180deg,#0f4a4a,#03141a)'],teach:['#ebefa0','linear-gradient(180deg,#ebefa0,#7ff3e4)'],alta:['#f7f2e6','linear-gradient(180deg,#8fe8c0,#ffb9a0)'],balance:['#1c1757','linear-gradient(180deg,#c8b9ff,#1c1757)']};
window.__pfWipe=function(x,el,cb){var v=site?+site.getAttribute('data-ver'):0,w=site&&$('.pf-wipe');
 if(RM||v<2||!w||!w.animate||!WC[x]){cb();return}
 var X=lastXY[0],Y=lastXY[1],rad=Math.hypot(Math.max(X,innerWidth-X),Math.max(Y,innerHeight-Y))+40,a;
 w.style.opacity=1;
 if(v===3){w.style.background=WC[x][0];a=w.animate([{clipPath:'circle(0px at '+X+'px '+Y+'px)'},{clipPath:'circle('+rad+'px at '+X+'px '+Y+'px)'}],{duration:520,easing:'cubic-bezier(.7,0,.2,1)',fill:'forwards'})}
 else{w.style.background=WC[x][1];a=w.animate([{clipPath:'inset(100% 0 0 0)'},{clipPath:'inset(0 0 0 0)'}],{duration:460,easing:'cubic-bezier(.7,0,.2,1)',fill:'forwards'})}
 var done=false;function fin(){if(done)return;done=true;cb();setTimeout(function(){var b=w.animate([{opacity:1},{opacity:0}],{duration:420,easing:'ease-out',fill:'forwards'});b.onfinish=function(){a.cancel();b.cancel();w.style.opacity=0}},60)}
 a.onfinish=fin;setTimeout(fin,800)};
window.__pfMail=function(){var t=document.getElementById('pftoast');t.hidden=false;clearTimeout(t._t);t._t=setTimeout(function(){t.hidden=true},6000);
 try{navigator.clipboard.writeText('Freddie.Grzybowski@gmail.com').then(function(){document.getElementById('pftm').textContent='Email address copied'},function(){})}catch(e){}};
document.addEventListener('DOMContentLoaded',function(){setVer(VER)});
})();
