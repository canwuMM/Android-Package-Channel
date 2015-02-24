# !/usr/bin/env python
# encoding:utf-8
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
    
    empty = file("empty_file", 'w')

    zipped = zipfile.ZipFile(tempFile, 'a', zipfile.ZIP_DEFLATED) 
    file_path = "META-INF/" + CHANNEL_PREFIX + "_{channel}"
    empty_channel_file = file_path.format(channel = channelName)

    zipped.write("empty_file", empty_channel_file)

    zipped.close()

    os.remove('empty_file')

    targetFile = fileName.replace(".apk", "-" + channelName) + ".apk"
    shutil.move(tempFile, targetFile)
    print "渠道名称: " + channelName
    print "生成文件: " + targetFile

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

f = open(sys.argv[2], 'r')
for line in f.readlines(): 
    line=line.strip('\n').strip()
    if line and not hasChinese(line) and not line.startswith('//'):
            packageWithChannel(sys.argv[1], line)
            position += 1
end  = datetime.datetime.now()
print '%s秒生成渠道包%s个' % ("{:.2f}".format((end-start).microseconds / 1000000.0), position)