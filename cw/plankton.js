(function(){
var RM=false;try{RM=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}
var COL=[[127,243,228],[143,232,192],[200,185,255],[235,239,160],[230,224,255]];
function rnd(a,b){return a+Math.random()*(b-a)}
function make(W,H){var n=Math.round(Math.max(14,Math.min(46,W*H/30000))),P=[];
 for(var i=0;i<n;i++)P.push({x:rnd(0,W),y:rnd(0,H),r:rnd(.45,1.15),vy:-rnd(.03,.12),wob:rnd(.2,.6),ph:rnd(0,6.28),tw:rnd(.5,1.4),c:COL[(Math.random()*2)|0],al:rnd(.25,.6)});
 return P}
function draw(o,P,W,H,t){o.clearRect(0,0,W,H);
 for(var i=0;i<P.length;i++){var p=P[i];
  if(!RM){p.y+=p.vy;p.x+=Math.sin(t*.0005*p.wob+p.ph)*.08;if(p.y<-6){p.y=H+6;p.x=rnd(0,W)}}
  var al=p.al*(RM?1:(.6+.4*Math.sin(t*.001*p.tw+p.ph))),cs='rgba('+p.c[0]+','+p.c[1]+','+p.c[2]+',';
  var g=o.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r*3.2);g.addColorStop(0,cs+(al*.5)+')');g.addColorStop(1,cs+'0)');o.fillStyle=g;o.beginPath();o.arc(p.x,p.y,p.r*3.2,0,6.283);o.fill();
  o.fillStyle=cs+al+')';o.beginPath();o.arc(p.x,p.y,p.r,0,6.283);o.fill()}}
var A=window.__pfAfter;
window.__pfAfter=function(s,R){A&&A(s,R);
 var d=s.querySelector('.pf-mn');if(!d)return;
 var cv=document.createElement('canvas');cv.className='pf-plk';cv.setAttribute('aria-hidden','true');d.insertBefore(cv,d.firstChild);
 var o=cv.getContext('2d'),W=0,H=0,P=[],raf=0,mx=-1,my=-1;
 function size(){var dpr=Math.min(2,window.devicePixelRatio||1);W=innerWidth;H=innerHeight;cv.width=W*dpr;cv.height=H*dpr;o.setTransform(dpr,0,0,dpr,0,0);P=make(W,H)}
 function loop(t){draw(o,P,W,H,t);raf=s.classList.contains('mo')&&!RM?requestAnimationFrame(loop):0}
 function start(){if(!W)size();if(RM){draw(o,P,W,H,0);return}if(!raf)raf=requestAnimationFrame(loop)}
 new MutationObserver(function(){if(s.classList.contains('mo'))start()}).observe(s,{attributes:true,attributeFilter:['class']});
 addEventListener('resize',function(){if(W){size();if(RM)draw(o,P,W,H,0)}});
 d.addEventListener('pointermove',function(e){mx=e.clientX;my=e.clientY});d.addEventListener('pointerleave',function(){mx=-1});
 if(s.classList.contains('mo'))start()};
})();
