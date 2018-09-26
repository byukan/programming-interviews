<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}</style>
    <script src="stocks_files/nr-998.js"></script><script id="facebook-jssdk" src="stocks_files/all.js"></script><script type="text/javascript" async="" src="stocks_files/analytics.js"></script><script type="text/javascript">
        
        window.IC = window.IC || {};
        window.IC.currentUser = JSON.parse('{"id":3526074,"username":"justwjr","email":"justwjr@ucla.edu","date_joined":"2016-09-28T23:25:25.894421+00:00","first_name":"Justin","last_name":"J. Wang","full_name":"Justin J. Wang","short_name":"Justin","is_anonymous":false,"is_on_last_question":false,"percent_done":7,"num_questions_done":3,"num_questions_remaining":41,"recruiting_is_interested_in_intros":null,"is_full_access":false,"first_payment_date":null,"last_payment_date":null,"num_free_questions_left":0,"terms_has_agreed_to_latest":false,"preferred_content_language":"python","preferred_notepad_language":"","is_staff":false,"auth_providers_human_readable_list":"Github","num_auth_providers":1,"auth_email":"justwjr@ucla.edu"}');
        
    </script>


    
    <script src="stocks_files/1358232165.js"></script>
    

    
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge"><script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,t,n){function r(n){if(!t[n]){var o=t[n]={exports:{}};e[n][0].call(o.exports,function(t){var o=e[n][1][t];return r(o||t)},o,o.exports)}return t[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(e,t,n){function r(){}function o(e,t,n){return function(){return i(e,[(new Date).getTime()].concat(u(arguments)),t?null:this,n),t?void 0:this}}var i=e("handle"),a=e(2),u=e(3),c=e("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var s=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit"],l="api-",p=l+"ixn-";a(s,function(e,t){f[t]=o(l+t,!0,"api")}),f.addPageAction=o(l+"addPageAction",!0),f.setCurrentRouteName=o(l+"routeName",!0),t.exports=newrelic,f.interaction=function(){return(new r).get()};var d=r.prototype={createTracer:function(e,t){var n={},r=this,o="function"==typeof t;return i(p+"tracer",[Date.now(),e,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return t.apply(this,arguments)}finally{c.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,t){d[t]=o(p+t)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,(new Date).getTime()])}},{}],2:[function(e,t,n){function r(e,t){var n=[],r="",i=0;for(r in e)o.call(e,r)&&(n[i]=t(r,e[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],3:[function(e,t,n){function r(e,t,n){t||(t=0),"undefined"==typeof n&&(n=e?e.length:0);for(var r=-1,o=n-t||0,i=Array(o<0?0:o);++r<o;)i[r]=e[t+r];return i}t.exports=r},{}],ee:[function(e,t,n){function r(){}function o(e){function t(e){return e&&e instanceof r?e:e?c(e,u,i):i()}function n(n,r,o){if(!p.aborted){e&&e(n,r,o);for(var i=t(o),a=v(n),u=a.length,c=0;c<u;c++)a[c].apply(i,r);var f=s[w[n]];return f&&f.push([y,n,r,i]),i}}function d(e,t){b[e]=v(e).concat(t)}function v(e){return b[e]||[]}function g(e){return l[e]=l[e]||o(n)}function m(e,t){f(e,function(e,n){t=t||"feature",w[n]=t,t in s||(s[t]=[])})}var b={},w={},y={on:d,emit:n,get:g,listeners:v,context:t,buffer:m,abort:a,aborted:!1};return y}function i(){return new r}function a(){(s.api||s.feature)&&(p.aborted=!0,s=p.backlog={})}var u="nr@context",c=e("gos"),f=e(2),s={},l={},p=t.exports=o();p.backlog=s},{}],gos:[function(e,t,n){function r(e,t,n){if(o.call(e,t))return e[t];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[t]=r,r}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],handle:[function(e,t,n){function r(e,t,n,r){o.buffer([e],r),o.emit(e,t,n)}var o=e("ee").get("handle");t.exports=r,r.ee=o},{}],id:[function(e,t,n){function r(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");t.exports=r},{}],loader:[function(e,t,n){function r(){if(!h++){var e=y.info=NREUM.info,t=l.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&t))return f.abort();c(b,function(t,n){e[t]||(e[t]=n)}),u("mark",["onload",a()],null,"api");var n=l.createElement("script");n.src="https://"+e.agent,t.parentNode.insertBefore(n,t)}}function o(){"complete"===l.readyState&&i()}function i(){u("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var u=e("handle"),c=e(2),f=e("ee"),s=window,l=s.document,p="addEventListener",d="attachEvent",v=s.XMLHttpRequest,g=v&&v.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:v,REQ:s.Request,EV:s.Event,PR:s.Promise,MO:s.MutationObserver},e(1);var m=""+location,b={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-998.min.js"},w=v&&g&&g[p]&&!/CriOS/.test(navigator.userAgent),y=t.exports={offset:a(),origin:m,features:{},xhrWrappable:w};l[p]?(l[p]("DOMContentLoaded",i,!1),s[p]("load",r,!1)):(l[d]("onreadystatechange",o),s[d]("onload",r)),u("mark",["firstbyte",a()],null,"api");var h=0},{}]},{},["loader"]);</script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"applicationTime":196,"transactionName":"ZVwAbEQCDUQCAUwKDFwWJE1YABdeDAwXDhpBUBZdGA4CXg0DSBNNRFAHT0VZMkIGEUwKDFxvC11BTQRSFw==","errorBeacon":"bam.nr-data.net","beacon":"bam.nr-data.net","queueTime":5,"licenseKey":"9e57878e2e","applicationID":"7328113","agent":""}</script>
        <link rel="shortcut icon" type="image/x-icon" href="https://www.interviewcake.com/images/favicon.ico?bust=132">
        <link rel="canonical" href="https://www.interviewcake.com/question/java/stock-price">
        <meta name="description" content="Figure out the optimal buy and sell time for a given stock, given its prices yesterday.">

        

        <meta property="og:title" content="Apple Stocks | Interview Cake">
        <meta property="og:description" content="Figure out the optimal buy and sell time for a given stock, given its prices yesterday.">
        <meta property="og:image" content="https://www.interviewcake.com/static/images/cake_white_on_blue_600_600_unrounded.png">
        <meta property="og:type" content="website">
        <meta property="og:locale" content="en_US">
        <meta property="og:site_name" content="Interview Cake: Programming Interview Questions and Tips">
        <meta property="fb:app_id" content="149278655279066">
        <meta property="fb:admins" content="514407734">
        <meta property="og:url" content="https://www.interviewcake.com/question/java/stock-price">

        <meta name="twitter:card" content="summary">
        <meta name="twitter:site" content="@interviewcake">
        <meta name="twitter:title" content="Apple Stocks | Interview Cake">
        <meta name="twitter:description" content="Figure out the optimal buy and sell time for a given stock, given its prices yesterday.">
        <meta name="twitter:creator" content="@interviewcake">
        <meta name="twitter:image:src" content="https://www.interviewcake.com/static/images/cake_white_on_blue_600_600_unrounded.png">
        <meta name="twitter:domain" content="interviewcake.com">

        <title>Apple Stocks | Interview Cake</title>
    


    

    
    <script type="text/javascript">
        window.analytics||(window.analytics=[]),window.analytics.methods=["identify","track","trackLink","trackForm","trackClick","trackSubmit","page","pageview","ab","alias","ready","group","on","once","off"],window.analytics.factory=function(a){return function(){var t=Array.prototype.slice.call(arguments);return t.unshift(a),window.analytics.push(t),window.analytics}};for(var i=0;i<window.analytics.methods.length;i++){var method=window.analytics.methods[i];window.analytics[method]=window.analytics.factory(method)}window.analytics.load=function(a){var t=document.createElement("script");t.type="text/javascript",t.async=!0,t.src=("https:"===document.location.protocol?"https://":"http://")+"d2dq2ahtl5zl1z.cloudfront.net/analytics.js/v1/"+a+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(t,n)},window.analytics.SNIPPET_VERSION="2.0.6",
        window.analytics.load("rowk0wc1g6"),
        window.analytics.page();
    </script>
    
    


    


    

        <link href="stocks_files/bootstrap.css" rel="stylesheet">
        <link href="stocks_files/bootstrap-glyphicons.css" rel="stylesheet">
        <link href="stocks_files/font-awesome.css" rel="stylesheet">
        <link href="stocks_files/katex.css" rel="stylesheet">
    
    
        <link rel="stylesheet" href="stocks_files/f89c26de9b74.css" type="text/css" media="all">
    




<!--
<link href='http://fonts.googleapis.com/css?family=Raleway:500,700,100' rel='stylesheet' type='text/css'>
-->
<!--
<link href='http://fonts.googleapis.com/css?family=Arimo:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
-->
<link href="stocks_files/css_002.css" rel="stylesheet" type="text/css">

<link rel="apple-touch-icon" href="https://www.interviewcake.com/images/cake_white_on_blue_128_128_unrounded.png">
<!--
thought maybe for headings. but nope.
<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300,700,300italic' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Droid+Sans:400,700' rel='stylesheet' type='text/css'>
-->




<meta name="50fc73d52056532c18787976ceb78fddb87b78b2" content="ceb4cec06fc4a780c7b31b85c07cf75d1ca58d9d">





