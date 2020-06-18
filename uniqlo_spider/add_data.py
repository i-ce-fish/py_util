# -*- coding:utf-8 -*-
import math
import random

import pandas as pd
import requests
import json
import time
import datetime
from uniqlo_spider.main import get_json, get_all_pro_code, get_pro_by_code

token = ''
server = 'http://shop.cdb99.com:8088/'

header = {
    'Content-Type': 'application/json',
    # 'Accept-Encoding':'gzip, deflate'
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTE1ODM2NjgsIm5iZiI6MTU5MTU4MzY2OCwianRpIjoiMTU0NDY3NTQtNzBmMy00N2NiLTk3ZTAtNzIyZmI5ODk1MzZiIiwiZXhwIjoxNTkyNDQ3NjY4LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.pXm-SPvY7-xD4ja9L-haaEzVeAQTihZ8_GP5XS-Cubc'
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    # 'Connection': 'keep-alive',
    # 'accept-encoding': 'accept-encoding',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'cache-control': 'max-age=0',
    # 'upgrade-insecure-requests': '1',
    # 'cookie': cookie
}


# 获取token
def set_token():
    res = requests.post(server + "/api/auth/login", data={'username': 'maxazure', 'password': 'test'})
    data = json.loads(str(res.content, encoding="utf-8"))
    token = 'Bearer ' + data['data']['token']
    header['Authorization'] = token


# 封装添加接口
def add(url, data):
    data_ = json.dumps(data)
    res = requests.post(server + '/api/' + url, headers=header, data=data_)
    try:
        res = json.loads(str(res.content, encoding="utf-8"))
        if res['code'] != 200:
            print(res)
            print(res['code'] + res['data'])
    except:
        print(res)
        print(res.content)
    print(url + "添加成功")
    return res


# 封装获取接口
# def get(url):
#     res = requests.get(server + '/api/' + url, headers=header)
#     try:
#         res = json.loads(str(res.content, encoding="utf-8"))
#     except:
#         print(res)
#         print(res.content)
#     print(url + "获取成功")
#     return res

# 删除接口
def del_(url, id):
    res = requests.delete(server + '/api/' + url + '/' + id, headers=header)
    try:
        res = json.loads(str(res.content, encoding="utf-8"))
    except:
        print(res)
        print(res.content)
    print(url + id + "删除成功")
    return res


# 读取excel，添加商品到数据库
# 添加商品=> product_id 添加颜色=> color_id 添加尺码
def add_product_by_excel():
    df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    row_size = df.shape[0]
    data = df.head(row_size)
    data_dict = data.to_dict()
    cols = df.columns.values

    product_data = {}
    for row in range(row_size):
        # set data
        for col in cols:
            product_data[col] = data_dict[col][row]
            # if(col=='carousels'):
            #     list = []
            #     for img in data_dict[col][row]:
            #         list.append({'uid': time.time(),'url':img})
            #     product_data[col]=list

        res = add('goods', product_data)
        product_id = res['data']['id']
        colors = json.loads(data_dict['colors'][row])
        sizes = json.loads(data_dict['sizes'][row])
        res_colors = []
        for color in colors:
            color['good_id'] = product_id
            res = add('goodcolors', color)
            res_colors.append(res['data'])

        for size in sizes:

            # 查找color_id
            for color in res_colors:
                if color['color_name'] == size['styleText']:
                    size['color_id'] = color['id']
            size['good_id'] = product_id
            size['inventory'] = random.randint(0, 99)
            add('goodsizes', size)
    print('添加完成')


# 获取优衣库分类json
def get_categories():
    res = get_json('https://www.uniqlo.cn/data/cms-config.json')
    return res['categories']


# 读取优衣库分类json文件
def get_categories_by_file():
    """"读取配置"""
    with open("cms-config.json", encoding='utf-8') as json_file:
        config = json.load(json_file)
    return config['categories']


# 添加优衣库的商品分类，递归，
def add_category(categories, parent_id='0'):
    # if()
    print(categories['name'])
    categories['parent_id'] = parent_id
    if 'categories' in categories:
        res = add('categories', categories)
        for category in categories['categories']:
            add_category(category, res['data']['id'])
    else:
        add('categories', categories)


# 删除范围内id 的商品
def del_all_data(url):
    # for i in range(500):
    for i in range(100, 400):
        del_(url, str(i))


# 添加多个分类
def add_categories():
    data = get_categories_by_file()
    for category in data:
        add_category(category)


# 添加文章栏目和文章内容
def add_catalogs_and_articles():
    list = [
        {'catalog_name': '本周推荐', 'description': '本周推荐简介'},
        {'catalog_name': '人气商品', 'description': '人气商品简介'},
        {'catalog_name': '潮流精选', 'description': '潮流精选简介'},
        {'catalog_name': '穿搭推荐', 'description': '穿搭推荐简介'}
    ]
    for i in list:
        res = add('catalogs', i)
        catalog_id = res['data']['id']
        add_articles(catalog_id)


