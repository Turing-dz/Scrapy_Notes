import gzip
from io import BytesIO

# 假设 compressed_data 是你已经提取的压缩数据部分
compressed_data = """?     旖y{壑???[Er* wZ杛e賜躥k祠揶躙]?E溶L傊掹?矚苢臬笛?[挼o杁蓇毻蜯毉m溰8便<餀€@ %*VR藟D瀍螠?s鎙3?{靏?|?'~?""蘑?/z鎄a硴淇?H蝠壝?<}赓g贏'RL<?|"蜠"""

# 解压缩
with gzip.GzipFile(fileobj=BytesIO(compressed_data)) as f:
    decompressed_data = f.read()

# 解码
html_content = decompressed_data.decode('gb2312')

print(html_content)
