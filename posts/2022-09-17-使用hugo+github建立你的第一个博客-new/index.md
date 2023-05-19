# 使用Hugo+github建立你的第一个博客


> 很多时候会发现事情做完了，但是却没有记录，想要回溯的时候就只剩下模糊的记忆了，所以建立个人博客就是一个很好的选择。<!--more-->

建站的过程主要分为三步：
{{< mermaid >}}
graph LR;
    A[1. 安装hugo] --> B[2. 生成网页] --> C[3. 推送至Github]
{{< /mermaid >}}

经过上述三步，即可生成一个可以访问的网页。

以下对建站的全过程进行记录，希望对你也有帮助。

## 1 安装hugo
hugo在windows下的安装可以通过Chocolatey和Scoop安装，这里仅记录通过Scoop安装hugo的方法。
### 1.1 安装scoop
在powershell中通过以下命令安装scoop
```Powershell
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
```
执行以下命令确认安装是否成功
```Powershell
scoop help
```
若正常显示帮助信息则表示安装成功
![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-2.jpg)

### 1.2 通过scoop安装hugo
执行以下命令安装hugo
```Powershell
scoop install hugo
```
使用以下命令进行验证
```Powershell
hugo version
```
正确显示以下信息，则安装完成
![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-3.jpg)

## 2 使用 Hugo

### 2.1 创建一个网页并开启本地调试
 在电脑某个位置建立一个文件夹，用于存放网页文件，如e:/hugo-site。 `cd e:/hugo-site`进入文件夹，通过以下命令建立网站。
```powershell
hugo new site blog
```

会生成一个blog文件夹，存放相应的网页文件，文件目录如下：
```
├── archetypes
│   └── default.md
├── config.toml         # 博客站点的配置文件
├── content             # 博客文章所在目录
├── data                
├── layouts             # 网站布局
├── static              # 一些静态内容
└── themes              # 博客主题
```

通过以下命令可以在本地调试
```
hugo server
```
正确显示以下信息，则成功开启本地调试，访问`http://localhost:1313/`可看到网站
   ![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-4.jpg)

{{< admonition >}}
启用`hugo server`后，此时对网页文件夹内所有的修改，包括博文、配置信息文件等，都会实时同步到`http://localhost:1313/`，可以很方便的进行网页效果的预览
{{< /admonition >}}

{{< admonition >}}
此时网页应该是空白的，因为刚刚建立的网站，没有给主题是不会显示内容的
{{< /admonition >}}

