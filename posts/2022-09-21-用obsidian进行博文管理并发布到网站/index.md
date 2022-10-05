# 用Obsidian进行博文管理，并发布到网站


## 用Obsidian管理你的博文<!--more-->
把hugo网页的存放文件夹作为Obsidian（以下简称OB）的库，就可以集中管理content文件夹下的博文.md文档。

不过，如果仅从集中管理.md文件的角度来说，OB并不算特别，用logseq也可以。从书写的角度来说，OB的书写体验也不算突出。

但是我还是认为，OB就是最适合的hugo博文管理工具，主要原因在于OB的quickadd、custom frame和shell commands这三个插件的配合，可以实现在OB中完成博文创建、调试和发布的全流程。

以下我会进行介绍。

<div align=center>
<img src="https://s1.vika.cn/space/2022/09/21/c1d8b7d160e2436aa0b2ad12c4b22e8f" alt="drawing" style="width:100%"/>
</div>

## Quickadd - 创建博文
hugo的博文是以.md文件存在，并且主题的特性依赖于yaml，以我用的LoveIt主题来说，支持的特性就非常多。具体可以参考Loveit主题的介绍[Theme Documentation - Content - LoveIt (hugoloveit.com)](https://hugoloveit.com/theme-documentation-content/)

这是官网给出的yaml例子
```yaml
---
title: "My First Post"
subtitle: ""
date: 2020-03-04T15:58:26+08:00
lastmod: 2020-03-04T15:58:26+08:00
draft: true
author: ""
authorLink: ""
description: ""
license: ""
images: []

tags: []
categories: []

featuredImage: ""
featuredImagePreview: ""

hiddenFromHomePage: false
hiddenFromSearch: false
twemoji: false
lightgallery: true
ruby: true
fraction: true
fontawesome: true
linkToMarkdown: true
rssFullText: false

toc:
  enable: true
  auto: true
code:
  copy: true
  maxShownLines: 50
math:
  enable: false
  # ...
mapbox:
  # ...
share:
  enable: true
  # ...
comment:
  enable: true
  # ...
library:
  css:
    # someCSS = "some.css"
    # located in "assets/"
    # Or
    # someCSS = "https://cdn.example.com/some.css"
  js:
    # someJS = "some.js"
    # located in "assets/"
    # Or
    # someJS = "https://cdn.example.com/some.js"
seo:
  images: []
  # ...
---

```

- titile、data、author这些比较基本的自不必说。
- tags、categories分别定于了标签和分类，这有利于网站上查找，也有利于OB文档的管理。
- featuredImagePreview、featuredImage分别定义了博文在首页的封面缩略图和博文的头图。
- draft定义了这篇博文是够是草稿，若为true，则不会发布到网页。

如果你仅用`hugo new`来新建博文，那么新建的.md文档的ymal中只会存在以下三条，这肯定是无法满足网站的需求。

```ymal
title: "Blog Test"
date: 2022-09-22T00:07:27+08:00
draft: true
```

如果用Quickadd来新建博文，则可以按照定义好的模板（template.md）生成，模板包含了我所需要的一些参数，日期可以自动生成，其余参数自行填入。
```ymal
---
weight: 4 
title:      ""
subtitle:   ""
description: ""
author:     "HLF"
date: {{DATE}}
tags: [""]
categories: [ "" ]
lightgallery: true
featuredImagePreview: ""
featuredImage: ""
math:
  enable: true
draft: false
---
```
{{< admonition >}}
不要把template.md文件放在content文件夹下，因为{{DATE}}无法被渲染，会出错，可以放在网页文件的根目录下。
{{< /admonition >}}

{{< admonition >}}
Quickadd插件的使用可以看[quickadd: QuickAdd for Obsidian](https://github.com/chhoumann/quickadd)
{{< /admonition >}}

## Custom Frames- 本地调试
当你执行`hugo server`命令开启本地调试之后，需要在浏览器中访问` http://localhost:1313`查看网页情况。

理想的状态是能够一边书写，一边查看网页渲染情况。简单的做法就是把OB和浏览器左右分屏，但是涉及到两个软件了，不太优雅。

用Custom Frames将`http://localhost:1313`嵌入OB之后，就可以实现下图效果，在OB中实现书写和预览。

<div align=center>
<img src="https://s1.vika.cn/space/2022/09/22/b257bf94e91e444b9567f0f4cacecd43" alt="drawing" style="width:100%"/>
</div>

你也可以将你的hugo网站嵌入OB作为主页。

<div align=center>
<img src="https://s1.vika.cn/space/2022/09/22/db490482055c4f6ab763b06ac790fa84" alt="drawing" style="width:100%"/>
</div>

{{< admonition >}}
Custom Frames插件的使用可以看[CustomFrames](https://github.com/Ellpeck/ObsidianCustomFrames)
{{< /admonition >}}

## Shell Commands - 发布
在[使用Hugo+github建立你的第一个博客](https://www.hlffmm.cc/posts/2022-09-17-%E4%BD%BF%E7%94%A8hugo+github%E5%BB%BA%E7%AB%8B%E4%BD%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8D%9A%E5%AE%A2/)中，我写了使用`git`命令将网页文件推送至github，命令很多，逐条执行也很麻烦。

shell commands插件的作用就是在OB中执行shell代码，只要将推送的代码填入插件，就可以一键执行了。

<div align=center>
<img src="https://s1.vika.cn/space/2022/09/22/87aae908f57d488b8205156021d196e7" alt="drawing" style="width:100%"/>
</div>

```powershell
hugo
cd public
git config --global core.autocrlf false
git add .
git commit -m "blog"
git pull --rebase origin master
git push -u origin master
```

that's all.
