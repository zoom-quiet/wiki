# 极简 Python 上手导念
[TOC]


好吧,这是有关如何在 
`42分钟之内` 
超高速上手 Python `开发` 的又一个不怎么靠谱的`心念`手册;-)

## 概述

    基于私人体验,分享主观感触
    完全 大妈 样儿, 任性建议!
    信了
        有所得,都是您自个儿应该的!
        没上手,一定是俺的错...
    不信
        那就瞧个乐,没收您銭不是也乎?


随着互联网的发展,就是用 baidu 也可以搜索到越来越多的中文 Python 技术资料了,
但是,这并没有令自学 Python 编程变成更加轻松!

常见现象是:

- 这么多教程应该看哪个?
- 为什么我看了这么多教程,依然不会用 Python 来编程?
- 到底应该怎么运行 Python 脚本/程序/软件 哪!?
- 有问题应该问谁去?
- ...

但是, 从大妈这么些年和真正的小白接触, 观察大家各自用不同的姿势上手了 Python 的全过程,
发现, 本质上都是 `心念` 的问题,自个儿吓自个儿, 多数情况是根本没有动用自个儿的头脑,
先放弃了,然后各种专业的傲娇感动了自个儿,坚定 Python 一定哪儿有什么问题,
然后, 才没有然后的.

所以, 任性的尝试给出一个极简 `心念` 手册, 来帮助大家自学 Python 时保持 `正念`, 
用最小的心智损耗, 在 `42` 分钟以内,
获得两次以上的快感, 
拥有对 Python 这门工具型脚本语言的全面自信.
从而,可以愉快的自在和 Python 在一起玩耍下去...

## 准入

是的, 听起来这么美好的事儿, 肯定是要有代价的!

代价就是, 您必须有以下经验, 否则,得追加对应建议的时间, 才能继续
这一极简的上手进程...

1. 心智健全, 这个非常关键, 否则持意曲解俺说的一切, 那真心没招儿的
    - 怎么检验这点?
    - 首先, E文过关,敢于阅读整屏的 E文日志输出
    - 其次, 习惯使用 Google 搜索, 并习惯一次输入3个以上的关键字
    - 最后, 愿意尝试不同的编程体验,不纠结类似 括号一定要单独一行,这种细节
2. 有编程经验, 已经建立起来基础的程序/代码/运行时 等概念
    - 这样, 你嘦愉快的瞬间用以往的概念找到 Python 中的表述形式,就完成了上手
    - 否则, 推荐先学习一下 JavaScript, 掌握编程的基本元知识再说:
        - 这样,目测得追加4小时
        - 0.5 小时熟悉 Chrome 的调试工具
        - 1 小时通读 JS 教程, 理解 DOM 的操作概念和过程
        - 1 小时练习 JS 基础数据结构
        - 1 小时练习 JS 函式的使用
        - 0.5 小时,完成一个简单的页面交互
        - 告诉自个儿,完成了一个软件的半成员
