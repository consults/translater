import os
import sys
import time
import requests
from lxml import etree
import argparse
import re

# error_file
error_files = []
# 成功个数
success_num = 0

parse = argparse.ArgumentParser(description='批量翻译文件名称工具')
parse.add_argument('-n', '--name', required=True, help='翻译目录')


def get_file_list(dir_path):
    files = []
    for i in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, i)):
            files.append(i)
    os.chdir(dir_path)
    return files


def is_chinese(files):
    results = []
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
    # zhmodel = re.compile(u'[^\u4e00-\u9fa5]')  #检查非中文
    for file in files:
        match = zhmodel.search(file)
        if match:
            print('{} 是中文不用翻译了'.format(file))
        else:
            results.append(file)
    return results


def translate_handle(files):
    for i in files:
        try:
            title = os.path.splitext(i)[0]
            title_fix = os.path.splitext(i)[1]
            youdao_url = 'http://m.youdao.com/translate'
            result = requests.post(url=youdao_url, data={'inputtext': title, "type": "AUTO"})
            html_element = etree.HTML(result.text)
            title = html_element.xpath('//*[@id="translateResult"]/li/text()')[0]
            os.rename(i, title + title_fix)
            print('修改文件：{}-----成功'.format(i))
            global success_num
            success_num += 1
            time.sleep(1)
        except Exception as e:
            print('{}修改失败 : {}'.format(i, e))
            global error_files
            error_files.append(i)
    os.chdir('..')


def get_dir_path(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    if not os.path.isdir(dir_path):
        raise OSError('目录不正确')
    return dir_path


def main():
    args = parse.parse_args()
    if args.name == ".":
        all_dir = os.listdir()
        for dir in all_dir:
            dir_path = get_dir_path(dir)
            files = get_file_list(dir_path)
            files = is_chinese(files)
            translate_handle(files)
    else:
        dir_path = get_dir_path(args.name)
        files = get_file_list(dir_path)
        files = is_chinese(files)
        translate_handle(files)
    print('成功个数：{}'.format(success_num))
    print('失败文件：{}'.format(error_files))
    sys.exit()


if __name__ == '__main__':
    main()
