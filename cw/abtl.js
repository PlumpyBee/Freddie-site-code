(function(){
var A=window.__pfAfter;
window.__pfAfter=function(s,R){A&&A(s,R);
 var st=document.createElement('style');st.textContent=window.__pfStar2CSS||'';R.appendChild(st);
 var RM=false;try{RM=matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){}
 var pg=s.querySelector('[data-pg=about]');if(!pg)return;
 function sizeCv(cv,cap){var W=cv.clientWidth,H=cv.clientHeight,dpr=Math.min(cap||2,devicePixelRatio||1);if(cv.width!==Math.round(W*dpr)||cv.height!==Math.round(H*dpr)){cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr)}var o=cv.getContext('2d');o.setTransform(dpr,0,0,dpr,0,0);return [o,W,H]}
 // ---------- timeline routes on the existing cards (4–6) ----------
 var box=pg.querySelector('.tl-steps');if(!box)return;
 var cv=document.createElement('canvas');cv.className='tlx';cv.setAttribute('aria-hidden','true');box.insertBefore(cv,box.firstChild.nextSibling);
 var steps=[].slice.call(box.querySelectorAll('.tl-step')),AC=['#7ff3e4','#ffd29a','#ffb9a0'],RGB=[[127,243,228],[255,210,154],[255,185,160]];
 var G=null,gk='',ign=[],P6=[],max6=-1,hist=[],run2=0;
 function rgba(i,a){var c=RGB[Math.max(0,Math.min(2,i))];return 'rgba('+c[0]+','+c[1]+','+c[2]+','+a+')'}
 function geo(){var r=box.getBoundingClientRect(),W=r.width,H=r.height,key=Math.round(W)+'x'+Math.round(H);if(key===gk&&G)return G;gk=key;
  var C=steps.map(function(stp){var hx=stp.querySelector('.tl-hex').getBoundingClientRect(),cd=stp.querySelector('.tl-card').getBoundingClientRect();var x=hx.left+hx.width/2-r.left;return {x:x,y:hx.top+hx.height/2-r.top,side:(cd.left+cd.width/2-r.left)>x?-1:1}});
  var mob=W<700;
  // curvy route (4 & 6): smooth curve through the chapter stars
  var pts=[[C[0].x,-10]].concat(C.map(function(c){return [c.x,c.y]})).concat([[C[C.length-1].x,H+10]]);var S=[],prev=null;
  for(var i=1;i<pts.length;i++){var a=pts[i-1],b=pts[i],sw=(i%2?1:-1)*(mob?18:Math.min(110,W*.08));for(var t=0;t<=1;t+=.004){var u=1-t;var x=u*u*u*a[0]+3*u*u*t*(a[0]+sw)+3*u*t*t*(b[0]+sw)+t*t*t*b[0],y=u*u*u*a[1]+3*u*u*t*(a[1]+(b[1]-a[1])*.5)+3*u*t*t*(b[1]-(b[1]-a[1])*.5)+t*t*t*b[1];if(!prev||Math.hypot(x-prev[0],y-prev[1])>=3){S.push([x,y]);prev=[x,y]}}}
  var dust=[];for(var j=0;j<S.length;j+=4){var p=S[j];dust.push([p[0]+(Math.random()-.5)*7,p[1]+(Math.random()-.5)*7,Math.random()*1.1+.35,Math.random()*6])}
  // constellation route (5): straight lines with in-between stars
  var V=[[C[0].x,-10]];C.forEach(function(c,i){if(i){var p0=C[i-1];[.34,.68].forEach(function(f,k){V.push([p0.x+(c.x-p0.x)*f+(mob?(k?-10:10):(k?-1:1)*W*.07*(i%2?1:-1)),p0.y+(c.y-p0.y)*f,'m'])})}V.push([c.x,c.y,'c',i])});V.push([C[C.length-1].x+(mob?0:W*.05),H-30,'m']);
  G={W:W,H:H,C:C,S:S,dust:dust,V:V,mob:mob};ign=C.map(function(){return 0});P6=[];max6=-1;hist=[];return G}
 function headY(){var r=box.getBoundingClientRect();if(RM)return r.height+20;return Math.max(-20,Math.min(r.height+20,innerHeight*.8-r.top+r.height*.04))}
 function segAt(y,C){var i=0;while(i<C.length&&C[i].y<=y+2)i++;return Math.max(0,i-1)}
 function star4(o,x,y,r,rot){o.save();o.translate(x,y);o.rotate(rot||0);o.beginPath();o.moveTo(0,-r);o.quadraticCurveTo(r*.12,-r*.12,r,0);o.quadraticCurveTo(r*.12,r*.12,0,r);o.quadraticCurveTo(-r*.12,r*.12,-r,0);o.quadraticCurveTo(-r*.12,-r*.12,0,-r);o.fill();o.restore()}
 function comet(o,x,y,c,tail,big){var g=o.createRadialGradient(x,y,0,x,y,big?34:24);g.addColorStop(0,'rgba(255,255,255,.95)');g.addColorStop(.25,c.replace(/[\d.]+\)$/,'.6)'));g.addColorStop(1,c.replace(/[\d.]+\)$/,'0)'));o.globalAlpha=1;o.fillStyle=g;o.beginPath();o.arc(x,y,big?34:24,0,6.283);o.fill();o.fillStyle='#fff';o.beginPath();o.arc(x,y,3.2,0,6.283);o.fill();
  if(tail&&tail.length>1){for(var i=1;i<tail.length;i++){var f=i/tail.length;o.strokeStyle=c.replace(/[\d.]+\)$/,(f*.8).toFixed(2)+')');o.lineWidth=f*(big?5:3.5);o.beginPath();o.moveTo(tail[i-1][0],tail[i-1][1]);o.lineTo(tail[i][0],tail[i][1]);o.stroke()}}}
 function chapterStars(o,g,t,hy){g.C.forEach(function(c,i){var lit=c.y<=hy+1;if(lit&&!ign[i])ign[i]=t;if(!lit)ign[i]=0;var e=ign[i]?Math.min(1,(t-ign[i])/900):0;
  if(!lit){o.globalAlpha=.5;o.fillStyle='rgba(254,253,246,.55)';star4(o,c.x,c.y,9,0);o.globalAlpha=.25;o.strokeStyle='rgba(254,253,246,.6)';o.lineWidth=1;o.beginPath();o.arc(c.x,c.y,15,0,6.283);o.stroke();return}
  var pul=RM?1:1+.06*Math.sin(t*.003+i);
  var gl=o.createRadialGradient(c.x,c.y,0,c.x,c.y,58);gl.addColorStop(0,rgba(i,.55));gl.addColorStop(1,rgba(i,0));o.globalAlpha=1;o.fillStyle=gl;o.beginPath();o.arc(c.x,c.y,58,0,6.283);o.fill();
  o.fillStyle='#fff';o.shadowColor=AC[i];o.shadowBlur=18;star4(o,c.x,c.y,(16+6*(1-e))*pul,RM?0:t*.0003+i);o.shadowBlur=0;o.globalAlpha=.9;star4(o,c.x,c.y,7,Math.PI/4);
  if(e<1&&!RM){o.globalAlpha=1-e;o.strokeStyle=AC[i];o.lineWidth=2*(1-e)+.5;o.beginPath();o.arc(c.x,c.y,16+e*60,0,6.283);o.stroke();
   for(var k=0;k<8;k++){var a=k/8*6.283+i,rr=18+e*46;o.fillStyle=AC[i];star4(o,c.x+Math.cos(a)*rr,c.y+Math.sin(a)*rr,4*(1-e)+1,0)}}
  o.globalAlpha=1})}
 // mini constellations for route 5 (music note, honeycomb, cursor)
 var MINI=[[[[-.55,.55],[-.2,.42],[-.08,.66],[-.42,.84],[-.55,.55]],[[-.08,.6],[0,-.85],[.46,-.5],[.38,-.1]]],
  (function(){function hx(cx,cy,r){var a=[];for(var i=0;i<=6;i++){var t=i/6*6.283+Math.PI/6;a.push([cx+Math.cos(t)*r,cy+Math.sin(t)*r])}return a}return [hx(-.36,.18,.42),hx(.37,-.25,.42)]})(),
  [[[-.45,-.85],[-.45,.6],[-.12,.28],[.12,.85],[.34,.74],[.1,.18],[.52,.18],[-.45,-.85]]]];
 var MNAME=['Music','Bees','Design'];
 function mini(o,g,t,i){if(g.mob)return;var c=g.C[i];if(!ign[i])return;var e=RM?1:Math.min(1,(t-ign[i]-200)/1400);if(e<=0)return;var R=Math.min(70,g.W*.055),cx=c.x+c.side*Math.min(250,g.W*.2),cy=c.y-10;
  var segs=[];MINI[i].forEach(function(pl){for(var k=1;k<pl.length;k++)segs.push([pl[k-1],pl[k]])});var n=segs.length*e;
  o.strokeStyle=rgba(i,.6);o.lineWidth=1.2;segs.forEach(function(sg,k){if(k>=n)return;var f=Math.min(1,n-k);var a=[cx+sg[0][0]*R,cy+sg[0][1]*R],b=[cx+sg[1][0]*R,cy+sg[1][1]*R];o.globalAlpha=1;o.beginPath();o.moveTo(a[0],a[1]);o.lineTo(a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f);o.stroke();o.fillStyle='#fff';o.shadowColor=AC[i];o.shadowBlur=8;o.beginPath();o.arc(a[0],a[1],1.8,0,6.283);o.fill();o.shadowBlur=0});
  o.globalAlpha=e*.75;o.fillStyle=AC[i];o.font='600 11px Montserrat, Arial, sans-serif';o.textAlign='center';o.fillText(('0'+(i+1))+' · '+MNAME[i].toUpperCase(),cx,cy+R+26);o.textAlign='left';o.globalAlpha=1}
 function frame(t){var tl=s.getAttribute('data-tl');if(['4','5','6'].indexOf(tl)<0||s.getAttribute('data-p')!=='about'||s.getAttribute('data-ver')!=='3'){run2=0;return}
  var r=box.getBoundingClientRect();if(r.bottom<-50||r.top>innerHeight+50){requestAnimationFrame(frame);return}
  var br=box.getBoundingClientRect(),pL=Math.max(0,Math.min(90,Math.floor(br.left))),pR=Math.max(0,Math.min(90,Math.floor(document.documentElement.clientWidth-br.right)));cv.style.left=(-pL)+'px';cv.style.width='calc(100% + '+(pL+pR)+'px)';var g=geo(),q=sizeCv(cv,1.5),o=q[0];o.clearRect(0,0,q[1],q[2]);o.translate(pL,0);var hy=headY();
  if(tl==='4'){ // refined star route: stardust trail + glowing line + comet
   g.dust.forEach(function(dd){var on=dd[1]<=hy,si=segAt(dd[1],g.C);o.globalAlpha=on?.55+.35*Math.sin(t*.002+dd[3]):.12+(RM?0:.08*Math.sin(t*.0015+dd[3]));o.fillStyle=on?AC[si]:'#e6fffb';o.beginPath();o.arc(dd[0],dd[1],dd[2],0,6.283);o.fill()});
   var hi=0;while(hi<g.S.length-1&&g.S[hi+1][1]<=hy)hi++;
   o.globalAlpha=1;o.lineCap='round';o.lineWidth=2.2;o.shadowBlur=10;for(var i=1;i<=hi;i++){var si=segAt(g.S[i][1],g.C);o.strokeStyle=rgba(si,.85);o.shadowColor=AC[si];o.beginPath();o.moveTo(g.S[i-1][0],g.S[i-1][1]);o.lineTo(g.S[i][0],g.S[i][1]);o.stroke()}o.shadowBlur=0;
   chapterStars(o,g,t,hy);
   if(hi>0&&hi<g.S.length-1){var hp=g.S[hi];comet(o,hp[0],hp[1],rgba(segAt(hp[1],g.C),1),g.S.slice(Math.max(0,hi-30),hi+1))}}
  else if(tl==='5'){ // constellation lines + mini constellations
   var V=g.V;o.lineCap='round';
   for(var k=1;k<V.length;k++){var a=V[k-1],b=V[k];o.globalAlpha=.22;o.strokeStyle='#e6fffb';o.setLineDash([2,8]);o.lineWidth=1.4;o.beginPath();o.moveTo(a[0],a[1]);o.lineTo(b[0],b[1]);o.stroke();o.setLineDash([]);
    if(a[1]<hy){var f=Math.min(1,(hy-a[1])/Math.max(1,b[1]-a[1]));var si=segAt(a[1]+1,g.C);o.globalAlpha=1;o.strokeStyle=rgba(si,.9);o.shadowColor=AC[si];o.shadowBlur=10;o.lineWidth=2;o.beginPath();o.moveTo(a[0],a[1]);var ex=a[0]+(b[0]-a[0])*f,ey=a[1]+(b[1]-a[1])*f;o.lineTo(ex,ey);o.stroke();o.shadowBlur=0;if(f<1&&!RM){comet(o,ex,ey,rgba(si,1),null)}}}
   V.forEach(function(v){if(v[2]!=='m')return;var on=v[1]<=hy;o.globalAlpha=on?1:.4;o.fillStyle='#fff';o.shadowColor=AC[segAt(v[1],g.C)];o.shadowBlur=on?12:0;o.beginPath();o.arc(v[0],v[1],on?3:2,0,6.283);o.fill();o.shadowBlur=0});
   chapterStars(o,g,t,hy);g.C.forEach(function(c,i){mini(o,g,t,i)})}
  else { // shooting star: stardust left behind as it travels
   var hi2=0;while(hi2<g.S.length-1&&g.S[hi2+1][1]<=hy)hi2++;
   if(RM&&!P6.length){g.S.forEach(function(p,i){if(i%2)return;P6.push({x:p[0]+(Math.random()-.5)*14,y:p[1]+(Math.random()-.5)*14,vx:0,vy:0,b:-9e9,c:segAt(p[1],g.C),s:Math.random()*1.3+.4,tw:Math.random()*6})});max6=g.S.length}
   if(hi2>max6){for(var m=Math.max(0,max6);m<=hi2;m++){var p=g.S[m],nx=0,ny=0;if(g.S[m+1]){var dx=g.S[m+1][0]-p[0],dy=g.S[m+1][1]-p[1],L=Math.hypot(dx,dy)||1;nx=-dy/L;ny=dx/L}for(var e2=0;e2<3;e2++){var off=(Math.random()-.5)*(Math.random()<.2?40:16);P6.push({x:p[0]+nx*off,y:p[1]+ny*off,vx:nx*(Math.random()-.5)*.5,vy:ny*(Math.random()-.5)*.5+(Math.random()-.5)*.2,b:t,c:segAt(p[1],g.C),s:Math.random()*1.4+.3,tw:Math.random()*6})}}max6=hi2}
   for(var gi=0;gi<g.S.length;gi+=10){if(gi<=max6)continue;o.globalAlpha=.07;o.fillStyle='#e6fffb';o.beginPath();o.arc(g.S[gi][0],g.S[gi][1],1,0,6.283);o.fill()}
   P6.forEach(function(z){var age=(t-z.b)/1000;if(age<2.5){z.x+=z.vx;z.y+=z.vy;z.vx*=.97;z.vy*=.97}var a=age<2?1-age*.32:.36;o.globalAlpha=Math.max(.15,a*(.7+.3*Math.sin(t*.003+z.tw)));o.fillStyle=age<.4?'#fff':AC[z.c];o.beginPath();o.arc(z.x,z.y,z.s*(age<.4?1.5:1),0,6.283);o.fill()});
   var hp2=g.S[hi2];hist.push([hp2[0],hp2[1]]);if(hist.length>16)hist.shift();var moving=hist.length>2&&Math.hypot(hist[0][0]-hp2[0],hist[0][1]-hp2[1])>4;
   chapterStars(o,g,t,hy);
   if(hi2>0&&hi2<g.S.length-1)comet(o,hp2[0],hp2[1],rgba(segAt(hp2[1],g.C),1),moving?g.S.slice(Math.max(0,hi2-60),hi2+1):g.S.slice(Math.max(0,hi2-6),hi2+1),true)}
  o.globalAlpha=1;requestAnimationFrame(frame)}
 function tlGo(){gk='';G=null;if(!run2){run2=1;requestAnimationFrame(frame)}}
 new MutationObserver(function(){setTimeout(tlGo,150)}).observe(s,{attributes:true,attributeFilter:['data-tl','data-p','data-ver','data-abh']});
 addEventListener('resize',function(){gk=''});
 setTimeout(tlGo,400);
};
})();
