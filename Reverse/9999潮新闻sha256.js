window = global;
navigator = {userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",platform:"MacIntel"}

function vt() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function(t) {
        var e = 16 * Math.random() | 0;
        return ("x" === t ? e : 3 & e | 8).toString(16)
    }
    ))
}
function createOutputMethod(e, t) {
    return function(n) {
        return new Sha256(t,!0).update(n)[e]()
    }
}
function i(e) {
    return function() {
        var t = this
          , n = arguments;
        return new Promise((function(i, o) {
            var a = e.apply(t, n);
            function s(e) {
                r(a, i, o, s, l, "next", e)
            }
            function l(e) {
                r(a, i, o, s, l, "throw", e)
            }
            s(void 0)
        }
        ))
    }
}
function v(t) {
    return t.match(/wechat/gi) || t.match(/MicroMessenger/gi)
}
function w(t) {
    // var t='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    return /HARMONYOS|Android|webOS|iPhone|iPod|iPad|BlackBerry|SymbianOS|Windows Phone/i.test(t) || v(t)
}
function p(e) {
    var n = Date.now()
      , a = (0,vt)();
    return {
        "X-SESSION-ID": "111111111111111111111111",
        "X-REQUEST-ID": a,
        "X-SIGNATURE": createOutputMethod("".concat(e, "||111111111111111111111111||").concat(a, "||").concat(n, "||").concat("opj!89#%$kddd")).toString(),
        "X-TIMESTAMP": n,
        "X-XSOURCE": (0,
        w)(window.navigator.userAgent) ? "WAP" : "PC"
    }
}
var e='/api/article/channel_list'
console.log(p(e))