
/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */

(function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var e=jQuery.fn.select2.amd;return e.define("select2/i18n/sr-Cyrl",[],function(){function e(e,t,n,r){return e%10==1&&e%100!=11?t:e%10>=2&&e%10<=4&&(e%100<12||e%100>14)?n:r}return{errorLoading:function(){return"Преузимање није успело."},inputTooLong:function(t){var n=t.input.length-t.maximum,r="Обришите "+n+" симбол";return r+=e(n,"","а","а"),r},inputTooShort:function(t){var n=t.minimum-t.input.length,r="Укуцајте бар још "+n+" симбол";return r+=e(n,"","а","а"),r},loadingMore:function(){return"Преузимање још резултата…"},maximumSelected:function(t){var n="Можете изабрати само "+t.maximum+" ставк";return n+=e(t.maximum,"у","е","и"),n},noResults:function(){return"Ништа није пронађено"},searching:function(){return"Претрага…"},removeAllItems:function(){return"Уклоните све ставке"}}}),{define:e.define,require:e.require}})();

/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */

!function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var n=jQuery.fn.select2.amd;n.define("select2/i18n/sr-Cyrl",[],function(){function n(n,e,r,u){return n%10==1&&n%100!=11?e:n%10>=2&&n%10<=4&&(n%100<12||n%100>14)?r:u}return{errorLoading:function(){return"Преузимање није успело."},inputTooLong:function(e){var r=e.input.length-e.maximum,u="Обришите "+r+" симбол";return u+=n(r,"","а","а")},inputTooShort:function(e){var r=e.minimum-e.input.length,u="Укуцајте бар још "+r+" симбол";return u+=n(r,"","а","а")},loadingMore:function(){return"Преузимање још резултата…"},maximumSelected:function(e){var r="Можете изабрати само "+e.maximum+" ставк";return r+=n(e.maximum,"у","е","и")},noResults:function(){return"Ништа није пронађено"},searching:function(){return"Претрага…"},removeAllItems:function(){return"Уклоните све ставке"}}}),n.define,n.require}();

