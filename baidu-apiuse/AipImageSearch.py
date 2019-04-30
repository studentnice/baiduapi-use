from aip import AipImageSearch
import base64

APP_ID = '16131949'
API_KEY = 'EsiuaMz0Z4NUqfte4hRBd4h0'
SECRET_KEY = 'q57P8ItFRKYpAgLernXfsiz9eNO5lo5a'

"""在这里的代码中 主要记住 以下几个参数
filepath 文件路径 
tags  你要把你的图片分到什么样的区间 100，11？ 102 ，12 ？ 都可以  
target 你的图片属于什么样的种类 ，病芒果？ 病樱桃？ 都可以 
numbers 你的图片在你的类里是什么样的序列 001？ 002？ 00？ 都可以"""

"""
get_file_content 获取图片内容，直接调用就好了
insert 插入图片 需要参数 filepath，tags，target，numbers
search 查找图片 需要参数 filepath tags
update 更新图片特征 需要参数 filepath tags target numbers
delete 删除图片 需要参数filepath
"""

"""如果出现报错，会有提示，记得看官方文档"""


clinet = AipImageSearch(APP_ID,API_KEY,SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def insert_to_database(filepath,tags,target,numbers):

    image = get_file_content(filepath)
    options = {}
    options["brief"] = "{\"name\":\"%s\", \"id\":\"%s\"}" %(target,numbers)
    options["tags"] = "%s" %tags
    result = clinet.similarAdd(image,options)
    if 'error_msg' in result.keys():
        print("插入失败 失败原因为 %s" %result['error_msg'])
    else:
        print("插入成功 唯一的cont_sign为 %s" %result["cont_sign"])
        return result["cont_sign"]


def search_on_database(filepath,tags):
    image = get_file_content(filepath)
    clinet.similarSearch(image)
    options = {}
    options["tags"] = "%s" %tags
    result = clinet.similarSearch(image,options)
    if 'error_msg' in result.keys():
        print("查找失败 失败原因为%s" %result['error_msg'])
    else:
        print("查找成功 成功率为 %d" %result['result'][0]['score'])

def update_to_database(filepath,tags,target,numbers):
    image = get_file_content(filepath)
    options = {}
    options['brief'] = "{\"name\":\"%s\", \"id\":\"%s\"}" %(target,numbers)
    options['tags'] = "%s" %tags
    result = clinet.similarUpdate(image,options)
    if 'error_msg' not in result.keys():
        print("更新成功 logid为：%s" %result['log_id'])


    #contSign = "8cnn32frvrr2cd901"
    #clinet.similarUpdateContSign(contSign)

def delete_on_database(filepath):
    image = get_file_content(filepath)
    result = clinet.similarDeleteByImage(image)
    if 'error_msg' in result.keys():
        print("删除失败 失败原因为 %s" %result['error'])
    else:
        print('删除成功 logid为 %s' %result['log_id'])


#search_on_database('1.jpg','102,22')
#insert_to_database('1.jpg',"102,22","manguo",'002')
#update_to_database('1.jpg','102,12',"damangguo","003")
#delete_on_database('1.jpg')