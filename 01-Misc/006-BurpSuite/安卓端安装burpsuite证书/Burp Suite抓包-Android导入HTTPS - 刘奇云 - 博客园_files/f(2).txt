(function(){/* 
 
 Copyright The Closure Library Authors. 
 SPDX-License-Identifier: Apache-2.0 
*/ 
'use strict';const e=Symbol(void 0);var g=Object,h=g.freeze,k=[];Object.isFrozen(k)||(e?k[e]|=1:void 0!==k.g?k.g|=1:Object.defineProperties(k,{g:{value:1,configurable:!0,writable:!0,enumerable:!1}}));h.call(g,k);/* 
 
 SPDX-License-Identifier: Apache-2.0 
*/ 
function l(a,b,d){a.addEventListener&&a.addEventListener(b,d,!1)};function m(a,b,d){if(Array.isArray(b))for(var c=0;c<b.length;c++)m(a,String(b[c]),d);else null!=b&&d.push(a+(""===b?"":"="+encodeURIComponent(String(b))))};function n(a,b){a.google_image_requests||(a.google_image_requests=[]);var d=a.document;d=void 0===d?document:d;d=d.createElement("img");d.src=b;a.google_image_requests.push(d)};function p(a=null){return a&&"22"===a.getAttribute("data-jc")?a:document.querySelector('[data-jc="22"]')};var q=document,r=window;function t(a){return"undefined"!==typeof a}function u(a){l(q,a.i,()=>{if(q[a.h])a.g&&(a.g=!1,a.j=Date.now(),v(a,0));else{if(-1!==a.j){const b=Date.now()-a.j;0<b&&(a.j=-1,v(a,1,b))}v(a,3)}})}function w(a){l(r,"click",b=>{a.handleClick(b)})} 
function v(a,b,d=0){var c={gqid:a.m,qqid:a.o};0===b&&(c["return"]=0);1===b&&(c["return"]=1,c.timeDelta=d);2===b&&(c.bgload=1);3===b&&(c.fg=1);b=[];for(var f in c)m(f,c[f],b);n(r,a.l+"&label=window_focus&"+b.join("&"));if(!(.01<Math.random())){a=p(document.currentScript);a=`https://${"pagead2.googlesyndication.com"}/pagead/gen_204?id=jca&jc=${22}&version=${a&&a.getAttribute("data-jc-version")||"unknown"}&sample=${.01}`;c=window;if(f=c.navigator)f=c.navigator.userAgent,f=/Chrome/.test(f)&&!/Edge/.test(f)? 
!0:!1;f&&c.navigator.sendBeacon?c.navigator.sendBeacon(a):n(c,a)}} 
var y=class{constructor(){var a=x["gws-id"],b=x["qem-id"];this.l=x.url;this.m=a;this.o=b;this.g=!1;a=t(q.hidden)?{h:"hidden",i:"visibilitychange"}:t(q.mozHidden)?{h:"mozHidden",i:"mozvisibilitychange"}:t(q.msHidden)?{h:"msHidden",i:"msvisibilitychange"}:t(q.webkitHidden)?{h:"webkitHidden",i:"webkitvisibilitychange"}:{h:"hidden",i:"visibilitychange"};this.h=a.h;this.i=a.i;this.j=-1;q[this.h]&&v(this,2);u(this);w(this)}handleClick(){this.g=!0;r.setTimeout(()=>{this.g=!1},5E3)}};const z=p(document.currentScript);if(null==z)throw Error("JSC not found 22");var x;const A={},B=z.attributes;for(let a=B.length-1;0<=a;a--){const b=B[a].name;0===b.indexOf("data-jcp-")&&(A[b.substring(9)]=B[a].value)}x=A;window.window_focus_for_click=new y;}).call(this);
