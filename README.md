mynote
======

mynote是一个浏览markdown笔记的小型web应用，自带web服务器(使用Python的BaseHttpServer)，特点是简单小巧。

Start
=====

修改run.bat (Windows)或者run.sh(Linux)，搞定python的路径。 --notes-file-path的值用自己的笔记代替就行了。再运行即可。例如：下面的参数表示笔记存放在/home/admin/note/notes目录下

    --notes-file-path=/home/admin/note/notes

运行后，打开浏览器访问 http://localhost:8000/，会自动显示--notes-file-path目录下所有的目录。

**注意：笔记文件的扩展名必须是md**

其他
====
- 修改样式 把static/markdown.css的内容换成你喜欢的markdown css。网上有很多现成的CSS。自带的CSS也是从Google到的，不过我忘了来源……


# Source
Fork from [jiangjizhong/mynote](https://bitbucket.org/jiangjizhong/mynote)