<script type="text/javascript">
var _vwo_code=(function(){
var account_id=50155,
settings_tolerance=2000,
library_tolerance=2500,
use_existing_jquery=false,
// DO NOT EDIT BELOW THIS LINE
f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());_vwo_settings_timer=_vwo_code.init();
</script><style type="text/css">img[src="/static/images/logos/small_grayscale/mixpanel.png"],
img[src="https://www.paypal.com/en_US/i/btn/btn_xpressCheckout.gif"]
{display:none !important;}</style><script src="stocks_files/j.php" type="text/javascript"></script>

<style type="text/css">.fb_hidden{position:absolute;top:-10000px;z-index:10001}.fb_reposition{overflow:hidden;position:relative}.fb_invisible{display:none}.fb_reset{background:none;border:0;border-spacing:0;color:#000;cursor:auto;direction:ltr;font-family:"lucida grande", tahoma, verdana, arial, sans-serif;font-size:11px;font-style:normal;font-variant:normal;font-weight:normal;letter-spacing:normal;line-height:1;margin:0;overflow:visible;padding:0;text-align:left;text-decoration:none;text-indent:0;text-shadow:none;text-transform:none;visibility:visible;white-space:normal;word-spacing:normal}.fb_reset>div{overflow:hidden}.fb_link img{border:none}@keyframes fb_transform{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}.fb_animate{animation:fb_transform .3s forwards}
.fb_dialog{background:rgba(82, 82, 82, .7);position:absolute;top:-10000px;z-index:10001}.fb_reset .fb_dialog_legacy{overflow:visible}.fb_dialog_advanced{padding:10px;-moz-border-radius:8px;-webkit-border-radius:8px;border-radius:8px}.fb_dialog_content{background:#fff;color:#333}.fb_dialog_close_icon{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 0 transparent;_background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/s816eWC-2sl.gif);cursor:pointer;display:block;height:15px;position:absolute;right:18px;top:17px;width:15px}.fb_dialog_mobile .fb_dialog_close_icon{top:5px;left:5px;right:auto}.fb_dialog_padding{background-color:transparent;position:absolute;width:1px;z-index:-1}.fb_dialog_close_icon:hover{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -15px transparent;_background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/s816eWC-2sl.gif)}.fb_dialog_close_icon:active{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/IE9JII6Z1Ys.png) no-repeat scroll 0 -30px transparent;_background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/s816eWC-2sl.gif)}.fb_dialog_loader{background-color:#f6f7f9;border:1px solid #606060;font-size:24px;padding:20px}.fb_dialog_top_left,.fb_dialog_top_right,.fb_dialog_bottom_left,.fb_dialog_bottom_right{height:10px;width:10px;overflow:hidden;position:absolute}.fb_dialog_top_left{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 0;left:-10px;top:-10px}.fb_dialog_top_right{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -10px;right:-10px;top:-10px}.fb_dialog_bottom_left{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -20px;bottom:-10px;left:-10px}.fb_dialog_bottom_right{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8YeTNIlTZjm.png) no-repeat 0 -30px;right:-10px;bottom:-10px}.fb_dialog_vert_left,.fb_dialog_vert_right,.fb_dialog_horiz_top,.fb_dialog_horiz_bottom{position:absolute;background:#525252;filter:alpha(opacity=70);opacity:.7}.fb_dialog_vert_left,.fb_dialog_vert_right{width:10px;height:100%}.fb_dialog_vert_left{margin-left:-10px}.fb_dialog_vert_right{right:0;margin-right:-10px}.fb_dialog_horiz_top,.fb_dialog_horiz_bottom{width:100%;height:10px}.fb_dialog_horiz_top{margin-top:-10px}.fb_dialog_horiz_bottom{bottom:0;margin-bottom:-10px}.fb_dialog_iframe{line-height:0}.fb_dialog_content .dialog_title{background:#6d84b4;border:1px solid #365899;color:#fff;font-size:14px;font-weight:bold;margin:0}.fb_dialog_content .dialog_title>span{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/Cou7n-nqK52.gif) no-repeat 5px 50%;float:left;padding:5px 0 7px 26px}body.fb_hidden{-webkit-transform:none;height:100%;margin:0;overflow:visible;position:absolute;top:-10000px;left:0;width:100%}.fb_dialog.fb_dialog_mobile.loading{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/3rhSv5V8j3o.gif) white no-repeat 50% 50%;min-height:100%;min-width:100%;overflow:hidden;position:absolute;top:0;z-index:10001}.fb_dialog.fb_dialog_mobile.loading.centered{width:auto;height:auto;min-height:initial;min-width:initial;background:none}.fb_dialog.fb_dialog_mobile.loading.centered #fb_dialog_loader_spinner{width:100%}.fb_dialog.fb_dialog_mobile.loading.centered .fb_dialog_content{background:none}.loading.centered #fb_dialog_loader_close{color:#fff;display:block;padding-top:20px;clear:both;font-size:18px}#fb-root #fb_dialog_ipad_overlay{background:rgba(0, 0, 0, .45);position:absolute;bottom:0;left:0;right:0;top:0;width:100%;min-height:100%;z-index:10000}#fb-root #fb_dialog_ipad_overlay.hidden{display:none}.fb_dialog.fb_dialog_mobile.loading iframe{visibility:hidden}.fb_dialog_content .dialog_header{-webkit-box-shadow:white 0 1px 1px -1px inset;background:-webkit-gradient(linear, 0% 0%, 0% 100%, from(#738ABA), to(#2C4987));border-bottom:1px solid;border-color:#1d4088;color:#fff;font:14px Helvetica, sans-serif;font-weight:bold;text-overflow:ellipsis;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0;vertical-align:middle;white-space:nowrap}.fb_dialog_content .dialog_header table{-webkit-font-smoothing:subpixel-antialiased;height:43px;width:100%}.fb_dialog_content .dialog_header td.header_left{font-size:12px;padding-left:5px;vertical-align:middle;width:60px}.fb_dialog_content .dialog_header td.header_right{font-size:12px;padding-right:5px;vertical-align:middle;width:60px}.fb_dialog_content .touchable_button{background:-webkit-gradient(linear, 0% 0%, 0% 100%, from(#4966A6), color-stop(.5, #355492), to(#2A4887));border:1px solid #29487d;-webkit-background-clip:padding-box;-webkit-border-radius:3px;-webkit-box-shadow:rgba(0, 0, 0, .117188) 0 1px 1px inset, rgba(255, 255, 255, .167969) 0 1px 0;display:inline-block;margin-top:3px;max-width:85px;line-height:18px;padding:4px 12px;position:relative}.fb_dialog_content .dialog_header .touchable_button input{border:none;background:none;color:#fff;font:12px Helvetica, sans-serif;font-weight:bold;margin:2px -12px;padding:2px 6px 3px 6px;text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog_content .dialog_header .header_center{color:#fff;font-size:16px;font-weight:bold;line-height:18px;text-align:center;vertical-align:middle}.fb_dialog_content .dialog_content{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat 50% 50%;border:1px solid #555;border-bottom:0;border-top:0;height:150px}.fb_dialog_content .dialog_footer{background:#f6f7f9;border:1px solid #555;border-top-color:#ccc;height:40px}#fb_dialog_loader_close{float:left}.fb_dialog.fb_dialog_mobile .fb_dialog_close_button{text-shadow:rgba(0, 30, 84, .296875) 0 -1px 0}.fb_dialog.fb_dialog_mobile .fb_dialog_close_icon{visibility:hidden}#fb_dialog_loader_spinner{animation:rotateSpinner 1.2s linear infinite;background-color:transparent;background-image:url(https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/t-wz8gw1xG1.png);background-repeat:no-repeat;background-position:50% 50%;height:24px;width:24px}@keyframes rotateSpinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
.fb_iframe_widget{display:inline-block;position:relative}.fb_iframe_widget span{display:inline-block;position:relative;text-align:justify}.fb_iframe_widget iframe{position:absolute}.fb_iframe_widget_fluid_desktop,.fb_iframe_widget_fluid_desktop span,.fb_iframe_widget_fluid_desktop iframe{max-width:100%}.fb_iframe_widget_fluid_desktop iframe{min-width:220px;position:relative}.fb_iframe_widget_lift{z-index:1}.fb_hide_iframes iframe{position:relative;left:-10000px}.fb_iframe_widget_loader{position:relative;display:inline-block}.fb_iframe_widget_fluid{display:inline}.fb_iframe_widget_fluid span{width:100%}.fb_iframe_widget_loader iframe{min-height:32px;z-index:2;zoom:1}.fb_iframe_widget_loader .FB_Loader{background:url(https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/jKEcVPZFk-2.gif) no-repeat;height:32px;width:32px;margin-left:-16px;position:absolute;left:50%;z-index:4}</style></head>
<body ng-app="prepApp" ng-init="questionIsEmbedded = false" class="ng-scope">



<div class="navbar navbar-inverse ng-scope" role="navigation" ng-controller="HeaderCtrl" language="python">
    <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="https://www.interviewcake.com/">
            Interview Cake
        </a>
    </div>

  <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav navbar-left">
            <li>
                <a href="https://www.interviewcake.com/coding-interview-tips">Tips and Tricks</a>
            </li>

            <li class="dropdown">
                <a href="" class="dropdown-toggle" data-toggle="dropdown" rel="nofollow">
                    Glossary <span class="caret"></span>
                </a>
                <ul class="dropdown-menu" role="menu">
                    <li>
                        <a href="https://www.interviewcake.com/big-o-notation-time-and-space-complexity">Big O Notation: <span complexity="n" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span></span></span></span>, <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span>, etc</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/article/logarithms">Logarithms</a>
                    </li>

                    <li role="separator" class="divider"></li>

                    <li>
                        <a href="https://www.interviewcake.com/concept/binary-search">Binary Search</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/counting-sort">Counting Sort</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/overlapping-subproblems">Overlapping Subproblems</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/memoization">Memoization</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/bottom-up">Bottom-Up Algorithms</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/lazy">Lazy Evaluation</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/garbage-collection">Garbage Collection</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/integer-overflow">Integer Overflow</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/js-closure">Closure</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/slice">Array Slicing</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/hashing">Hashing</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/mutable">Mutable vs Immutable</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/in-place">In-Place Operation</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/triangular-series">Triangular Series</a>
                    </li>

                    <li role="separator" class="divider"></li>

                    <li>
                        <a href="https://www.interviewcake.com/concept/array">Array</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/dynamic-array-amortized-analysis">Dynamic Array</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/hash-map">Hash Table</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/linked-list">Linked List</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/queue">Queue</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/stack">Stack</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/binary-tree">Binary Tree</a>
                    </li>

                    <li role="separator" class="divider"></li>

                    <li>
                        <a href="https://www.interviewcake.com/concept/binary-numbers">Binary Numbers</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/and">Bitwise AND</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/or">Bitwise OR</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/not">Bitwise NOT</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/xor">Bitwise XOR</a>
                    </li>
                    <li>
                        <a href="https://www.interviewcake.com/concept/bit-shift">Bit Shifting</a>
                    </li>
                </ul>
            </li>

            
            <li>
                

                <a ng-hide="currentUser.is_full_access" href="https://www.interviewcake.com/upgrade">Upgrade</a>
            </li>
            
            
            <li>
                
                <a href="https://www.interviewcake.com/all-questions/python">All Questions</a>
                
            </li>
            
            <li>
                
                <a href="https://www.interviewcake.com/about">About</a>
                
            </li>
        </ul>



        <ul class="nav navbar-nav navbar-right" ng-show="currentUserSet">

            
            



            
            <li class="dropdown language-dropdown ng-scope" ng-controller="NavbarTranslationCtrl" ng-show="contentLanguage ">
                <a rel="nofollow" href="" class="dropdown-toggle ng-binding" data-toggle="dropdown">
                    Python <span class="caret"></span>
                </a>
                <ul class="dropdown-menu" role="menu">
                
                    <!-- ngRepeat: language in contentLanguages --><li ng-repeat="language in contentLanguages" class="ng-scope">
                        <a href="" ng-click="updateLanguage(language, true)" class="ng-binding">Python</a>
                    </li><!-- end ngRepeat: language in contentLanguages --><li ng-repeat="language in contentLanguages" class="ng-scope">
                        <a href="" ng-click="updateLanguage(language, true)" class="ng-binding">Ruby</a>
                    </li><!-- end ngRepeat: language in contentLanguages --><li ng-repeat="language in contentLanguages" class="ng-scope">
                        <a href="" ng-click="updateLanguage(language, true)" class="ng-binding">Java</a>
                    </li><!-- end ngRepeat: language in contentLanguages --><li ng-repeat="language in contentLanguages" class="ng-scope">
                        <a href="" ng-click="updateLanguage(language, true)" class="ng-binding">JavaScript</a>
                    </li><!-- end ngRepeat: language in contentLanguages --><li ng-repeat="language in contentLanguages" class="ng-scope">
                        <a href="" ng-click="updateLanguage(language, true)" class="ng-binding">C++ (beta)</a>
                    </li><!-- end ngRepeat: language in contentLanguages -->
                
                </ul>
            </li>
            

            <li>
                <p class="navbar-text">
                    
                    'sup <a rel="nofollow" trackling="" the-event="Settings Link Click" href="https://www.interviewcake.com/account">Justin</a>.
                    
                    <span ng-show="currentUser.is_full_access" class="glyphicon glyphicon-star full-access-badge ng-hide"></span>
                </p>
            </li>
            <li ng-hide="currentUser.is_anonymous">
                <a rel="nofollow" tracklink="" the-event="Logout Link Click" the-properties="{&quot;which&quot; : &quot;header top right&quot;}" href="https://www.interviewcake.com/auth/logout/?next=/" class="ng-isolate-scope">Log out</a>
            </li>

            <li ng-show="currentUser.is_anonymous" class="ng-hide">
                <a href="" rel="nofollow" ng-click="loginClick('header top right')">Log in to save progress</a>
            </li>
        </ul>
    </div>

</div>

<div class="below-nav">

    <div class="ic-alerts">
        
        
    </div>

    

    
    

<div class="quiz ng-scope" ng-controller="PrepSeshApp">
    
        
            

<div ng-controller="NumberlineCtrl" class="numberline-wrapper ng-scope">

    <section ng-controller="NumberlineScrollingCtrl" class="numberline-scrolling ng-scope" ngc-scroll="setEdgeFadeIntensity()">
        
            
                <div class="numberline-number-wrapper current                                                              done                             ng-scope" ng-controller="NumberlineCurrentQuestionCtrl">

    
    
        <a href="https://www.interviewcake.com/question/stock-price" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Apple Stocks">
    
    

            <span class="number">
                1
            </span>

            
                <i class="fa fa-check"></i>
            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                done
                           ">

    
    
        <a href="https://www.interviewcake.com/question/product-of-other-numbers" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Product of All Other Numbers">
    
    

            <span class="number">
                2
            </span>

            
                <i class="fa fa-check"></i>
            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/highest-product-of-3" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Highest Product of 3">
    
    

            <span class="number">
                3
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/merging-ranges" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Merging Meeting Times">
    
    

            <span class="number">
                4
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/coin" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Making Change">
    
    

            <span class="number">
                5
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/rectangular-love" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Rectangular Love">
    
    

            <span class="number">
                6
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/temperature-tracker" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Temperature Tracker">
    
    

            <span class="number">
                7
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                unfinished
                           ">

    
    
        <a href="https://www.interviewcake.com/question/balanced-binary-tree" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Balanced Binary Tree">
    
    

            <span class="number">
                8
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/bst-checker" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Binary Search Tree Checker">
    
    

            <span class="number">
                9
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/second-largest-item-in-bst" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="2nd Largest Item in a Binary Search Tree">
    
    

            <span class="number">
                10
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/compress-url-list" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="MillionGazillion">
    
    

            <span class="number">
                11
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/find-in-ordered-set" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Find in Ordered Set">
    
    

            <span class="number">
                12
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/find-rotation-point" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Find Rotation Point">
    
    

            <span class="number">
                13
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/inflight-entertainment" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Inflight Entertainment">
    
    

            <span class="number">
                14
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/nth-fibonacci" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Compute nth Fibonacci Number">
    
    

            <span class="number">
                15
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                unfinished
                           ">

    
    
        <a href="https://www.interviewcake.com/question/cake-thief" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="The Cake Thief">
    
    

            <span class="number">
                16
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/js-scope" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="JavaScript Scope">
    
    

            <span class="number">
                17
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/js-whats-wrong" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="What's Wrong with This JavaScript?">
    
    

            <span class="number">
                18
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/queue-two-stacks" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Queue Two Stacks">
    
    

            <span class="number">
                19
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/largest-stack" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Largest Stack">
    
    

            <span class="number">
                20
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/find-unique-int-among-duplicates" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="The Stolen Breakfast Drone">
    
    

            <span class="number">
                21
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/delete-node" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Delete Node">
    
    

            <span class="number">
                22
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/linked-list-cycles" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Does This Linked List Have A Cycle?">
    
    

            <span class="number">
                23
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/reverse-linked-list" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Reverse A Linked List">
    
    

            <span class="number">
                24
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/kth-to-last-node-in-singly-linked-list" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Kth to Last Node in a Singly-Linked List">
    
    

            <span class="number">
                25
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                done
                           ">

    
    
        <a href="https://www.interviewcake.com/question/reverse-string-in-place" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Reverse String in Place">
    
    

            <span class="number">
                26
            </span>

            
                <i class="fa fa-check"></i>
            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/reverse-words" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Reverse Words">
    
    

            <span class="number">
                27
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/matching-parens" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Parenthesis Matching">
    
    

            <span class="number">
                28
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/bracket-validator" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Bracket Validator">
    
    

            <span class="number">
                29
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/permutation-palindrome" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Permutation Palindrome">
    
    

            <span class="number">
                30
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/recursive-string-permutations" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Recursive String Permutations">
    
    

            <span class="number">
                31
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/top-scores" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Top Scores">
    
    

            <span class="number">
                32
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/which-appears-twice" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Which Appears Twice">
    
    

            <span class="number">
                33
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/word-cloud" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Word Cloud Data">
    
    

            <span class="number">
                34
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/shuffle" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="In-Place Shuffle">
    
    

            <span class="number">
                35
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/single-rifle-check" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Single Riffle Shuffle">
    
    

            <span class="number">
                36
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/simulate-5-sided-die" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Simulate 5-sided die">
    
    

            <span class="number">
                37
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/simulate-7-sided-die" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Simulate 7-sided die">
    
    

            <span class="number">
                38
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/two-egg-problem" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Two Egg Problem">
    
    

            <span class="number">
                39
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/find-duplicate-optimize-for-space" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Find Repeat, Space Edition">
    
    

            <span class="number">
                40
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/find-duplicate-optimize-for-space-beast-mode" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Find Repeat, Space Edition BEAST MODE">
    
    

            <span class="number">
                41
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/find-duplicate-files" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Find Duplicate Files">
    
    

            <span class="number">
                42
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/merge-sorted-arrays" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="Merge Sorted Arrays">
    
    

            <span class="number">
                43
            </span>

            

    
    
        </a>
    
    
</div>

            
        
            
                <div class="numberline-number-wrapper 
                           
                                future
                           ">

    
    
        <a href="https://www.interviewcake.com/question/url-shortener" title="" data-toggle="tooltip" data-placement="bottom" data-delay="{ &quot;show&quot;: 0, &quot;hide&quot;: 0}" data-original-title="URL Shortener">
    
    

            <span class="number">
                44
            </span>

            

    
    
        </a>
    
    
</div>

            
        
    </section>

    <div class="edge-fade left" ng-style="{left: edgeFadePositions.left + 'px'}" style="left: -160px;"></div>
    <div class="edge-fade right" ng-style="{right: edgeFadePositions.right + 'px'}" style="right: 0px;"></div>

    <div class="scroll-on-hover left ng-hide" ng-mouseenter="scrollDirection = '-'; toggleScroll()" ng-mouseleave="toggleScroll()" ng-hide="edgeFadePositions.left === -edgeFadeWidth">
    </div>
    <div class="scroll-on-hover right" ng-mouseenter="scrollDirection = '+'; toggleScroll()" ng-mouseleave="toggleScroll()" ng-hide="edgeFadePositions.right &lt;= -(edgeFadeWidth - 2)"> <!-- cuz chrome only scrolls to 2px less than it can -->
    </div>

</div>

        
    

    
        <div class="free-questions-left" ng-show="currentUserSet &amp;&amp; !currentUser.is_full_access">


<p>
<span ng-show="currentUser.getNumFreeQuestionsLeft()&gt;0" class="ng-hide">

    <span ng-show="currentUser.getNumFreeQuestionsLeft()==1" class="ng-hide">Just </span>
    <strong class="num ng-binding">0</strong>

</span>
<span ng-show="currentUser.getNumFreeQuestionsLeft()==0">
    No
</span>

more free question<span ng-show="currentUser.getNumFreeQuestionsLeft() != 1">s</span>

left!
</p>



<a href="https://www.interviewcake.com/upgrade" class="btn btn-default btn-sm btn-rarr">
    Upgrade Now
</a>

</div>

    

    
    <div class="wrapper-hack" ng-init="slug='stock-price'">
<div class="card ng-scope" ng-class="{'started': btnPresses.length &gt; 0}" ng-controller="CardCtrl">

    <div class="sections">
        
    <div>
<span class="question-data" data-name="Apple Stocks" data-meta_desc="Figure out the optimal buy and sell time for a given stock, given its prices yesterday." data-title="" data-meta_keywords="" data-weight="8" data-difficulty="7" data-num-hints="15" data-num-gotchas="3" ng-init="setNumHints(15); setNumGotchas(3); ">
</span>

<div class="section-wrapper ng-isolate-scope section-question" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()" section="question">
    <h3 class="heading slide ng-binding ng-isolate-scope ng-hide" ng-show="shouldShow()" heading="question" hide-heading=""></h3>

    <div class="section section-question" ng-class="getSectionClass()" ng-transclude="">
<p class="ng-scope">
<strong>
Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.
</strong>
</p>

<p class="ng-scope">
Suppose we could access yesterday's stock prices as <span class="ic-words ng-isolate-scope" ng-transclude="" words="question__stock-price__an-array"><span class="ng-scope">a list</span></span>, where:
</p>
<ul class="ng-scope">
<li>
The indices are the time in minutes past trade opening time, which was 9:30am local time.
</li>
<li>
The values are the price in dollars of Apple stock at that time.
</li>
</ul>
<p class="ng-scope">
So if the stock cost $500 at 10:30am, <span class="ic-code-inline ng-isolate-scope" ng-transclude="" code-inline="question__stock-price__stock-prices-yesterday-example"><span class="ng-scope">stock_prices_yesterday[60] = 500</span></span>.
</p>

<p class="ng-scope">
Write an efficient function that takes <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__stock-prices-yesterday"><span class="ng-scope">stock_prices_yesterday</span></span> and returns <strong>the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.</strong>
</p>

<p class="ng-scope">
For example:
</p>

<div code-block="question__stock-price__input-output-example" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope"><pre class="  language-python">  <code class="  language-python" ng-transclude="">stock_prices_yesterday <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">10</span><span class="token punctuation">,</span> <span class="token number">7</span><span class="token punctuation">,</span> <span class="token number">5</span><span class="token punctuation">,</span> <span class="token number">8</span><span class="token punctuation">,</span> <span class="token number">11</span><span class="token punctuation">,</span> <span class="token number">9</span><span class="token punctuation">]</span>

get_max_profit<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span>
<span class="token comment" spellcheck="true"># returns 6 (buying for $5 and selling for $11)</span></code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>

<span class="ic-words ng-isolate-scope" ng-transclude="" words="question__stock-price__using-namespace-std"></span>

<p class="ng-scope">
No "shorting"—you must buy before you sell. You may not buy <em>and</em> sell in the same time step (at least 1 minute must pass).
</p>
</div>

    
</div>

<div class="section-wrapper ng-isolate-scope section-gotchas" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()" section="gotchas" style="">
    <h3 class="heading slide ng-binding ng-isolate-scope" ng-show="shouldShow()" heading="gotchas" hide-heading="" style="display: block;">Gotchas</h3>

    <div class="section section-gotchas" ng-class="getSectionClass()" ng-transclude="">
<div class="note slide ng-isolate-scope highlight-flash" ng-show="shouldShow()" note="" number="1" type="gotcha" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
<strong>It is not sufficient to simply take the difference between the highest price and the lowest price</strong>, because the highest price may come <em>before</em> the lowest price. You must buy before you sell.
</p>
</div>
</div>

<div class="note slide ng-isolate-scope highlight-flash" ng-show="shouldShow()" note="" number="2" type="gotcha" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
What if the stock value <em>goes down all day</em>? In that case, the best profit will be <strong>negative</strong>.
</p>
</div>
</div>

<div class="note slide ng-isolate-scope highlight-flash" ng-show="shouldShow()" note="" number="3" type="gotcha" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
You can do this in <span complexity="n" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span></span></span></span> time and <span complexity="1" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">O(1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord">1</span><span class="mclose">)</span></span></span></span></span></span></span> space!
</p>
</div>
</div>
</div>

    
</div>

<div class="section-wrapper ng-isolate-scope section-breakdown" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()" section="breakdown" style="">
    <h3 class="heading slide ng-binding ng-isolate-scope" ng-show="shouldShow()" heading="breakdown" hide-heading="" style="display: block;">Breakdown</h3>

    <div class="section section-breakdown" ng-class="getSectionClass()" ng-transclude="">

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="1" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
To start, try writing an example value for <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__stock-prices-yesterday"><span class="ng-scope">stock_prices_yesterday</span></span> and finding the maximum profit "by hand." What's your process for figuring out the maximum profit?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="2" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
The <span concept="brute-force" class="ng-isolate-scope"><span class="concept-wrapper" ng-init="showConcept=false">

    <span ng-click="showConcept=!showConcept" class="concept">
        <span class="concept-name" ng-transclude=""><span class="ng-scope">brute force</span></span>
        <span class="show-concept-icon">↴</span>
    </span>

    <!-- ngInclude: conceptPartialUrl --><div ng-show="showConcept" class="slide concept-explanation ng-scope ng-hide" ng-include="conceptPartialUrl" style=""><div class="ng-scope">
<p>
A <strong>brute force</strong> algorithm simply enumerates all possible answers to the question and checks them for correctness.
</p>

<p>
It's seldom the most efficient approach, but it can be helpful to 
consider the time cost of the brute force approach when building an 
optimized solution. If your solution isn't faster than the brute force 
approach, it may not be optimal.
</p>
<script type="text/javascript"></script>
</div>
</div>

</span>
</span> approach would be to try <em>every pair of times</em> (treating the earlier time as the buy time and the later time as the sell time) and see which one is higher.
</p>
<div code-block="question__stock-price__brute-force" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope" style="width: 100%;"><pre class="  language-python">  <code class="  language-python" ng-transclude=""><span class="token keyword">def</span> <span class="token function">get_max_profit</span><span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">:</span>

    max_profit <span class="token operator">=</span> <span class="token number">0</span>

    <span class="token comment" spellcheck="true"># go through every time</span>
    <span class="token keyword">for</span> outer_time <span class="token keyword">in</span> xrange<span class="token punctuation">(</span>len<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">:</span>

        <span class="token comment" spellcheck="true"># for every time, go through every OTHER time</span>
        <span class="token keyword">for</span> inner_time <span class="token keyword">in</span> xrange<span class="token punctuation">(</span>len<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">:</span>

            <span class="token comment" spellcheck="true"># for each pair, find the earlier and later times</span>
            earlier_time <span class="token operator">=</span> min<span class="token punctuation">(</span>outer_time<span class="token punctuation">,</span> inner_time<span class="token punctuation">)</span>
            later_time   <span class="token operator">=</span> max<span class="token punctuation">(</span>outer_time<span class="token punctuation">,</span> inner_time<span class="token punctuation">)</span>

            <span class="token comment" spellcheck="true"># and use those to find the earlier and later prices</span>
            earlier_price <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span>earlier_time<span class="token punctuation">]</span>
            later_price   <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span>later_time<span class="token punctuation">]</span>

            <span class="token comment" spellcheck="true"># see what our profit would be if we bought at the</span>
            <span class="token comment" spellcheck="true"># earlier price and sold at the later price</span>
            potential_profit <span class="token operator">=</span> later_price <span class="token operator">-</span> earlier_price

            <span class="token comment" spellcheck="true"># update max_profit if we can do better</span>
            max_profit <span class="token operator">=</span> max<span class="token punctuation">(</span>max_profit<span class="token punctuation">,</span> potential_profit<span class="token punctuation">)</span>

    <span class="token keyword">return</span> max_profit</code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>
<p class="ng-scope">
But that will take <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span> time, since we have two nested loops—for <em>every</em> time, we're going through <em>every other</em> time. Can we do better?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="3" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
Well, we’re doing a lot of extra work. We’re looking at every pair <em>twice</em>. We know we have to buy before we sell, so in our <em>inner for loop</em> we could just look at every price <strong>after</strong> the price in our <em>outer for loop</em>.
</p>
<p class="ng-scope">
That could look like this:
</p>
<div code-block="question__stock-price__smarter-brute-force" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope" style="width: 100%;"><pre class="  language-python">  <code class="  language-python" ng-transclude=""><span class="token keyword">def</span> <span class="token function">get_max_profit</span><span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">:</span>

    max_profit <span class="token operator">=</span> <span class="token number">0</span>

    <span class="token comment" spellcheck="true"># go through every price (with its index as the time)</span>
    <span class="token keyword">for</span> earlier_time<span class="token punctuation">,</span> earlier_price <span class="token keyword">in</span> enumerate<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">:</span>

        <span class="token comment" spellcheck="true"># and go through all the LATER prices</span>
        <span class="token keyword">for</span> later_price <span class="token keyword">in</span> stock_prices_yesterday<span class="token punctuation">[</span>earlier_time<span class="token operator">+</span><span class="token number">1</span><span class="token punctuation">:</span><span class="token punctuation">]</span><span class="token punctuation">:</span>

            <span class="token comment" spellcheck="true"># see what our profit would be if we bought at the</span>
            <span class="token comment" spellcheck="true"># earlier price and sold at the later price</span>
            potential_profit <span class="token operator">=</span> later_price <span class="token operator">-</span> earlier_price

            <span class="token comment" spellcheck="true"># update max_profit if we can do better</span>
            max_profit <span class="token operator">=</span> max<span class="token punctuation">(</span>max_profit<span class="token punctuation">,</span> potential_profit<span class="token punctuation">)</span>

    <span class="token keyword">return</span> max_profit</code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>
<p class="ng-scope">
<strong>What’s our runtime now?</strong>
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="4" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
Well, our outer for loop goes through <em>all</em> the times and prices, but our inner for loop goes through <em>one fewer price each time</em>. So our total number of steps is the sum <span concept="summation-1-to-n" class="ng-isolate-scope"><span class="concept-wrapper" ng-init="showConcept=false">

    <span ng-click="showConcept=!showConcept" class="concept">
        <span class="concept-name" ng-transclude=""><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>+</mo><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mi>n</mi><mo>−</mo><mn>2</mn><mo>)</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">n + (n - 1) + (n - 2) ... + 2 + 1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">+</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span><span class="mclose">)</span><span class="mbin">+</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">2</span><span class="mclose">)</span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span><span class="mbin">+</span><span class="mord">2</span><span class="mbin">+</span><span class="mord">1</span></span></span></span></span></span>
        <span class="show-concept-icon">↴</span>
    </span>

    <!-- ngInclude: conceptPartialUrl --><div ng-show="showConcept" class="slide concept-explanation ng-scope ng-hide" ng-include="conceptPartialUrl" style=""><div class="ng-scope">
