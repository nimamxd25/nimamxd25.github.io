# 快速清空GitHub仓库


由于一些原因，你可能需要清空一个GitHub仓库，并重新开始，比如你搞砸了一个项目，或者生成的网页你不需要了。<!--more-->

首先，使用以下命令，将需要清空的仓库`clone`下来
```powershell
git clone 需要清空的仓库地址
```
接着，删除你不需要的文件，留下`.git`文件夹

最后执行以下命令，推送到GitHub，即可完成清空
```powershell
git init
git add .
git commit -m "随便写点什么"
git push -u origin master
```
{{< admonition note "Note" >}}
不要用重要的仓库测试！
{{< /admonition >}}

