CSDN 中 Likianta Me 的测试结论:<br>
https://blog.csdn.net/Likianta/article/details/89363973<br>
<br>
在 Flask 中, HTML 的相对路径逻辑完全失效, 只能按照 Flask 的逻辑来走<br>
Flask 的逻辑是以 Flask.__init__() 中的 static_folder 参数为准
[外链图片转存失败(img-lQaVwhCy-1563030961553)(https://i.loli.net/2019/04/17/5cb71a338c608.png)]<br>
static_folder 的路径是 相对于 启动文件 (本例中的 myproject/A/launch.py) 设置的. 也就是说默认情况下, 只有 myproject/A/static/ (本项目中未创建) 为虚拟资源的目录入口的.<br>
所以这里我把 static_folder 设为 “…/” 就是为了能够让 Flask 以 myproject/ 为虚拟资源的入口<br>
由于 static_folder 不允许向上查找路径 (这也就是为什么 HTML 中的 “…/…/…/” 居然都指向同一个值的原因), 也就是说 “…/…/…/…” 之类的父级路径符号, 都会被删除掉 — 可以变相地认为, 一旦 static_folder 设置了一个目录, 则该目录的所有上级目录的资源都将无法访问.<br>
