###################### 4.1 文件基础 #############################

#4.1.1 基础概念

'''
1、文件是存储在磁盘的数据集合，如文本、视频、音频、图像、代码等

2、文件通过文件名和路径来定位管理，文件通常包含文件的扩展名

3、文件路径可以是相对路径和绝对路径
相对路径：./heel.py
绝对路径：E:/aa/hel.py

4、文件分类
纯文本：有统一的编码，可以看作是存储在磁盘的长字符串，格式有 ascii、utf-8、gbk、gb2312等
二进制文件：没有统一的编码，直接由0和1组成，如图片和视频等
'''


#4.1.2 文件的打开和关闭
'''
1、打开和关闭文件
f = open('aaa.txt','w')
f.write('hello world\n')
f.write('my name is python\n')
f.close()

'''

#4.1.2 读写数据
'''
1、写入数据

f = open('aaa.txt','w')
f.write('hello world\n')
f.write('my name is python\n')
f.close()

2、读数据
1)read([]) 可以从文件中读数据，size表示从中读取文件的长度，单位是字节，如果么有传入的size则读取文件中所有的数据
f = open('./aaa.txt','rt')
print(f.read())
f.close()

2)readline([size]) ：可以冲文件中读取整行的数据，返回列表，也可以通过size设置读取数据的长度
f = open('./aaa.txt','rt')
#print(f.readline(3))
print(f.readlines())
f.close()
'''
