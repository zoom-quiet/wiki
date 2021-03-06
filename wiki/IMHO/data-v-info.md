# 数据可视化 到 可视化信息 浅述
[TOC]

~直觉式的阐述个人当前数据可视化世界观


![datav2vinfo.png(PNG 图像,776x814 像素) -  Graphviz 生成](http://0.zoomquiet.top/ZQCollection/map/datav2vinfo.png?imageView2/2/w/600)


- 源代码: [datav2vinfo.dot](https://bitbucket.org/ZoomQuiet/tangle/src/f7d3402616263fe1ba3b9fd360c623e257349f1d/dot/obp/datav2vinfo.dot?at=default)

数据可视化(Data Visualization)突然热了,但是为什么?!

- N 久以前就有的技术/思想/实践了哪?!
- 为此,仅从个人非专业角度,试图直白的阐述数据可视化之于我们的意义,
以及可视化的基本操作过程,来号召现在就开始学习数据可视化技术应用到生活中吧.

## 我们的湿件

对应电脑的硬件(hard ware)以及软件(soft ware),
我们的大脑就是种湿件([Wet ware](http://www.isfdb.org/cgi-bin/title.cgi?868))
具有更加深沉的内置规范/机制/原则... 而且无法随便升级的,只能经过大自然上亿年的进化,才能改进一丝丝 ;-(

推荐读物,刘未鹏 的[思维改变生活](http://mindhacks.cn/topics/mind/)
系列文章,其中 "["逃出你的肖申克(三):遇见20万年前的自己"](http://mindhacks.cn/2010/03/18/escape-from-your-shawshank-part3/)",非常精要的指出了,面对信息大潮的我们可怜的湿件各种不适应;-(

虽然,湿件本身具有这个宇宙可能最高的可动态扩展性,
但是其扩展只能通过湿件自身的努力,暂时还没有什么标准件可以即插即用式的扩展每一个湿件的能力 ; 所以,对于我们绝大多数人,只能先迁就湿件的品性,不论是否愿意.


## 7±2 原则

是认知科学中最基础的定理之一.
大意就是,由于人类大脑处理信息的能力有限,它会将复杂信息划分成块和小的单元.
根据乔治A米勒(George A. Miller)的研究,人类短期记忆一般一次只能记住5-9个事物.这一事实经常被用来作为限制导航菜单选项到7个的论据; 然而关于神奇的"7,加2或者减2"还是引起了激烈的讨论. 

参考:[[1]](http://www.musanim.com/miller1956/) ; [[2]](http://drdobbs.com/web-development/184412300)

所以,在信息爆炸时代,怎么在同类的海量信息中,让受众,更加容易认同自个儿的,
就得尽量不违反 "7±2 原则"

## 万事无绝对!-)

首先,得明确,这儿的"信息"究竟是什么?!
其实: 消息/数据/信息/资料 等等概念,一般都是混的...

俺也不是专家,只能掉个书袋先:
信息论创始人,香农(Shannon)的信息定义: 

- "**信息是确定性的增加**"

越品越有意味的...

基本上,所有对于此类概念的描述所指,只是两种事物

参考:[[3]](http://www.qbzz.org/oa/pdfdow.aspx?Type=pdf&FileName=42f488f2-eb7f-419d-95c8-4c492cac9669.pdf)

- 数据~对客观的某种记录形式
- 信息~经过提炼的数据,包含提炼者以及解读者价值观的湿件内部记录.

在信息学中指出信息构成是:

+ 信息源
+ 内容
+ 载体
+ 传输
+ 接受者

可见,信息不是可以简单物化的,是包含过程和受众的一种社会化行动的整体.

而其中,信息的传输至关重要,如果处理不当,再重要的信息,也可能被忽视/误解/曲解... 
因为人类,天生是视觉生物!
同一信息通过声音/文字/图片/影像 的传递效率是完全不同的,可以相差上百倍!

一个经典案例:

![](http://datavlab.org/wp-content/uploads/2012/03/poster_OrigMinard.gif)

图片来自: [Charles Joseph Minard – Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Charles_Joseph_Minard)



是由Minard 绘制的地图,展现了 1812 年拿破仑的大军团进军俄国的路线(上半 部分)和撤退时的气温变化(下半部分). 这一历史事件中,法军数量的急剧减少 以及恶劣的气候条件一览无遗,法国科学家 Étienne-Jules Marey 称"该图所展现出 的雄辩对历史学家的笔是一种极大的挑战".

在单独一张图片中:

+ 军队数量
+ 时间数据
+ 地理数据
+ 变化趋势
+ 气温数据
+ 军事策略
+ 士气变化
+ 历史态度
+
....

包含的信息远超过7±2个点,但是,所有看到图的一瞬间,就基本把握住了所有信息!

这就是信息图(infographics)的威力!

而信息图探索出来的各种可视化手法,被设计成各种工具/规范后,就被快速复用在各种场景中,
对大量数据进行高度浓缩式的展现!

可以简单,武断的认为,数据可视化:

- 就是要将大量数据以合理的,吻合湿件秉性的适当形式展现出来!
- 因为,这样才能最高效率的传递重要信息,引发合理的决策

## 数据可视化的宏观过程

个人体会,至少包含以下环节:

    收集
     ^  `->整理
     |    ^   `->设计
     |    +-----/|^|
     +-----------/||
                  | `->输出
                  |     `->传达
                  |         |
                  +---------/

### 数据收集

要解决的问题有:

- 收集什么数据?
- 怎么收集?
- 如何避免误差?
- 怎么存储数据?

好在之于 web 应用领域,基本都早已有标准方案,老实用就好!

### 数据整理

每次可视化都是为了解决特定问题的,所以,面对海量以标准形式收集的数据,
怎么针对领域问题合理抽取对应的数据?要解决的问题有:

- 什么数据对于可视化的需求有用?
- 怎么从现有数据中抽取?
- 抽取出来的数据应该是什么格式?怎么存储?
- ...

同样,在 web 应用领域,配合丰富的 Unix 小工具,以是分分钟的事儿;
不过,正则表达式一定要理解, Python/Perl/Ruby 脚本語言,怎么着都得掌握一个... 

### 可视化设计

这个环节,个人以为是最吃功夫,也最考驗天赋的了,要解决的问题有:

- 要解决的问题本质是什么?
- 以什么数据集来回答最合适?
- 目标数据集有多少有意义的切面?
- 以什么信息图的形式来同时展示这些切面最合理?
- 还能再简洁点嘛?
- 顔色可以选择嘛?
- 应该暗示受众什么?
- 受众目前可以接受的形式是什么?
...

最要命的是,所有问题,都要归结为一个单一形式来回应!而且有对应的工具可以进行生成!

个人以为,可视化设计,决定了数据可视化后的信息传达效果,
所以,这不应该是一錘子买卖,也是需要根据传达效果,以及对问题的不断理解,
掌握问题背后的真正领域需求,不料调整所有环节,改进,增强可视化效果的一个长期过程.
可视化输出

动用工具,合理的输出成合理的形式,要解决的问题有::

- 选择什么工具?
- 能否自动化输出?
- 输出成什么格式?

好吧,这步问题比较单纯,但是,面对日益丰富的可视化工具/服务,怎么选择,才能"长治久安"?
而且,现成的工具能力肯定是有限的,怎么合理组合,或是自行后期处理,增补,
得以更好的输出成吻合设计的形式!?
都是需要深入折腾的... 

### 可视化传达

`"酒香也怕巷子深"`,这道理之于数据可视化反而不存在,
为毛?!

- 发动数据可视化,不是简单的事儿
- 必定是有强烈需求时,才感觉到只能可视化了,否则太多重要数据根本理解不来了,,,
- 所以,对于数据可视化的成果,已经可视化的信息,是有具体的明确的受众,严正期待的

只是,一但設計不良,没有在第一时宜打动受众,获得认同,
那就有一堆要解决的问题了:

- 在哪?什么时机?誰来展示?
- 怎么配文字?
- 需要支持查询原始数据?
- 如果有变化,是否/怎么提醒目标受众?
- 展示效果如何,怎么收集反馈?

同样,此阶段也会产生数据/信息,也需要立即反馈回設計阶段,加入改进的考虑因素.


## 谁应该学习/使用数据可视化?

好吧得承认,以上描述的都是理想状态中的数据可视化世界,
但是,多数情景中,数据从来不被人们真正认真对待的,,,

所以,即使身为数据分析师也在努吼:"[数据是一种信仰](http://blog.sina.com.cn/s/blog_5025e3880100qjbf.html)"

我想,这恰恰是数据可视化的机会呢:

- 任何人/组织,都需要高效/及时/可靠的信息支持
- 当关键信息超过 7±2 点时,湿件就会抱怨,对信息的汲取效率就大大降低
- 这时,将所有关键信息凝聚到可视化信息图中,就能很好的解决信息高效传递问题了

而且,现代城市生活,每个社会人每天每时每刻,都必须处理大量信息:

- 每个人,都同时处于不同角色中
- 每个角色,在下同时刻,又都有各自的关键任务
- 每个任务,都依赖一堆关键数据的变化
- 每一堆关键数据的变化,对应的关键信息,都需要及时数据/理解

一个人尚且如此,一个团队?组织?企业?!
不过,对于企业,再好再漂亮的数据可视化输出,如果没有和具体的业务结合的话,
那是根本没有吸引力的哦.

随着信息技术的高速发展,我们对于社会生产活动的数据收集能力,越来越深入/神奇

- 故而,可以用以决策的关键信息,也能高速丰富的数据中不断挖掘出,
- 那未,也就意味着,每一項决策,需要理解的实时信息也就越来越多,
- 可惜,我们的湿件,从自身生物特性上决定了无法立即跟上这种高速变化,
- 综上,数据可视化技术,生成的高度复合,而又吻合湿件秉性的可视化信息,一定会流行起来,
- 所以,任何有好奇心,智力正当的人,都应该开始学习,使用数据可视化技术/思想,
通过对可视化信息的使用,增强自己对大量社会信息的处理能力,
同时,也为所在组织/团队/企业,进行技术储备,关键时刻顶上去,就发达了吼,,,

## 是也乎

- 181210 发现大图 URI 错误, fixed
- 150101 发现从 [杂谈集](http://datavlab.org/cat/thoughts) 消失了,于是使用 md 重制收录
- 120311 发布在: [数据可视化 到 可视化信息 浅述 - DataVlab.org](http://datavlab.org/2012/03/11/2503)
