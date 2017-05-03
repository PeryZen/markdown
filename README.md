记录一下自己所需的Markdown技巧和工具

## 目录
- [链接](#9)
- [插入图片](#10)

<h2 id="9">链接</h2>
### 直接链接
直接使用<...>包括URL或Email地址将自动生成链接并直接呈现<>中的内容，如：
```
<http://www.google.com>
<zengpeiyu@gmail.com>
```
<http://www.google.com>  
<zengpeiyu@gmail.com>

### 注解式链接
使用```[注解](URL)```生成的链接会呈现[...]中的内容并生成(...)中描述的链接，如：
```
[Google](http://www.google.com)
[Email](zengpeiyu@gmail.com)
```
[Google](http://www.google.com)  
[Email](zengpeiyu@gmail.com)

<h2 id="10">插入图片</h2>
### 语法
```
// Markdown
![desc](url)

// HTML
<img alt="desc" src="url">
```

Markdown是纯文本编辑的，无法像富文本那样直接引用图片，只能引用图片的URL（本地图片URL，网络图片URL），例如：

* 本地图片
```
// Markdown
![复仇者联盟之超人笑笑](/Users/Pery/Pictures/复仇者联盟之超人笑笑.png)

// HTML
<img alt="复仇者联盟之超人笑笑" src="/Users/Pery/Pictures/复仇者联盟之超人笑笑.png">
```

* 网络图片
```
// Markdown
![复仇者联盟之超人笑笑](https://github.com/PeryZen/MarkdownImages/blob/master/复仇者联盟之超人笑笑.jpeg)

// HTML
<img alt="复仇者联盟之超人笑笑" src="https://github.com/PeryZen/MarkdownImages/blob/master/复仇者联盟之超人笑笑.jpeg">
```

因此，在Markdown中插入图片，需要提前准备好图片的URL。


### 图床
如上所述，Markdown文档中只能引用图片的URL，不能直接插入图片文件。
如果需要对外共享Markdown文档，则不能使用本地图片URL，需要使用图床来提供网络图片URL。

现在有很多专业的图床服务提供商，如国内的七牛，极简图床等，他们会提供一些工具来简化图片的管理操作，不过要么需要付费，要么不够稳定。
其实，Github也可以提供类似的图床功能，免费，稳定，速度也快。具体方法如下：  
1，创建一个Github工程，如：  
```
https://github.com/PeryZen/MarkdownImages
```

2，上传图片至工程中，则该文件的访问路径即为可用的图片URL，如：
```
https://github.com/PeryZen/markdown/blob/master/img/复仇者联盟之超人笑笑.jpeg
```

3，引用图床上的图片URL


### 图片插入自动化脚本
要想利用图床生成一个图片URL并插入Markdown的步骤太多，手动过于低效，可利用脚本来简化操作。  
本人喜欢使用Mac+SublimeText3的环境来编辑Markdown文档，故基于python实现了一个拷贝剪切板图片并生成图片URL的小脚本，并配合Sublime插件来实现了自动插入图片的小工具。

源码：<https://github.com/PeryZen/Markdown/tree/master/InsertImagePlugin>  


