//生成请求头参数portal-sign
const CryptoJS=require("crypto")
e={
    "ts": (new Date).getTime(),
    "type": "12",
    "IS_IMPORT": 1,
    "pageSize": 3
}
function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
} 
function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}
function s(text) {
    return CryptoJS.createHash('md5').update(text).digest('hex');
  }
function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = "B3978D054A72A7002063637CCDF6B2E5" + u(t);
    return s(n).toLocaleLowerCase()
}
console.log(d(e)) 