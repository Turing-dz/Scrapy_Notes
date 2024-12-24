//加密
const Crypto=require("crypto")// npm install crypto-js
function _u_e(e) {
    if (null == e)
        return null;
    e = e.replace(/\r\n/g, "\n");
    for (var t = "", n = 0; n < e.length; n++) {
        var r = e.charCodeAt(n);
        r < 128 ? t += String.fromCharCode(r) : r > 127 && r < 2048 ? (t += String.fromCharCode(r >> 6 | 192),
        t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
        t += String.fromCharCode(r >> 6 & 63 | 128),
        t += String.fromCharCode(63 & r | 128))
    }
    return t
}
var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
              , _p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O";
function e1(e) {
    if (null == e)
        return null;
    for (var t, n, r, o, i, a, u, c = "", l = 0; l < e.length; )
        o = (t = e.charCodeAt(l++)) >> 2,
        i = (3 & t) << 4 | (n = e.charCodeAt(l++)) >> 4,
        a = (15 & n) << 2 | (r = e.charCodeAt(l++)) >> 6,
        u = 63 & r,
        isNaN(n) ? a = u = 64 : isNaN(r) && (u = 64),
        c = c + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(u);
    return c
}
function e2(e) {
    if (null == (e = _u_e(e)))
        return null;
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t
}
function md5(text) {
    return Crypto.createHash('md5').update(text).digest('hex')
  }
function sig(e) {
    return md5(e + _p).toUpperCase()//使用md5在线加密网站，加密e + _p的值，发现网站加密结果和返回值一样，所以可以直接使用md5包
}
var payload={"code":['M0ZBXTHL', 'ZUB5G98E', 'QZDVA0G4', 'YOGAVOU2', 'SUBCWVA1', 'DEMZPJAJ', 'shzhshlbshkj', '823015e994ac2fd9987cb1bd5a4708f8', 'yingsite95', 'YYWHLKBA', 'D55941M1', '0RUR5V2C', 'DNQ3OIY4', 'WPKIKD7V', 'CZEWRH3A', 'WU9E8W4T', 'MBOFS71V', 'OYY50C45', 'SHQPAJLV', 'RLRN8YIJ']}
var f = e1(e2(JSON.stringify(payload)))
        , p = sig(f);
console.log(p)
//解密
function d1(e) {
    var t, n, r, o, i, a, u = "", c = 0;
    for (e = e.replace(/[^A-Za-z0-9\+\/\=]/g, ""); c < e.length; )
        t = _keyStr.indexOf(e.charAt(c++)) << 2 | (o = _keyStr.indexOf(e.charAt(c++))) >> 4,
        n = (15 & o) << 4 | (i = _keyStr.indexOf(e.charAt(c++))) >> 2,
        r = (3 & i) << 6 | (a = _keyStr.indexOf(e.charAt(c++))),
        u += String.fromCharCode(t),
        64 != i && (u += String.fromCharCode(n)),
        64 != a && (u += String.fromCharCode(r));
    return u
}
function _u_d(e) {
    for (var t = "", n = 0, r = 0, o = 0, i = 0; n < e.length; )
        (r = e.charCodeAt(n)) < 128 ? (t += String.fromCharCode(r),
        n++) : r > 191 && r < 224 ? (o = e.charCodeAt(n + 1),
        t += String.fromCharCode((31 & r) << 6 | 63 & o),
        n += 2) : (o = e.charCodeAt(n + 1),
        i = e.charCodeAt(n + 2),
        t += String.fromCharCode((15 & r) << 12 | (63 & o) << 6 | 63 & i),
        n += 3);
    return t
}
function d2(e) {
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t = _u_d(t)
}
s='LBcnV1QrZGB4bXsmWTE0awgPTRZaPTlCLCArEj8hEHVlA3AJCHl3dmoiNi9IJDswbTdZUFxwbhAfAgADbhx7BXVIaEMSLSk3OCA3O2csMWsIZgMNCGdjCmFsMSI7NVMhLmonV1QrZGBqeRwRenYTG3F2SxhCcDddID4zIy8aWyt1D3YKAX1wbnxteyFXKCUoXC1pV1Y2MRB3bGEOHwkAFgFsZkUcNWQ5JywpI1Y8CiBWdgwFDmthAXR9fm81Kl8/Nls9Z1MhIj9qe3txawEGCANhbBZEfi8QLiE/PTcrSxA+UWYCCXp3aHl0dWBbKjg5UzpPa1o9MFdvdHApMTZaNT9eIEJTIi0wajx1ORomOiRCNVhNZjswEHd6Yn1ncgRjdVYrVUAvKCMXIjYmXWdva0g8V1peMCFWLCFwMHo+ECw4WDRZXjcZMyxjY3AAc2J6AngUV1Y/JFMjNw0uOSFXbW0XMFdeKTQ/Jjg4LUEgdzQeLxRXVj8kUyM3DSQyZwh8ZQR0AQB8angrLjQyWSssFlE7UlEbaHZ0GncaA2EcY20qGT8aUyErKikvIB1RIXdzAWYHBABiZB5vLT0gJiRcNghWK1xVbHx4DQNsEgwWHxkQKRpPGzE7Xz0vPDQJLFZtbQZ2CQB2c2tkYzotVTU0J0sLVVtdN3YIbxhhHBJ1YAQTFzkUS2wlNSUxOCxBGjwtEG4EAwphZQR0YnAuOShCLjlMG1tfKiN4cmMDdm0PBBphFhRJFSl2USIjIiw4PG0mMxd+CgJ/dW9+d3VgWyo4OVM6T2taPTBXb3RwHg8KB38HY3MaTWI9eCsuNDJZKywWWzAUDgtgZQJ+fWVhdCZdIidUKkFvLSk+LWNjYHccZ3F7bQZ2Gy94SW8tPSAmJFw2CFwgGgp/f2pxc2xxFGc2Jl8kV1pADTddKStwd3QoUyYkXC5RVXhweDVtImBbKjg5UzpPa1A2dgh8d2J5Y30FY3VWK1VALygjFyI2Jl1nb2sLYHlieBoWBm8zfjZ0Jl0iJ1QqQW8nInhycGFxCX1jeR52VVtUIjVcNBExIjIgEHV1QSVRWDssMzkoKydWZyhlSXZVW1QiNVw0ETspdH8DeGUNdAoBYmQ5JywpI1Y8CipdMFMWA3AnWiU2ICY8PVU8ZAVmRRw1ZDknLCkjVjwKIFZ2DAUNZmEAf3t+bzUqXz82Wz1nUyEiP2p7eyFQPT4jSjNFAwpwKR42bDEiOzVTIS5qLVwSdHFieXZpdxRnNiZfJFdaQA03XSkrcHd0L1shLV0lVlclIzAhYyRuQ2c2Jl8kV1pADT1Wb3Rlf2dxB3x7FydXXT4nNDEeOi1cIHdzEBJgBQ5qH3cFbC8QemdGICNUKBoKenFucG17L102JihVMRQOVyc4XjA='
var d = d1(s)
, y = d2(d)
, v = JSON.parse(y);
console.log(v)
