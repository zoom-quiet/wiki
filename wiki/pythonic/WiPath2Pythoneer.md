# 理解 Pythoneer 路线图
[TOC]

## 背景
~ 忽然收到关联邀请

> 2016-01-20 17:45 GMT+08:00 
> subject: 邀请您写一篇解读Python知识图谱的文章 ...


- [Pythoneer 路线图 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/Path2Pythoneer)
- 转化为: [Python - 知识库 - 你身边的技术百科全书 - CSDN](http://lib.csdn.net/base/11/structure)
- 但是,需要进一步的解说....

## 什么是编程

如果你没有任何编程体验,那得先从什么是编程说起来了, 否则可以跳到下一节 ;-)

参考: [极简编程导念 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistProgramStart)


文艺点的说法就是:

- 编程是种表述能力
- 将自己的意识向 syber 世界表述,从而推动世界改良
- 编程,行为上只是编写程序
- 而程序看起来就象混乱的英文
- 这主要是因为,人类的思想以及语言本身就是混乱的
- 当电脑要求逻辑严密的命令序列时
- 计算机科学家从逻辑学以及各种其它科学借用了各种妙物
- 发明了和计算机对话的专用语言: 编程语言
    + 至今已经创造出 1500 多种了...
    + 每一种都能用另外一种专用软件编译(翻译)为机械语言
    + 即硬件相关的机械指令
    + ...
    + 这个分支不多解释
- 但是,现实是:
    + 人类世界早已被电脑浸透到底儿透了
    + 可以说,一但所有电脑停止运行,人类可能立即将灭绝
    + 因为人类现代社会的核心凝聚力:
        * 经济关系
        * 法律责任
        * 军事主权
        * ...
        * 可都在电脑管理/控制中
    + 住浅里说,现代人,每天随身都携带有一个以上智能设备
    + 每时每刻都在有意无意的和互联网以及 syber 世界进行沟通
    + 但是,这种沟通是被动的严格控制的
    + 要想真正理解,进而能改良这种沟通
    + 必须通过编程的学习
    + 否则,将逐渐成为现代社会中意识上的原始人...


## 为什么Python
前略, 对于 程序猿 的读者而言是不用解释什么是编程的.
那么最大的问题来了,为什么我坚定的一直推荐使用 Python ?

一般性中肯的说:

