//登录接口的account和password都是经过加密的，登录按钮的点击函数全局搜索或者click事件，进入函数，查看函数（搜加密，注释有）
window = global;
const JSEncrypt=require("jsencrypt")//npm install jsencrypt
global.window = {}; 
function et(_0x32033c) {
    var _0x283d00 = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsgDq4OqxuEisnk2F0EJFmw4xKa5IrcqEYHvqxPs2CHEg2kolhfWA2SjNuGAHxyDDE5MLtOvzuXjBx/5YJtc9zj2xR/0moesS+Vi/xtG1tkVaTCba+TV+Y5C61iyr3FGqr+KOD4/XECu0Xky1W9ZmmaFADmZi7+6gO9wjgVpU9aLcBcw/loHOeJrCqjp7pA98hRJRY+MML8MK15mnC4ebooOva+mJlstW6t/1lghR8WNV8cocxgcHHuXBxgns2MlACQbSdJ8c6Z3RQeRZBzyjfey6JCCfbEKouVrWIUuPphBL3OANfgp0B+QG31bapvePTfXU48TYK0M5kE+8LgbbWQIDAQAB';
    var _0x1defd6 = new JSEncrypt();
    _0x1defd6['setPublicKey'](_0x283d00);
    var _0x4bd6d3 = _0x1defd6['encrypt'](_0x32033c);
    return _0x4bd6d3;
}
console.log(et("hhhhhhhhh"))






// const NodeRSA = require('node-rsa');

// // 创建一个 RSA 密钥
// const key = new NodeRSA({ b: 2048 });// 使用 2048 位密钥

// // 获取公钥和私钥
// const publicKey = key.exportKey('public');
// const privateKey = key.exportKey('private');

// // 使用公钥加密
// const encrypted = key.encrypt('hhhhhhhhh', 'base64');
// console.log('Encrypted:', encrypted);

// // 使用私钥解密
// const decrypted = key.decrypt(encrypted, 'utf8');
// console.log('Decrypted:', decrypted);







// const NodeRSA = require('node-rsa');

// // 你的公钥，确保它是一个完整的 PEM 格式的公钥
// const publicKey = `-----BEGIN PUBLIC KEY-----
// MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsgDq4OqxuEisnk2F0EJFmw4xKa5IrcqEYHvqxPs2CHEg2kolhfWA2SjNuGAHxyDDE5MLtOvzuXjBx/5YJtc9zj2xR/0moesS+Vi/xtG1tkVaTCba+TV+Y5C61iyr3FGqr+KOD4/XECu0Xky1W9ZmmaFADmZi7+6gO9wjgVpU9aLcBcw/loHOeJrCqjp7pA98hRJRY+MML8MK15mnC4ebooOva+mJlstW6t/1lghR8WNV8cocxgcHHuXBxgns2MlACQbSdJ8c6Z3RQeRZBzyjfey6JCCfbEKouVrWIUuPphBL3OANfgp0B+QG31bapvePTfXU48TYK0M5kE+8LgbbWQIDAQAB
// -----END PUBLIC KEY-----`;

// // 创建 RSA 密钥对象，并指定密钥格式
// const key = new NodeRSA(publicKey, 'pkcs8-public');

// // 设置加密时使用的编码（可以是 base64、utf8 等）
// const encrypted = key.encrypt('hhhhhhhhh', 'base64');

// console.log('Encrypted:', encrypted);

