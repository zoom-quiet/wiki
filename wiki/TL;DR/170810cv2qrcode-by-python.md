# 如何 Pythonic 的折腾 QR 码?
~ 兼论什么样的模块值得嗯哼...

[TOC]

## 背景
最近在折腾机器视觉相关的项目, 其中有一项核心需求是:

- 实时的从摄像头视频中
- 识别出特定的标记物
- 并对多个标记物可以区别
- 进而记录所有标记物的 ID 和屏幕坐标
- 记录下来以便另外的系统事后统计/分析/可视化

## 嗯哼

### IRMarker
~ 即红外线标定器

- 之前折腾了很长时间, 配合创客自制了专用的 IRMarker
- 开始是 850nm 的, 因为没有红暴, 人眼基本不可感知
    + 但是,发现太弱, 在复杂现实光线中杯具
- 然后,还是传统的 940nm ,人眼微弱感知
    + 但是,能量发射足
    + 相关元件品种/产量也大
- 可惜:
    + 红外光在视频中只有亮度没有颜色
    + 和阳光/反射/灯泡 等等所有亮度能到 `(255,255,255)` 的
    + 图像中和 IRMarker 的光没有区别
    + 尝试用特殊的点阵图形来识别+区分
    + 那叫个蛋痛...

### QRMark
~ 即, 纸质二维码

