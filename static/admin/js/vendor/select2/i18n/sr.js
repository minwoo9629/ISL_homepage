
/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */

(function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var e=jQuery.fn.select2.amd;return e.define("select2/i18n/sr",[],function(){function e(e,t,n,r){return e%10==1&&e%100!=11?t:e%10>=2&&e%10<=4&&(e%100<12||e%100>14)?n:r}return{errorLoading:function(){return"Preuzimanje nije uspelo."},inputTooLong:function(t){var n=t.input.length-t.maximum,r="Obrišite "+n+" simbol";return r+=e(n,"","a","a"),r},inputTooShort:function(t){var n=t.minimum-t.input.length,r="Ukucajte bar još "+n+" simbol";return r+=e(n,"","a","a"),r},loadingMore:function(){return"Preuzimanje još rezultata…"},maximumSelected:function(t){var n="Možete izabrati samo "+t.maximum+" stavk";return n+=e(t.maximum,"u","e","i"),n},noResults:function(){return"Ništa nije pronađeno"},searching:function(){return"Pretraga…"},removeAllItems:function(){return"Уклоните све ставке"}}}),{define:e.define,require:e.require}})();

/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */

!function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var n=jQuery.fn.select2.amd;n.define("select2/i18n/sr",[],function(){function n(n,e,r,t){return n%10==1&&n%100!=11?e:n%10>=2&&n%10<=4&&(n%100<12||n%100>14)?r:t}return{errorLoading:function(){return"Preuzimanje nije uspelo."},inputTooLong:function(e){var r=e.input.length-e.maximum,t="Obrišite "+r+" simbol";return t+=n(r,"","a","a")},inputTooShort:function(e){var r=e.minimum-e.input.length,t="Ukucajte bar još "+r+" simbol";return t+=n(r,"","a","a")},loadingMore:function(){return"Preuzimanje još rezultata…"},maximumSelected:function(e){var r="Možete izabrati samo "+e.maximum+" stavk";return r+=n(e.maximum,"u","e","i")},noResults:function(){return"Ništa nije pronađeno"},searching:function(){return"Pretraga…"},removeAllItems:function(){return"Уклоните све ставке"}}}),n.define,n.require}();