# 通过优衣库接口，添加文章（栏目id，文章数量）
def add_articles(catalog_id, num=8):
    pro_list = get_all_pro_code()
    for pro in range(num):
        randomProduct = pro_list[random.randint(0, len(pro_list) - 1)]
        product = get_pro_by_code(randomProduct['productCode'])
        data = {}
        if 'description' in product['desc'] and 'detailsPic' in product['desc']['description']:
            content = product['desc']['instruction'] + product['desc']['description']['detailsPic']
            data['title'] = product['summary']['fullName']
            data['body'] = content
            data['author'] = "crawler"
            data['catalog_id'] = catalog_id
            # data['front_pic'] = content
            data['is_col_header'] = True
            data['is_header'] = True
            add('articles', data)


# 下载articles 保存为excel文件
def get_articles_excel():
    pro_list = get_all_pro_code()
    excel_list = []
    for pro in range(50):
        randomProduct = pro_list[random.randint(0, len(pro_list) - 1)]
        product = get_pro_by_code(randomProduct['productCode'])
        data = {}
        if 'description' in product['desc'] and 'detailsPic' in product['desc']['description']:
            content = product['desc']['instruction'] + product['desc']['description']['detailsPic']
            # data['title'] = product['summary']['fullName']
            data['title'] = '文章标题' + product['summary']['listYearSeason'] + product['summary']['code']
            data['body'] = content
            data['author'] = "crawler"
            data['catalog_id'] = ''
            # data['front_pic'] = content
            data['is_col_header'] = True
            data['is_header'] = True
            # add('articles', data)
            excel_list.append(data)
    df = pd.DataFrame(excel_list)
    df.to_excel('articles.xlsx', index=False)


# 添加4个栏目50个文章
def add_catalog_and_articels_by_excel():
    list = [
        {'catalog_name': '本周推荐', 'description': '本周推荐简介'},
        {'catalog_name': '人气商品', 'description': '人气商品简介'},
        {'catalog_name': '潮流精选', 'description': '潮流精选简介'},
        {'catalog_name': '穿搭推荐', 'description': '穿搭推荐简介'}
    ]
    articles = get_excel_list('articles.xlsx')
    for i in range(len(list)):
        res = add('catalogs', list[i])
        catalog_id = res['data']['id']
        # 分割数组，等分成len(list)份
        list_ = list_split(articles,len(list))
        articles_ = list_[i]
        for j in articles_:
            j['catalog_id'] = catalog_id
            add('articles',j)
# 添加4个种类60个关联产品
def add_category_and_products_by_excel():
    list = [
        {'name': '男装', 'sort': '1'},
        {'name': '女装', 'sort': '2'},
        {'name': '婴幼儿', 'sort': '3'},
        {'name': '童装', 'sort': '4'}
    ]
    goods = get_excel_list('goods.xlsx')
    for i in range(len(list)):
        res = add('categories', list[i])
        catalog_id = res['data']['id']
        # 分割数组，等分成len(list)份
        split = list_split(goods, len(list))
        articles_ = split[i]
        for j in articles_:
            j['category_id'] = catalog_id
            add('goods',j)


# 通过读取excel，将数据添加到数据库，excel文件中的sheetName = api地址，
def add_other_data_by_excel(filename,table):
    df = pd.read_excel(filename, sheet_name=table)
    row_size = df.shape[0]
    data_dict = df.head(row_size).to_dict()
    cols = df.columns.values

    product_data = {}
    for row in range(row_size):
        # set data
        for col in cols:
            product_data[col] = data_dict[col][row]
        add(table, product_data)
    print('添加完成')

# 获取excel文件中的 list[{}]
def get_excel_list(filename,table='Sheet1'):
    df = pd.read_excel(filename, sheet_name=table)
    row_size = df.shape[0]
    data_dict = df.head(row_size).to_dict()
    cols = df.columns.values
    result = []

    for row in range(row_size):
        # set data
        product_data = {}
        for col in cols:
            product_data[col] = data_dict[col][row]
        result.append(product_data)
    return result

# 分割数组
def list_split(items, n):
    # return [items[i:i+n] for i in range(0, len(items), n)]
    result=[]
    for i in range(n):
        result.append(items[math.floor(i / n * len(items)):math.floor((i + 1) / n * len(items))])
    return result

if __name__ == '__main__':
    set_token()
    # del_all_data('')

    # add_categories()
    # add_product_by_excel()
    # add_other_data_by_excel('other_data.xlsx','customers')
    add_catalog_and_articels_by_excel()
    # add_category_and_products_by_excel()
