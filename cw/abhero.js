(function(){
var A=window.__pfAfter;
try{CSS.registerProperty({name:'--hcang',syntax:'<angle>',inherits:false,initialValue:'0deg'})}catch(e){}
if(!window.__pfGxBar){window.__pfGxBar=1;document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.pfb button[data-gx]');if(!b)return;var h=document.getElementById('na-host'),s=h&&h.shadowRoot.querySelector('#site');if(!s)return;s.setAttribute('data-gx',b.dataset.gx);try{localStorage.setItem('pfgx',b.dataset.gx)}catch(x){}[].forEach.call(document.querySelectorAll('.pfb [data-gx]'),function(x){x.setAttribute('aria-pressed',x===b)});if(s.getAttribute('data-p')!=='home'){var a=s.querySelector('.nv [data-go=home]');a&&a.click()}scrollTo({top:0,behavior:'smooth'})})}
if(!window.__pfHcBar){window.__pfHcBar=1;document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.pfb button[data-hc]');if(!b)return;var h=document.getElementById('na-host'),s=h&&h.shadowRoot.querySelector('#site');if(!s)return;s.setAttribute('data-hc',b.dataset.hc);try{localStorage.setItem('pfhc4',b.dataset.hc)}catch(x){}[].forEach.call(document.querySelectorAll('.pfb [data-hc]'),function(x){x.setAttribute('aria-pressed',x===b)});if(s.getAttribute('data-p')!=='home'){var a=s.querySelector('.nv [data-go=home]');a&&a.click()}scrollTo({top:0,behavior:'smooth'})})}
window.__pfAfter=function(s,R){A&&A(s,R);
 var st=document.createElement('style');st.textContent=window.__pfStar3CSS||'';R.appendChild(st);
 var RM=false;try{RM=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}
 var pg=s.querySelector('[data-pg=about]');if(!pg)return;
 var hero=pg.querySelector('.ab-hero'),lp=hero&&hero.querySelector('.lead'),lead=lp?lp.textContent.trim():'';
 var k=lead.indexOf('. '),st1=k>0?lead.slice(0,k+1):lead,rest=k>0?lead.slice(k+2):'';
 // real profile links (they used to open email) + heading levels + footer link size
 var LNK={LinkedIn:'https://www.linkedin.com/in/freddiegrzybowski/',Medium:'https://medium.com/@freddie.grzybowski'};
 function fixLinks(){[].forEach.call(s.querySelectorAll('[data-go=mail]'),function(e){var t=e.textContent.trim();if(!LNK[t])return;var a=e;if(e.tagName!=='A'){a=document.createElement('a');a.className=e.className;a.textContent=t;e.parentNode.replaceChild(a,e)}a.removeAttribute('data-go');a.href=LNK[t];a.target='_blank';a.rel='noopener';a.setAttribute('aria-label',t+' (opens in a new tab)')})}
 fixLinks();new MutationObserver(function(){if(s.querySelector('[data-go=mail]')&&[].some.call(s.querySelectorAll('[data-go=mail]'),function(e){return LNK[e.textContent.trim()]}))fixLinks()}).observe(s,{childList:true,subtree:true});
 [].forEach.call(s.querySelectorAll('.x-tk h4'),function(h){h.setAttribute('role','heading');h.setAttribute('aria-level','3')});
 var hfx=s.querySelector('[data-pg=home] .hfx');
 [].forEach.call(s.querySelectorAll('.tl-big'),function(e){e.setAttribute('aria-hidden','true')});
 var TXT='<div class="rcol"><p class="st1">'+st1+'</p>'+(rest?'<p class="rest">'+rest+'</p>':'')+'<div class="cta"><a class="bt" data-pfw4 href="#work">See my work <span aria-hidden="true">→</span></a><a class="rt" data-pfroute4 href="#route">How I got here <i aria-hidden="true">↓</i></a></div></div>';
 var HEAD='<p class="ey">About me</p><h1>Hey, I’m<b>Freddie.</b></h1>';
 ['70','71'].forEach(function(n){var d=document.createElement('div');d.className='pf-abh hb7 ah'+n;
  d.innerHTML='<div class="stage"><div class="aur4" aria-hidden="true"></div><canvas class="stars" aria-hidden="true"></canvas>'+(n!=='68'?'<div class="grp">'+HEAD+TXT+'</div>':HEAD+TXT)+'</div>';
  if(hfx)d.querySelector('.aur4').appendChild(hfx.cloneNode(true));hero.appendChild(d)});
 hero.addEventListener('click',function(e){var b=e.target.closest('[data-pfw4],[data-pfroute4]');if(!b)return;e.preventDefault();
  if(b.hasAttribute('data-pfroute4')){var t=pg.querySelector('.tl-sec');if(t)t.scrollIntoView({behavior:RM?'auto':'smooth'});return}
  var hm=s.querySelector('.nv [data-go=home]');if(hm)hm.click();setTimeout(function(){var w=s.querySelector('#work');if(w)w.scrollIntoView({behavior:'smooth'})},900)},true);
 function sizeCv(cv){var W=cv.clientWidth,H=cv.clientHeight,dpr=Math.min(2,devicePixelRatio||1);if(cv.width!==Math.round(W*dpr)||cv.height!==Math.round(H*dpr)){cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr)}var o=cv.getContext('2d');o.setTransform(dpr,0,0,dpr,0,0);return [o,W,H]}
 var SK={};
 ['70','71'].forEach(function(key){var w=hero.querySelector('.ah'+key+' .stage'),cv=w.querySelector('canvas.stars'),au=w.querySelector('.aur4'),BG=[],SH=[],mx=-9e3,my=-9e3,tx=0,cx=0,run=0;
  w.addEventListener('pointermove',function(e){var r=w.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top;tx=mx/r.width-.5});
  w.addEventListener('pointerleave',function(){mx=my=-9e3;tx=0});
  function loop(t){if(s.getAttribute('data-abh')!==key||s.getAttribute('data-p')!=='about'){run=0;return}
   var rr=w.getBoundingClientRect();if(rr.bottom<0){requestAnimationFrame(loop);return}
   var r=sizeCv(cv),o=r[0],W=r[1],H=r[2];o.clearRect(0,0,W,H);
   if(!BG.length)for(var q=0;q<Math.round(W*H/5000);q++)BG.push([Math.random(),Math.random()*.75,Math.random()<.08?Math.random()*1.1+1.1:Math.random()*.9+.3,Math.random()*6,Math.random()*.4+.15]);
   if(!RM)cx+=(tx-cx)*.03;
   var sc=Math.max(0,Math.min(1,-rr.top/(rr.height*.8)));
   au.style.opacity=(1-sc*.6).toFixed(3);
   BG.forEach(function(b){var x=b[0]*W,y=b[1]*H,dd=Math.hypot(x-mx,y-my),boost=dd<170?(1-dd/170):0;o.globalAlpha=Math.min(1,b[4]+(RM?0:.22*Math.sin(t*.0012+b[3]))+boost*.8);o.fillStyle=b[2]>1.1?'#fffbe6':'#e6fffb';o.beginPath();o.arc(x,y,b[2]+boost*1.2,0,6.283);o.fill()});
   if(!RM&&Math.random()<.004&&!SH.length)SH.push({x:W*(.15+Math.random()*.6),y:H*(.04+Math.random()*.2),vx:7+Math.random()*3,vy:2.4+Math.random()*1.5,l:1});
   SH=SH.filter(function(z){z.x+=z.vx;z.y+=z.vy;z.l-=.016;var g=o.createLinearGradient(z.x,z.y,z.x-z.vx*16,z.y-z.vy*16);g.addColorStop(0,'rgba(255,255,255,'+Math.max(0,z.l)+')');g.addColorStop(1,'rgba(127,243,228,0)');o.globalAlpha=1;o.strokeStyle=g;o.lineWidth=1.6;o.beginPath();o.moveTo(z.x,z.y);o.lineTo(z.x-z.vx*16,z.y-z.vy*16);o.stroke();return z.l>0});
   o.globalAlpha=1;requestAnimationFrame(loop)}
  SK[key]=function(){if(!run){run=1;requestAnimationFrame(loop)}}});

 // ---- calm starfield behind the top of every page (replaces the drifting dots) ----
 (function(){var bg=s.querySelector('.bgfx');if(!bg||bg.querySelector('.stx'))return;var cv=document.createElement('canvas');cv.className='stx';cv.setAttribute('aria-hidden','true');bg.appendChild(cv);
  var ST=[],SH=[],mx=-9e3,my=-9e3,run=0,lw=0;
  addEventListener('pointermove',function(e){var r=cv.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top},{passive:true});
  function loop(t){if(s.getAttribute('data-ver')!=='3'){run=0;return}
   var p=s.getAttribute('data-p');if(p==='about'||p==='alta'||scrollY>900||document.hidden){requestAnimationFrame(loop);return}
   var r=sizeCv(cv),o=r[0],W=r[1],H=r[2];if(!W){requestAnimationFrame(loop);return}
   if(W!==lw){lw=W;ST=[];for(var q=0;q<Math.round(W*H/5200);q++)ST.push([Math.random(),Math.random()*.85,Math.random()<.07?Math.random()*1+1.1:Math.random()*.8+.3,Math.random()*6,Math.random()*.35+.15])}
   o.clearRect(0,0,W,H);
   ST.forEach(function(b){var x=b[0]*W,y=b[1]*H,d=Math.hypot(x-mx,y-my),k=d<150?(1-d/150):0;o.globalAlpha=Math.min(1,b[4]+(RM?0:.2*Math.sin(t*.0011+b[3]))+k*.7);o.fillStyle=b[2]>1.1?'#fffbe6':'#e6fffb';o.beginPath();o.arc(x,y,b[2]+k,0,6.283);o.fill()});
   if(!RM&&Math.random()<.0025&&!SH.length)SH.push({x:W*(.1+Math.random()*.6),y:H*(.03+Math.random()*.2),vx:7+Math.random()*3,vy:2.2+Math.random()*1.4,l:1});
   SH=SH.filter(function(z){z.x+=z.vx;z.y+=z.vy;z.l-=.016;var g=o.createLinearGradient(z.x,z.y,z.x-z.vx*16,z.y-z.vy*16);g.addColorStop(0,'rgba(255,255,255,'+Math.max(0,z.l)+')');g.addColorStop(1,'rgba(127,243,228,0)');o.globalAlpha=1;o.strokeStyle=g;o.lineWidth=1.5;o.beginPath();o.moveTo(z.x,z.y);o.lineTo(z.x-z.vx*16,z.y-z.vy*16);o.stroke();return z.l>0});
   o.globalAlpha=1;requestAnimationFrame(loop)}
  if(!run){run=1;requestAnimationFrame(loop)}})();
 if(document.querySelector('.pfb')&&!s.getAttribute('data-hc')){var hc='1';try{hc=localStorage.getItem('pfhc4')||'12'}catch(e){}s.setAttribute('data-hc',hc)}

 // ---- closing headline: 'people love.' painted letter by letter in aurora colours ----
 (function(){var ch=[].slice.call(s.querySelectorAll('[data-pg=about] .cta2 h2 .wd:nth-child(n+4) .ch'));var C=[[127,243,228],[200,185,255],[255,185,160],[255,210,154]];ch.forEach(function(e,i){var t=ch.length>1?i/(ch.length-1):0,k=Math.min(C.length-2,Math.floor(t*(C.length-1))),f=t*(C.length-1)-k,a=C[k],b=C[k+1];e.style.setProperty('--cc','rgb('+a.map(function(v,j){return Math.round(v+(b[j]-v)*f)}).join(',')+')')})})();
 // ---- home hero galaxy options ----
 (function(){var hero=s.querySelector('[data-pg=home] .hero');if(!hero||hero.querySelector('.gx'))return;var g=document.createElement('div');g.className='gx';g.setAttribute('aria-hidden','true');g.innerHTML='<div class="gxs"><canvas></canvas></div><div class="gxm"><canvas></canvas></div><div class="gxn"><i></i><i></i><i></i><i></i><canvas></canvas></div>';hero.insertBefore(g,hero.firstChild);
  function rnd(a){var x=Math.sin(a*12.9898)*43758.5453;return x-Math.floor(x)}
  function spiral(cv){var S=600;cv.width=cv.height=S;var o=cv.getContext('2d'),c=S/2;var gl=o.createRadialGradient(c,c,0,c,c,c*.9);gl.addColorStop(0,'rgba(255,240,220,.9)');gl.addColorStop(.08,'rgba(255,220,200,.45)');gl.addColorStop(.35,'rgba(160,140,255,.12)');gl.addColorStop(1,'rgba(40,200,220,0)');o.fillStyle=gl;o.fillRect(0,0,S,S);
   for(var i=0;i<5200;i++){var arm=i%2,t=rnd(i+1)*4.2,r=8+t*62+rnd(i+7)*18,a=t*1.15+arm*Math.PI+(rnd(i+3)-.5)*.55,x=c+Math.cos(a)*r,y=c+Math.sin(a)*r,f=1-r/290;if(f<=0)continue;o.globalAlpha=Math.min(1,f*.9)*(.35+rnd(i+5)*.65);o.fillStyle=rnd(i+9)<.5?'#e6fffb':(rnd(i+11)<.5?'#c8b9ff':'#ffd6c4');o.fillRect(x,y,rnd(i+2)<.06?1.8:1,rnd(i+2)<.06?1.8:1)}o.globalAlpha=1}
  function band(cv){var W=cv.width=Math.min(2400,cv.clientWidth*1.5||1800),H=cv.height=Math.round(W*.55),o=cv.getContext('2d');o.clearRect(0,0,W,H);
   o.save();o.translate(W*.5,H*.42);o.rotate(-.32);var gr=o.createLinearGradient(0,-H*.22,0,H*.22);gr.addColorStop(0,'rgba(120,150,255,0)');gr.addColorStop(.35,'rgba(150,130,255,.16)');gr.addColorStop(.5,'rgba(220,210,255,.24)');gr.addColorStop(.65,'rgba(80,200,220,.14)');gr.addColorStop(1,'rgba(80,200,220,0)');o.fillStyle=gr;o.fillRect(-W,-H*.22,W*2,H*.44);
   for(var i=0;i<9000;i++){var x=(rnd(i+1)-.5)*W*1.6,y=(rnd(i+2)+rnd(i+3)+rnd(i+4)-1.5)*H*.16;o.globalAlpha=.25+rnd(i+5)*.6;o.fillStyle=rnd(i+6)<.15?'#fff4e0':'#e6fffb';var z=rnd(i+7)<.04?1.6:.8;o.fillRect(x,y,z,z)}
   o.globalAlpha=.55;for(var k=0;k<14;k++){var dx=(rnd(k+40)-.5)*W*1.3,dy=(rnd(k+50)-.5)*H*.06;var d=o.createRadialGradient(dx,dy,0,dx,dy,60+rnd(k+60)*120);d.addColorStop(0,'rgba(3,20,26,.8)');d.addColorStop(1,'rgba(3,20,26,0)');o.fillStyle=d;o.fillRect(dx-200,dy-200,400,400)}o.restore();o.globalAlpha=1}
  function cluster(cv){var W=cv.width=1600,H=cv.height=900,o=cv.getContext('2d');[[.14,.24,120],[.84,.2,90]].forEach(function(cl,ci){for(var i=0;i<cl[2];i++){var a=rnd(i+ci*300)*6.283,r=Math.pow(rnd(i+ci*300+1),2)*160;o.globalAlpha=.3+rnd(i+ci*300+2)*.7;o.fillStyle=rnd(i+ci*300+3)<.3?'#fff4e0':'#e6fffb';var z=rnd(i+ci*300+4)<.1?2.2:1.1;o.beginPath();o.arc(cl[0]*W+Math.cos(a)*r,cl[1]*H+Math.sin(a)*r*.7,z,0,6.283);o.fill()}});o.globalAlpha=1}
  spiral(g.querySelector('.gxs canvas'));cluster(g.querySelector('.gxn canvas'));
  var b2=g.querySelector('.gxm canvas');function doBand(){if(s.getAttribute('data-gx')==='2'&&!b2.dataset.done){b2.dataset.done=1;band(b2)}}
  new MutationObserver(doBand).observe(s,{attributes:true,attributeFilter:['data-gx','data-p']});setTimeout(doBand,200);
  if(document.querySelector('.pfb')&&!s.getAttribute('data-gx')){var v='0';try{v=localStorage.getItem('pfgx')||'0'}catch(e){}s.setAttribute('data-gx',v)}
 })();
 function go(){if(s.getAttribute('data-p')!=='about')return;var a=s.getAttribute('data-abh');if(SK[a])SK[a]()}
 new MutationObserver(go).observe(s,{attributes:true,attributeFilter:['data-abh','data-p']});setTimeout(go,300);
};
})();
