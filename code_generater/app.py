from jinja2 import Template
import os, codecs, json, sys, shutil
import importlib
from code_generater.lib.util import read_file

json_file = ''
model_name = ''
module_name = ''
keep_dirs = False

if (len(sys.argv) == 4):
    module_name = str(sys.argv[1])
    json_file = str(sys.argv[2])
    model_name = str(sys.argv[3])
elif (len(sys.argv) == 5):
    module_name = str(sys.argv[1])
    json_file = str(sys.argv[2])
    model_name = str(sys.argv[3])
    if (str(sys.argv[3]) == 'keep'):
        keep_dirs = True
    else:
        print('参数错误,请检查参数.例如:')
        print(
            'run.py gmodel d:\\code_generator\\json\\yunxiang.json model_name keep'
        )
        exit()
else:
    print('参数错误,请检查参数.例如:')
    print(
        'run.py gmodel C:\\Users\\maxaz\\OneDrive\\code_generator\\json\\yunxiang.json model_name'
    )
    exit()

base_path = os.path.abspath(os.path.dirname(__file__))
jsonstr = read_file(json_file)
out_path = '{}\\..\\output'.format(base_path)

if (model_name != ''):
    module = importlib.import_module('plugins.{}'.format(module_name))
    module.run(base_path, jsonstr, keep_dirs, out_path, model_name)
