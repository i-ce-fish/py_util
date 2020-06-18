from jinja2 import Template

from code_generater.lib.util import (read_file, write_file, mkdir, find_in_list,
                       find_all_in_list, get_all_fields_by, replace_all_tag, generate_model_db_fields, generate_routers,
                       generate_post_parser_fields, generate_update_parser_fields, generate_query_parser_fields,
                       generate_conditisons, generate_update_all_fields_method, generate_output_fields,
                       generate_sortable_fields, generate_test)
import os, codecs, json, sys, shutil

# env = Environment(extensions=['jinja2.ext.loopcontrols'])

json_file = ''
model_name = ''
keep_dirs = False


if(len(sys.argv)==3):
    json_file = str(sys.argv[1])
    model_name = str(sys.argv[2])
elif(len(sys.argv)==4):
    json_file = str(sys.argv[1])
    model_name = str(sys.argv[2])
    if(str(sys.argv[3])=='keep'):
        keep_dirs = True
    else:
        print('参数错误,请检查参数.例如:')
        print('run.py d:\\code_generator\\json\\yunxiang.json model_name keep')
        exit()
else:
    print('参数错误,请检查参数.例如:')
    print('run.py C:\\Users\\maxaz\\OneDrive\\code_generator\\json\\yunxiang.json model_name')
    exit()

# TODO 1 (scaffold) 需要生成基础框架 主程序 util.py router.py requirements.txt
# TODO 2 (auth)生成用户模块 用户管理api 登录 注册 找回密码 api

base_path = os.path.abspath(os.path.dirname(__file__))
jsonstr = read_file(json_file)

# 1. 读取模板
# resource_tpl = read_file("d:/Users/binyu/Desktop/test/target1/test.txt".format(base_path))
# model_tpl = read_file("d:/Users/binyu/Desktop/test/target1/test.txt".format(base_path))
# helper_tpl = read_file("d:/Users/binyu/Desktop/test/target1/test.txt".format(base_path))
# routers_tpl = read_file("d:/Users/binyu/Desktop/test/target1/test.txt".format(base_path))
# routers_tpl = read_file("{}/vue_templates/test.html".format(base_path))

#  vue  模板
vue_api_tpl=read_file('./templates/api.js'.format(base_path))
vue_router_tpl=read_file('./templates/router.js'.format(base_path))
vue_index_tpl=read_file('./templates/index.vue'.format(base_path))
vue_add_tpl=read_file('./templates/add.vue'.format(base_path))
vue_edit_tpl=read_file('./templates/edit.vue'.format(base_path))
vue_router_index_tpl=read_file('./templates/router_index.js'.format(base_path))


data_list = json.loads(jsonstr)

# model = find_in_list(data_list, 'ModelNameSingular','catalog')
model = find_in_list(data_list, 'ModelNameSingular',model_name)
# print(resource_tpl)

model_dict = {}
# 替换model 里的 数据库字段
# 2. 定义模板中替换变量 变量名为 xxxx的话  方法就是 generate_xxxx
model_dict['output_fields'] = generate_output_fields(model['Fields'])

model_dict['db_fields'] = generate_model_db_fields(model['Fields'])

model_dict['post_parser_fields'] = generate_post_parser_fields(model['Fields'])

model_dict['update_parser_fields'] = generate_update_parser_fields(model['Fields'])

model_dict['query_parser_fields'] = generate_query_parser_fields(model['Fields'])

model_dict['conditisons'] = generate_conditisons(model['Fields'])

model_dict['update_all_fields_method'] = generate_update_all_fields_method(model['Fields'])
model_dict['sortable_fields'] =generate_sortable_fields(model['Fields'])
routers_str = generate_routers(data_list)


# vue

# 模块名
model_dict['ModelNameSingular'] =model.get('ModelNameSingular')
# 模块名复数
model_dict['ModelNamePlural'] =model.get('ModelNamePlural')
# 模块中文名
model_dict['ModuleNameCn'] = model.get('ModuleNameCn')
# 字段列表
model_dict['Fields'] = model.get('Fields')

# 替换 helper里的字段

# 3. 建立模板对象
# model_template = Template(model_tpl)
# helper_template = Template(helper_tpl)
# routers_template = Template(routers_tpl)


