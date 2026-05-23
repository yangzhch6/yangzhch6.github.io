一个学术网站的 Github Pages 模板。 这是由 [Stuart Geiger](https://github.com/staeiou) 从 [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) 分叉（然后分离），这是 ©2016 Michael Rose 在 MIT 许可下发布。参见 LICENSE.md。

我想我已经顺利运行并修复了一些主要错误，但是如果您想改进通用模板/主题，请随时提交问题或提出拉取请求。

### 注意：如果您正在使用这个 repo 并且现在收到有关安全漏洞的通知，请删除 Gemfile.lock 文件。

# 介绍

1. 如果您没有，请注册一个 GitHub 帐户并确认您的电子邮件（必需！）
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by 单击右上角的“fork”按钮. 
1. 转到存储库的设置（以“Code”开头的选项卡中最右侧的项目应位于“unwatch”下方）. Rename the repository "[your GitHub username].github.io", 这也将是您网站的网址（URL）.
1. 设置站点范围的配置并创建内容和元数据 (see below -- also see [this set of diffs](http://archive.is/3TPas) 显示更改设置的文件 [an example site](https://getorg-testacct.github.io) 对于具有用户名的用户 "getorg-testacct")
1. 上传任何文件 (like PDFs, .zip files, etc.) to the files/ directory. 他们将出现在 https://[your GitHub username].github.io/files/example.pdf.  
1. 通过转到存储库设置检查状态, in the "GitHub pages" section
1. (Optional) 在 `markdown_generator` folder 中使用 Jupyter notebooks 或 python 脚本 从 TSV 文件生成出版物和谈话的 Markdown 文件.

在 https://academicpages.github.io/ 查看更多信息

## 在本地运行（不在 GitHub Pages 上，在您自己的计算机上运行）

1. 克隆存储库并按照上面的详细说明进行更新
1. 确保你已经安装了 ruby​​-dev、bundler 和 nodejs: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. 如果出现错误，请删除 Gemfile.lock 并重试。
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` 本地服务器将在更改时自动重建和刷新页面.

# 变更日志——错误修正和增强

像学术页面这样的现成模板主题存在一个逻辑问题，这使得修复错误和更新核心主题变得有点棘手。 如果你 fork 这个存储库，定制它，然后再次拉取，你可能会遇到合并冲突。 如果你想保存你的各种 .yml 配置文件和 markdown 文件，你可以删除存储库并再次 fork 它。 或者您可以手动修补。

为了支持这一模板，对底层代码的所有更改都显示为标签的已解决问题 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). 每个问题线程都包含一个链接到单个提交或跨多个提交的差异的注释，因此那些拥有分叉存储库的人可以轻松识别他们需要修补的内容。

# 修改_config.yml
进入 [config.yml](https://github.com/zhoulvbang/zhoulvbang.github.io/blob/master/_config.yml)文件，这个文件使用[Jekyll](https://jekyllrb.com/)编写而成，此配置文件用于影响整个站点的设置、值，您应该设置一次，之后很少需要编辑。出于技术原因，此文件不会在您使用时自动重新加载。

您需要着重设置该文件中的 Site Settings部分和Site Author部分，还有一些内容由于个人水平有限，暂时无法进行修改与配置，如果借鉴我的博客的朋友有擅长这方面的，不妨深入一下。

# 修改_pages
进入[pages](https://github.com/zhoulvbang/zhoulvbang.github.io/tree/master/_pages)，这个文件下有很多.md和.html文档，编辑404.md你可以制作一个个性化的404页面，其他也是如此。

如何修改网页说明语：进入_pages文件，点击[abou.md](https://github.com/zhoulvbang/zhoulvbang.github.io/blob/master/_pages/about.md)文件进行修改。

# 配置私有域名
由于网络问题，大陆地区一般是不可以访问[GitHub](https://github.com/)，为了让自己的主页/网站可以被访问，我们可以配置一个私有域名，域名可以自行前去[腾讯云](https://console.cloud.tencent.com/)和[阿里云](https://cn.aliyun.com/)购买，购买之后等待其确认，然后解析这个域名，将上述域名(及www域名)解析到[yourname].github.io的IP地址，主机地址是GitHub的主机地址，一般有两个，分别是 `192.30.252.153`、`192.30.252.154`，将其解析好后，转到GitHub界面，直接在`github.io`仓库的`Settings`的`GitHub Pages`项直接设置`Custom domain`，GitHub会自动添加`CNAME`文件，你可以选择在`Custom domain`中直接输入你的域名`www.xxx.cn`或者在`CNAME`文件中进行修改，将你的域名输入，保存。然后刷新~

# 其他的可以自己去探索一下，不妨给个关注与点个星星
