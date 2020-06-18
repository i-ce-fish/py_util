# -*- coding:utf-8 -*-

import datetime
import os
import re
import time
import urllib
import pandas as pd
import requests
import json
from collections import OrderedDict

baseUrl = 'https://www.uniqlo.cn'

# cookie = 'Hm_lvt_d29ea3c4f4552d0924ac41da7202b6f8=1570086127; XSRF-TOKEN=eyJpdiI6ImpLaDdvK1lyZmR4VHlmYktTTHpITWc9PSIsInZhbHVlIjoiZDRcL3lIVk8rQ2duVzY0RHVPZVg1b0d2VGRRT1JCVGIxVExtclwvOGw2d3F6b3NNcWJ1Y0pcLytZaXY5WklCMlBIayIsIm1hYyI6IjFjMzY0ODdjOTc4OTYwY2I4MmRmNjE1Zjg0ZmU2ZDhmODFkY2Y5ZTg4MjZjNjc0Mzc1ZjdiZTE1ZDEzYmU5NmQifQ%3D%3D; laravel_session=eyJpdiI6IjdnXC9mZ2xMdDFDTnk1MzI2c1FJRG1BPT0iLCJ2YWx1ZSI6IjlMWDBqYXFQaU5IUXk3Q1pjZ09NR2ZFMXFuSnRIZGo5S2tZS0QrKzdpUlNoZVhRTW1rMTRwaG1VcmxGTlFZenYiLCJtYWMiOiJhZDgyNWY0OWM0M2VkODhiNzNhZTU5NGZiMzEwYTdjZGE3NmQyYWI2MWViOGRmZTUxY2M4YTRhNWYzNzc0ODBlIn0%3D; Hm_lpvt_d29ea3c4f4552d0924ac41da7202b6f8=1570087929'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'accept-encoding',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    # 'cookie': cookie
}


# header={
#
#     GET /data/pages/women_outer.html.json HTTP/1.1
# Host: www.uniqlo.cn
# Connection: keep-alive
# sec-ch-ua: "\\Not;A\"Brand";v="99", "Google Chrome";v="85", "Chromium";v="85"
# sec-ch-ua-mobile: ?0
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4164.4 Safari/537.36
# Accept: */*
# Sec-Fetch-Site: same-origin
# Sec-Fetch-Mode: cors
# Sec-Fetch-Dest: empty
# Referer: https://www.uniqlo.cn/women_outer.html
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Cookie: _md_tempid=u859311585037790266; NTKF_T2D_CLIENTID=guest6A2B8471-EB1F-CC1F-E8E5-0B9D554CB43B; _gcl_au=1.1.2055814714.1587629939; _ga=GA1.2.2135817365.1587629940; _gid=GA1.2.35183189.1591582354; _md_tempid3=u207631591591090619; nTalk_CACHE_DATA={uid:kf_9552_ISME9754_guest6A2B8471-EB1F-CC,tid:1591601050802771}; OZ_SI_1761=sTime=1585037792&sIndex=1615; OZ_1U_1761=vid=ve79c1e094d3d0.0&ctime=1591601642&ltime=1591601641; OZ_1Y_1761=erefer=https%3A//open.weibo.cn/oauth2/authorize&eurl=https%3A//h.uniqlo.cn/&etime=1591447479&ctime=1591601642&ltime=1591601641&compid=1761
# If-None-Match: W/"0x8D80929C0781499"
# If-Modified-Since: Fri, 05 Jun 2020 08:23:40 GMT
#    }


def download_page(url):
    return requests.get(url, headers=header).content


def get_json(url):
    json_loads = json.loads(str(download_page(url), encoding="utf-8"))
    print('get' + url + 'success')
    return json_loads


def get_pro_code(url):
    list = []
    json = get_json(url)
    for section in json:
        if (json[section]['component'] == 'ProductGroup'):
            list.extend(json[section]['props']['items'])
    # return list
    return list[:20]


def get_all_pro_code():
    all_pro_code = []
    all_pro_url = ['https://www.uniqlo.cn/data/pages/women_outer.html.json',
                   'https://www.uniqlo.cn/data/pages/kids_top.html.json',
                   'https://www.uniqlo.cn/data/pages/women_jeans.html.json']
    for url in all_pro_url:
        list = get_pro_code(url)
        all_pro_code.extend(list)
    return all_pro_code


def get_pro_by_code(code):
    product_url = 'https://www.uniqlo.cn/data/products/spu/zh_CN/' + code + '.json'
    return get_json(product_url)