### 2.2 给网页一个主题
刚刚生成的网站是没有任何内容的，需要下载个主题。Hugo 社区有很丰富的主题，可以通过官网 [Themes](https://themes.gohugo.io/) 菜单选择自己喜欢的风格。我选择的是[LoveIt ](https://themes.gohugo.io/themes/loveit/)这个主题，以下讲述一下配置过程。
#### 一般主题的使用方法
`cd blog`进入网页文件夹，通过以下命令将主题下载到theme文件夹下
```powershell
git clone https://github.com/dillonzq/LoveIt.git themes/LoveIt
```
或	
```powershell
git init
git submodule add https://github.com/dillonzq/LoveIt.git themes/LoveIt
```
或者你可以下载主题的 [最新版本 .zip 文件](https://github.com/dillonzq/LoveIt/releases) 并且解压放到 `themes` 目录.

接着，将theme/LoveIt/exampleSite/文件下所有文件复制到blog根目录下，再次通过`hugo server`命令，访问 `http://localhost:1313` 即可看到网页内容

{{< admonition >}}
通过`scoop install git`安装git模块
{{< /admonition >}}

#### 关于LoveIt主题
一般主题按照上述的方法即可正常使用，不过对于LoveIt主题，按照上述方法是会出错的。

首先，LoveIt主题exampleSite中提供的config.toml无法通过上述方法使用，具体怎么修改这里不做赘述，直接将以下内容替换到config.toml中。
```toml
baseURL = "http://example.org/"

# Change the default theme to be use when building the site with Hugo
theme = "LoveIt"

# website title
title = "My New Hugo Site"

# language code ["en", "zh-CN", "fr", "pl", ...]
languageCode = "en"
# language name ["English", "简体中文", "Français", "Polski", ...]
languageName = "English"

# Author config
[author]
  name = "xxxx"
  email = ""
  link = ""

# Menu config
[menu]
  [[menu.main]]
    weight = 1
    identifier = "posts"
    # you can add extra information before the name (HTML format is supported), such as icons
    pre = ""
    # you can add extra information after the name (HTML format is supported), such as icons
    post = ""
    name = "Posts"
    url = "/posts/"
    # title will be shown when you hover on this menu link
    title = ""
  [[menu.main]]
    weight = 2
    identifier = "tags"
    pre = ""
    post = ""
    name = "Tags"
    url = "/tags/"
    title = ""
  [[menu.main]]
    weight = 3
    identifier = "categories"
    pre = ""
    post = ""
    name = "Categories"
    url = "/categories/"
    title = ""

# Markup related configuration in Hugo
[markup]
  # Syntax Highlighting (https://gohugo.io/content-management/syntax-highlighting)
  [markup.highlight]
    # false is a necessary configuration (https://github.com/dillonzq/LoveIt/issues/158)
    noClasses = false
```
再删除exampleSite/content/posts下的所有文件，这个操作是避免.md内容中存在Youtube、Tweet等网站信息，由于网络问题导致无法渲染。

上述关于LoveIt主题的修改，仅保证主题能够正常运行。其余特性的设置，请参考[Theme Documentation - Basics - LoveIt (hugoloveit.com)](https://hugoloveit.com/theme-documentation-basics/)进行设置。
### 2.3 发布一个博文
当正确开启本地调试之后，可以通过以下代码发布新文章，文章会显示在`http://localhost:1313/`网页上
```Powershell
hugo new posts/blog-test.md
```
你可以用Obsidian、Typora等软件进行Markdown文章书写，书写内容也会直接同步至调试网页，很方便。
![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-5.jpg)

## 3 建立Github pages并部署到线上
如果你能够不出错的完成上面的所有操作，那恭喜你已经完成了建站的第一步。

接下来，需要将你调试好的网页部署到GitHub Page
### 3.1 建立Github仓库
你需要注册一个Github账号，并新建一个仓库，建立仓库的过程可以自行查询，唯一要注意的是需要将仓库名改为`username.github.io`，其中`username`是你的Github账户名。

![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-6.jpg)

{{< admonition >}}
如果你的仓库名字设置错了，可以进仓库设置中重命名
{{< /admonition >}}

再进入仓库Pages设置页面，设置成下图所示。其中，`https://nimamxd25.github.io`就是你的网站地址，需要将config.toml中的`baseURL`修改为该地址。
![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-7.jpg)

### 3.2 将网页推送至Github仓库
当你在本地调试好网页，确认无误后，执行以下代码生成静态网页文件
```Powershell
hugo
```
生成的静态网页文件存放在**Public**文件夹下，需要做的就是将**Public**下的所有文件，推送至Github仓库。

第一次推送时，执行以下命令：
```powershell
cd public
git init
git remote add origin https://github.com/**username**/**username**.github.io.git
git add .
git commit -m "随便写点什么"
git push -u origin master
```
随后每次写完文章，执行以下命令：
```powershell
cd public
git add .
git commit -m "随便写点什么"
git push -u origin master
```
{{< admonition >}}
在执行`git add .` 时可能会出现`LF will be replaced by CRLF the next time Git touches it`错误，需要在`git add .`之前先执行`git config --global core.autocrlf false`命令
{{< /admonition >}}

{{< admonition >}}
📌**Note**
第一次Push失败的话，执行`git push -u origin master -f`
{{< /admonition >}}

## 4 换一个你喜欢的域名
Github Pages可以绑定自己的域名，域名可以去阿里云或腾讯云购买，将域名解析到Github Pages主机上。

我买的是腾讯云，域名购买这里不做详细介绍，主要讲一下域名解析。域名解析主要是需要获取Github Pages主机的IP地址。

![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-8.jpg)

Github Pages主机IP可以采用`ping username.github.io`获取，其中`185.199.110.153`就是本站的主机IP，将IP填入并开始解析即可。

![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-9.jpg)

再将解析好的域名填入GitHub Pages对应位置即可，接着即可使用域名访问网站
![](https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/2022-09-17-使用Hugo+github建立你的第一个博客-10.jpg)

## 5 使用Obsidian进行网站笔记管理和发布
comming soon……
