from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","cnblogs"])#命令行执行scrapy crawl cnblogs

execute(["scrapy","crawl","zhihu"])

# execute(["scrapy","crawl","myblog"])
# execute(["scrapy","crawl","lagou"])