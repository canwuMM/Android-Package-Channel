## 目的
把Android多渠道打包时间缩短到一分钟内
## 实现原理

因为Android在安装apk时，不对META-INF文件夹的文件经行签名校验，

所以可以在这个文件夹随添加/修改相关文件作为渠道标识

详解请参看[美团技术博客](http://tech.meituan.com/mt-apk-packaging.html)

## 示例
新建渠道列表文件，每行一个，在终端中如下使用python脚本

	python pakckage.py ***.apk 渠道列表文件名
	
![screenshot](https://github.com/s1rius/Android-Package-Channel/blob/master/screenshot.png)