<p>
The <strong>sum of integers <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>1</mn><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi>n</mi></mrow><annotation encoding="application/x-tex">1..n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.64444em; vertical-align: 0em;"></span><span class="base textstyle uncramped"><span class="mord">1</span><span class="mord">.</span><span class="mord">.</span><span class="mord mathit">n</span></span></span></span></span></strong> is <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>≈</mo><mfrac><mrow><msup><mi>n</mi><mn>2</mn></msup></mrow><mrow><mn>2</mn></mrow></mfrac></mrow><annotation encoding="application/x-tex">\approx \frac{n^2}{2}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.97032em;"></span><span class="strut bottom" style="height: 1.31532em; vertical-align: -0.345em;"></span><span class="base textstyle uncramped"><span class="mrel">≈</span><span class="minner reset-textstyle textstyle uncramped"><span class="mfrac"><span class="vlist"><span class="" style="top: 0.345em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle cramped"><span class="mord scriptstyle cramped"><span class="mord">2</span></span></span></span><span class="" style="top: -0.23em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle textstyle uncramped frac-line"></span></span><span class="" style="top: -0.394em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord scriptstyle uncramped"><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.0714286em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-scriptstyle scriptscriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span></span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span></span></span></span></span></span>, which is <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span>
</p>

<!--
<p>
This actually comes up quite a bit. For example:
</p>

<div code-block>
def get_possible_pairs_unordered(list_of_people):
    '''
    get all possible pairs from a list of people
    order doesn't matter. in other words, we don't want to count
    (alice, bob) and (bob, alice) as separate possible pairs-
    we just want to count them as one possible pair
    '''

    possible_pairs_unordered = []
    for id, first_person in list_of_people.iteritems():
        for second_person in list_of_people[id:]:
            possible_pairs_unordered.append((first_person, second_person))
    return possible_pairs_unordered

</div>

<p>
Here we have two nested loops, which we know is usually <span complexity="n^2"></span>. But the inner loop only looks at people "past" the person the outer loop is on, so that we avoid counting the same pair twice. So early on our inner loop does close to <span math>n</span> operations...but in the last iteration of our outer loop, the inner loop doesn't even run! And in the second-to-last iteration of the outer loop, the inner loop only runs once, etc.
</p>

<p>
So if we look at this starting from the beginning, it feels like the inner loop runs <span complexity="n"></span> times, for a total of <span complexity="n^2"></span> runtime. But if you look at it starting from the end, it feels like the inner loop runs a constant number of times, for a total of <span complexity="n"></span> runtime. Which is it??
</p>
-->

<p>
Series' like this actually come up quite a bit:
</p>

<span class="ic-math ng-isolate-scope block" ng-class="{'block': isBlock()}" ng-transclude="" math="" block=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>1</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>3</mn><mo>+</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>+</mo><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi>n</mi></mrow><annotation encoding="application/x-tex">
1 + 2 + 3 + ... + (n-1) + n
</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span class="mord">1</span><span class="mbin">+</span><span class="mord">2</span><span class="mbin">+</span><span class="mord">3</span><span class="mbin">+</span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span><span class="mbin">+</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord mathit">n</span></span></span></span></span>

<p>
Or, equivalently, the other way around:
</p>

<span class="ic-math ng-isolate-scope block" ng-class="{'block': isBlock()}" ng-transclude="" math="" block=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>+</mo><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo><mo>+</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">
n + (n-1) + ... + 3 + 2 + 1
</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">+</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span><span class="mbin">+</span><span class="mord">3</span><span class="mbin">+</span><span class="mord">2</span><span class="mbin">+</span><span class="mord">1</span></span></span></span></span>

<p>
And sometimes the last <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.43056em;"></span><span class="strut bottom" style="height: 0.43056em; vertical-align: 0em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span></span></span></span></span> is omitted, but as we'll see it doesn't affect the big o:
</p>

<span class="ic-math ng-isolate-scope block" ng-class="{'block': isBlock()}" ng-transclude="" math="" block=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo><mo>+</mo><mo>(</mo><mi>n</mi><mo>−</mo><mn>2</mn><mo>)</mo><mo>+</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>+</mo><mn>3</mn><mo>+</mo><mn>2</mn><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">
(n-1) + (n-2) + ... + 3 + 2 + 1
</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span><span class="mclose">)</span><span class="mbin">+</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">2</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span><span class="mbin">+</span><span class="mord">3</span><span class="mbin">+</span><span class="mord">2</span><span class="mbin">+</span><span class="mord">1</span></span></span></span></span>

<p>
Let's draw this out. Let's say <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>=</mo><mn>1</mn><mn>0</mn></mrow><annotation encoding="application/x-tex">n=10</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.64444em; vertical-align: 0em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mrel">=</span><span class="mord">1</span><span class="mord">0</span></span></span></span></span>, so we'll represent <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">n-1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span></span></span></span></span> as nine circles:
</p>

<div class="diagram">
    <img src="stocks_files/summation_1_to_n__n_minus_1_circles.svg" alt="A row of 9 circles." width="215" height="31">


    
</div>


<p>
We can continue the pattern with <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>−</mo><mn>2</mn></mrow><annotation encoding="application/x-tex">n-2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">2</span></span></span></span></span>
</p>

<div class="diagram">
    <img src="stocks_files/summation_1_to_n__n_minus_2_circles.svg" alt="2 rows of cirlces: 9 on top, 8 on the bottom." width="215" height="48">


    
</div>


<p>
And <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>−</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">n-3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">3</span></span></span></span></span>, <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>−</mo><mn>4</mn></mrow><annotation encoding="application/x-tex">n-4</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">4</span></span></span></span></span>, etc, all the way down to 1:
</p>

<div class="diagram">
    <img src="stocks_files/summation_1_to_n__circles_down_to_1.svg" alt="9 rows of circles: 9 on top, and one fewer circle in each row, down to 1 circle on the bottom." width="215" height="159">


    
</div>


<p>
Notice both the top and right "sides" of our set of circles have <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">n-1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span></span></span></span></span> items:
</p>

<div class="diagram">
    <img src="stocks_files/summation_1_to_n__n_minus_1_sides.svg" alt="In a right triangle formed by 9 rows of cirlces (9 in the top row, down to 1 in the bottom row) the top and left side of the triangle are 9 circles long." width="215" height="177">


    
</div>


<p>
In fact, we could imagine our circles inside of a square with sides of length n-1:
</p>

<div class="diagram">
    <img src="stocks_files/summation_1_to_n__square.svg" alt="A square around 9 rows of cirlces (9 in the top row, down to 1 in the bottom row) so the square is 9 by 9 circles." width="215" height="181">


    
</div>


<p>
Notice that we've filled in just about half of the square!
</p>

<p>
Of course, the area of the square is <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo><mo>∗</mo><mo>(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">(n-1) * (n-1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span><span class="mclose">)</span><span class="mbin">∗</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span><span class="mclose">)</span></span></span></span></span>, which is <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span>. Our total number of circles is about half of that, so <span complexity="n^2/2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mi mathvariant="normal">/</mi><mn>2</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2/2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mord">/</span><span class="mord">2</span><span class="mclose">)</span></span></span></span></span></span></span>, which is still <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span>. Remember: with <a href="https://www.interviewcake.com/big-o-notation-time-and-space-complexity">big O notation</a>, we throw out the constants.
</p>

<p>
If we had started from <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.43056em;"></span><span class="strut bottom" style="height: 0.43056em; vertical-align: 0em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span></span></span></span></span> instead of <span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">n-1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.64444em;"></span><span class="strut bottom" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="base textstyle uncramped"><span class="mord mathit">n</span><span class="mbin">−</span><span class="mord">1</span></span></span></span></span> we'd have <span complexity="n^2 + n" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>+</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2 + n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mbin">+</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span></span></span></span>, which again is still <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span> since in big O notation we drop the less significant terms.
</p>
<script type="text/javascript"></script>
</div>
</div>

</span>
</span>, which is <em>still</em> <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span> time.
</p>
<p class="ng-scope">
We can do better!
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="5" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
If we're going to do better than <span complexity="n^2" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><msup><mi>n</mi><mn>2</mn></msup><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n^2)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.814108em;"></span><span class="strut bottom" style="height: 1.06411em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord"><span class="mord mathit">n</span><span class="vlist"><span class="" style="top: -0.363em; margin-right: 0.05em;"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span><span class="reset-textstyle scriptstyle uncramped"><span class="mord">2</span></span></span><span class="baseline-fix"><span class="fontsize-ensurer reset-size5 size5"><span class="" style="font-size: 0em;">​</span></span>​</span></span></span><span class="mclose">)</span></span></span></span></span></span></span>, we're probably going to do it in either <span complexity="nlgn" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>lg</mo><mrow><mi>n</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n\lg{n})</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mop">l<span style="margin-right: 0.01389em;">g</span></span><span class="mord textstyle uncramped"><span class="mord mathit">n</span></span><span class="mclose">)</span></span></span></span></span></span></span> or <span complexity="n" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span></span></span></span>. <span complexity="nlgn" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>lg</mo><mrow><mi>n</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n\lg{n})</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mop">l<span style="margin-right: 0.01389em;">g</span></span><span class="mord textstyle uncramped"><span class="mord mathit">n</span></span><span class="mclose">)</span></span></span></span></span></span></span>
 comes up in sorting and searching algorithms where we're recursively 
cutting the set in half. It's not obvious that we can save time by 
cutting the set in half here. Let's first see how well we can do by 
looping through the set only <em>once</em>.
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="6" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
Since we're trying to loop through the set once, let's use a <span concept="greedy" class="ng-isolate-scope"><span class="concept-wrapper" ng-init="showConcept=false">

    <span ng-click="showConcept=!showConcept" class="concept">
        <span class="concept-name" ng-transclude=""><span class="ng-scope">greedy</span></span>
        <span class="show-concept-icon">↴</span>
    </span>

    <!-- ngInclude: conceptPartialUrl --><div ng-show="showConcept" class="slide concept-explanation ng-scope ng-hide" ng-include="conceptPartialUrl" style=""><div class="ng-scope">
