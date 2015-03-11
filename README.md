## 目的
把Android多渠道打包时间缩短到一分钟内
## 实现原理

因为Android在安装apk时，不对~/META-INF 文件夹的文件经行签名校验，

所以可以在这个文件夹添加/修改相关文件作为渠道标识，通过ChannelUtil.java类中的方法得到相应的渠道名称，就能做统计分析了。

详解请参看[美团技术博客](http://tech.meituan.com/mt-apk-packaging.html)

## 示例
在终端中使用如下python脚本

对单个渠道打包

	python pakckage.py ***.apk 渠道名

对多个个渠道打包，可以新建渠道列表文件，每行一个渠道名

	python pakckage.py ***.apk 渠道列表文件的文件名
	
![screenshot](https://github.com/s1rius/Android-Package-Channel/blob/master/screenshot.png)