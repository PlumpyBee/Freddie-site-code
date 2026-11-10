(function(){
var MN='a';try{var m=localStorage.getItem('pfmn');if(/^[a-e]$/.test(m||''))MN=m}catch(e){}
if(window.__pfLive)MN='b';
var ITEMS=[
 ['home','Home','Start here',['UX/UI designer','Portfolio','Based in UK'],'#7ff3e4'],
 ['about','About','The scenic route to design',['Beekeeper','Streaming','Guitar teaching','UK-based'],'#ffb9a0'],
 ['teach','Teaching','Four years of teaching UX',['UX teaching','4 years','General Assembly','Berghs'],'#ebefa0'],
 ['alta','Alta Flora','Healthtech · 3 week sprint',['Mobile app','Healthtech','3 weeks','Onboarding'],'#8fe8c0'],
 ['balance','Balance','Wellbeing · 2 week sprint',['Mobile app','Wellbeing','2 weeks','EEG data'],'#c8b9ff'],
 ['mail','Say hello','Freddie.Grzybowski@gmail.com',['Email','LinkedIn','Medium'],'#fefdf6']];
var W3={home:['#0b3a44','#fefdf6','rgba(127,243,228,.35)'],about:['#ffb9a0','#03141a'],teach:['#ebefa0','#0a332b'],alta:['#f7f2e6','#12352b','rgba(143,232,192,.8)'],balance:['#1c1757','#f4f1ff','rgba(200,185,255,.35)'],mail:['#7ff3e4','#03141a']};
var NOTE={'1a':'Menu A: page links with a contact card (copy email, LinkedIn, Medium, London time).','1b':'Menu B: page links with a short “about me” in brief.',
 '2a':'Menu A: big centred links; the aurora behind them changes to each page’s colour as you hover.','2b':'Menu B: rows fill with the page colour and a ticker of tags runs across.',
 '3a':'Menu A: full-height colour bands, one per page; the one you hover grows.','3b':'Menu B (live now): colour tiles in each page’s world colour.','3c':'Menu C: colour circles that grow in from a dot, like the How might we circles.','3d':'Menu D: the whole menu floods with each page’s colour as you hover its name.','3e':'Menu E: a bento grid, Home large, each tile in its world colour.'};
var EMAIL='Freddie.Grzybowski@gmail.com',LI='https://www.linkedin.com/in/freddiegrzybowski/',MED='https://medium.com/@freddie.grzybowski';
var site=null;
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function links(cls,fn){return '<nav class="'+cls+'" aria-label="Site">'+ITEMS.map(fn).join('')+'</nav>'}
function go(t){return 'data-go="'+t[0]+'" href="#'+t[0]+'"'}
function foot(mv){return '<div class="pm-ft mz2" data-mv="'+mv+'" style="--i:8"><a href="'+LI+'" target="_blank" rel="noopener">LinkedIn ↗</a><a href="'+MED+'" target="_blank" rel="noopener">Medium ↗</a><a data-go="mail" href="#mail">'+EMAIL+'</a><span class="tm" data-pfclk>London</span></div>'}
function build(){
 var h='<button class="pf-mx" data-close type="button">Close <span aria-hidden="true">✕</span></button>';
 var l1=links('pl1',function(t,i){return '<a class="mz2" '+go(t)+' style="--c:'+t[4]+';--i:'+i+'"><i>0'+(i+1)+'</i><span>'+t[1]+'</span><u aria-hidden="true">→</u></a>'});
 h+='<div class="p1" data-mv="1a">'+l1+'<aside class="pcard mz2" style="--i:6" aria-label="Contact"><p class="ey" style="margin:0">Get in touch</p><h3>Say hello</h3><span class="em">'+EMAIL+'</span><div class="row"><button class="pbtn pri" type="button" data-pfcopy>Copy email</button><a class="pbtn" href="'+LI+'" target="_blank" rel="noopener">LinkedIn ↗</a><a class="pbtn" href="'+MED+'" target="_blank" rel="noopener">Medium ↗</a></div><p class="loc" style="margin-bottom:0"><b aria-hidden="true"></b><span>Based in the UK, working remote · <span data-pfclk>London</span></span></p></aside></div>';
 h+='<div class="p1" data-mv="1b">'+l1+'<aside class="pnow mz2" style="--i:6"><p class="ey" style="margin:0">In brief</p><p class="bio">Creative UX/UI Designer and avid beekeeper based in the UK. Coming from a background in streaming and guitar teaching.</p><dl><div><dt>Based in</dt><dd><b style="--c:#7ff3e4">UK</b> · Remote</dd></div><div><dt>Designing</dt><dd><b style="--c:#8fe8c0">UX/UI</b> · Mobile apps</dd></div><div><dt>Teaching</dt><dd><b style="--c:#ebefa0">4 years</b> of UX</dd></div><div><dt>Off duty</dt><dd><b style="--c:#ffb9a0">Bees</b> · Guitar</dd></div></dl></aside></div>';
 h+=foot('1a 1b');
 h+='<div class="p2a" data-mv="2a"><div class="paur" aria-hidden="true"><i></i><i></i><i></i></div>'+links('pl2a',function(t,i){return '<a class="mz2" '+go(t)+' style="--c:'+t[4]+';--i:'+i+'"><i>0'+(i+1)+'</i><span>'+t[1]+'</span><em>'+esc(t[2])+'</em></a>'})+'</div>';
 h+='<div class="p2b" data-mv="2b">'+links('pl2b',function(t,i){var tg=t[3].map(function(x){return '<b>'+x+'</b>'}).join('');tg=tg+tg;return '<a class="mz2" '+go(t)+' style="--c:'+t[4]+';--i:'+i+'"><i>0'+(i+1)+'</i><span>'+t[1]+'</span><div class="tk" aria-hidden="true"><div>'+tg+tg+'</div></div><u aria-hidden="true">→</u></a>'})+'</div>';
 h+=foot('2a 2b');
 h+='<div class="p3a" data-mv="3a">'+links('pl3a',function(t,i){var w=W3[t[0]];return '<a '+go(t)+' style="--c:'+w[0]+';--t:'+w[1]+';--i:'+i+'"><i>0'+(i+1)+'</i><div class="nm"><span>'+t[1]+'</span><em>'+esc(t[2])+'</em></div><u aria-hidden="true">→</u></a>'})+'</div>';
 h+='<div class="p3b" data-mv="3b">'+links('pl3b',function(t,i){var w=W3[t[0]];return '<a '+go(t)+' style="--c:'+w[0]+';--t:'+w[1]+';--i:'+i+';--r:'+(i%2?'1.5deg':'-1.5deg')+(w[2]?';--b:'+w[2]:'')+'"><div class="tp"><i>0'+(i+1)+'</i><u aria-hidden="true">→</u></div><div><span>'+t[1]+'</span><em>'+esc(t[2])+'</em></div></a>'})+'</div>';
 h+='<div class="p3c" data-mv="3c">'+links('pl3c',function(t,i){var w=W3[t[0]];return '<a '+go(t)+' style="--c:'+w[0]+';--t:'+w[1]+';--i:'+i+'"><i>0'+(i+1)+'</i><span>'+t[1]+'</span></a>'})+'</div>';
 h+='<div class="p3d" data-mv="3d">'+links('pl3d',function(t,i){var w=W3[t[0]];return '<a class="mz2" '+go(t)+' data-fl="'+w[0]+'" data-ft="'+w[1]+'" style="--i:'+i+'"><i>0'+(i+1)+'</i><span>'+t[1]+'</span><em>'+esc(t[2])+'</em></a>'})+'</div>';
 h+='<div class="p3e" data-mv="3e">'+links('pl3e',function(t,i){var w=W3[t[0]];return '<a '+go(t)+' style="--c:'+w[0]+';--t:'+w[1]+';--i:'+i+(w[2]?';--b:'+w[2]:'')+'"><div class="tp"><i>0'+(i+1)+'</i><u aria-hidden="true">→</u></div><div><span>'+t[1]+'</span><em>'+esc(t[2])+'</em></div></a>'})+'</div>';
 h+=foot('3b 3c 3d 3e');
 return h}
function clock(){if(!site)return;var t='';try{t=new Date().toLocaleTimeString('en-GB',{timeZone:'Europe/London',hour:'2-digit',minute:'2-digit'})}catch(e){}
 [].forEach.call(site.querySelectorAll('[data-pfclk]'),function(e){e.textContent='London · '+t})}
function mark(){if(!site)return;var p=site.getAttribute('data-p');[].forEach.call(site.querySelectorAll('.pf-mn [data-go]'),function(a){var on=a.getAttribute('data-go')===p;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')})}
function note(){var v=site?site.getAttribute('data-ver'):'1',n=document.getElementById('pfmnote');if(n)n.textContent=v==='0'?'Menu: your current menu.':(NOTE[v+MN]||'');
 [].forEach.call(document.querySelectorAll('.pfb [data-mn]'),function(b){b.setAttribute('aria-pressed',b.dataset.mn===MN)});
 [].forEach.call(document.querySelectorAll('.pfb [data-mn]'),function(b){b.disabled=v==='0'})}
function setMn(m){MN=m;try{localStorage.setItem('pfmn',m)}catch(e){}if(site)site.setAttribute('data-mn',m);note()}
function openMenu(){if(!site)return;var b=site.querySelector('.mbtn');if(!site.classList.contains('mo')&&b)b.click()}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.pfb button');if(!b)return;
 if(b.dataset.mn){setMn(b.dataset.mn);openMenu()}
 else if(b.hasAttribute('data-open'))openMenu();
 else if(b.dataset.v!=null)setTimeout(note,0)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&site&&site.classList.contains('mo')){var b=site.querySelector('.mbtn');if(b)b.click()}});
var A=window.__pfAfter,M=window.__pfMark;
window.__pfAfter=function(s,R){A&&A(s,R);site=s;
 var st=document.createElement('style');st.textContent=window.__pfMenuCSS;R.appendChild(st);
 var menu=s.querySelector('.menu');if(menu&&!menu.querySelector('.pf-mn')){var d=document.createElement('div');d.className='pf-mn';d.innerHTML=build();menu.appendChild(d);
  function flood(e){var a=e.target.closest&&e.target.closest('.pl3d a');if(a){d.style.setProperty('--fl',a.getAttribute('data-fl'));d.style.setProperty('--ft',a.getAttribute('data-ft'));d.classList.add('fld')}}
  d.addEventListener('pointerover',flood);d.addEventListener('focusin',flood);d.addEventListener('pointerleave',function(){d.classList.remove('fld')});
  function tint(e){var a=e.target.closest&&e.target.closest('.pl2a a');if(a)d.style.setProperty('--mc',a.style.getPropertyValue('--c'))}
  d.addEventListener('pointerover',tint);d.addEventListener('focusin',tint);
  d.addEventListener('keydown',function(e){var m=e.target.closest('[data-pfmail]');if(m&&(e.key==='Enter'||e.key===' ')){e.preventDefault();m.click()}});
  d.addEventListener('click',function(e){
   var c=e.target.closest('[data-pfcopy]');if(c){e.stopPropagation();try{navigator.clipboard.writeText(EMAIL).then(function(){c.textContent='Copied ✓';setTimeout(function(){c.textContent='Copy email'},2000)},function(){c.textContent='Select the address above'})}catch(x){c.textContent='Select the address above'}return}
   var m=e.target.closest('[data-pfmail]');if(m){e.stopPropagation();e.preventDefault();var b=s.querySelector('.mbtn');if(s.classList.contains('mo')&&b)b.click();if(window.__pfMail)window.__pfMail();return}
   if(e.target.closest('a[target=_blank]')){e.stopPropagation();return}
   var g=e.target.closest('a[data-go]');if(g)e.preventDefault()},true)}
 function pad(){var n=s.querySelector('.nav'),mu=s.querySelector('.menu'),d2=s.querySelector('.pf-mn');if(!n||!mu||!d2)return;var mt=mu.getBoundingClientRect().top,nb=n.getBoundingClientRect().bottom;d2.style.setProperty('--pmt',Math.max(0,Math.round(nb-mt))+'px');d2.style.setProperty('--mtop',Math.round(mt)+'px')}
 pad();addEventListener('resize',pad);new MutationObserver(function(){setTimeout(pad,30)}).observe(s,{attributes:true,attributeFilter:['class']});
 s.setAttribute('data-mn',MN);mark();clock();setInterval(clock,20000);note();
 new MutationObserver(note).observe(s,{attributes:true,attributeFilter:['data-ver']})};
window.__pfMark=function(p){M&&M(p);mark()};
})();
(function(){
var HSN={'1':'Hero strip 1 (live now): 4 years teaching, 14+ cohorts, 8 years keeping bees.','2':'Hero strip 2: three colour chips that jump to each project, previewing its colour world.','3':'Hero strip 3: just “Scroll”, with a line that drips through the three project colours.','4':'Hero strip 4: based in the UK, working remote, and the live London time.','5':'Hero strip 5: a slow ticker of what you do: UX research, UI design, prototyping, testing, teaching, beekeeping.'};
function S(){var h=document.getElementById('na-host');return h&&h.shadowRoot&&h.shadowRoot.querySelector('#site')}
function sync(){var s=S();if(!s)return;var v=s.getAttribute('data-ver'),hs=s.getAttribute('data-hs')||'1',m=s.getAttribute('data-mn');document.body.classList.toggle('v3',v==='3');
 [].forEach.call(document.querySelectorAll('.pfb [data-hs]'),function(b){b.setAttribute('aria-pressed',b.dataset.hs===hs)});
 if(v!=='3'&&/[cde]/.test(m||'')){var b=document.querySelector('.pfb [data-mn="b"]');if(b){b.click()}}
 var n=document.getElementById('pfhnote');if(n)n.textContent=v==='3'?HSN[hs]:''}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.pfb button');if(!b)return;
 if(b.dataset.hs){var s=S();if(s){s.setAttribute('data-hs',b.dataset.hs);try{localStorage.setItem('pfhs',b.dataset.hs)}catch(x){}
  if(s.classList.contains('mo')){var mb=s.querySelector('.mbtn');if(mb)mb.click()}
  if(s.getAttribute('data-p')!=='home'){var hm=s.querySelector('.nv [data-go=home]');if(hm)hm.click()}else window.scrollTo({top:0,behavior:'smooth'})}}
 setTimeout(sync,30)});
var t=setInterval(function(){var s=S();if(s&&s.classList.contains('pfjs')){clearInterval(t);sync();new MutationObserver(sync).observe(s,{attributes:true,attributeFilter:['data-ver','data-hs','data-mn']})}},200);
})();