首先可以搜索到: [zbar 0.10 : Python Package Index](https://pypi.python.org/pypi/zbar/)

- 这货已经有 8 年没有任何更新了
- 而且 win 版本也没有, 是第三方好人折腾了一个
- 这怎么敢用嚓...

然后继续尝试 Google+Youtube 大法:

- [Scanning QR Codes: Verifying the finder patterns - AI Shack - Tutorials for OpenCV, computer vision, deep learning, image processing, neural networks and artificial intelligence.](http://zqdevres.qiniucdn.com/data/20170808172611/index.html)
- [OpenCV: QR Code detection and extraction \- YouTube](https://www.youtube.com/watch?v=NxHdIdNXIO4)
    + [Pocket: OpenCV: QR Code detection and extraction](http://zqdevres.qiniucdn.com/data/20170807165718/index.html)
- [QR code detection and decode in python \- YouTube](https://www.youtube.com/watch?v=c8EhR8AYsoM)
    + ...
- [学习笔记：使用 OpenCV 识别 QRCode \| Why's Blog](https://blog.callmewhy.com/2016/04/23/opencv-find-qrcode-position/)

果断有狠人, 根据 QR Code 标准, 准备用 OpenCV 直接手工来解析...

好在所有知识点都是标准的:


![qr-code-parts.png（PNG 图像，1229x624 像素） - 缩放 (88%)](http://openmindclub.qiniucdn.com/res/usee/snap/qr-code-parts.png?imageView2/2/w/420)

QR Code 结构

![QR code](http://zqdevres.qiniucdn.com/data/20170807161848/8fe49b7a7cfcbe20f134a592dcc5ca20_b.png)

QR 形式数据读取顺序

![QR](http://zqdevres.qiniucdn.com/data/20170807161848/aae80a14bb8286db81fbb87f921da65a_b.png)

QR 解码顺序...


![cv2.RETR_TREE](http://zqdevres.qiniucdn.com/data/20170807165536/61d238c7jw1f35n5f1l1qj218g0xcaei.jpg?imageView2/2/w/360)

cv2.findContours 函式 cv2.RETR_TREE 模式的嵌套结构


![QR 标定点](http://zqdevres.qiniucdn.com/data/20170807165536/61d238c7gw1f36lht551bj214l0l3jto.jpg?imageView2/2/w/360)

QR 标定点识别方法之一



![QR 标定点识别](http://zqdevres.qiniucdn.com/data/20170808172634/qr-finder-pattern.jpg)
QR 标定点识别方法之二

...

![QRCodeOrientation](http://paginas.fe.up.pt/~ee09082/images/QRCodeOrientation.png)

QR 方向判别



所以,纯 OpenCV 的 QR 识别思路是明确的:

- 图像预处理->二值化处理
- 根据 `cv2.findContours` 的结果,找到吻合 `Position Detection Pattern` 的结构
- 如果几个嵌套盒结构间的空间关系或是之间的 `Timing` 数据吻合 QR 标准
- 则推导出对应 QR 码的有效面积
- 再进行整形
- 然后根据 QR 的数据区黑白变化提取为 0/1 值, 再进行标准的 decode 就还原为文字了

![bitsextraction2](http://zqdevres.qiniucdn.com/data/20170809232225/bitsextraction2.png)


## 撞哉

- 一切按照思路以及代码
- 很快冲过 单一 QR 码在视频中的情况
- 当然, 最后读取内容还是用 zbar
- 但是, 多个 QR 码出现在视频中时
- 杯具了:
    + 无论怎么调整参数
    + 明明非常清晰的图像
    + 预处理也非常良好

![qrcode-findContours-edges.png（PNG 图像，173x502 像素）](http://openmindclub.qiniucdn.com/res/usee/snap/qrcode-findContours-edges.png?imageView2/2/w/360)

**但是!** 原先工作良好的代码,死活就是识别不出所有 `Position Detection Pattern` 

## 柳岸
~ 碎了一觉起来...

- 想想为毛这么多年就没有 zbar 同类模块出没?
- 回去看了一下官网:[ZBar bar code reader](http://zbar.sourceforge.net/)

![zbar](http://zbar.sourceforge.net/img/zbar.200.png)

嗯哼? 感觉不是大家懒, 而是 QR Code 标准又没有变, zbar 完美解决了问题的话, 
自然没有后来 `Yet another zbar` 之类的嗯哼了...

只是, 对应python 模块的文档实在简洁, 搜索案例代码:

[» Unusual tasks with video files – reading bar\-codes and qr\-codes](http://kurokesu.com/main/2016/08/22/unusual-tasks-with-video-files-reading-bar-codes-and-qr-codes/)

才发现:

    ...
    for l in symbol.location:
        text = str(symbol.type) + ': ' + str(symbol.data) + ' / ' + str(symbol.quality)
        ...

![symbol.location](http://kurokesu.com/main/wp-content/uploads/2016/08/out-1.gif)

嗯哼?! what?! 人家 zbar 一直就支持:

- 直接识别并读取多个 QR 码
- 并返回每个 QR 码的坐标
- `눈_눈` <-- 那为毛,内么多文章都是拼命用各种姿势通过 OpenCV 识别出 QR 码
    + 然后小心的剪裁出来
    + 再合理旋转,平整
    + 最后喂给 zbar 只有 QR 砩的图片片段?!
- 结果, 核心代码就这么几行

:

    import zbar
    from PIL import Image

    ...
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    zimage = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(zimage)

    for symbol in zimage:
        for l in symbol.location:
            text = str(symbol.type) + ': ' + str(symbol.data) + ' / ' + str(symbol.quality)


快速重构原先代码, 几下就完成了原定目标


## 致谢
-> [汪海](https://blog.callmewhy.com/about/)

一位认真的普通程序猿, 目测也是折腾了 10小时以上, 幸好依细致的记录了各种基础知识点,
才令俺及时回过味儿来, 找到正确的道路...

特别的回应一下依后来没有嗯哼下去的: `仿射变换`

- 直接使用 [4 Point OpenCV getPerspective Transform Example \- PyImageSearch](http://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/) 中给出的两个函式:
- `order_points()` -> 获得合理的4点坐标
- 代入 -> `four_point_transform()` -> 就获得修正后的图片了.

## PS:

[ArUco: a minimal library for Augmented Reality applications based on OpenCV | Aplicaciones de la Visión Artificial](http://www.uco.es/investiga/grupos/ava/node/26)

![ArUco](http://zqdevres.qiniucdn.com/data/20170809231640/board.png)

ArUco 更小的标定码形式

[OpenCV: Detection of ArUco Markers](http://docs.opencv.org/master/d5/dae/tutorial_aruco_detection.html)

问题在, 必须 OpenCV 3.0 以上版本环境才支持!

# (￣▽￣)

- 170810 残念
- 170809 南墙
- 170808 部分达成
- 170807 折腾
- 170806 动念