def main(self):
    print('START')
    all_catalog = 'https://www.uniqlo.cn/data/cms-config.json'
    data_dic = get_json(all_catalog)

    add_data_url = ''
    for c1 in data_dic['categories']:

        # todo add c1 and get c1 id
        if ('categories' in c1):
            for c2 in c1['categories']:
                # todo add c2 and get c2 id
                # todo get product by c2.code and add product
                code = 'u0000000014439'
                # product_url = 'https://www.uniqlo.cn/data/products/prodInfo/zh_CN/' + code + '.json'
                product_url = 'https://www.uniqlo.cn/data/products/spu/zh_CN/' + code + '.json'

                print(get_json(product_url))


def pro_data_pre(data):
    # result = data['summary']
    result = {}
    product_imgs = get_product_img_by_code(data['summary']['productCode'])


    # 图片太大，只要保留前3张
    # details = product_imgs['mDetailPic']
    # 轮播图数据预处理（适配多图片上传组件）
    carousels = []
    for img in product_imgs['main1000'][:3]:
        carousels.append({'uid': time.time(), 'url': img})
        save_img(get_img_url(img), get_img_name(img), get_img_path(img))

    details = product_imgs['mDetailPic'][:3]
    # save_imgs(carousels)
    save_imgs(details)

    colors = product_imgs['colorList']

    sizes = []
    sizesDict = OrderedDict()
    for item in data['rows']:
        del item['enabledFlag']
        del item['name']
        del item['taxRate']
        item['size_name'] = item['size']
        item['display_name'] = item['sizeText']
        # sizes.setdefault(item['size'], {**item, 'freq':0})['freq'] += 1
        sizesDict.setdefault(item['size'], {**item})

    for size in sizesDict:
        sizes.append(sizesDict[size])

    for color in colors:
        img = color['chipPic']
        color['color_name'] = color['styleText']
        color['color_thumbnail'] = color['chipPic']
        color['colorNo'] = color['colorNo']

        save_img(get_img_url(img), get_img_name(img), get_img_path(img))

    # color_id/good_id/inventory    /size_name
    colors_json = json.dumps(colors, ensure_ascii=False)
    sizes_json = json.dumps(sizes, ensure_ascii=False)
    result['product_name'] = data['summary']['name']
    result['product_sn'] = data['summary']['productCode']
    result['carousels'] = json.dumps(carousels, ensure_ascii=False)
    result['detail'] = json.dumps(details, ensure_ascii=False)
    result['colors'] = colors_json
    result['sizes'] = sizes_json
    result['instruduce'] = data['desc']['instruction']
    temp = 0
    if (data['summary']['sex'] == '女装'):
        temp = 1
    result['gender'] = temp
    result['main_pic'] = carousels[0]
    result['original_price'] = data['summary']['originPrice']
    result['onsale_price'] = data['summary']['originPrice'] * 0.9
    result['vip_price'] = data['summary']['originPrice'] * 0.8
    # result['produt_parameter'] =  data['summary']['productCode']
    result['type_sn'] = data['summary']['groupCode']

    # del result['activeTags']
    # del result['caseFlag']
    # del result['customMadeFlag']
    # del result['deliveryTemplateId']
    # del result['gDept']
    # del result['gDeptValue']
    # del result['groupCode']
    # del result['identity']
    # del result['intenCode']
    # del result['isConcessionalRate']
    # del result['isExpress']
    # del result['isNew']
    # del result['isNoReasonToReturn']
    # del result['isPickup']
    # del result['isShoesOrSocks']
    # del result['isTimeDoptimal']
    # del result['makePantsLengthFlag']
    # del result['minFinalInseam']
    # del result['mobileSubtitleUrl']
    # del result['modelHeight']
    # del result['modelSize']
    # del result['platformUrl']
    # del result['priceColor']
    # del result['subTitlePc']
    # del result['subtitleUrl']
    # del result['weight']

    return result


def get_product_img_by_code(code):
    product_url = 'https://www.uniqlo.cn/data/products/zh_CN/' + code + '.json'
    return get_json(product_url)


def get_img_url(img):
    return baseUrl + img


def get_img_name(img):
    pattern = re.compile(r'^\/(\w|\/)*\/')
    path = re.match(pattern, img, flags=0).group()
    return img.replace(path, '')


def get_img_path(img):
    pattern = re.compile(r'^\/(\w|\/)*\/')
    return 'img' + re.match(pattern, img, flags=0).group()[:-1]


def save_img(img_url, file_name, file_path='\img'):
    pass
    # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 \img文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹', file_path, '不存在，重新建立')
            # os.mkdir(file_path)
            os.makedirs(file_path)
        # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)


def save_imgs(list):
    for img in list:
        save_img(get_img_url(img), get_img_name(img), get_img_path(img))


if __name__ == '__main__':
    excel_list = []
    for code in get_all_pro_code():
        dic1 = pro_data_pre(get_pro_by_code(code['productCode']))
        excel_list.append(dic1)

    df = pd.DataFrame(excel_list)
    df.to_excel('goods.xlsx', index=False)
