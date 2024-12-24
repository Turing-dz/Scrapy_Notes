import json
import pprint
with open("14690062-employees.json","r", encoding="utf-8") as file:
    data=json.load(file)#文件对象内地数据转换为python对象；loads方法是将string数据转换成python对象
    
# printer=pprint.PrettyPrinter()
# printer.pprint(data)
employees=data.get("employees")#python对象获取属性值用get,没有就返回None，用[]获取属性值，没有会报错
for employee in employees:
    print(employee.get("fullname"),employee.get("phone_number"))