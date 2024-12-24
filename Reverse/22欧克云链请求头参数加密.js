//搜索参数名：x-apikey或者headers. headers[ headers( ，最后我是搜索encrypt定位的window.btoa(str)就是Base64编码的
window=global;
API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
var p = 1111111111111;
function encryptApiKey() {
    var t = API_KEY
        , e = t.split("")
        , r = e.splice(0, 8);
    return t = e.concat(r).join("")
}
function mathRandom() {
    return Math.random()
}
function encryptTime(t) {
    var e = (1 * t + p).toString().split("")
        , r = parseInt(10 * mathRandom(), 10)
        , n = parseInt(10 * mathRandom(), 10)
        , o = parseInt(10 * mathRandom(), 10);
    return e.concat([r, n, o]).join("")
}
function comb(t, e) {
    var r = "".concat(t, "|").concat(e);
    return window.btoa(r)
}
function getApiKey() {
    var t = (new Date).getTime()
      , e = encryptApiKey();
    return t = encryptTime(t),
    comb(e, t)
}
console.log(getApiKey())