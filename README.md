## 一个关于C30自动打卡签到的Python脚本

今年某带专从学习通实习签到换成c30 没法用现成的脚本了，故自己写了一个。

全部采用python语言，使用到的库 **requests** 和 **datetime**

#### 原理分析

1.使用fd类的抓包分析一下签到，ios无法开着抓取会一直在界面转圈圈，建议使用安卓或者模拟器抓取。![1](https://github.com/a37324614/C30Sign/blob/main/1.png)

2.抓取到分析后发现，只是用post的方式进行，但是在文件里包含了token，以及body里带了一些位置信息。

![2](https://github.com/a37324614/C30Sign/blob/main/2.png)

3.那么token从哪来呢，如果是ios的朋友可以选择用模拟器抓或者安卓抓，退出登录，再登录一次会发现一个登录请求get的方式，里面就有我们想要的token。

![3](https://github.com/a37324614/C30Sign/blob/main/3.png)

4.打卡之旅

前面说到它是利用0或1判断上午还是下午，所以这里利用datetime库获取当前时间，如果上午返回0下午返回1即可。

![4](https://github.com/a37324614/C30Sign/blob/main/4.png)

参数都获取到了，最后利用requests的post请求，再加上定时即可完美食用。

![5](https://github.com/a37324614/C30Sign/blob/main/5.png)

## **建议配合云函数食用最佳**

# 
