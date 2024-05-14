#coding:utf-8
import os
import subprocess
import glob
import time

IDA_PATH = "D:\\Downloads\\Genius-master\\Genius-master\\raw-feature-extractor_py3_ida7.7\\IDA_Pro_7.7\\ida64.exe"
PLUGIN_PATH = "D:\\Downloads\\Genius-master\\Genius-master\\raw-feature-extractor_py3_ida7.7\\preprocessing_ida.py"  #必须绝对路径

# 获取所有需要分析的二进制文件路径
ELF_PATH = "D:\\Downloads\\Genius-master\\Genius-master\\raw-feature-extractor_py3_ida7.7\\data\\glibc"
print(ELF_PATH)
DST_path = "D:\\Downloads\\Genius-master\\Genius-master\\raw-feature-extractor_py3_ida7.7\\extract"


#Get all the compiled files(.o) in the data folder
def file_search(data_path):
    file_list = []
    for home, dirs, files in os.walk(data_path):
        for f in files:
            if f.endswith('.o'):
                file_list.append(os.path.join(home,f))
            else:
                pass
    return file_list

if __name__ == '__main__':
    core_num = 2  ##并行的个数，或者电脑有几个核心
    start = 0
    file_list = file_search(ELF_PATH)
    for elf in file_list:
        print(elf)
        cmd = IDA_PATH + " -c -S" + PLUGIN_PATH + " " + elf
        print(cmd)
        if start >= core_num:
            finish = len(os.listdir(DST_path))
            while start-core_num >= finish:
                time.sleep(5)
                finish = len(os.listdir(DST_path))
                print(start, finish)

        subprocess.Popen(cmd)
        start += 1

