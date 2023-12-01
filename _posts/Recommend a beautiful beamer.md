今天是农历辛丑年最后一天，用一个beamer做一年LaTeX学习的告别，接下来的一年自己要准备考研，所以在LaTeX上面的画的时间将不会有以前的那么多了。

本次推荐的是Metropolis这一beamer主题模板，自己花了一些时间进行翻译与完善（好像也没做啥）

Beamer 是一个用于创建演示文稿 LaTeX 的文档类。它同时支持LaTeX + dvips、pdfLaTeX、LuaLaTeX以及XeLaTeX。它的名称取自德语词汇 Beamer（pseudo-anglicism），意思是影像演示。

Beamer文档类并不是最早开发出的LaTeX演示文稿工具。2003年2月，Till Tantau为其博士论文答辩编写了beamer包，并于一个月之后发布在CTAN上。

作为LaTeX的一个文档类，Beamer文档和LaTeX文档一样都是纯文本文件。且beamer兼容LaTeX常见的命令，和其他宏包的兼容性良好。当然也有支持Beamer语法的图形界面，如AUCTEX和LyX。

Beamer也可以通过使用兼容包来支持其他LaTeX演示文稿宏包的语法，包括 Prosper和Foils。

Beamer默认生成PDF文件用于演示，其动态效果依靠创建多页幻灯片实现。

若要打印出每张幻灯片的最终效果用于分发给听众，需开启handout选项；想要在一张纸上打印多页幻灯片，需要用pgfpages宏包；也可以输出适合印刷在A4或者标准信纸上的文档效果。

'frame'的标题将变为段落的标题，不再包括原有的外观主题，同时保证了原有章节结构不被破坏——这就可以方便的输出演讲的提纲。

Beamer的一些功能是依赖于PGF的。

Metropolis这款beamer非常优美，第一次了解到这个主题还是在ElegantLaTeX作者的主页上。

当时作者说有很多人让他出一个Elegant系列的beamer主题，作者的回答是有Metropolis这一珠玉在前，就先不做了。

我那时抱着好奇去看了看，的确很不错，Metropolis一款视觉噪音极小的 Beamer 主题，灵感来自Benjamin Weiss 的 HSRM Beamer 主题。 

Metropolis的源文件也在GitHub之中，位置为[https://github.com/matze/mtheme](https://github.com/matze/mtheme)，
本仓库也保存了一份[该文件](https://github.com/zhoulvbang/zhoulvbang.github.io/blob/master/files/Metropolis%20Beamer%20Theme.zip)，
同时也放置了[我修改后的文件](https://github.com/zhoulvbang/zhoulvbang.github.io/blob/master/files/Metropolis%20Beamer%20Theme%202.0.zip)。

配置域名后，可以使用'www.lazyzhou.cn/blob/master/files/Metropolis%20Beamer%20Theme%202.0.zip' 来进行访问。