<p>
A <strong>greedy</strong> algorithm iterates through the problem space taking the optimal solution "so far," until it reaches the end.
</p>

<p>
The greedy approach is only optimal if the problem has "optimal 
substructure," which means stitching together optimal solutions to 
subproblems yields an optimal solution.
</p>

<!--
This is not true, for example, in path finding.
-->
<script type="text/javascript"></script>
</div>
</div>

</span>
</span> approach, where we keep a running <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> until we reach the end. We'll start our <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> at $0. As we're iterating, how do we know if we've found a new <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span>?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="7" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
At each iteration, our <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> is either:
</p>
<ol class="ng-scope">
<li>the same as the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> at the last time step, or</li>
<li>the max profit we can get by selling at the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span>
</li>
</ol>
<p class="ng-scope">
How do we know when we have case (2)?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="8" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
The max profit we can get by selling at the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span> is simply the difference between the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span> and the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span> from earlier in the day. If this difference is greater than the current <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span>, we have a new <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span>.
</p>
<p class="ng-scope">
So for every price, we’ll need to:
</p>
<ul class="ng-scope">
<li>keep track of the <strong>lowest price we’ve seen so far</strong>
</li>
<li>see if we can get a <strong>better profit</strong>
</li>
</ul>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="9" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
Here’s one possible solution:
</p>
<div code-block="question__stock-price__solution-before-edge-cases" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope" style="width: 100%;"><pre class="  language-python">  <code class="  language-python" ng-transclude=""><span class="token keyword">def</span> <span class="token function">get_max_profit</span><span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">:</span>

    min_price <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
    max_profit <span class="token operator">=</span> <span class="token number">0</span>

    <span class="token keyword">for</span> current_price <span class="token keyword">in</span> stock_prices_yesterday<span class="token punctuation">:</span>

        <span class="token comment" spellcheck="true"># ensure min_price is the lowest price we've seen so far</span>
        min_price <span class="token operator">=</span> min<span class="token punctuation">(</span>min_price<span class="token punctuation">,</span> current_price<span class="token punctuation">)</span>

        <span class="token comment" spellcheck="true"># see what our profit would be if we bought at the</span>
        <span class="token comment" spellcheck="true"># min price and sold at the current price</span>
        potential_profit <span class="token operator">=</span> current_price <span class="token operator">-</span> min_price

        <span class="token comment" spellcheck="true"># update max_profit if we can do better</span>
        max_profit <span class="token operator">=</span> max<span class="token punctuation">(</span>max_profit<span class="token punctuation">,</span> potential_profit<span class="token punctuation">)</span>

    <span class="token keyword">return</span> max_profit</code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>
<p class="ng-scope">
We’re finding the max profit with one pass and constant space!
</p>
<p class="ng-scope">
<strong>Are we done?</strong> Let’s think about some edge cases. What if the stock value <em>stays the same</em>? What if the stock value <em>goes down all day</em>?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="10" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
If the stock price doesn't change, the max possible profit is 0. Our function will correctly return that. So we're good.
</p>
<p class="ng-scope">
But if the value <em>goes down all day</em>, we’re in trouble. Our function would return 0, but there’s no way we could break even if the price always goes down.
</p>
<p class="ng-scope">
<strong>How can we handle this?</strong>
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="11" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
Well, what are our options? Leaving our function as it is and just returning zero is <em>not</em> a reasonable option—we wouldn't know if our best profit was negative or <em>actually</em> zero, so we'd be losing information. Two reasonable options could be:
</p>
<ol class="ng-scope">
<li>
<strong>return a negative profit</strong>. “What’s the least badly we could have done?”</li>
<li>
<strong>throw an error</strong>. “We should not have purchased stocks yesterday!”</li>
</ol>
<p class="ng-scope">
In this case, it’s probably best to go with option (1). The advantages of returning a negative profit are:
</p>
<ul class="ng-scope">
<li>We <strong>more accurately answer the challenge</strong>. If profit is "revenue minus expenses", we’re returning the <em>best</em> we could have done.</li>
<li>It's <strong>less opinionated</strong>. We'll leave decisions up to 
our function’s users. It would be easy to wrap our function in a helper 
function to decide if it’s worth making a purchase.</li>
<li>We allow ourselves to <strong>collect better data</strong>. It <em>matters</em> if we would have lost money, and it <em>matters</em> how much we would have lost. If we’re trying to get rich, we’ll probably care about those numbers.</li>
</ul>
<p class="ng-scope">
<strong>How can we adjust our function to return a negative profit if we can only lose money?</strong> Initializing <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> to 0 won’t work...
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="12" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
Well, we started our <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span> at the first price, so let’s start our <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> at the <em>first profit we could get</em>—if we buy at the first time and sell at the second time.
</p>
<div code-block="question__stock-price__first-min-price-and-max-profit" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope"><pre class="  language-python">  <code class="  language-python" ng-transclude="">min_price <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
max_profit <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">-</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span></code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>
<p class="ng-scope">
But we have the potential for an index out of bounds error here, if <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__stock-prices-yesterday"><span class="ng-scope">stock_prices_yesterday</span></span> has fewer than 2 prices.
</p>

<p class="ng-scope">
We <em>do</em> want to throw an error in that case, since <em>profit</em> requires buying <em>and</em>
 selling, which we can't do with less than 2 prices. So rather than 
throwing a confusing index out of bounds error, let's explicitly catch 
that case and throw a more helpful error message:
</p>
<div code-block="question__stock-price__error-requires-two-prices" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope"><pre class="  language-python">  <code class="  language-python" ng-transclude=""><span class="token keyword">if</span> len<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span> <span class="token operator">&lt;</span> <span class="token number">2</span><span class="token punctuation">:</span>
    <span class="token keyword">raise</span> IndexError<span class="token punctuation">(</span><span class="token string">'Getting a profit requires at least 2 prices'</span><span class="token punctuation">)</span>

min_price <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
max_profit <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">-</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>

<span class="token comment" spellcheck="true"># etc...</span></code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>
<p class="ng-scope">
Ok, does that work?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="13" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
No! <strong><span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> is still always 0!</strong> What’s happening?
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="14" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
If the price always goes down, <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span> is always set to the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span>. So <span class="ic-code-inline ng-isolate-scope" ng-transclude="" code-inline="question__stock-price__current-price-minus-min-price"><span class="ng-scope">current_price - min_price</span></span> comes out to 0, which of course will always be greater than a negative profit.
</p>
<p class="ng-scope">
When we’re calculating the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span>, we need to make sure we never have a case where we try <strong>both buying and selling stocks at the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span></strong>.
</p>
</div>
</div>

<div class="note slide ng-isolate-scope" ng-show="shouldShow()" note="" number="15" type="hint" style="display: block;">
    <div class="note-content" ng-transclude="">
<p class="ng-scope">
To make sure we’re always buying at an <em>earlier</em> price, never the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span>, let’s switch the order around so we calculate <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> <em>before</em> we update <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span>.
</p>

<p class="ng-scope">
We'll also need to pay special attention to time 0. Make sure we don't try to buy <em>and</em> sell at time 0!
</p>
<p class="ng-scope">
</p>
</div>
</div>

<div class="section-wrapper ng-isolate-scope section-solution slide highlight-flash" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()" section="solution" style="display: block;">
    <h3 class="heading slide ng-binding ng-isolate-scope" ng-show="shouldShow()" heading="solution" hide-heading="">Solution</h3>

    <div class="section section-solution" ng-class="getSectionClass()" ng-transclude="">

<p class="ng-scope">
We’ll <span concept="greedy" class="ng-isolate-scope"><span class="concept-wrapper" ng-init="showConcept=false">

    <span ng-click="showConcept=!showConcept" class="concept">
        <span class="concept-name" ng-transclude=""><span class="ng-scope">greedily</span></span>
        <span class="show-concept-icon">↴</span>
    </span>

    <!-- ngInclude: conceptPartialUrl --><div ng-show="showConcept" class="slide concept-explanation ng-scope ng-hide" ng-include="conceptPartialUrl" style=""><div class="ng-scope">
<p>
A <strong>greedy</strong> algorithm iterates through the problem space taking the optimal solution "so far," until it reaches the end.
</p>

<p>
The greedy approach is only optimal if the problem has "optimal 
substructure," which means stitching together optimal solutions to 
subproblems yields an optimal solution.
</p>

<!--
This is not true, for example, in path finding.
-->
<script type="text/javascript"></script>
</div>
</div>

</span>
</span> walk through the <span class="ic-words ng-isolate-scope" ng-transclude="" words="question__stock-price__array"><span class="ng-scope">list</span></span> to track the max profit and lowest price so far.
</p>

<p class="ng-scope">
For every price, we check if:
</p>

<ul class="ng-scope">
<li>we can get a better profit by buying at <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span> and selling at the <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__current-price"><span class="ng-scope">current_price</span></span>
</li>
<li>we have a new <span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span>
</li>
</ul>

<p class="ng-scope">
To start, we initialize:
</p>

<ol class="ng-scope">
<li>
<span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__min-price"><span class="ng-scope">min_price</span></span> as the first price of the day</li>
<li>
<span class="ic-variable ng-isolate-scope" ng-transclude="" var="question__stock-price__max-profit"><span class="ng-scope">max_profit</span></span> as the first profit we could get</li>
</ol>

<p class="ng-scope">
We decided to return a <em>negative</em> profit if the price decreases 
all day and we can't make any money. We could have thrown an error 
instead, but returning the negative profit is cleaner, makes our 
function less opinionated, and ensures we don't lose information.
</p>

<div code-block="question__stock-price__solution" language="python" translation-highlighting="dynamic" class="ng-scope ng-isolate-scope" style="width: 100%;"><pre class="  language-python">  <code class="  language-python" ng-transclude=""><span class="token keyword">def</span> <span class="token function">get_max_profit</span><span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">:</span>

    <span class="token comment" spellcheck="true"># make sure we have at least 2 prices</span>
    <span class="token keyword">if</span> len<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span> <span class="token operator">&lt;</span> <span class="token number">2</span><span class="token punctuation">:</span>
        <span class="token keyword">raise</span> IndexError<span class="token punctuation">(</span><span class="token string">'Getting a profit requires at least 2 prices'</span><span class="token punctuation">)</span>

    <span class="token comment" spellcheck="true"># we'll greedily update min_price and max_profit, so we initialize</span>
    <span class="token comment" spellcheck="true"># them to the first price and the first possible profit</span>
    min_price <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
    max_profit <span class="token operator">=</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> <span class="token operator">-</span> stock_prices_yesterday<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>

    <span class="token keyword">for</span> index<span class="token punctuation">,</span> current_price <span class="token keyword">in</span> enumerate<span class="token punctuation">(</span>stock_prices_yesterday<span class="token punctuation">)</span><span class="token punctuation">:</span>

        <span class="token comment" spellcheck="true"># skip the first (0th) time</span>
        <span class="token comment" spellcheck="true"># we can't sell at the first time, since we must buy first,</span>
        <span class="token comment" spellcheck="true"># and we can't buy and sell at the same time!</span>
        <span class="token comment" spellcheck="true"># if we took this out, we'd try to buy /and/ sell at time 0.</span>
        <span class="token comment" spellcheck="true"># this would give a profit of 0, which is a problem if our</span>
        <span class="token comment" spellcheck="true"># max_profit is supposed to be /negative/--we'd return 0!</span>
        <span class="token keyword">if</span> index <span class="token operator">==</span> <span class="token number">0</span><span class="token punctuation">:</span>
            <span class="token keyword">continue</span>

        <span class="token comment" spellcheck="true"># see what our profit would be if we bought at the</span>
        <span class="token comment" spellcheck="true"># min price and sold at the current price</span>
        potential_profit <span class="token operator">=</span> current_price <span class="token operator">-</span> min_price

        <span class="token comment" spellcheck="true"># update max_profit if we can do better</span>
        max_profit <span class="token operator">=</span> max<span class="token punctuation">(</span>max_profit<span class="token punctuation">,</span> potential_profit<span class="token punctuation">)</span>

        <span class="token comment" spellcheck="true"># update min_price so it's always</span>
        <span class="token comment" spellcheck="true"># the lowest price we've seen so far</span>
        min_price  <span class="token operator">=</span> min<span class="token punctuation">(</span>min_price<span class="token punctuation">,</span> current_price<span class="token punctuation">)</span>

    <span class="token keyword">return</span> max_profit</code>
</pre>
<span class="warning-message ng-binding ng-hide" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage">

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Ruby">Ruby</option><option value="2" label="Java">Java</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C++ (beta)">C++ (beta)</option></select>

</div>
<span class="only-content-language ng-binding ng-hide" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</div>

</div>

    
</div>

<div class="section-wrapper ng-isolate-scope section-complexity slide highlight-flash" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()" section="complexity" style="display: block;">
    <h3 class="heading slide ng-binding ng-isolate-scope" ng-show="shouldShow()" heading="complexity" hide-heading="">Complexity</h3>

    <div class="section section-complexity" ng-class="getSectionClass()" ng-transclude="">
    <p class="ng-scope">
    <span complexity="n" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span></span></span></span> time and <span complexity="1" class="ng-isolate-scope"><span class="complexity"><span class="ic-math ng-isolate-scope" ng-class="{'block': isBlock()}" ng-transclude="" math=""><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">O(1)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height: 0.75em;"></span><span class="strut bottom" style="height: 1em; vertical-align: -0.25em;"></span><span class="base textstyle uncramped"><span style="margin-right: 0.02778em;" class="mord mathit">O</span><span class="mopen">(</span><span class="mord">1</span><span class="mclose">)</span></span></span></span></span></span></span> space. We only loop through the <span class="ic-words ng-isolate-scope" ng-transclude="" words="question__stock-price__array"><span class="ng-scope">list</span></span> once.
    </p>
</div>

    
</div>

<div class="section-wrapper ng-isolate-scope section-learnings slide highlight-flash" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()" section="learnings" style="display: block;">
    <h3 class="heading slide ng-binding ng-isolate-scope" ng-show="shouldShow()" heading="learnings" hide-heading="">What We Learned</h3>

    <div class="section section-learnings" ng-class="getSectionClass()" ng-transclude="">
<p class="ng-scope">
This one's a good example of the <span concept="greedy" class="ng-isolate-scope"><span class="concept-wrapper" ng-init="showConcept=false">

    <span ng-click="showConcept=!showConcept" class="concept">
        <span class="concept-name" ng-transclude=""><span class="ng-scope">greedy</span></span>
        <span class="show-concept-icon">↴</span>
    </span>

    <!-- ngInclude: conceptPartialUrl --><div ng-show="showConcept" class="slide concept-explanation ng-scope ng-hide" ng-include="conceptPartialUrl" style=""><div class="ng-scope">
<p>
A <strong>greedy</strong> algorithm iterates through the problem space taking the optimal solution "so far," until it reaches the end.
</p>

<p>
The greedy approach is only optimal if the problem has "optimal 
substructure," which means stitching together optimal solutions to 
subproblems yields an optimal solution.
</p>

<!--
This is not true, for example, in path finding.
-->
<script type="text/javascript"></script>
</div>
</div>

</span>
</span> approach in action. Greedy approaches are great because they're <em>fast</em> (usually just one pass through the input). But they don't work for every problem.
</p>

<p class="ng-scope">
How do you know if a problem will lend itself to a greedy approach? Best
 bet is to try it out and see if it works. Trying out a greedy approach 
should be one of the first ways you try to break down a new question.
</p>

<p class="ng-scope">
To try it on a new problem, start by asking yourself:
</p>

<p class="ng-scope">
"Suppose we <em>could</em> come up with the answer in one pass through the input, by simply updating the 'best answer so far' as we went. What <strong><em>additional values</em></strong> would we need to keep updated as we looked at each item in our set, in order to be able to update the <strong>'best answer so far'</strong> in constant time?"
</p>

<p class="ng-scope">
In <em>this</em> case:
</p>

<p class="ng-scope">
The "<strong>best answer so far</strong>" is, of course, the max profit that we can get based on the prices we've seen so far.
</p>

<p class="ng-scope">
The "<strong>additional value</strong>" is the minimum price we've seen 
so far. If we keep that updated, we can use it to calculate the new max 
profit so far in constant time. The max profit is the larger of:
</p>

<ol class="ng-scope">
<li>
The previous max profit
</li>
<li>
The max profit we can get by selling now (the current price minus the minimum price seen so far)
</li>
</ol>

<p class="ng-scope">
Try applying this greedy methodology to future questions.
</p>

</div>

    
</div>

