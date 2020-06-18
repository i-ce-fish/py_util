
import codecs
import os

def read_file(filename):
    data = open(filename, 'r', encoding='utf-8').read()
    return data

def write_file(str, filename):
    with open(filename,'w', encoding='utf-8') as f:
        f.write(str)

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

def find_in_list(mlist,key_name, v):
    for item in mlist:
        if(item.get(key_name) == v):
            return item
# 取出list中的所有dict 并且这些dict中有一个key name 等于 V
def find_all_in_list(mlist, key_name, v):
    res = list()
    for item in mlist:
        if(item.get(key_name) == v):
            res.append(item)
    return res

#取出list中dict里的字段名，并且该dict某个bool字段为 True
# 用于做 sortable 字段的
def get_all_fields_by(mlist, bool_field_name, retrieved_field):
    mlist = list()
    for item in mlist:
        if(item.get(bool_field_name)):
            mlist.append(item.get(retrieved_field))
    return mlist

def replace_all_tag(field_list, singular, plural, tablename, tpl_str):
    return tpl_str.replace(plural, field_list.get('ModelNamePlural'))\
        .replace(singular.capitalize(), field_list.get('ModelNameSingular').capitalize())\
        .replace(singular, field_list.get('ModelNameSingular'))\
        .replace(plural.capitalize(), field_list.get('ModelNamePlural').capitalize())\
        .replace(tablename, field_list.get('TableName'))


#------------------generate_model_db_fields-------start------#
def convert_to_output_type(typestr):

    switch = typestr.split('(')[0]
    type_list = {
        'String': 'String',
        'Text': 'String',
        'Boolean': 'Boolean',
        'Integer': 'Integer',
        'Float': 'String',
        'DECIMAL': 'String',
        'Enum': 'String',
        'Date': 'String',
        'DateTime': 'String',
        'relationship': 'String',
    }

    return type_list[switch]

def digtal_for_fieldsize(size):
    return '' if(size == 0) else str(size)

def is_required(isRequied):
    if(isRequied):
        return ', nullable=False'
    else:
        return ''

def is_unique(isUnique):
    if(isUnique):
        return ', unique=True'
    else:
        return ''

def generate_model_db_fields(field_list):
    res = ""
    for item in field_list:
        res += '    {} = db.Column(db.{}{}{})\n'.format(item.get('FieldNameEn'),
                        item.get('FieldType'), is_required(item.get('IsRequired')), is_unique(item.get('IsUnique')))
    return res
#------------------generate_model_db_fields-------end------#

def generate_output_fields(field_list):
    res = ""

    for item in field_list:
        if(item.get('IsOutput')):
            res += '    \'{}\': fields.{},\n'.format(item.get('FieldNameEn'), convert_to_output_type(item.get('FieldType')))
    return res

def generate_post_parser_fields(field_list):
    res = ""
    for item in field_list:
        res += 'category_post_parser.add_argument(\'{}\', type={}, {})\n'.format(item.get('FieldNameEn'),
            item.get('ParameterType'), item.get('ParameterDefault'))
    return res

def generate_update_parser_fields(field_list):
    res = ""
    for item in field_list:
        if(item.get('Editable')):
            res += 'category_update_parser.add_argument(\'{}\', type={})\n'.format(item.get('FieldNameEn'),
            item.get('ParameterType'))
    return res

def generate_query_parser_fields(field_list):
    res = ""
    for item in field_list:
        if(item.get('Searchable')):
            res += 'category_query_parser.add_argument(\'{}\', type={})\n'.format(item.get('FieldNameEn'),
            item.get('ParameterType'))
    return res
# --------------------辅助方法-------------------------------
def convert_searchable(searchCondition, field):
    arg = 'args[\'{}\']'.format(field)
    items ={
        '==': '{}=={}'.format(field, arg),
        '<': '{}<{}'.format(field, arg),
        '>': '{}>{}'.format(field, arg),
        '>=': '{}>={}'.format(field, arg),
        '<=': '{}<={}'.format(field, arg),
        'in': '{}.in({})'.format(field, arg),
        'like': '{}.like(\'%\'+{}+\'%\')'.format(field, arg)
    }
    return items[searchCondition]

# --------------------辅助方法-------------------------------

def generate_conditisons(field_list):
    res = ""
    for item in field_list:
        if(item.get('Searchable')):
            res += '    if args[\'{}\'] is not None:\n'.format(item.get('FieldNameEn'))
            res += '        conditions.append(Category.{})\n'.format(convert_searchable(item.get('SearchCondition'),
                            item.get('FieldNameEn') ))
    return res


def generate_update_all_fields_method(field_list):
    res = ""
    for item in field_list:
        if(item.get('Editable')):
            res += '    if args[\'{}\']:\n'.format(item.get('FieldNameEn'))
            res += '        o.{} = args[\'{}\']\n'.format( item.get('FieldNameEn'),
                            item.get('FieldNameEn') )
    return res

def generate_sortable_fields(field_list):
    res = ""
    for item in field_list:
        if(item.get('Orderable')):
            res += '\''+item.get('FieldNameEn')+'\', '
    return res

def generate_routers(mlist):
    res = ""
    for item in mlist:
        res += 'from resourses.{}_resource import {}Resource\n'.format(item.get('ModelNamePlural'),item.get('ModelNamePlural').capitalize())
        res += 'api.add_resource({}Resource, \'/{}\', \'/{}/<int:{}_id>\')\n\n'.format(item.get('ModelNamePlural').capitalize(),item.get('ModelNamePlural'), item.get('ModelNamePlural'), item.get('ModelNameSingular'))
    return res



def generate_test(mlist):
    res = ""
    for item in mlist:
        res = item.get('FieldNameCn')
        # print(item)
    return res

