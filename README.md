记录一下自己所需的Markdown技巧和工具

## 目录
<!-- MarkdownTOC -->

- [代码框](#代码框)
- [链接](#链接)
    - [直接链接](#直接链接)
    - [注解式链接](#注解式链接)
    - [页内跳转](#页内跳转)
- [插入图片](#插入图片)
    - [语法](#语法)
    - [图床](#图床)
    - [图片插入自动化脚本](#图片插入自动化脚本)
- [内嵌CSS](#内嵌css)
- [语法注意事项](#语法注意事项)

<!-- /MarkdownTOC -->

<a name="代码框"></a>
## 代码框

* **单行代码框**使用单个或三个符号 **`** 将代码包括起来
~~~
`xxx` 或 ```xxx```
~~~

* **多行代码框**使用三个符号 **`** 或 **~** 将代码包括起来
~~~
```
xxx
xxx
xxx
```
~~~
或者
```
~~~
xxx
xxx
xxx
~~~
```

* **代码语法高亮**使用代码框标识符紧跟语言名称的方式
```
~~~java
// main function
void main() {

}
~~~
```

* **代码框中输入特殊字符｀** 用两个或三个特殊字符 **｀** 将内容包括起来，需要在代码框中还原显示的特殊字符 **｀** 要与边界符号间有个空格，如下所示：
~~~
``ctrl + ` ``

```ctrl + ` ```
~~~
还有种办法是使用中文的字符**｀**来替代。

<a name="链接"></a>
## 链接

<a name="直接链接"></a>
### 直接链接

直接使用<...>包括URL或Email地址将自动生成链接并直接呈现<>中的内容，如：
```
<http://www.google.com>
<zengpeiyu@gmail.com>
```
<http://www.google.com>  
<zengpeiyu@gmail.com>

<a name="注解式链接"></a>
### 注解式链接

使用```[注解](URL)```生成的链接会呈现[...]中的内容并生成(...)中描述的链接，如：
```
[Google](http://www.google.com)
[Email](zengpeiyu@gmail.com)
```
[Google](http://www.google.com)  
[Email](zengpeiyu@gmail.com)

<a name="页内跳转"></a>
### 页内跳转

同一个Markdown文件里的跳转链接有两种：

1. 同TOC实现的语法  
跳转按钮及按钮描述`[desc](#link)`  
跳转位置`<a name="link"></a>`  

2. 索引语法（这种语法的按钮描述只会是一个小小蓝色数字）  
跳转按钮及按钮描述`[^1]`  
跳转位置`[^1]: `

<a name="插入图片"></a>
## 插入图片

<a name="语法"></a>
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


<a name="图床"></a>
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


<a name="图片插入自动化脚本"></a>
### 图片插入自动化脚本

要想利用图床生成一个图片URL并插入Markdown的步骤太多，手动过于低效，可利用脚本来简化操作。  
本人喜欢使用Mac+SublimeText3的环境来编辑Markdown文档，故基于python实现了一个拷贝剪切板图片并生成图片URL的小脚本，并配合Sublime插件来实现了自动插入图片的小工具。

源码：<https://github.com/PeryZen/Markdown/tree/master/InsertImagePlugin>  

<a name="内嵌css"></a>
## 内嵌CSS

有时候Markdown实现的样式并不能满足需求，但又不是通用样式，只需要针对某一个Markdown文件做处理，这时候可以使用内嵌CSS的模式。

例如：markdown语法生成表格必须带有表头，但有些场景不需要表头，则可使用如下方式来实现
~~~
// 文件头部加入CSS，隐藏表格的表头
<head>
    <style type="text/css">
        th {
            display: none;
        }
    </style>
</head>

// 空表头
|              |              |
|--------------|--------------|  
| row 1, col 1 | row 1, col 2 |  
| row 2, col 1 | row 2, col 2 |  
~~~

<a name="语法注意事项"></a>
## 语法注意事项

1. **在标题上下用空行隔开，除非标题在文档开头。** 有些Markdown解析器（Github）不能识别标题下没有空行的标题格式。
2. **避免在同一个Markdown文件中使用相同的标题名称。** 许多的Markdown解释器会依据标题的内容生成标题的IDs。
3. 