</div>

    
</div>
<script type="text/javascript">
            var elTranslations = {"code-inlines": {"question__stock-price__using-namespace-std": {"default": "", "cpp": "using namespace std"}, "question__stock-price__stock-prices-yesterday-example": {"camel": "stockPricesYesterday[60] = 500;", "snake": "stock_prices_yesterday[60] = 500"}, "question__stock-price__current-price-minus-min-price": {"camel": "currentPrice - minPrice", "snake": "current_price - min_price"}}, "words": {"question__stock-price__using-namespace-std": {"javascript": "", "default": "", "ruby": "", "cpp": "<p class=\"aside\">\n    In our C++ code, we assume we're <span code-inline=\"using-namespace-std\">using namespace std</span>.\n    Interviewers will commonly expect this when you're writing on a whiteboard because\n    it simplifies your code. <strong>But it's not good practice in production</strong>&#8212;it\n    floods the global namespace with things we don't need.\n</p>", "python": "", "java": ""}, "question__stock-price__an-array": {"javascript": "an array", "default": "an array", "ruby": "an array", "java": "an array", "python": "a list", "cpp": "an array"}, "question__stock-price__array": {"javascript": "array", "default": "array", "ruby": "array", "java": "array", "python": "list", "cpp": "array"}}, "vars": {"question__stock-price__max-profit": {"camel": "maxProfit", "snake": "max_profit"}, "question__stock-price__current-price": {"camel": "currentPrice", "snake": "current_price"}, "question__stock-price__min-price": {"camel": "minPrice", "snake": "min_price"}, "question__stock-price__stock-prices-yesterday": {"camel": "stockPricesYesterday", "snake": "stock_prices_yesterday"}}, "code-blocks": {"question__stock-price__smarter-brute-force": {"c": {"tests": "{\n    int i;\n    for (i = 0; i < 3; i++) {\n        testInputAndOutput((const int*) postitiveTestInputs[i], postitiveTestLengths[i],\n                           positiveTestOutputs[i], getMaxProfit);\n    }\n}", "code": "#define MAX(a, b) (((a) > (b)) ? (a) : (b))\n#define MIN(a, b) (((a) &lt; (b)) ? (a) : (b))\n\nint getMaxProfit(const int *stockPricesYesterday, size_t length) {\n    size_t earlierTime;\n    int maxProfit = 0;\n\n    // go through every price and time\n    for (earlierTime = 0; earlierTime &lt; length; earlierTime++) {\n        size_t laterTime;\n\n        // and go through all the LATER prices\n        for (laterTime = earlierTime + 1; laterTime &lt; length; laterTime++) {\n            int earlierPrice = stockPricesYesterday[earlierTime];\n            int laterPrice = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            int potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = MAX(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}, "python": {"tests": "test(positive_tests)", "code": "def get_max_profit(stock_prices_yesterday):\n\n    max_profit = 0\n\n    # go through every price (with its index as the time)\n    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):\n\n        # and go through all the LATER prices\n        for later_price in stock_prices_yesterday[earlier_time+1:]:\n\n            # see what our profit would be if we bought at the\n            # earlier price and sold at the later price\n            potential_profit = later_price - earlier_price\n\n            # update max_profit if we can do better\n            max_profit = max(max_profit, potential_profit)\n\n    return max_profit"}, "java": {"tests": "for (int n = 0; n < positiveTestInputs.length; n++) {\n    assertEqual(t.getMaxProfit(positiveTestInputs[n]), positiveTestOutputs[n]);\n}", "code": "public int getMaxProfit(int[] stockPricesYesterday) {\n\n    int maxProfit = 0;\n\n    // go through every price and time\n    for (int earlierTime = 0; earlierTime &lt; stockPricesYesterday.length; earlierTime++) {\n        int earlierPrice = stockPricesYesterday[earlierTime];\n\n        // and go through all the LATER prices\n        for (int laterTime = earlierTime + 1; laterTime &lt; stockPricesYesterday.length; laterTime++) {\n            int laterPrice = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            int potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = Math.max(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}, "ruby": {"tests": "test(positive_tests)", "code": "def get_max_profit(stock_prices_yesterday)\n\n    max_profit = 0\n\n    # go through every price (with it's index as the time)\n    stock_prices_yesterday.each_with_index do |earlier_price, earlier_time|\n\n        # and go through all the LATER prices\n        for later_price in stock_prices_yesterday[earlier_time+1..-1]\n\n            # see what our profit would be if we bought at the\n            # earlier price and sold at the later price\n            potential_profit = later_price - earlier_price\n\n            # update max_profit if we can do better\n            max_profit = [max_profit, potential_profit].max\n        end\n    end\n\n    return max_profit\nend"}, "cpp": {"tests": "for (size_t i = 0; i < positiveTestInputs.size(); ++i) {\n    assertEqual(getMaxProfit(positiveTestInputs[i]), positiveTestOutputs[i]);\n}", "code": "int getMaxProfit(const vector&lt;int>& stockPricesYesterday) {\n\n    int maxProfit = 0;\n\n    // go through every price and time\n    for (size_t earlierTime = 0; earlierTime &lt; stockPricesYesterday.size(); ++earlierTime) {\n        int earlierPrice = stockPricesYesterday[earlierTime];\n\n        // and go through all the LATER prices\n        for (size_t laterTime = earlierTime + 1; laterTime &lt; stockPricesYesterday.size(); ++laterTime) {\n            int laterPrice = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            int potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = max(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}, "javascript": {"tests": "test(positiveTests);", "code": "function getMaxProfit(stockPricesYesterday) {\n\n    var maxProfit = 0;\n\n    // go through every price and time\n    for (var earlierTime = 0; earlierTime &lt; stockPricesYesterday.length; earlierTime++) {\n        var earlierPrice = stockPricesYesterday[earlierTime];\n\n        // and go through all the LATER prices\n        for (var laterTime = earlierTime + 1; laterTime &lt; stockPricesYesterday.length; laterTime++) {\n            var laterPrice = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            var potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = Math.max(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}}, "question__stock-price__solution": {"c": {"tests": "{\n    int i;\n    for (i = 0; i < 3; i++) {\n        testInputAndOutput((const int*) postitiveTestInputs[i], postitiveTestLengths[i],\n                           positiveTestOutputs[i], getMaxProfit);\n    }\n\n    for (i = 0; i < 3; i++) {\n        testInputAndOutput((const int*) negativeTestInputs[i], negativeTestLengths[i],\n                           negativeTestOutputs[i], getMaxProfit);\n    }\n\n    // Test empty input\n    const int array[] = { 1 };\n    ASSERT_RAISES(getMaxProfit(array, 0));\n\n    // Test 1 input\n    ASSERT_RAISES(getMaxProfit(array, 1));\n}", "code": "#define MAX(a, b) (((a) > (b)) ? (a) : (b))\n#define MIN(a, b) (((a) &lt; (b)) ? (a) : (b))\n\nint getMaxProfit(const int *stockPricesYesterday, size_t length) {\n    int minPrice, maxProfit;\n    size_t i;\n\n    // make sure we have at least 2 prices\n    assert(length >= 2);\n\n    // we'll greedily update minPrice and maxProfit, so we initialize\n    // them to the first price and the first possible profit\n    minPrice = stockPricesYesterday[0];\n    maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];\n\n    // start at the second (index 1) time\n    // we can't sell at the first time, since we must buy first,\n    // and we can't buy and sell at the same time!\n    // if we started at index 0, we'd try to buy /and/ sell at time 0.\n    // this would give a profit of 0, which is a problem if our\n    // maxProfit is supposed to be /negative/--we'd return 0!\n    for (i = 1; i &lt; length; i++) {\n        int currentPrice = stockPricesYesterday[i];\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        int potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = MAX(maxProfit, potentialProfit);\n\n        // update minPrice so it's always\n        // the lowest price we've seen so far\n        minPrice = MIN(minPrice, currentPrice);\n    }\n\n    return maxProfit;\n}"}, "python": {"tests": "test(positive_tests)\ntest(negative_tests)\n\ndef pass_one_price():\n    get_max_profit([1])\n\ndef pass_empty_array():\n    get_max_profit([])\n\nassertRaisesError(pass_one_price, 'An array with 1 element', 'requires at least 2 prices')\nassertRaisesError(pass_empty_array, 'An empty array', 'requires at least 2 prices')", "code": "def get_max_profit(stock_prices_yesterday):\n\n    # make sure we have at least 2 prices\n    if len(stock_prices_yesterday) &lt; 2:\n        raise IndexError('Getting a profit requires at least 2 prices')\n\n    # we'll greedily update min_price and max_profit, so we initialize\n    # them to the first price and the first possible profit\n    min_price = stock_prices_yesterday[0]\n    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]\n\n    for index, current_price in enumerate(stock_prices_yesterday):\n\n        # skip the first (0th) time\n        # we can't sell at the first time, since we must buy first,\n        # and we can't buy and sell at the same time!\n        # if we took this out, we'd try to buy /and/ sell at time 0.\n        # this would give a profit of 0, which is a problem if our\n        # max_profit is supposed to be /negative/--we'd return 0!\n        if index == 0:\n            continue\n\n        # see what our profit would be if we bought at the\n        # min price and sold at the current price\n        potential_profit = current_price - min_price\n\n        # update max_profit if we can do better\n        max_profit = max(max_profit, potential_profit)\n\n        # update min_price so it's always\n        # the lowest price we've seen so far\n        min_price  = min(min_price, current_price)\n\n    return max_profit"}, "java": {"tests": "for (int n = 0; n < positiveTestInputs.length; n++) {\n    assertEqual(t.getMaxProfit(positiveTestInputs[n]), positiveTestOutputs[n]);\n}\n\nfor (int n = 0; n < negativeTestInputs.length; n++) {\n    assertEqual(t.getMaxProfit(negativeTestInputs[n]), negativeTestOutputs[n]);\n}\n\nassertRaisesError(t.new PassOnePrice(), \"An array with 1 element\", \"requires at least 2 prices\");\nassertRaisesError(t.new PassOnePrice(), \"An empty array\", \"requires at least 2 prices\");", "setup": "public class PassOnePrice implements VoidFunctionToTest {\n    public void call() {\n        t.getMaxProfit(new int[]{7});\n    }\n}\n\npublic class PassEmptyArray implements VoidFunctionToTest {\n    public void call() {\n        t.getMaxProfit(new int[0]);\n    }\n}", "code": "public int getMaxProfit(int[] stockPricesYesterday) {\n\n    // make sure we have at least 2 prices\n    if (stockPricesYesterday.length &lt; 2) {\n        throw new IllegalArgumentException(\"Getting a profit requires at least 2 prices\");\n    }\n\n    // we'll greedily update minPrice and maxProfit, so we initialize\n    // them to the first price and the first possible profit\n    int minPrice = stockPricesYesterday[0];\n    int maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];\n\n    // start at the second (index 1) time\n    // we can't sell at the first time, since we must buy first,\n    // and we can't buy and sell at the same time!\n    // if we started at index 0, we'd try to buy /and/ sell at time 0.\n    // this would give a profit of 0, which is a problem if our\n    // maxProfit is supposed to be /negative/--we'd return 0!\n    for (int i = 1; i &lt; stockPricesYesterday.length; i++) {\n        int currentPrice = stockPricesYesterday[i];\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        int potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = Math.max(maxProfit, potentialProfit);\n\n        // update minPrice so it's always\n        // the lowest price we've seen so far\n        minPrice = Math.min(minPrice, currentPrice);\n    }\n\n    return maxProfit;\n}"}, "ruby": {"tests": "test(positive_tests)\ntest(negative_tests)\n\ndef pass_one_price\n    get_max_profit([1])\nend\n\ndef pass_empty_array\n    get_max_profit([])\nend\n\nassertRaisesError(method(:pass_one_price), 'An array with 1 element', 'requires at least 2 prices')\nassertRaisesError(method(:pass_empty_array), 'An empty array', 'requires at least 2 prices')", "code": "def get_max_profit(stock_prices_yesterday)\n\n    # make sure we have at least 2 prices\n    if stock_prices_yesterday.length &lt; 2\n        raise IndexError, 'Getting a profit requires at least 2 prices'\n    end\n\n    # we'll greedily update min_price and max_profit, so we initialize\n    # them to the first price and the first possible profit\n    min_price = stock_prices_yesterday[0]\n    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]\n\n    stock_prices_yesterday.each_with_index do |current_price, index|\n\n        # skip the first time, since we already used it\n        # when we initialized min_price and max_profit\n        if index == 0 then next end\n\n        # see what our profit would be if we bought at the\n        # min price and sold at the current price\n        potential_profit = current_price - min_price\n\n        # update max_profit if we can do better\n        max_profit = [max_profit, potential_profit].max\n\n        # update min_price so it's always\n        # the lowest price we've seen so far\n        min_price  = [min_price, current_price].min\n    end\n\n    return max_profit\nend"}, "cpp": {"tests": "for (size_t i = 0; i < positiveTestInputs.size(); ++i) {\n    assertEqual(getMaxProfit(positiveTestInputs[i]), positiveTestOutputs[i]);\n}\n\nfor (size_t i = 0; i < negativeTestInputs.size(); ++i) {\n    assertEqual(getMaxProfit(negativeTestInputs[i]), negativeTestOutputs[i]);\n}\n\n// test on empty vector\n{\n    vector<int> v0;\n    assertRaisesError<invalid_argument>(\"empty input vector\", &getMaxProfit, v0);\n}\n\n// test on array with 1 element\n{\n    vector<int> v1{7};\n    assertRaisesError<invalid_argument>(\"input vector with one element\", &getMaxProfit, v1);\n}", "code": "int getMaxProfit(const vector&lt;int>& stockPricesYesterday) {\n\n    // make sure we have at least 2 prices\n    if (stockPricesYesterday.size() &lt; 2) {\n        throw invalid_argument(\"Getting a profit requires at least 2 prices\");\n    }\n\n    // we'll greedily update minPrice and maxProfit, so we initialize\n    // them to the first price and the first possible profit\n    int minPrice = stockPricesYesterday[0];\n    int maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];\n\n    // start at the second (index 1) time\n    // we can't sell at the first time, since we must buy first,\n    // and we can't buy and sell at the same time!\n    // if we started at index 0, we'd try to buy /and/ sell at time 0.\n    // this would give a profit of 0, which is a problem if our\n    // maxProfit is supposed to be /negative/--we'd return 0!\n    for (size_t i = 1; i &lt; stockPricesYesterday.size(); i++) {\n        int currentPrice = stockPricesYesterday[i];\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        int potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = max(maxProfit, potentialProfit);\n\n        // update minPrice so it's always\n        // the lowest price we've seen so far\n        minPrice = min(minPrice, currentPrice);\n    }\n\n    return maxProfit;\n}"}, "javascript": {"tests": "test(positiveTests);\ntest(negativeTests);\n\nfunction passOnePrice() {\n    getMaxProfit([1]);\n}\n\nfunction passEmptyArray() {\n    getMaxProfit([]);\n}\n\nassertRaisesError(passOnePrice, 'An array with 1 element', 'requires at least 2 prices');\nassertRaisesError(passEmptyArray, 'An empty array', 'requires at least 2 prices');", "code": "function getMaxProfit(stockPricesYesterday) {\n\n    // make sure we have at least 2 prices\n    if (stockPricesYesterday.length &lt; 2) {\n        throw new Error('Getting a profit requires at least 2 prices');\n    }\n\n    // we'll greedily update minPrice and maxProfit, so we initialize\n    // them to the first price and the first possible profit\n    var minPrice = stockPricesYesterday[0];\n    var maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];\n\n    // start at the second (index 1) time\n    // we can't sell at the first time, since we must buy first,\n    // and we can't buy and sell at the same time!\n    // if we started at index 0, we'd try to buy /and/ sell at time 0.\n    // this would give a profit of 0, which is a problem if our\n    // maxProfit is supposed to be /negative/--we'd return 0!\n    for (var i = 1; i &lt; stockPricesYesterday.length; i++) {\n        var currentPrice = stockPricesYesterday[i];\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        var potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = Math.max(maxProfit, potentialProfit);\n\n        // update minPrice so it's always\n        // the lowest price we've seen so far\n        minPrice = Math.min(minPrice, currentPrice);\n    }\n\n    return maxProfit;\n}"}}, "setup": {"c": "const int postitiveTestInputs[3][4] = {\n    {10, 20, 5},\n    {10, 5, 10, 20},\n    {10, 10, 10}\n};\n\nconst size_t postitiveTestLengths[3] = {\n    3,\n    4,\n    3\n};\n\nconst int positiveTestOutputs[3] = {\n    10,\n    15,\n    0\n};\n\nconst int negativeTestInputs[3][3] = {\n    {35, 20, 10},\n    {30, 20, 10},\n    {100, 70, 50}\n};\n\nconst size_t negativeTestLengths[3] = {\n    3,\n    3,\n    3\n};\n\nconst int negativeTestOutputs[3] = {\n    -10,\n    -10,\n    -20\n};\n\nvoid testInputAndOutput(const int *inputs, size_t inputsLength, int output,\n                        int (*func) (const int *inputs, size_t length))\n{\n    int testOutput;\n\n    testOutput = func(inputs, inputsLength);\n    ASSERT(testOutput == output);\n}", "python": "positive_tests = [\n    ([10, 20, 5],     10),  # simple buy and sell\n    ([10, 5, 10, 20], 15),  # wait to buy and sell\n    ([10, 10, 10],    0),   # no change\n]\n\nnegative_tests = [\n    ([35, 20, 10],  -10),   # decrease in value all day\n    ([30, 20, 10],  -10),   # steady decrease\n    ([100, 70, 50], -20),   # decrease, wait to buy\n]\n\ndef test(tests):\n    for input, output in tests:\n        assertEqual(get_max_profit(input), output)", "java": "int[][] positiveTestInputs = new int[][]{\n    {10, 20, 5},\n    {10, 5, 10, 20},\n    {10, 10, 10},\n};\n\nint[] positiveTestOutputs = new int[]{\n    10,\n    15,\n    0,\n};\n\nint[][] negativeTestInputs = new int[][]{\n    {35, 20, 10},\n    {30, 20, 10},\n    {100, 70, 50},\n};\n\nint[] negativeTestOutputs = new int[]{\n    -10,\n    -10,\n    -20,\n};", "ruby": "positive_tests = [\n    [[10, 20, 5],     10],\n    [[10, 5, 10, 20], 15],\n    [[10, 10, 10],    0],\n]\n\nnegative_tests = [\n    [[35, 20, 10],  -10],\n    [[30, 20, 10],  -10],\n    [[100, 70, 50], -20],\n]\n\ndef test(tests)\n    tests.each do |input, output|\n        assertEqual(get_max_profit(input), output)\n    end\nend", "cpp": "const vector<vector<int>> positiveTestInputs {\n    vector<int>{10, 20, 5},\n    vector<int>{10, 5, 10, 20},\n    vector<int>{10, 10, 10},\n};\n\nconst vector<int> positiveTestOutputs {\n    10,\n    15,\n    0\n};\n\nconst vector<vector<int>> negativeTestInputs {\n    vector<int>{35, 20, 10},\n    vector<int>{30, 20, 10},\n    vector<int>{100, 70, 50},\n};\n\nconst vector<int> negativeTestOutputs {\n    -10,\n    -10,\n    -20\n};", "javascript": "var positiveTests = [\n    [[10, 20, 5],     10],\n    [[10, 5, 10, 20], 15],\n    [[10, 10, 10],    0],\n];\n\nvar negativeTests = [\n    [[35, 20, 10],  -10],\n    [[30, 20, 10],  -10],\n    [[100, 70, 50], -20],\n];\n\nfunction test(tests) {\n    tests.forEach(function(inputAndOutput) {\n        assertEqual(getMaxProfit(inputAndOutput[0]), inputAndOutput[1]);\n    });\n}"}, "question__stock-price__solution-before-edge-cases": {"c": {"tests": "{\n    int i;\n    for (i = 0; i < 3; i++) {\n        testInputAndOutput((const int*) postitiveTestInputs[i], postitiveTestLengths[i],\n                           positiveTestOutputs[i], getMaxProfit);\n    }\n}", "code": "#define MAX(a, b) (((a) > (b)) ? (a) : (b))\n#define MIN(a, b) (((a) &lt; (b)) ? (a) : (b))\n\nint getMaxProfit(const int *stockPricesYesterday, size_t length) {\n    size_t i;\n    int maxProfit = 0;\n    int minPrice = stockPricesYesterday[0];\n\n    for (i = 0; i &lt; length; i++) {\n        int currentPrice = stockPricesYesterday[i];\n\n        // ensure min_price is the lowest price we've seen so far\n        minPrice = MIN(minPrice, currentPrice);\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        int potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = MAX(maxProfit, potentialProfit);\n    }\n\n    return maxProfit;\n}"}, "python": {"tests": "test(positive_tests)", "code": "def get_max_profit(stock_prices_yesterday):\n\n    min_price = stock_prices_yesterday[0]\n    max_profit = 0\n\n    for current_price in stock_prices_yesterday:\n\n        # ensure min_price is the lowest price we've seen so far\n        min_price = min(min_price, current_price)\n\n        # see what our profit would be if we bought at the\n        # min price and sold at the current price\n        potential_profit = current_price - min_price\n\n        # update max_profit if we can do better\n        max_profit = max(max_profit, potential_profit)\n\n    return max_profit"}, "java": {"tests": "for (int n = 0; n < positiveTestInputs.length; n++) {\n    assertEqual(t.getMaxProfit(positiveTestInputs[n]), positiveTestOutputs[n]);\n}", "code": "public int getMaxProfit(int[] stockPricesYesterday) {\n\n    int minPrice = stockPricesYesterday[0];\n    int maxProfit = 0;\n\n    for (int currentPrice : stockPricesYesterday) {\n\n        // ensure min_price is the lowest price we've seen so far\n        minPrice = Math.min(minPrice, currentPrice);\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        int potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = Math.max(maxProfit, potentialProfit);\n    }\n\n    return maxProfit;\n}"}, "ruby": {"tests": "test(positive_tests)", "code": "def get_max_profit(stock_prices_yesterday)\n\n    min_price = stock_prices_yesterday[0]\n    max_profit = 0\n\n    stock_prices_yesterday.each do |current_price|\n\n        # ensure min_price is the lowest price we've seen so far\n        min_price = [min_price, current_price].min\n\n        # see what our profit would be if we bought at the\n        # min price and sold at the current price\n        potential_profit = current_price - min_price\n\n        # update max_profit if we can do better\n        max_profit = [max_profit, potential_profit].max\n    end\n\n    return max_profit\nend"}, "cpp": {"tests": "for (size_t i = 0; i < positiveTestInputs.size(); ++i) {\n    assertEqual(getMaxProfit(positiveTestInputs[i]), positiveTestOutputs[i]);\n}", "code": "int getMaxProfit(const vector&lt;int>& stockPricesYesterday) {\n\n    int minPrice = stockPricesYesterday[0];\n    int maxProfit = 0;\n\n    for (size_t i = 0; i &lt; stockPricesYesterday.size(); ++i) {\n\n        int currentPrice = stockPricesYesterday[i];\n\n        // ensure min_price is the lowest price we've seen so far\n        minPrice = min(minPrice, currentPrice);\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        int potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = max(maxProfit, potentialProfit);\n    }\n\n    return maxProfit;\n}"}, "javascript": {"tests": "test(positiveTests);", "code": "function getMaxProfit(stockPricesYesterday) {\n\n    var minPrice = stockPricesYesterday[0];\n    var maxProfit = 0;\n\n    for (var i = 0; i &lt; stockPricesYesterday.length; i++) {\n        var currentPrice = stockPricesYesterday[i];\n\n        // ensure min_price is the lowest price we've seen so far\n        minPrice = Math.min(minPrice, currentPrice);\n\n        // see what our profit would be if we bought at the\n        // min price and sold at the current price\n        var potentialProfit = currentPrice - minPrice;\n\n        // update maxProfit if we can do better\n        maxProfit = Math.max(maxProfit, potentialProfit);\n    }\n\n    return maxProfit;\n}"}}, "question__stock-price__error-requires-two-prices": {"c": "assert(length >= 2);\n\nint minPrice = stockPricesYesterday[0];\nint maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];", "python": "if len(stock_prices_yesterday) &lt; 2:\n    raise IndexError('Getting a profit requires at least 2 prices')\n\nmin_price = stock_prices_yesterday[0]\nmax_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]\n\n# etc...", "java": "if (stockPricesYesterday.length &lt; 2) {\n    throw new IllegalArgumentException(\"Getting a profit requires at least 2 prices\");\n}\n\nint minPrice = stockPricesYesterday[0];\nint maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];", "ruby": "if stock_prices_yesterday.length &lt; 2\n    raise IndexError, 'Getting a profit requires at least 2 prices'\nend\n\nmin_price = stock_prices_yesterday[0]\nmax_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]\n\n# etc...", "cpp": "if (stockPricesYesterday.size() &lt; 2) {\n    throw invalid_argument(\"Getting a profit requires at least 2 prices\");\n}\n\nint minPrice = stockPricesYesterday[0];\nint maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];", "javascript": "if (stockPricesYesterday.length &lt; 2) {\n    throw new Error('Getting a profit requires at least 2 prices');\n}\n\nvar minPrice = stockPricesYesterday[0];\nvar maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];"}, "question__stock-price__brute-force": {"c": {"tests": "{\n    int i;\n    for (i = 0; i < 3; i++) {\n        testInputAndOutput((const int*) postitiveTestInputs[i], postitiveTestLengths[i],\n                           positiveTestOutputs[i], getMaxProfit);\n    }\n}", "code": "#define MAX(a, b) (((a) > (b)) ? (a) : (b))\n#define MIN(a, b) (((a) &lt; (b)) ? (a) : (b))\n\nint getMaxProfit(const int *stockPricesYesterday, size_t length) {\n    size_t outerTime;\n    int maxProfit = 0;\n\n    // go through every time\n    for (outerTime = 0; outerTime &lt; length; outerTime++) {\n        size_t innerTime;\n\n        // for every time, got through every OTHER time\n        for (innerTime = 0; innerTime &lt; length; innerTime++) {\n\n            // for each pair, find the earlier and later times\n            int earlierTime = MIN(outerTime, innerTime);\n            int laterTime   = MAX(outerTime, innerTime);\n\n            // and use those to find the earlier and later prices\n            int earlierPrice = stockPricesYesterday[earlierTime];\n            int laterPrice   = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            int potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = MAX(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}, "python": {"tests": "test(positive_tests)", "code": "def get_max_profit(stock_prices_yesterday):\n\n    max_profit = 0\n\n    # go through every time\n    for outer_time in xrange(len(stock_prices_yesterday)):\n\n        # for every time, go through every OTHER time\n        for inner_time in xrange(len(stock_prices_yesterday)):\n\n            # for each pair, find the earlier and later times\n            earlier_time = min(outer_time, inner_time)\n            later_time   = max(outer_time, inner_time)\n\n            # and use those to find the earlier and later prices\n            earlier_price = stock_prices_yesterday[earlier_time]\n            later_price   = stock_prices_yesterday[later_time]\n\n            # see what our profit would be if we bought at the\n            # earlier price and sold at the later price\n            potential_profit = later_price - earlier_price\n\n            # update max_profit if we can do better\n            max_profit = max(max_profit, potential_profit)\n\n    return max_profit"}, "java": {"tests": "for (int n = 0; n < positiveTestInputs.length; n++) {\n    assertEqual(t.getMaxProfit(positiveTestInputs[n]), positiveTestOutputs[n]);\n}", "code": "public int getMaxProfit(int[] stockPricesYesterday) {\n\n    int maxProfit = 0;\n\n    // go through every time\n    for (int outerTime = 0; outerTime &lt; stockPricesYesterday.length; outerTime++) {\n\n        // for every time, got through every OTHER time\n        for (int innerTime = 0; innerTime &lt; stockPricesYesterday.length; innerTime++) {\n\n            // for each pair, find the earlier and later times\n            int earlierTime = Math.min(outerTime, innerTime);\n            int laterTime   = Math.max(outerTime, innerTime);\n\n            // and use those to find the earlier and later prices\n            int earlierPrice = stockPricesYesterday[earlierTime];\n            int laterPrice   = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            int potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = Math.max(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}, "ruby": {"tests": "test(positive_tests)", "code": "def get_max_profit(stock_prices_yesterday)\n\n    max_profit = 0\n\n    # go through every time\n    for outer_time in (0...stock_prices_yesterday.length)\n\n        # for every time, go through every OTHER time\n        for inner_time in (0...stock_prices_yesterday.length)\n\n            # for each pair, find the earlier and later times\n            earlier_time = [outer_time, inner_time].min\n            later_time   = [outer_time, inner_time].max\n\n            # and use those to find the earlier and later prices\n            earlier_price = stock_prices_yesterday[earlier_time]\n            later_price   = stock_prices_yesterday[later_time]\n\n            # see what our profit would be if we bought at the\n            # earlier price and sold at the later price\n            potential_profit = later_price - earlier_price\n\n            # update max_profit if we can do better\n            max_profit = [max_profit, potential_profit].max\n        end\n    end\n\n    return max_profit\nend"}, "cpp": {"tests": "for (size_t i = 0; i < positiveTestInputs.size(); ++i) {\n    assertEqual(getMaxProfit(positiveTestInputs[i]), positiveTestOutputs[i]);\n}", "code": "int getMaxProfit(const vector&lt;int>& stockPricesYesterday) {\n\n    int maxProfit = 0;\n\n    // go through every time\n    for (size_t outerTime = 0; outerTime &lt; stockPricesYesterday.size(); ++outerTime) {\n\n        // for every time, go through every OTHER time\n        for (size_t innerTime = 0; innerTime &lt; stockPricesYesterday.size(); ++innerTime) {\n\n            // for each pair, find the earlier and later times\n            size_t earlierTime = min(outerTime, innerTime);\n            size_t laterTime   = max(outerTime, innerTime);\n\n            // and use those to find the earlier and later prices\n            int earlierPrice = stockPricesYesterday[earlierTime];\n            int laterPrice   = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            int potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = max(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}, "javascript": {"tests": "test(positiveTests);", "code": "function getMaxProfit(stockPricesYesterday) {\n\n    var maxProfit = 0;\n\n    // go through every time\n    for (var outerTime = 0; outerTime &lt; stockPricesYesterday.length; outerTime++) {\n\n        // for every time, got through every OTHER time\n        for (var innerTime = 0; innerTime &lt; stockPricesYesterday.length; innerTime++) {\n\n            // for each pair, find the earlier and later times\n            var earlierTime = Math.min(outerTime, innerTime);\n            var laterTime   = Math.max(outerTime, innerTime);\n\n            // and use those to find the earlier and later prices\n            var earlierPrice = stockPricesYesterday[earlierTime];\n            var laterPrice   = stockPricesYesterday[laterTime];\n\n            // see what our profit would be if we bought at the\n            // min price and sold at the current price\n            var potentialProfit = laterPrice - earlierPrice;\n\n            // update maxProfit if we can do better\n            maxProfit = Math.max(maxProfit, potentialProfit);\n        }\n    }\n\n    return maxProfit;\n}"}}, "question__stock-price__input-output-example": {"cpp": "vector&lt;int> stockPricesYesterday{10, 7, 5, 8, 11, 9};\n\ngetMaxProfit(stockPricesYesterday);\n// returns 6 (buying for $5 and selling for $11)", "c": "int stockPricesYesterday[6] = {10, 7, 5, 8, 11, 9};\nsize_t numStockPrices = 6;\n\ngetMaxProfit(stockPricesYesterday, numStockPrices);\n// returns 6 (buying for $5 and selling for $11)", "javascript": "var stockPricesYesterday = [10, 7, 5, 8, 11, 9];\n\ngetMaxProfit(stockPricesYesterday);\n// returns 6 (buying for $5 and selling for $11)", "java": "int[] stockPricesYesterday = new int[]{10, 7, 5, 8, 11, 9};\n\ngetMaxProfit(stockPricesYesterday);\n// returns 6 (buying for $5 and selling for $11)", "snake": "stock_prices_yesterday = [10, 7, 5, 8, 11, 9]\n\nget_max_profit(stock_prices_yesterday)\n# returns 6 (buying for $5 and selling for $11)"}, "question__stock-price__first-min-price-and-max-profit": {"camel": "minPrice = stockPricesYesterday[0];\nmaxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];", "snake": "min_price = stock_prices_yesterday[0]\nmax_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]"}}};
            var codeTypes = ['words', 'code-blocks', 'vars', 'funcs', 'code-inlines'];

            var mergeObjects = function(objectA, objectB) {
                objectA = objectA || {};
                objectB = objectB || {};
                for (var key in objectB) {
                    objectA[key] = objectB[key];
                }
                return objectA;
            }

            if (!window.contentTranslations) {
                window.contentTranslations = elTranslations;
            } else {
                for (var i=0; i<codeTypes.length; i++) {
                    window.contentTranslations[codeTypes[i]] = mergeObjects(window.contentTranslations[codeTypes[i]], elTranslations[codeTypes[i]]);
                }
            }
            </script>
</div>


    </div>

    <div class="btn-sets">

        <p class="prompt ng-binding" ng-bind="getPromptStr()" ng-hide="'full' !== 'full' &amp;&amp; endedQuestion">Did you get it right?</p>

        <div class="btn-set btn-set-during ng-hide" ng-show="isSingleTrack &amp;&amp; getBtnSet()=='during'">
                <a ng-click="showPress()" id="btn-show" class="btn btn-default btn-large" style=""><span class="glyphicon glyphicon-chevron-down"></span><span class="text ng-binding" ng-bind="getShowBtnText()">Show answer</span></a>
        </div>

        <div class="btn-set btn-set-during ng-hide" ng-show="!isSingleTrack &amp;&amp; getBtnSet()=='during'" style="">
                <a ng-click="haveAnswerPress()" id="btn-got-it" class="btn btn-default btn-large" style=""><span class="glyphicon glyphicon-ok"></span><span class="text ng-binding" ng-bind="getHaveAnswerBtnText()">Yes, check answer!</span></a>
                <a ng-click="dontHaveAnswerPress()" id="btn-hint" class="btn btn-default btn-large" style=""><span class="fa fa-question"></span><span class="text ng-binding" ng-bind="getDontHaveAnswerBtnText()">I give up!</span></a>
        </div>

        
            <div class="btn-set btn-set-after-option" ng-show="getBtnSet()=='after-option'" style="">
                    <a ng-click="feelExpertPress()" id="btn-feel-good" class="btn btn-default btn-large" style=""><span class="glyphicon glyphicon-ok"></span><span class="text">Yes, I'm expert on this</span></a>
                    <a ng-click="dontFeelExpertPress()" id="btn-need-review" class="btn btn-default btn-large" style=""><span class="glyphicon glyphicon-repeat"></span><span class="text">Not quite, review later</span></a>
            </div>
            <div class="btn-set btn-set-after-must-review ng-hide" ng-show="getBtnSet()=='after-must-review'">
                    <a ng-click="nextQuestionPress()" id="btn-next" class="btn btn-default btn-large" style=""><span class="glyphicon glyphicon-chevron-right"></span><span class="text">Next question</span></a>
            </div>
        

        <div class="share-btns share-btns-quiz-end" ng-show="getBtnSet()=='after-option'" style="">
            <p>
                Like this problem? Pass it on!
            </p>

            

<a class="custom-share facebook-share ng-isolate-scope" href="https://www.facebook.com/sharer/sharer.php?u=https%3A//www.interviewcake.com/question/python/stock-price" target="_blank" tracklink="" the-event="FB share click" the-properties="{&quot;which&quot; : &quot;post-question option&quot;}"><i class="fa fa-facebook"> </i> Share</a>
<a class="custom-share twitter-share ng-isolate-scope" href="https://twitter.com/intent/tweet?text=Solved%20this%20coding%20interview%20question%21&amp;via=interviewcake&amp;related=interviewcake&amp;url=https%3A//www.interviewcake.com/question/python/stock-price" target="_blank" tracklink="" the-event="Twitter share click" the-properties="{&quot;which&quot; : &quot;post-question option&quot;}"><i class="fa fa-twitter"> </i> Tweet</a>
<a class="custom-share linkedin-share ng-isolate-scope" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A//www.interviewcake.com/question/python/stock-price&amp;title=&amp;summary=Solved%20this%20coding%20interview%20question%21&amp;source=Interview%20Cake" target="_blank" tracklink="" the-event="LinkedIn share click" the-properties="{&quot;which&quot; : &quot;post-question option&quot;}"><i class="fa fa-linkedin"> </i> Share</a>


        </div>
        <div class="share-btns share-btns-quiz-end ng-hide" ng-show="getBtnSet()=='after-must-review'">
            <p>
                Like this problem? Pass it on!
            </p>

            

<a class="custom-share facebook-share ng-isolate-scope" href="https://www.facebook.com/sharer/sharer.php?u=https%3A//www.interviewcake.com/question/python/stock-price" target="_blank" tracklink="" the-event="FB share click" the-properties="{&quot;which&quot; : &quot;post-question must review&quot;}"><i class="fa fa-facebook"> </i> Share</a>
<a class="custom-share twitter-share ng-isolate-scope" href="https://twitter.com/intent/tweet?text=Tough%20coding%20interview%20question%21&amp;via=interviewcake&amp;related=interviewcake&amp;url=https%3A//www.interviewcake.com/question/python/stock-price" target="_blank" tracklink="" the-event="Twitter share click" the-properties="{&quot;which&quot; : &quot;post-question must review&quot;}"><i class="fa fa-twitter"> </i> Tweet</a>
<a class="custom-share linkedin-share ng-isolate-scope" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A//www.interviewcake.com/question/python/stock-price&amp;title=&amp;summary=Tough%20coding%20interview%20question%21&amp;source=Interview%20Cake" target="_blank" tracklink="" the-event="LinkedIn share click" the-properties="{&quot;which&quot; : &quot;post-question must review&quot;}"><i class="fa fa-linkedin"> </i> Share</a>

        </div>

    </div>

    
        <div ng-controller="NotepadCtrl" class="notepad-outer-wrapper ng-scope tab-mode" ng-class="notepadMode" style="bottom: 0px;">
    <div class="notepad-inner-wrapper tab-mode" ng-class="notepadMode">
        <div class="notepad-buttons tab-mode" ng-class="notepadMode">
            <div class="select-language ng-hide" ng-mousedown="isNotepadRelatedElementClicked=true" ng-mouseup="isNotepadRelatedElementClicked=false" ng-show="notepadMode!=='tab-mode'">
                <select ng-model="selectedLanguage" ng-options="language.display_name for language in codemirrorLanguages | orderBy: 'dropdown_rank'" ng-change="selectFromLanguageDropdown()" class="ng-pristine ng-untouched ng-valid"><option value="0" selected="selected" label="Python">Python</option><option value="1" label="Java">Java</option><option value="2" label="Ruby">Ruby</option><option value="3" label="JavaScript">JavaScript</option><option value="4" label="C (beta)">C (beta)</option><option value="5" label="C++ (beta)">C++ (beta)</option><option value="6" label="C#">C#</option><option value="7" label="Objective C">Objective C</option><option value="8" label="PHP">PHP</option><option value="9" label="Haskell">Haskell</option><option value="10" label="No syntax">No syntax</option></select>
            </div>
            <span class="tab ng-hide" ng-mousedown="isNotepadRelatedElementClicked=true" ng-click="clickIcon('tab-mode')" ng-mouseup="isNotepadRelatedElementClicked=false" ng-show="notepadMode!=='tab-mode'"></span>
            <span class="type-and-look" ng-mousedown="isNotepadRelatedElementClicked=true" ng-click="clickIcon('type-and-look-mode')" ng-mouseup="isNotepadRelatedElementClicked=false"></span>
            <span class="focus" ng-mousedown="isNotepadRelatedElementClicked=true" ng-click="clickIcon('focus-mode')" ng-mouseup="isNotepadRelatedElementClicked=false"></span>
        </div>
        <div class="notepad-typing tab-mode" ng-class="{'output-displayed': outputDisplayed &amp;&amp; selectedLanguage.codewars}">
            <div class="ng-pristine ng-untouched ng-valid cm-s-default CodeMirror" ui-codemirror-opts="editorOptions" ui-refresh="isCodemirrorUpdated" ng-model="userCode"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 26px; left: 22px;"><textarea style="position: absolute; padding: 0px; width: 1px; height: 1em; outline: medium none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" wrap="off"></textarea></div><div class="CodeMirror-vscrollbar" not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" not-content="true"></div><div class="CodeMirror-gutter-filler" not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="true"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: -15px; border-right-width: 15px; min-width: 87px; min-height: 29px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: medium none;"><div class="CodeMirror-measure"><span><span>​</span>x</span></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 0px; top: 0px; height: 17.85px;">&nbsp;</div></div><div class="CodeMirror-code"><pre><span><span class="cm-variable">Type</span> <span class="cm-variable">code</span><span class="cm-operator">!</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 15px; width: 1px; top: 29px;"></div><div class="CodeMirror-gutters" style="display: none; height: 62px;"></div></div></div>
        </div>

        

        <div class="notepad-run tab-mode" ng-class="notepadMode" ng-show="selectedLanguage.codewars">
            <span class="output-button ng-binding ng-hide" ng-mousedown="isNotepadRelatedElementClicked=true" ng-click="outputDisplayed = !outputDisplayed; codemirrorElement.focus()" ng-mouseup="isNotepadRelatedElementClicked=false" ng-show="outputDisplayed || output !== undefined" ng-bind="outputDisplayed ? 'HIDE' : 'SHOW'">SHOW</span>
            <span class="output-button" ng-mousedown="isNotepadRelatedElementClicked=true" ng-click="runCode()" ng-mouseup="isNotepadRelatedElementClicked=false">RUN</span>
        </div>
        <div class="notepad-output tab-mode" ng-class="notepadMode" ng-show="selectedLanguage.codewars" ng-mousedown="isNotepadRelatedElementClicked=true" ng-mouseup="isNotepadRelatedElementClicked=false">
            <span class="powered-by">
                Code execution powered by Qualified.io
            </span>
            <p class="content output-help ng-binding ng-hide" ng-show="outputHelp" ng-bind="outputHelp"></p>
            <p class="content output ng-binding ng-hide" ng-show="output" ng-bind="output"></p>
            <p class="content output-error ng-binding" ng-bind="outputError"></p>
        </div>

        
    </div>
</div>

    

</div>
</div>



    <div ng-view=""></div>
</div>


    
    
    

    <div id="footer">

        <a class="newsletter-link" href="https://www.interviewcake.com/free-weekly-coding-interview-problem-newsletter">Subscribe to our weekly question email list »</a>

        <div class="links">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-6">
                        <div class="by-company">
                            <h5>
                                Programming interview questions by company:
                            </h5>
                            <ul>
                                <li>
                                    <a href="https://www.interviewcake.com/google-interview-questions">Google interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/facebook-interview-questions">Facebook interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/amazon-interview-questions">Amazon interview questions</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="by-language">
                            <h5>
                                Programming interview questions by language:
                            </h5>
                            <ul>
                                <li>
                                    <a href="https://www.interviewcake.com/java-interview-questions">Java interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/python-interview-questions">Python interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/ruby-interview-questions">Ruby interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/javascript-interview-questions">JavaScript interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/sql-interview-questions">SQL interview questions</a>
                                </li>
                                <li>
                                    <a href="https://www.interviewcake.com/testing-and-qa-interview-questions">Testing and QA interview questions</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="social-media">

            <a class="facebook ng-isolate-scope" href="https://www.facebook.com/interviewcake" target="_blank" tracklink="" the-event="FB footer click"><i class="fa fa-facebook"></i></a>
            <a class="twitter ng-isolate-scope" href="https://www.twitter.com/interviewcake" target="_blank" tracklink="" the-event="Twitter footer click"><i class="fa fa-twitter"></i></a>
        </div>

        

            <div itemscope="" itemtype="http://schema.org/Corporation">
                <span class="schemaorghide" itemprop="description">Programming interview practice and tips for software engineers looking for jobs.</span>

                Copyright © 2016
                <span itemprop="name">Cake Labs, Inc.</span> All rights reserved.
                <span class="schemaorghide" itemprop="image">https://www.interviewcake.com/static//images/cake_white_on_blue_600.png</span>
                <span class="schemaorghide" itemprop="logo">https://www.interviewcake.com/static//images/cake_white_on_blue_600.png</span>
                <span class="schemaorghide" itemprop="url">https://www.interviewcake.com</span>
                <span class="schemaorghide" itemprop="telephone">(804) 876-2253</span>

                <address itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
                    <span itemprop="streetAddress">228 Park Ave S #82632</span>,
                    <span itemprop="addressLocality">New York</span>,
                    <span itemprop="addressRegion">NY</span>
                    <span itemprop="addressCountry">US</span>
                    <span itemprop="postalCode">10003</span>
                    <span itemprop="telephone">(804) 876-2253</span>
                </address>

                <address class="schemaorghide" itemprop="location" itemscope="" itemtype="http://schema.org/PostalAddress">
                    <span itemprop="addressCountry">US</span>
                    <span itemprop="addressLocality">New York</span>
                    <span itemprop="addressRegion">NY</span>
                    <span itemprop="streetAddress">228 Park Ave S #82632</span>
                    <span itemprop="postalCode">10003</span>
                    <span itemprop="telephone">(804) 876-2253</span>
                </address>

                <div itemprop="location" itemscope="" itemtype="http://schema.org/Place">
                    <div itemprop="geo" itemscope="" itemtype="http://schema.org/GeoCoordinates">
                        <meta itemprop="latitude" content="37.76480">
                        <meta itemprop="longitude" content="-122.41872">
                    </div>
                </div>
            </div>
        
        <div>

            
            
            <a rel="nofollow" href="https://www.interviewcake.com/privacy-policy">Privacy</a>
            |
            <a rel="nofollow" href="https://www.interviewcake.com/terms-and-conditions">Terms</a>
        </div>
    </div>
</div> <!-- /"below-nav" -->

    
    <script src="stocks_files/jquery_002.js"></script>
    <script src="stocks_files/bootstrap.js"></script>
    <script src="stocks_files/angular.js"></script>
    <script src="stocks_files/angular-route.js"></script>
    <script src="stocks_files/angular-cookies.js"></script>
    <script src="stocks_files/angular-animate.js"></script>
    <script src="stocks_files/katex.js"></script>

    

    
    <script src="stocks_files/underscore-min.js"></script>
    <script src="stocks_files/angular-django-rest-resource.js"></script>
    <script src="stocks_files/angular-seo.js"></script>
    <script src="stocks_files/sticky.js"></script>
    

    <script type="text/javascript">
        (function(){
  var FLAGS = {
    'learnings': true,'only_3_free_questions': true,'new_header': false
    },
    SWITCHES = {
    
    },
    SAMPLES = {
    
    };
  window.waffle = {
    "flag_is_active": function waffle_flag(flag_name) {
      
      return !!FLAGS[flag_name];
    },
    "switch_is_active": function waffle_switch(switch_name) {
      
      return !!SWITCHES[switch_name];
    },
    "sample_is_active": function waffle_sample(sample_name) {
      
      return !!SAMPLES[sample_name];
    },
    "FLAGS": FLAGS,
    "SWITCHES": SWITCHES,
    "SAMPLES": SAMPLES
  };
})();

    </script>

    <script src="stocks_files/base.js"></script>

    
    <script src="stocks_files/prism.js"></script>
    <script src="stocks_files/codemirror.js"></script>
    <script src="stocks_files/python.js"></script>
    <script src="stocks_files/ruby.js"></script>
    <script src="stocks_files/javascript.js"></script>
    <script src="stocks_files/clike.js"></script>
    <script src="stocks_files/php.js"></script>
    <script src="stocks_files/haskell.js"></script>
    <script src="stocks_files/ui-codemirror.js"></script>
    <script src="stocks_files/jquery.js"></script>
    <script src="stocks_files/edgeUtils.js"></script>
    


    <script type="text/javascript">
        window.CACHEBUST_QUERY_STR = '?bust=132';
        //TODO: move above into the below
        window.JS_CONSTANTS = {"CODEMIRROR_LANGUAGES": [{"notepad_template": "using System;\n\nclass Solution{\n    public static string MyFunction(string arg){\n        // write the body of your function here\n        return \"running with \" + arg;\n    }\n\n    static void Main(string[] args){\n        // run your function through some test cases here\n        // remember: debugging is half the battle!\n        Console.WriteLine(MyFunction(\"test input\"));\n    }\n}", "codewars": "csharp", "display_name": "C#", "short_name": "csharp", "dropdown_rank": 7, "codemirror": "text/x-csharp"}, {"notepad_template": "#import <Foundation/Foundation.h>\n#import <stdio.h>\n\n@interface Solution : NSObject\n\n+ (NSString *)myFunction:(NSString *)arg;\n\n@end\n\n@implementation Solution\n\n+ (NSString *)myFunction:(NSString *)arg\n{\n  // write the body of your function here\n  return [@\"running with \" stringByAppendingString:arg];\n}\n\n@end\n\nint main (int argc, const char * argv[])\n{\n  @autoreleasepool {\n    // run your function through some test cases here\n    // remember: debugging is half the battle!\n    NSString * result = [Solution myFunction:@\"test input\"];\n    printf(\"%s\", [result UTF8String]);\n  }\n}", "display_name": "Objective C", "dropdown_rank": 8, "codemirror": "text/x-objectivec", "short_name": "objectivec"}, {"notepad_template": "<?php\n\nfunction myFunction($arg) {\n    // write the body of your function here\n    return \"running with \" . $arg;\n}\n\n// run your function through some test cases here\n// remember: debugging is half the battle!\necho myFunction(\"test input\");\n\n?>", "prism": "php", "display_name": "PHP", "short_name": "php", "dropdown_rank": 9, "codemirror": "text/x-php"}, {"notepad_template": "myFunction :: String -> String\n-- write the body of your function here\nmyFunction arg = \"running with \" ++ arg\n\nmain = do\n  -- run your function through some test cases here\n  -- remember: debugging is half the battle!\n  let result = myFunction \"test input\"\n  putStrLn result\n", "codewars": "haskell", "display_name": "Haskell", "short_name": "haskell", "dropdown_rank": 10, "codemirror": "text/x-haskell"}, {"display_name": "No syntax", "codemirror": "", "prism": "none", "dropdown_rank": 11, "short_name": "nolanguage"}, {"notepad_template": "def my_function(arg):\n    # write the body of your function here\n    return 'running with %s' % arg\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nprint my_function('test input')\n", "codewars": "python", "codemirror": "text/x-python", "display_name": "Python", "short_name": "python", "case_convention": "snake", "prism": "python", "dropdown_rank": 1}, {"notepad_template": "def my_function(arg)\n    # write the body of your function here\n    return \"running with #{arg}\"\nend\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nputs my_function('test input')\n", "codewars": "ruby", "codemirror": "text/x-ruby", "display_name": "Ruby", "short_name": "ruby", "case_convention": "snake", "prism": "ruby", "dropdown_rank": 3}, {"notepad_template": "public class Solution {\n    public static String myFunction(String arg) {\n        // write the body of your function here\n        return \"running with \" + arg;\n    }\n    public static void main(String[] args) {\n        // run your function through some test cases here\n        // remember: debugging is half the battle!\n        String testInput = \"test input\";\n        System.out.println(myFunction(testInput));\n    }\n}", "codewars": "java", "codemirror": "text/x-java", "display_name": "Java", "short_name": "java", "case_convention": "camel", "prism": "java", "dropdown_rank": 2}, {"notepad_template": "function myFunction(arg) {\n    // write the body of your function here\n    return 'running with ' + arg;\n}\n\n// run your function through some test cases here\n// remember: debugging is half the battle!\nconsole.log(myFunction('test input'));\n", "codewars": "javascript", "codemirror": "text/javascript", "display_name": "JavaScript", "short_name": "javascript", "case_convention": "camel", "prism": "javascript", "dropdown_rank": 4}, {"notepad_template": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nconst char * my_function(char * arg){\n    // write the body of your function here\n    return arg;\n}\n\nint main(){\n    // run your function through some test cases here\n    // remember: debugging is half the battle!\n    printf(\"%s\", my_function(\"test input\"));\n    return 0;\n}", "prism": "c", "codewars": "c", "closest_languages": ["cpp", "java"], "display_name": "C (beta)", "short_name": "c", "case_convention": "camel", "codemirror": "text/x-csrc", "dropdown_rank": 5}, {"notepad_template": "#include <iostream>\nusing namespace std;\n\nstring myFunction (const string& arg) {\n    // write the body of your function here\n    return \"running with \" + arg;\n}\n\nint main () {\n    // run your function through some test cases here\n    // remember: debugging is half the battle!\n    cout << myFunction (\"test input\");\n    return 0;\n}", "prism": "cpp", "codewars": "cpp", "closest_languages": ["c", "java"], "display_name": "C++ (beta)", "short_name": "cpp", "case_convention": "camel", "codemirror": "text/x-c++src", "dropdown_rank": 6}], "next_step_type_enum": {"login": "_NEXT_STEP_TYPE_LOGIN_", "purchase": "_NEXT_STEP_TYPE_PURCHASE_", "question": "_NEXT_STEP_TYPE_QUESTION_", "done": "_NEXT_STEP_TYPE_DONE_"}, "CACHEBUST_QUERY_STR": "?bust=132", "PRISM_LANGUAGES": [{"notepad_template": "<?php\n\nfunction myFunction($arg) {\n    // write the body of your function here\n    return \"running with \" . $arg;\n}\n\n// run your function through some test cases here\n// remember: debugging is half the battle!\necho myFunction(\"test input\");\n\n?>", "prism": "php", "display_name": "PHP", "short_name": "php", "dropdown_rank": 9, "codemirror": "text/x-php"}, {"display_name": "No syntax", "codemirror": "", "prism": "none", "dropdown_rank": 11, "short_name": "nolanguage"}, {"display_name": "HTML", "prism": "markup", "short_name": "html"}, {"display_name": "SQL", "prism": "sql", "short_name": "sql"}, {"notepad_template": "def my_function(arg):\n    # write the body of your function here\n    return 'running with %s' % arg\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nprint my_function('test input')\n", "codewars": "python", "codemirror": "text/x-python", "display_name": "Python", "short_name": "python", "case_convention": "snake", "prism": "python", "dropdown_rank": 1}, {"notepad_template": "def my_function(arg)\n    # write the body of your function here\n    return \"running with #{arg}\"\nend\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nputs my_function('test input')\n", "codewars": "ruby", "codemirror": "text/x-ruby", "display_name": "Ruby", "short_name": "ruby", "case_convention": "snake", "prism": "ruby", "dropdown_rank": 3}, {"notepad_template": "public class Solution {\n    public static String myFunction(String arg) {\n        // write the body of your function here\n        return \"running with \" + arg;\n    }\n    public static void main(String[] args) {\n        // run your function through some test cases here\n        // remember: debugging is half the battle!\n        String testInput = \"test input\";\n        System.out.println(myFunction(testInput));\n    }\n}", "codewars": "java", "codemirror": "text/x-java", "display_name": "Java", "short_name": "java", "case_convention": "camel", "prism": "java", "dropdown_rank": 2}, {"notepad_template": "function myFunction(arg) {\n    // write the body of your function here\n    return 'running with ' + arg;\n}\n\n// run your function through some test cases here\n// remember: debugging is half the battle!\nconsole.log(myFunction('test input'));\n", "codewars": "javascript", "codemirror": "text/javascript", "display_name": "JavaScript", "short_name": "javascript", "case_convention": "camel", "prism": "javascript", "dropdown_rank": 4}, {"notepad_template": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nconst char * my_function(char * arg){\n    // write the body of your function here\n    return arg;\n}\n\nint main(){\n    // run your function through some test cases here\n    // remember: debugging is half the battle!\n    printf(\"%s\", my_function(\"test input\"));\n    return 0;\n}", "prism": "c", "codewars": "c", "closest_languages": ["cpp", "java"], "display_name": "C (beta)", "short_name": "c", "case_convention": "camel", "codemirror": "text/x-csrc", "dropdown_rank": 5}, {"notepad_template": "#include <iostream>\nusing namespace std;\n\nstring myFunction (const string& arg) {\n    // write the body of your function here\n    return \"running with \" + arg;\n}\n\nint main () {\n    // run your function through some test cases here\n    // remember: debugging is half the battle!\n    cout << myFunction (\"test input\");\n    return 0;\n}", "prism": "cpp", "codewars": "cpp", "closest_languages": ["c", "java"], "display_name": "C++ (beta)", "short_name": "cpp", "case_convention": "camel", "codemirror": "text/x-c++src", "dropdown_rank": 6}], "INTEGRATIONS_SETTING_ONLY_INTEGRATIONS_THAT_SUPPORT_FRONT_END_ONLY": {"Facebook Pixel": true, "Google Analytics": true, "All": false, "Adwords": true, "Optimizely": true}, "DEFAULT_C18N_LANGUAGE": {"notepad_template": "def my_function(arg):\n    # write the body of your function here\n    return 'running with %s' % arg\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nprint my_function('test input')\n", "codewars": "python", "codemirror": "text/x-python", "display_name": "Python", "short_name": "python", "case_convention": "snake", "prism": "python", "dropdown_rank": 1}, "C18N_LANGUAGES": [{"notepad_template": "def my_function(arg):\n    # write the body of your function here\n    return 'running with %s' % arg\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nprint my_function('test input')\n", "codewars": "python", "codemirror": "text/x-python", "display_name": "Python", "short_name": "python", "case_convention": "snake", "prism": "python", "dropdown_rank": 1}, {"notepad_template": "def my_function(arg)\n    # write the body of your function here\n    return \"running with #{arg}\"\nend\n\n# run your function through some test cases here\n# remember: debugging is half the battle!\nputs my_function('test input')\n", "codewars": "ruby", "codemirror": "text/x-ruby", "display_name": "Ruby", "short_name": "ruby", "case_convention": "snake", "prism": "ruby", "dropdown_rank": 3}, {"notepad_template": "public class Solution {\n    public static String myFunction(String arg) {\n        // write the body of your function here\n        return \"running with \" + arg;\n    }\n    public static void main(String[] args) {\n        // run your function through some test cases here\n        // remember: debugging is half the battle!\n        String testInput = \"test input\";\n        System.out.println(myFunction(testInput));\n    }\n}", "codewars": "java", "codemirror": "text/x-java", "display_name": "Java", "short_name": "java", "case_convention": "camel", "prism": "java", "dropdown_rank": 2}, {"notepad_template": "function myFunction(arg) {\n    // write the body of your function here\n    return 'running with ' + arg;\n}\n\n// run your function through some test cases here\n// remember: debugging is half the battle!\nconsole.log(myFunction('test input'));\n", "codewars": "javascript", "codemirror": "text/javascript", "display_name": "JavaScript", "short_name": "javascript", "case_convention": "camel", "prism": "javascript", "dropdown_rank": 4}, {"notepad_template": "#include <iostream>\nusing namespace std;\n\nstring myFunction (const string& arg) {\n    // write the body of your function here\n    return \"running with \" + arg;\n}\n\nint main () {\n    // run your function through some test cases here\n    // remember: debugging is half the battle!\n    cout << myFunction (\"test input\");\n    return 0;\n}", "prism": "cpp", "codewars": "cpp", "closest_languages": ["c", "java"], "display_name": "C++ (beta)", "short_name": "cpp", "case_convention": "camel", "codemirror": "text/x-c++src", "dropdown_rank": 6}]};

        
        window.JS_VARS = {"url_content_type": "question", "questions_fully_attempted": ["stock-price", "product-of-other-numbers", "cake-thief", "kth-to-last-node-in-singly-linked-list", "reverse-string-in-place", "balanced-binary-tree"]};
        

        
    </script>



    

    
    <script type="text/javascript" src="stocks_files/a.js"></script>
    <script type="text/javascript">
        Stripe.setPublishableKey('pk_live_4wtgGTkgBtk4YIB9JDjYdOD0');
    </script>
    

    
    
    <div id="fb-root" class=" fb_reset"><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div><iframe name="fb_xdm_frame_https" allowtransparency="true" allowfullscreen="true" scrolling="no" id="fb_xdm_frame_https" aria-hidden="true" title="Facebook Cross Domain Communication Frame" tabindex="-1" style="border: medium none;" src="stocks_files/fTmIQU3LxvB.html" frameborder="0"></iframe></div></div><div style="position: absolute; top: -10000px; height: 0px; width: 0px;"><div></div></div></div>
    <script>(function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=149278655279066";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));</script>

    <script id="twitter-wjs" src="stocks_files/widgets.js"></script>
    

    
    
        
            <script type="text/ng-template" id="/partials/animation.html"><div class="animation-wrapper">
    <div class="animation" id="Stage-[[getCompId()]]" ng-class="getCompId()">
    </div>
</div>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/animation_iframe.html"><div class="animation-iframe-wrapper">
    <iframe class="animation-iframe animation-iframe-[[getCompId()]]"></iframe>
</div>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/code-inline.html"><span class="ic-code-inline" ng-transclude></span></script>
        
    
        
            <script type="text/ng-template" id="/partials/code-block.html"><pre class="language-[[language]]">
  <code class="language-[[language]]" ng-transclude></code>
</pre>
<span class="warning-message" ng-show="warningMessage" ng-bind="warningMessage"></span>
<div class="select-content-language" ng-hide="staticLanguage" ng-cloak>

    <select ng-model="contentLanguage" ng-options="language.display_name for language in contentLanguages" ng-change="updateLanguage(contentLanguage)"></select>

</div>
<span class="only-content-language" ng-show="staticLanguage" ng-bind="onlyLanguage"></span>
<!-- FE TESTING <button class="run-tests" ng-show="showTests && hasTests" ng-click="runTests()">TEST</button> -->
</script>
        
    
        
            <script type="text/ng-template" id="/partials/complexity.html"><span class="complexity"><span math>O([[getComplexityMarkup()]])</span></span>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/concept.html"><span class="concept-wrapper" ng-init="showConcept=false">

    <span ng-click="showConcept=!showConcept" class="concept">
        <span class="concept-name" ng-transclude></span>
        <span class="show-concept-icon">&#8628;</span>
    </span>

    <div ng-show="showConcept" class="slide concept-explanation" ng-include="conceptPartialUrl">
        Loading...
    </div>

</span>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/function.html"><span class="ic-function"><span class="name" ng-transclude></span>()</span>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/heading.html"><h3 class="heading slide" ng-show="shouldShow()" ng-cloak>[[getHeadingText()]]</h3>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/inline-footnote.html"><span class="footnote-wrapper" ng-init="show = false">
    <span class="show-footnote-icon" ng-click="show = !show">&#8628;</span>
    <p class="footnote" ng-transclude ng-show="show">Loading...</p>
</span>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/loading.html"><div class="Loading">
    Loading...
</div>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/math.html"><span class="ic-math" ng-class="{'block': isBlock()}" ng-transclude></span>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/note.html"><div class="note slide" ng-show="shouldShow()">
    <div class="note-content" ng-transclude>
    </div>
</div>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/section.html"><div class="section-wrapper" ng-class="getSectionClass()" ng-init="ready=false" ng-show="shouldShow()">
    <span heading="[[section]]" hide-heading="[[hideHeading]]"></span>

    <div class="section" ng-class="getSectionClass()" ng-transclude>
    </div>

    
</div>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/variable.html"><span class="ic-variable" ng-transclude></span>
</script>
        
    
        
            <script type="text/ng-template" id="/partials/words.html"><span class="ic-words" ng-transclude></span>
</script>
        
    


    <!-- load current-user json with initial http request -->
    <div class="hidden" data-preload-resource="/api/v1/current-user/" data-thejson="{&quot;id&quot;:3526074,&quot;username&quot;:&quot;justwjr&quot;,&quot;email&quot;:&quot;justwjr@ucla.edu&quot;,&quot;date_joined&quot;:&quot;2016-09-28T23:25:25.894421+00:00&quot;,&quot;first_name&quot;:&quot;Justin&quot;,&quot;last_name&quot;:&quot;J. Wang&quot;,&quot;full_name&quot;:&quot;Justin J. Wang&quot;,&quot;short_name&quot;:&quot;Justin&quot;,&quot;is_anonymous&quot;:false,&quot;is_on_last_question&quot;:false,&quot;percent_done&quot;:7,&quot;num_questions_done&quot;:3,&quot;num_questions_remaining&quot;:41,&quot;recruiting_is_interested_in_intros&quot;:null,&quot;is_full_access&quot;:false,&quot;first_payment_date&quot;:null,&quot;last_payment_date&quot;:null,&quot;num_free_questions_left&quot;:0,&quot;terms_has_agreed_to_latest&quot;:false,&quot;preferred_content_language&quot;:&quot;python&quot;,&quot;preferred_notepad_language&quot;:&quot;&quot;,&quot;is_staff&quot;:false,&quot;auth_providers_human_readable_list&quot;:&quot;Github&quot;,&quot;num_auth_providers&quot;:1,&quot;auth_email&quot;:&quot;justwjr@ucla.edu&quot;}">
        
{"id":3526074,"username":"justwjr","email":"justwjr@ucla.edu","date_joined":"2016-09-28T23:25:25.894421+00:00","first_name":"Justin","last_name":"J.
 Wang","full_name":"Justin J. 
Wang","short_name":"Justin","is_anonymous":false,"is_on_last_question":false,"percent_done":7,"num_questions_done":3,"num_questions_remaining":41,"recruiting_is_interested_in_intros":null,"is_full_access":false,"first_payment_date":null,"last_payment_date":null,"num_free_questions_left":0,"terms_has_agreed_to_latest":false,"preferred_content_language":"python","preferred_notepad_language":"","is_staff":false,"auth_providers_human_readable_list":"Github","num_auth_providers":1,"auth_email":"justwjr@ucla.edu"}

    </div>

    

    <!-- Login Modal -->
    <div ng-controller="LoginModalCtrl" class="modal fade login-modal ng-scope" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="Log In" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <h3 ng-bind="note" class="ng-binding">Log in to continue</h3>
                    <button type="button" ng-show="closeable" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                    <div class="login-btns">
    <a ng-href="/auth/login/github/?next=%2Fnext" class="btn btn-soc-github" href="https://www.interviewcake.com/auth/login/github/?next=%2Fnext"><i class="fa fa-github"></i> | Log in with Github</a>
    <a ng-href="/auth/login/google-oauth2/?next=%2Fnext" class="btn btn-soc-google-plus" href="https://www.interviewcake.com/auth/login/google-oauth2/?next=%2Fnext"><i class="fa my-fa-google-plus"></i> | Log in with Google</a>
    <a ng-href="/auth/login/facebook/?next=%2Fnext" class="btn btn-soc-facebook" href="https://www.interviewcake.com/auth/login/facebook/?next=%2Fnext"><i class="fa my-fa-facebook"></i> | Log in with Facebook</a>
</div>
<p class="login-reassurance">
    <small>
        We'll never post on your wall or message your friends.
    </small>
</p>

                </div>
            </div>
        </div>
    </div>


    

    <input name="csrfmiddlewaretoken" value="fNbtGVTOxJrKet0DcRtrf2ADALgEZwtoW7TGfkvzqzHurBnchQsCCHgWgE7GfY29" type="hidden">
<div id="loading">
. . .
</div>


<link href="stocks_files/css.css" rel="stylesheet" type="text/css">

<iframe name="stripeXDM_default655446_provider" id="stripeXDM_default655446_provider" style="position: absolute; top: -2000px; left: 0px;" src="stocks_files/channel.html" frameborder="0"></iframe><iframe id="rufous-sandbox" scrolling="no" allowtransparency="true" allowfullscreen="true" style="position: absolute; visibility: hidden; display: none; width: 0px; height: 0px; padding: 0px; border: medium none;" frameborder="0"></iframe></body></html>