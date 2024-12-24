//https://ggzy.jcs.gov.cn/website/transaction/index
//全局搜索参数名projectId和projectInfo定位 ,定位到有一个参数是"ZBGG"，是对这两个参数做了处理，全局搜索"ZBGG"，定位到了参数对应的字典对象，然后进入处理方法（或者搜索encrypt）,处理方法的结尾处打上断点，调试，看一下输入输出
const CryptoJS=require("crypto-js")
var i = {
            keyHex: CryptoJS.enc.Utf8.parse(Object({
                NODE_ENV: "production",
                VUE_APP_BASE_API: "/pro-api",
                VUE_APP_CONSTRUCTION_API: "/pro-api-construction",
                VUE_APP_CONSTRUCTION_IP: "http://192.168.30.35:8082/dev-api-construction",
                VUE_APP_DEFAULT_IP: "http://192.168.30.35:8081/dev-api",
                VUE_APP_DEV_FILE_PREVIEW: "/lyjcdFileView/onlinePreview",
                VUE_APP_FILE_ALL_PATH: "http://www.lyjcd.cn:8089",
                VUE_APP_FILE_PREFIX: "/mygroup",
                VUE_APP_FILE_UPLOAD_ZG_ADDRESS: "/zgTenderFile/push/doAnonUploadTBFile.html",
                VUE_APP_LAND_API: "/pro-api-land",
                VUE_APP_LAND_IP: "http://192.168.30.243:8084/dev-api-land",
                VUE_APP_PREVIEW_PREFIX: "/lyjcdFileView",
                VUE_APP_PROCUREMENT_API: "/pro-api-procurement",
                VUE_APP_PROCUREMENT_IP: "http://192.168.30.243:8083/dev-api-procurement",
                VUE_APP_WINDOW_TITLE: "金昌市公共资源交易网",
                BASE_URL: "/"
            }).VUE_APP_CUSTOM_KEY || "54367819"),
            ivHex: CryptoJS.enc.Utf8.parse(Object({
                NODE_ENV: "production",
                VUE_APP_BASE_API: "/pro-api",
                VUE_APP_CONSTRUCTION_API: "/pro-api-construction",
                VUE_APP_CONSTRUCTION_IP: "http://192.168.30.35:8082/dev-api-construction",
                VUE_APP_DEFAULT_IP: "http://192.168.30.35:8081/dev-api",
                VUE_APP_DEV_FILE_PREVIEW: "/lyjcdFileView/onlinePreview",
                VUE_APP_FILE_ALL_PATH: "http://www.lyjcd.cn:8089",
                VUE_APP_FILE_PREFIX: "/mygroup",
                VUE_APP_FILE_UPLOAD_ZG_ADDRESS: "/zgTenderFile/push/doAnonUploadTBFile.html",
                VUE_APP_LAND_API: "/pro-api-land",
                VUE_APP_LAND_IP: "http://192.168.30.243:8084/dev-api-land",
                VUE_APP_PREVIEW_PREFIX: "/lyjcdFileView",
                VUE_APP_PROCUREMENT_API: "/pro-api-procurement",
                VUE_APP_PROCUREMENT_IP: "http://192.168.30.243:8083/dev-api-procurement",
                VUE_APP_WINDOW_TITLE: "金昌市公共资源交易网",
                BASE_URL: "/"
            }).VUE_APP_CUSTOM_IV || "54367819")
        };
// function c(t) {
//     return -1 != (t = CryptoJS.DES.decrypt({
//         ciphertext: CryptoJS.enc.Hex.parse(t)
//     }, i.keyHex, {
//         iv: i.ivHex,
//         mode: CryptoJS.mode.CBC,
//         padding: CryptoJS.pad.Pkcs7
//     }).toString(CryptoJS.enc.Utf8)).indexOf("{") && -1 != t.indexOf("}") ? JSON.parse(t) : t
// }
function c(t) {
    return CryptoJS.DES.encrypt(t, i.keyHex, {
        iv: i.ivHex,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).ciphertext.toString()
}
console.log(c("ZBGG"))