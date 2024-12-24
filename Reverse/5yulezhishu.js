//AES加密
const CryptoJS=require("crypto-js")
function dataFilter(data,lastFetchTime) {
    var i = CryptoJS.enc.Utf8.parse(lastFetchTime + "000")
        , a = CryptoJS.enc.Utf8.parse(lastFetchTime + "000")
        , s = CryptoJS.AES.decrypt(data.toString(), i, {
        iv: a
    })
    return s.toString(CryptoJS.enc.Utf8)      
} 
console.log(dataFilter(data))