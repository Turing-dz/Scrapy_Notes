import scrapy


class AppSpider(scrapy.Spider):
    name = 'app'
    # allowed_domains = ['www.cheshi.com']
    # start_urls = ['https://my.cheshi.com/user/']
    def start_requests(self):
        #1.使用cookie直接访问
        # url='https://my.cheshi.com/user/'
        # cookies="pv_uid=1732254874878; cheshi_UUID=01JD96ZEWPDK2ZKK8X3WGFFPVS; cheshi_pro_city=MV%2FljJfkuqxfMV%2FkuJzln47ljLpfYmVpamluZw%3D%3D; Hm_lvt_8fe47348e12ba11be217fd389b115472=1732254888,1732494411; HMACCOUNT=0F938E3E8702278B; Hm_lvt_ed9cf33799965fb6c868762ac84e663e=1732674587; PHPSESSID=bd0f056bb72ef681c01a68b853bde882; cheshi_user_prevLogintime=1732674716; Hm_lpvt_ed9cf33799965fb6c868762ac84e663e=1732675618; cheshi_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6ImNoZXNoaV9oNV9zaWduIn0.eyJpc3MiOiJodHRwczpcL1wvYXBpLmNoZXNoaS5jb20iLCJhdWQiOiJodHRwczpcL1wvYXBpLmNoZXNoaS5jb20iLCJqdGkiOiJjaGVzaGlfaDVfc2lnbiIsImlhdCI6MTczMjY3NTY2OSwibmJmIjoxNzMyNjc1NzI5LCJleHAiOjE3MzMyODA0NjksInVpZCI6IjkxMDcxNDIifQ.txhZVRGAHLpMP8whjQ3fPcgNicQmVYake_8s0J1EKzk; cheshi_user_authv2=MzI2NDUyNAlsaXR0bGVaCXYyCWJjZDYzMWQ4NDZlMTQ4ZWQwY2UzZThhMTFkYTE2YmQxCTE3MzI2NzU2NjkJMzMyMjhkMGRmNDc3ZTc2YmVlMTQ0Y2JmODg1Zjk5OTY=; cheshi_user_info=OTEwNzE0MglsaXR0bGVaCXYyCWJjZDYzMWQ4NDZlMTQ4ZWQwY2UzZThhMTFkYTE2YmQxCTE3MzI2NzU2NjkJMzMyMjhkMGRmNDc3ZTc2YmVlMTQ0Y2JmODg1Zjk5OTYJaHR0cHM6Ly9pbWcuY2hlc2hpLWltZy5jb20vdXNlcnBob3RvL25ldy85MTA3MTQyL2FkNzc3NzZkYmRiM2M5NGFhZTE2YWYyM2M3OGRlMjkzLmpwZwkwCXdhbmdzaGFuZ2NoZXNoaQ==; cheshi_user_info_for_index=OTEwNzE0MglsaXR0bGVaCXYyCWJjZDYzMWQ4NDZlMTQ4ZWQwY2UzZThhMTFkYTE2YmQxCTE3MzI2NzU2NjkJMzMyMjhkMGRmNDc3ZTc2YmVlMTQ0Y2JmODg1Zjk5OTYJaHR0cHM6Ly9pbWcuY2hlc2hpLWltZy5jb20vdXNlcnBob3RvL25ldy85MTA3MTQyL2FkNzc3NzZkYmRiM2M5NGFhZTE2YWYyM2M3OGRlMjkzLmpwZwkwCXdhbmdzaGFuZ2NoZXNoaQ==; lv=1732685873; vn=8; Hm_lpvt_8fe47348e12ba11be217fd389b115472=1732685874; pv_cheshit=1732685902509; pv_source="
        # cookies={ item.split("=")[0] : item.split("=")[1] for item in cookies.split("; ")}
        # yield scrapy.Request(url=url,callback=self.parse,cookies=cookies)
        #2.通过login获取cookie
        url_login="https://api.cheshi.com/services/common/api.php?api=login.Login"
        data={
        "act": "login",
        "mobile": "hhhhhhhhh",
        "source": "pc",
        "password": "PASSWORDdz",
        "hold_time": "yes",
        }
        yield scrapy.FormRequest(url=url_login,formdata=data,callback=self.parse)
    def parse(self, response):
        # print(response.text)#这个是cookies，不用设置，scrapy后台自动会保存携带这个cookies
        url="https://my.cheshi.com/user/"
        yield scrapy.Request(url=url,callback=self.parse_admin)
    def parse_admin(self,response):
        print(response.text)
        
        
