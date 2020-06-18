# source_file:源路径, target_ir:目标路径
import os
import codecs
import shutil
from code_generater.lib.util import mkdir


# 复制文件夹内所有文件
def copy_files(source_dir, target_dir):
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)
        if os.path.isfile(source_file):
            shutil.copy(source_file, target_dir)

        if os.path.isdir(source_file):
            mkdir(target_dir + '/' + file)
            new_dir = target_dir + '/' + file
            copy_files(source_file, new_dir)


# 替换文件夹下所有文件的字符串
def replace(target_dir, old_str, new_str):
    for file in os.listdir(target_dir):

        source_file = os.path.join(target_dir, file);
        if os.path.isfile(source_file):
            # 编码问题
            # f = open(dir_entry_path,'r')
            old_file = codecs.open(source_file, 'r', encoding=u'utf-8', errors='ignore')
            file_content = old_file.read().replace(old_str, new_str)
            old_file.close()
            # t = open(source_file, 'w')
            new_file = codecs.open(source_file, 'w', encoding=u'utf-8', errors='ignore')
            new_file.write(file_content)
            new_file.close()

        if os.path.isdir(source_file):
            new_dir = target_dir + '/' + file
            replace(new_dir, old_str, new_dir)

# 创建项目文件夹
def main(source_dir, target_dir, old_str, new_str):
    target_dir = target_dir + '/' + new_str
    mkdir(target_dir)

    copy_files(source_dir, target_dir)

    replace(target_dir, old_str, new_str)


if __name__ == '__main__':
    source_dir = 'D:/vue/git/项目模板/cms'
    target_dir = 'd:/Users/binyu/Desktop/test/target1'
    new_str = "test5"

    main(source_dir, target_dir, 'cms', new_str)
