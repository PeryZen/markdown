记录一下自己所需的Markdown技巧

## 目录
- [插入图片](#10)

<h2 id="1">插入图片</h2>
### 语法
```![desc](url)``` === ```<img alt="desc" src="url">```

Markdown是纯文本编辑的，无法像富文本那样直接引用图片，只能引用图片的URL（本地图片URL，网络图片URL），例如：

* 本地图片
```
// Markdown
![复仇者联盟之超人笑笑](/Users/Pery/Pictures/复仇者联盟之超人笑笑.png)

// HTML
<img alt="复仇者联盟之超人笑笑" src="/local/L1VzZXJzL1BlcnkvUGljdHVyZXMvU2NyZWVuc2hvdF8yMDE2LTExLTE3LTE3LTEyLTIzLnBuZw==">
```

* 网络图片
```
// Markdown
![复仇者联盟之超人笑笑](https://github.com/PeryZen/markdown/blob/master/img/%E5%A4%8D%E4%BB%87%E8%80%85%E8%81%94%E7%9B%9F%E4%B9%8B%E8%B6%85%E4%BA%BA%E7%AC%91%E7%AC%91.jpeg)

// HTML
<img alt="复仇者联盟之超人笑笑" src="https://github.com/PeryZen/markdown/blob/master/img/%E5%A4%8D%E4%BB%87%E8%80%85%E8%81%94%E7%9B%9F%E4%B9%8B%E8%B6%85%E4%BA%BA%E7%AC%91%E7%AC%91.jpeg">
```

因此，在Markdown中插入图片，需要提前准备好图片的URL。

### 图床
Markdown文档中只能引用图片的URL，不能直接插入图片文件。
如果需要对外共享Markdown文档，则不能使用本地图片URL，需要使用图床来提供网络图片URL。

现在有很多专业的图床服务提供商，如国内的七牛，极简图床等，他们会提供一些工具来简化图片的管理操作，不过要么需要付费，要么不够稳定。
其实，Github也可以提供类似的图床功能，免费，稳定，速度也快。具体方法如下：  
1，创建一个Github工程，如：  
```
https://github.com/PeryZen/markdown
```

2，上传图片至工程中，则该文件的访问路径即为可用的图片URL，如：
```
https://github.com/PeryZen/markdown/blob/master/img/%E5%A4%8D%E4%BB%87%E8%80%85%E8%81%94%E7%9B%9F%E4%B9%8B%E8%B6%85%E4%BA%BA%E7%AC%91%E7%AC%91.jpeg
```

### 图片插入自动化脚本
要想利用图床生成一个图片URL并插入Markdown的步骤太多，手动过于低效，



