window=global;
function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function d(d, e, f, g) {
    var h = {}
      , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}
RU1x=[
    "色",
    "流感",
    "这边",
    "弱",
    "嘴唇",
    "亲",
    "开心",
    "呲牙",
    "憨笑",
    "猫",
    "皱眉",
    "幽灵",
    "蛋糕",
    "发怒",
    "大哭",
    "兔子",
    "星星",
    "钟情",
    "牵手",
    "公鸡",
    "爱意",
    "禁止",
    "狗",
    "亲亲",
    "叉",
    "礼物",
    "晕",
    "呆",
    "生病",
    "钻石",
    "拜",
    "怒",
    "示爱",
    "汗",
    "小鸡",
    "痛苦",
    "撇嘴",
    "惶恐",
    "口罩",
    "吐舌",
    "心碎",
    "生气",
    "可爱",
    "鬼脸",
    "跳舞",
    "男孩",
    "奸笑",
    "猪",
    "圈",
    "便便",
    "外星",
    "圣诞"
]

i1x={
    "csrf_token": "61e0797f1b50d21d11689c14153d8c99"
}
gO2x = function(i1x) {
    return Hb9S(i1x, "function")
}
bh1x = function(k1x, cH1x, O1x) {
    if (!k1x || !k1x.length || !gO2x(cH1x))
        return this;
    if (!!k1x.forEach) {
        k1x.forEach(cH1x, O1x);
        return this
    }
    for (var i = 0, l = k1x.length; i < l; i++)
        cH1x.call(O1x, k1x[i], i, k1x);
    return this
}
var bsc6W = function(cya8S) {
    var m1x = [];
    bh1x(cya8S, function(cxZ8R) {
        m1x.push(RU1x.emj[cxZ8R])
    });
    return m1x.join("")
};

var bVk5p = d(JSON.stringify(i1x), bsc6W(["流泪", "强"]), bsc6W(RU1x), bsc6W(["爱心", "女孩", "惊恐", "大笑"]));
console.log(bVk5p)