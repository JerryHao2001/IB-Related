# 关于使用Git 实现GitHub repository和本地文件的同步
1.下载 Git
2.登陆
$ git config --global user.name "你的用户名"
$ git config --global user.email "你的邮箱"
3.生成ssh key
$ ssh-keygen -t rsa -C "你的邮箱"
4.从电脑中找的你的ssh key
C:\Users\hyt.ssh 用记事本打开id_rsa.pub
4.将ssh key用于你的GitHub账户
GitHub/setting/ssh key/add new ssh key
5.建立本地文件夹 并右键文件夹选择 Git Bash Here
6.
$ git init
$ git add .
$ git commit -m "你的备注"

7.将你的repository与本地文件夹链接
	1. 在github中取得地址
	2. $ git remote add origin https://github.com/----------  （输入你的地址）
8.
$ git pull origin master (下载)
$ git push -u origin master（上传）



# git & branch
摘自 [GitHub简明教程 菜鸟教程](http://www.runoob.com/w3cnote/git-guide.html)

分支
分支是用来将特性开发绝缘开来的。在你创建仓库的时候，master 是"默认的"分支。在其他分支上进行开发，完成后再将它们合并到主分支上。

branches
创建一个叫做"feature_x"的分支，并切换过去：
git checkout -b feature_x
切换回主分支：
git checkout master
再把新建的分支删掉：
git branch -d feature_x
除非你将分支推送到远端仓库，不然该分支就是 不为他人所见的：
git push origin <branch>

更新与合并
要更新你的本地仓库至最新改动，执行：
git pull
以在你的工作目录中 获取（fetch） 并 合并（merge） 远端的改动。
要合并其他分支到你的当前分支（例如 master），执行：
git merge <branch>
在这两种情况下，git 都会尝试去自动合并改动。遗憾的是，这可能并非每次都成功，并可能出现冲突（conflicts）。 这时候就需要你修改这些文件来手动合并这些冲突（conflicts）。改完之后，你需要执行如下命令以将它们标记为合并成功：
git add <filename>
在合并改动之前，你可以使用如下命令预览差异：
git diff <source_branch> <target_branch>


#Branch and GitHub flow
[知乎](https://www.zhihu.com/question/20070065)
[GitHub Guides](https://guides.github.com/introduction/flow/)

#Find difference between two files by using FC in window's cmd and diff in git dush
[udacity](https://classroom.udacity.com/courses/ud775/lessons/2980038599/concepts/29607789270923)