过去:Python 一直在稳健发展;从来没有退出过世界语言排行
参考: [TIOBE 1月编程语言排行榜](http://www.oschina.net/news/69606/tiobe-2016-1)
发布的时间够早,94年和 JAVA 几乎同时发布,
而且,从一开始就坚持 "开箱即用" 的策略,
官方发行版本就内置了上百个常用库,以至嘦安排好基本的 Python 运行环境就可以完成
日常几乎所有任务了.

持续的深刻影响着其它语言;
因为 Python 是从一种面向儿童教育的语言演化来的,
从一开始设计语法时就非常看重语言的易用/读,
社区又良好的运行几十年, 在程序员圈子里是种非常低调但是基础的工具型通用脚本语言.

参考 github 上这一关系图谱 [fatiherikli/programming-language-network - Game Maker Language](https://github.com/fatiherikli/programming-language-network)
可以看到有多少语言受到了 Python 的影响.
事实上2000年以后诞生的各种现代 DSL(领域特殊语言)
都多少参考了 Python 的语法.
因为实在是太容易使用了 ;-)

未来,虽然创建人 guido 开辟了不兼容旧版本的 Python 3 分支,引发了各种非意,
但是, Python 为核心的开发生态已成型,在不同领域都有杀手级别的软件.
特别是近年,随着大数据理念的兴起,
非 IT 行业的各种科研/金融/教育领域非专业程序员用户的进入,
著名的交互式 环境 ipython 适时协同 SciPy/numpy/Pandas 等等
数据科学相关的专用大型库,
对 数据分析/机器学习 等等未来异常重要的领域任务,
完成了非常友好的支持环境,
可以在网页上轻松的输入代码/文档的同时,可以随时运行对应代码并获得足够精美的图表.
这使得 Python 已经成为事实上数据科学家的首选编程语言.

好吧,以上都是传统的推荐,
当前的我,对于拿不准主意是否学习 Python 的程序员,只有一句话:

    一个下午就能用起来的语言
    为什么不用起来?


## 怎么Pythonic

当年 [可爱的Python (2009)](http://book.douban.com/subject/3884108/)
[行者箴言](http://wiki.woodpecker.org.cn/moin/ObpLovelyPython/LpyAttach1motto)
中,我们就说过:

    用之
    弗学

现在,通过几年来各种形式的培训后,
发现这种理念代表另外一种认知学的理论:

    输出是更残酷的输入!
    因为教会他人是唯一证明真正学会的指标 ;-)

以往其它语言的自学,其实都是对学校教育中课程设计的一种缩小和自我复制.
然而在 Python 领域,除了官方文档中 guido 唯一传世的大型文档: [The Python Tutorial](https://docs.python.org/2.7/tutorial/index.html) 之外,
最推荐的入门图书是:
[“笨办法”学Python (Learn Python the Hard Way)](http://book.douban.com/subject/26264642/) (一般缩写为 LPTHW)

为什么呢? 因为 LPTHW 给出了一种最正确的自学开发语言的途径:

用最短时间刷得最核心的20%知识点,然后就别学了,直接来解决实际问题吧!
千万别将一门开发语言,弄成一门学科来研究/深入.

这其实也是在安装好 Python 环境,建议输入的第一个命令:

    import this

时,输出的 `蠎之禅` 中包含的 Pythonic 精神了.

因为,自学其实最难的就在无法获得有足够成就感的持续的正反馈.
永远有各种意外,又对整个领域技术没有宏观把握前,
那种好象所有任务都有无数种可能性,自己无论怎么尝试都无法理解全部的挫败感.

但是, LPTHW 的形式,给出了明确的建议:

    常见的任务就这么几个
    每个就这么几个标准处理
    嘦先习惯 Python 的最小调试循环:
        输入
        运行
        输出
        调整
    就进入了和 Python 自然对话的状态
    一切就是问题的定义/分解/解决了
    不要纠结 Python 的精妙

这样,其实就是给出了一系列有现实代表意义的常见小任务,
对任务的解决思路,就是 Python 内置的建议思路和程序逻辑,
在毎一章节设计的几个都不超过20行代码量的案例尝试过程中,
每一章的练习都能在集中精力的情况丁,15分钟以内获得成功的正反馈.
自然就能坚持下来了.

当然, LPTHW 其实也不用都刷完,通过前 20 章的练习,理论上就已经是名合格的 Python 新人了.

只是想高效向专家级进发,就得在入门后,面对两个关键问题:

1. 如何检验当前掌握的知识点是对的?!
2. 如何明确自己的学习路径是合理的?!

前一问题,的建议是:

    输出是更残酷的输入!

重要的事得重复三次:

    输出是更残酷的输入!

这句口号的含义有几层意思:

首先, 输出是残酷的!

因为通过实践,在我们头脑中形成的经验,其实是非理性的模糊的未固化的,过于私人的,
很多时候,我们以为我们明白了,
但是,当众阐述时,总是感觉讲不清楚,
其实,讲不清楚就是没有真正明白!

因为,经验在没有外化为语言/文字时,只是我们自身思维中的一种新模式;
但是,语言/文字,是人类社会公众知识领域的通用模式,
任何新的思维模式,要想从私人经验,变成大众知识,
这其中,首先撞到的就是将立体/网状的经验感觉,变成一维线性的吻合大众期待可理解/接受的陈述/比喻....
这其实是写作领域的技能要求了,
对于一般没有相关训练的程序猿而言,当然难!

其次, 对自身的再输入更残酷!

但是,再难也必须作,因为这是唯一可以自证学到学对的渠道.
因为,通过输出,倒逼自己对新知识进行反复的多维度的审视,
才能补齐欠缺的理解, 形成整体概念,进而找到大众可以直觉理解的隐喻,
甚至于,可以根据自身的学习过程逆推出,建议的对应知识点掌握的层次和过程,
并配上对应的案例和解说,
这其实是一系列,反复的对相同知识点的,不同姿势/方向/模式的演示/练,阐述!
等于逼自己创造出全新的个人原创的知识点记载形式,
其实创造难道相当于将诗经翻译给美国人.

然后, 这种输出必须是持续的刻意的,
并形成习惯,这样在学习新技能的同时,就自动在想象将来应该如何通过文章/演讲来传授这一新知识点,
从而自然而然的从教授的角度来备课,或是说探索知识点的相关维度信息.
进而,形成自己独特的自学流程,
并持续优化,外在体现可能就是学的越来越快了.


以上,有关如何自学 Python 的几个阶段的经验都是可以通过自身努力掌握的,
但是,最后一层问题:

    如何明确自己的学习路径是合理的?!

这真心只能有"老中医"来帮忙了,
这的确是只有经验才能回答的专门问题了.
因为,这必须是对领域技术有足够深入又广泛的了解后,
并对相关行业中, 领域技术应用的层次有足够的体会,
才能对领域技术进行整体描述.

所以, CSDN 出面组织的各种技术图谱,就是想集成各个专家的经验,
形成一个相同公允的整体路径,给自学的程序猿一个足够的 big image
以便自行决定如何,从哪个角度高效攀爬技能树.





参考: [Soft Skills: The software developer's life manual: John Sonmez: 9781617292392: Amazon.com: Books](http://www.amazon.com/Soft-Skills-software-developers-manual/dp/1617292397)


## 历史沿革...
~ 其它背景参考链接

- 2008:
    + [蟒营流程 · ZoomQuiet/kcpycamp](https://github.com/ZoomQuiet/kcpycamp/blob/wiki/KcPyCampFlow.md)
    + [KcPyCamp Intro.(powered by S5)v1.1~080918](http://s5rst.qiniucdn.com/080920-oscamp-intro-cpc/index.html)
- 2014:
    + [蠎营101](http://s5rst.qiniucdn.com/141101-pythonicamp-101/index.html)
- 2015:
    + [极简 Python 上手导念 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart)
- [零基础学编程？Python 中文社区创始人给你五个建议 | 开智学院](https://mp.weixin.qq.com/s?__biz=MzA4ODM4ODQ3MQ==&mid=207987028&idx=1&sn=f3bcfe35c3359a99c39ee1fb93dd0ecd&scene=1&srcid=0122szoiqCcNCpnMLv1FTfxY&key=710a5d99946419d9255c526e3c4fb2bd55acd9f4d2e2c0bed77516576d8b81dea73880eb4928fa1c2cc9ea5413d0e607&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.11.2+build(15C50)&version=11020201&pass_ticket=txfz7GZTb43JU6KZjvO4BPp4JcuwbP5ZB%2FTlazDRtp1RaGWrU2qPKXoXiT9qzcCd)
    + [一个妈妈和编程的270天死磕日记](https://mp.weixin.qq.com/s?__biz=MzA4ODM4ODQ3MQ==&mid=401758678&idx=1&sn=3404194c50cea16318ab6971da0482d2&scene=0&key=710a5d99946419d96fa1d50623e51325e6f4b3e100e26e14ad31f4af9ced4fc95e11c0114517f7e5cf56d5c0711545bd&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.11.2+build(15C50)&version=11020201&pass_ticket=txfz7GZTb43JU6KZjvO4BPp4JcuwbP5ZB%2FTlazDRtp1RaGWrU2qPKXoXiT9qzcCd)
    + [在开智学堂学编程是一种什么体验？](https://mp.weixin.qq.com/s?__biz=MzA4ODM4ODQ3MQ==&mid=401872261&idx=1&sn=858793823e8aca754ed3dfa5d748d711&scene=0&key=710a5d99946419d92c9595663a1c1dde2f9f79960b62c8fb33a061a03c812565551216991717381b091b29e4b470a194&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.11.2+build(15C50)&version=11020201&pass_ticket=txfz7GZTb43JU6KZjvO4BPp4JcuwbP5ZB%2FTlazDRtp1RaGWrU2qPKXoXiT9qzcCd)
    + [破茧成蝶：我走在「程序媛」的道路上](https://mp.weixin.qq.com/s?__biz=MzA4ODM4ODQ3MQ==&mid=401932950&idx=1&sn=c8ca4dd3f1a514a2de5ff104fd846c74&scene=0&key=710a5d99946419d9669002a1bf606cbb60f42ba9a92c70b2d83bb243730f1d121dc7ed35ca6397f7be329aff10105728&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.11.2+build(15C50)&version=11020201&pass_ticket=txfz7GZTb43JU6KZjvO4BPp4JcuwbP5ZB%2FTlazDRtp1RaGWrU2qPKXoXiT9qzcCd)


## (￣▽￣)

- 160124 增补为非 outline 式行文
- 160122 完成结构
- 160120 创建


