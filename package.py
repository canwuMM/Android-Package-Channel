# !/usr/bin/env python
# -*- coding:utf-8 -*-
import zipfile,sys,shutil,os,datetime

def hasChinese(str):
    hasChinese = False
    for c in str.decode('utf-8'):
        if u'\u4e00' <= c <= u'\u9fff':
            hasChinese = True
    return hasChinese

def packageWithChannel(fileName, channelName):
    CHANNEL_PREFIX = "channel"

    tempFile = fileName + "___tem"
    shutil.copy(fileName, tempFile)
    
    empty_file_name = CHANNEL_PREFIX + '_' + channelName
    empty = file(empty_file_name, 'w')

    zipped = zipfile.ZipFile(tempFile, 'a', zipfile.ZIP_DEFLATED) 
    file_path = "META-INF/" + empty_file_name

    zipped.write(empty_file_name, file_path)
    zipped.close()
    empty.close()

    targetFile = fileName.replace(".apk", "_" + channelName) + ".apk"
    shutil.move(tempFile, targetFile)
    # delete unuse file
    if os.path.exists(empty_file_name):
        os.remove(empty_file_name)

    print u'渠道名称:' + channelName
    print  u'生成文件:' + targetFile

if len(sys.argv) < 3 :
    print "parameter error"
    sys.exit()

if sys.argv[1].endswith('.apk') != True:
	print "First parameter must be apk file !"
	sys.exit()

if os.path.isfile(sys.argv[1]) != True:
	print sys.argv[1] + " not exist !"
	sys.exit()

start = datetime.datetime.now()
position = 0;

if os.path.isfile(sys.argv[2]):
	f = open(sys.argv[2], 'r')
	for line in f.readlines(): 
	    line=line.strip('\n').strip()
	    if line and not hasChinese(line) and not line.startswith('//'):
	            packageWithChannel(sys.argv[1], line)
	            position += 1
else:
	packageWithChannel(sys.argv[1], sys.argv[2])
	position += 1
end  = datetime.datetime.now()
use_time = "{:.2f}".format((end-start).microseconds / 1000000.0)
desc = use_time + u'秒生成渠道包' + '%d'%position + u'个'
print desc