//搜索 sign:  然后找到方法，打断点
const Crypto=require("crypto")
function _(e) {
    return Crypto.createHash("md5").update(e.toString()).digest("hex")
}
function S(e, t) {
            return _(`client=${"fanyideskweb"}&mysticTime=${e}&product=${"webfanyi"}&key=${t}`)
        }
var e = (new Date).getTime()
t="EZAmCfVOH2CrBGMtPrtIPUzyv3bheLdk" 
console.log(S(e, t))