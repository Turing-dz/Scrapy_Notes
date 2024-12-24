s1="好"
s2=s1.encode("utf-8")#使用utf-8字符集进程编码b'\xe5\xa5\xbd'（文字-数字-二进制数字）
s3=s1.encode("unicode-escape")#b'\\u597d'
print(s2,s3)
s4=s2.decode("utf-8")
s5=s3.decode("unicode-escape")
print(s4,s5)