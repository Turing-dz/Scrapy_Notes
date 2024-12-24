function e(t) {
    var n;
    return l.a.wrap(function(e) {
        for (; ; )
            switch (e.prev = e.next) {
            case 0:
                if (!A.includes(t.url)) {
                    e.next = 6;
                    break
                }
                return e.next = 3,
                p();
            case 3:
                n = e.sent,
                t.headers = t.headers || {},
                t.headers["Cipher-Text"] = n;
            case 6:
                if (!h.includes(t.url)) {
                    e.next = 12;
                    break
                }
                if (_) {
                    e.next = 10;
                    break
                }
                return e.next = 10,
                d();
            case 10:
                t.headers = t.headers || {},
                t.headers.index_csrftoken = _;
            case 12:
                return t.url.includes("hairuo") && (t.headers = t.headers || {},
                t.headers["content-type"] = "application/x-www-form-urlencoded"),
                e.abrupt("return", t);
            case 14:
            case "end":
                return e.stop()
            }
    }, e, this)
}