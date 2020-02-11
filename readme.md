# 											MouseTranck 

## 																				

[GitHub主页]: @https://github.com/DOCCA0

​		这是一个能够记录鼠标键盘操作的小程序，类似于按键精灵，但是在按键精灵的基础上增加了：

**①记录鼠标移动**

**②记录鼠标滚轮（还不太精确，有待后续更新）**

**③拖放功能**

程序使用pynput包，将操作记录为JSON格式保存在.txt中，如下：

```json
[
{"time":"0.1582","action":"move 348 874"},  				鼠标移动
{"time":"0.0757","action":"move 315 898"},
{"time":"0.2822","action":"press Key.space"},				键盘按下空格
{"time":"0.1162","action":"release Key.space"},
{"time":"0.0630","action":"press Key.enter"},
{"time":"0.0788","action":"release Key.enter"},
{"time":"1.1334","action":"move 504 89"},
{"time":"0.0568","action":"scroll 452 294 0 -1"},			鼠标滚轮华东一格
{"time":"0.0736","action":"move 429 671"},
{"time":"0.6384","action":"click 429 663 Button.left True"}, 鼠标左键按下
{"time":"0.0741","action":"click 429 663 Button.left False"},鼠标左键抬起
{"time":"0.0743","action":"move 981 685"},
{"time":"0.0120","action":"scroll 927 483 0 -1"},
{"time":"0.0736","action":"move 1125 219"},
{"time":"0.0761","action":"move 1053 315"}
]


```

  但是，scroll记录的-1和+1代表的是鼠标滚轮滑动一格，但是在运行脚本的时候scroll需要的是像素变化，所以经过我多次测试，我把每个scroll的值都乘以72（不准确，慎用），我因此尝试了pyautogui和win32api，需要的都是像素值，卡了很久，放弃了，如果您有更好的解决方式，可以提交PR。

​	如果您在使用过程中鼠标发生错位，请调整缩放与布局：

![](D:\projects\python\MouseTranck\percent.png)





​																								

​																													2020年2月11日 15:35:04