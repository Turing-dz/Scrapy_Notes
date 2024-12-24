#查看url解碼后的參數，是自己搜索的關鍵字
from urllib import parse#url的编解码
print(parse.unquote("%7B%22name%22:%22%E7%BD%91%E7%BB%9C%E8%B4%B7%E6%AC%BE%22,%22wordType%22:1%7D"))