3. 有靠谱环境, 这可能是相对困难的一方面
    - Linux/MAC 用户,比较幸福, 什么都是现成的, 而且各种爽利
    - M$ 用户,请允许俺致以最大的同情, 然后,敬请自行先安装好:
        - [activestate.com/activepython](http://www.activestate.com/activepython)
        - [Sublime Text 2](http://www.sublimetext.com/2)
            + 并配置好 Python 支持插件

### 福利:给文科森

~ *[极简编程导念](MinimalistProgramStart)*

## 环境
在开始学习 Python 之前,需要先配置好 Python 的常用环境,
这可能是个 `先有鳮,还是先有蛋` 的事儿,
但是,就是这么任性!

所谓常用环境指:

- [yyuu/pyenv](https://github.com/yyuu/pyenv)
    + 支持你任性的使用指定版本的 Python 环境
- [pip](https://pip.pypa.io/en/latest/installing.html)
    + 支持你任性的安装想安装的第三方模块
- [IPython](http://ipython.org/install.html)
    + 支持你任性的用各种姿势探索 Python 
    + `残念:` 实在想推荐使用 `IPy[:] Notebook` 的,但是,涉及太多大型软件的支持了,对 M$ 用户实在是种折磨,先用基础的 `IP[:]` 吧...
        * `PS:` 此种言及的大型是指 Unix 兼容系统中的,超过10M 都是大型软件了,不是 M$ 中100M 都算小软件的世界观...

关键是,在以上常用环境的配置过程中, 你将体验到 Python 的宏大生态环境,
以及怎么接触,玩耍的通用过程.

## 然后

先来个第一印象:

![120417-coffeeghost-q-in-py.png](http://zoomq.qiniudn.com/CPyUG/zoomquiet-design-collection/py101/120417-coffeeghost-q-in-py.png?imageView2/2/w/720)


- 这42行代码,是可执行的,
- 同时包含了几乎 80% 的 Python 代码常见情景.
- 来自: [ZqQuickIntoPy - Woodpecker Wiki for CPUG](http://wiki.woodpecker.org.cn/moin/ZqQuickIntoPy)

### 开始

- 进入 IPython 交互式编程环境中
    + 参考官方文档中的教程
    + 或参考 [笨办法学 Python （Learn Python The Hard Way） — 笨办法学 Python 3.0 documentation](http://www.jb51.net/shouce/Pythonbbf/latest/) 前 21 课中有关部分
    + 多使用 `dir()`,`help()` 来检验运行时内存里的 Python 对象是否如自个儿的设想
    + 用10分钟,专心熟悉以下核心数据类型:
        * 数字
        * 文本, UTF-8/中文 文本
        * 列表,嵌套列表,列表推导式 简单的 `for in` 循环
        * 字典,嵌套字典
- 用 Sublime Text 编写几个简短的脚本
    + 在终端上运行, 检验自个儿的想法是否正确
    + 完成以下常见工程行为:
        * 函式, 完成一个函式,可以拼接两行文本为新文件保存到硬盘
        * 模块, 将函式发布为一个模块,可以在另外一个脚本中调用
        * 文件, 调用此模块,将两个指定 `.txt` 文件的内容,逐行交错合并为一个新文件
        * 网络, 改进此模块,可以将两个指定网页的内容, 逐行交错合并为一个新文件
- 或是 [笨办法学 Python （Learn Python The Hard Way） — 笨办法学 Python 3.0 documentation](http://www.jb51.net/shouce/Pythonbbf/latest/) 参考 22 课之后的有关部分练习
    + 在 32分钟以内, 完成以上建议的行为




## 没有然后了

- 还要学习什么?
- 不用了哪
- 您已经掌握了 Python 了呢!
    - 当然不是全部知识
    - 但是, 上手 Python 是来用的,不是来研究的
    - Python 这种通用脚本语言, 就是能用 2% 的功能,完成 80% 常见任务的哪
    - 如果只是要通过 Python 了解什么是程序猿生活, 到此,基本已经有足够的体验可以和 码农们愉快的沟通了!
- 还有兴趣?
    + 参考: [vinta/awesome-python](https://github.com/vinta/awesome-python) 了解 Python 的任性范畴
    + 参考: [aosabook/500lines](https://github.com/aosabook/500lines) 体验一下 500 行以内的 Python 程序能折腾出什么来
    + 参考: [探索一门编程语言 | 轻单](https://qdan.me/list/VL46v0rYbAgUsSIS) 扎下去

真心就没有然后了,
你已经是名合格的 Pythonista 了,
自在的使用 Python 来完成梦想吧!

## 知乎

- [你是如何自学 Python 的？ - 陈铮的回答 - 知乎](http://www.zhihu.com/question/20702054/answer/15908321)


## 参考:

- [The Python Tutorial — Python 3.4.3rc1 documentation](https://docs.python.org/3/tutorial/index.html)
- [The Python Tutorial — Python 2.7.9 documentation](https://docs.python.org/2.7/tutorial/index.html)
- [Starting A Python Project The Right Way](http://jeffknupp.com/blog/2014/02/04/starting-a-python-project-the-right-way/)
- [First Steps With Python - Real Python](https://realpython.com/learn/python-first-steps/)
    - [jacebrowning/template-python](https://github.com/jacebrowning/template-python)
    - [audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
    - [rcarmo/ink-bottle](https://github.com/rcarmo/ink-bottle)
- ...


## 是也乎

为毛有这篇文章?

- 看过太多越来越长的 `入门教程`
- 回想自个儿真正上手其实就是那几个瞬间
- 感觉,得有正式的形式来分享那几个瞬间


### btw.

> 以下两文同品
> 有火腿味儿..

- [不要轻易在简历上写我热爱编程，我热爱学习 - 简书](http://www.jianshu.com/p/67a0cf352986)
- ![why-girl-hard-coding.png](http://pyconcn.qiniudn.com/zoomquiet/res/snap/why-girl-hard-coding.png)


## 修订

- 150304 根据 OMY 的反馈,增补 `负基础` 的定义,以及进入的姿势
- 150108 `开智青年故事会` 微群中被MM AT 出来的念头, 42分钟以内快速成型


