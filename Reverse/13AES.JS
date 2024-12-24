const CryptoJS=require("crypto-js")
function b(t) {
    var e = CryptoJS.enc.Utf8.parse("EB444973714E4A40876CE66BE45D5930")
      , n = CryptoJS.enc.Utf8.parse("B5A8904209931867")
      , a = CryptoJS.AES.decrypt(t, e, {
        iv: n,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return a.toString(CryptoJS.enc.Utf8)
}
t='MZphJmFlelDpw2aSCfdFb5y2Gzdx4AtEEXvB7fXbF2GPPm0BHW6As+dkNeqYzf0fn6M4gjfCDecwrOIAdOuC1hQyzwdFGGzdC21G4mfIHEL/r3Lg4PNJoz+tSnj2YHGRP2WE8seUangIqyPLrwAHCIOV0hm9G/JvkTuf3CLrWz+0y3YPe0PiafH9bSM6AmJYLfjRqBg1/EwKLlj0ez/7uUR7wTWt89Yg6yauTxX7kJ2+xFj29iHaHvP+2/wcobvp1Y045vTPzFcchj1b9j5x5Qwl4ES8h631bKJNCVRPnbJGg+d6vZgUn6M9DIf/xkL0AypQnMBWmg5Nl50np5R4RTrrhrWPNSQEQ5c/PlTzlQijhxXtNlhr3kHd58/kJyP2UAorDN6ys18eMkVkOSGxpocyPxwg2r6xMviPD+NkvA6dqzG/qY/4NhDD1rPj+TpUf92Hhf/WA1Xc1Ktc/xFb7U6XvM1l03UgXwxfkeDDmHw1z9jTFomOth9LYRDfk/0cYJ1WZAgHuS6Y1xPyS2o3CzqVWmDrhgAEAQlk/2YazrKYlQIafSK3V+0/VCk/FiMEBdb6AxwYkB3ltzEQtJN0D0CzKzY6XrJevYbu897Rm7jl7OOqAhyqayX0CxIamxYaF7af48uH60in+e4wO31rC8/WNOXaj6qWvHbEIftHqCsQ4JCEz1HjCMeE22Gz4YLhDQ7UdjL9VwQEXJiuqVglhY7TtiDcFdopgMY0a/sAw5LxATiA3vrCzJ9Hp0TPvQ9ML2gTBx/uwRGkmER0x8wZ2FaJFx9f3A3G5r63sTghJPcl+hNXw+EtDC84cuveqw+/NQElIY7K9WnMOj6J7waGgk53op4ZCzHALNAhL7apPp6Yu1iqsFZjzq0pvlXzWDk+jGvP7H0U+N/7jr0XTSQuTw=='
console.log(b(t))