# vue
# 配置循环控制的拓展
env = ['jinja2.ext.loopcontrols']

vue_api_template = Template(vue_api_tpl, extensions = env)
vue_router_template = Template(vue_router_tpl, extensions = env)
vue_index_template = Template(vue_index_tpl, extensions = env)
vue_add_template = Template(vue_add_tpl, extensions = env)
vue_edit_template = Template(vue_edit_tpl, extensions = env)
vue_router_index_template = Template(vue_router_index_tpl,extensions = env)

# 3. 渲染模板
# model_res = model_template.render(model_dict)
# helper_res = helper_template.render(model_dict)
# routers_res = routers_template.render({'routers': routers_str})

# vue
vue_api_res = vue_api_template.render(model_dict)
vue_router_res = vue_router_template.render(model_dict)

vue_index_res = vue_index_template.render(model_dict)
vue_add_res = vue_add_template.render(model_dict)
vue_edit_res = vue_edit_template.render(model_dict)
vue_router_index_res = vue_router_index_template.render(model_dict)


# 4. 替换模板中的特殊字符 例如对象名 表名
# model_res = replace_all_tag(model, 'category', 'categories', 'category', model_res)
# helper_res = replace_all_tag(model, 'category', 'categories', 'category', helper_res)
# resource_res = replace_all_tag(model, 'category', 'categories', 'category', resource_tpl)

# 5. 输出到特定目录
out_path = '{}\\..\\output'.format(base_path)

# output_helper = "{}/helpers/examples_resource_helper.py".format(out_path).replace('examples',model.get('ModelNamePlural'))
# output_model = "{}/models/example.py".format(out_path).replace('example',model.get('ModelNameSingular'))
# output_resource = "{}/resourses/examples_resource.py".format(out_path).replace('examples',model.get('ModelNamePlural'))
# if(not keep_dirs):
#     shutil.rmtree(out_path,True)
# os.makedirs(out_path + '\\helpers',exist_ok=True)
# os.makedirs(out_path + '\\models', exist_ok=True)
# os.makedirs(out_path + '\\resourses', exist_ok=True)
# print(base_path)


# vue

# todo python模板字符串

output_vue_api  = "{}/api/examples.js".format(out_path).replace('examples',model.get('ModelNameSingular'))
output_vue_router  = "{}/router/modules/examples.js".format(out_path).replace('examples',model.get('ModelNameSingular'))
output_vue_router_index  = "{}/router/router_index.js".format(out_path).replace('examples',model.get('ModelNameSingular'))
output_vue_index  = "{}/views/examples/index.vue".format(out_path).replace('examples',model.get('ModelNameSingular'))
output_vue_add  = "{}/views/examples/add.vue".format(out_path).replace('examples',model.get('ModelNameSingular'))
output_vue_edit  = "{}/views/examples/edit.vue".format(out_path).replace('examples',model.get('ModelNameSingular'))


os.makedirs(out_path + '/api',exist_ok=True)
os.makedirs(out_path + '/views/examples'.format(out_path).replace('examples',model.get('ModelNameSingular')),exist_ok=True)
os.makedirs(out_path + '/router/modules'.format(out_path).replace('examples',model.get('ModelNameSingular')),exist_ok=True)

# 6. 输出
# write_file(helper_res, output_helper)
# print(output_helper)
#
# write_file(model_res, output_model)
# print(output_model)
#
# write_file(resource_res, output_resource)
# print(output_resource)
#
# write_file(routers_res,out_path + '/routers.py')
# print(out_path+ '/routers.py')


# vue
write_file(vue_api_res,output_vue_api)
write_file(vue_router_res,output_vue_router)
write_file(vue_index_res,output_vue_index)
write_file(vue_add_res,output_vue_add)
write_file(vue_edit_res,output_vue_edit)
write_file(vue_router_index_res,output_vue_router_index)


print(output_vue_api)
print(output_vue_router)
print(output_vue_router_index)
print(output_vue_index)
print(output_vue_add)
print(output_vue_edit)


if(len(sys.argv)==3):
    os.system('start explorer {}'.format(out_path))

