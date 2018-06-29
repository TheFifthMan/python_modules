#!/usr/bin/env python
#-*- coding:utf-8 -*-

import shutil 

#shutil.copyfile('D://new_folder2/test2/testsample.txt',"D://new_folder2//testsample.txt")
#shutil.copy('D://new_folder2//test2//testsample.txt',"D://new_folder2//testsample2.txt")
#shutil.copytree('D://new_folder2//test2',"D://new_folder2//test222",copy_function=shutil.copy2)
# shutil.rmtree("D://new_folder2//test222")
# print(shutil.move('D://new_folder2/test2','D://new_folder2/test4'))
# print(shutil.disk_usage('D://'))
# shutil.make_archive("D://new_folder2/test3",'zip','D://new_folder2/test3','D://new_folder2/')
shutil.unpack_archive('D://new_folder2/test3.zip',"D://new_folder2//test1","zip")