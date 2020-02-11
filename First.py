# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import time
from typing import TextIO
import pynput
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon
import recordWindow


json_obj = []
filename: str
f: TextIO

key_dic = {16777264: pynput.keyboard.Key.f1, 16777265: pynput.keyboard.Key.f2, 16777266: pynput.keyboard.Key.f3,
           16777267: pynput.keyboard.Key.f4, 16777268: pynput.keyboard.Key.f5, 16777269: pynput.keyboard.Key.f6,
           16777270: pynput.keyboard.Key.f7, 16777271: pynput.keyboard.Key.f8, 16777272: pynput.keyboard.Key.f9}


class Ui_Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.a=1
        self.setWindowIcon(QIcon('ico.ico'))
        self.mouse_listener = pynput.mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll,on_move=self.on_move)
        self.keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setFixedSize(808, 487)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 431))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonRecord = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonRecord.setMinimumSize(QtCore.QSize(300, 300))
        self.pushButtonSaveFile = QtWidgets.QPushButton(self)
        self.pushButtonSaveFile.setText('保存脚本')
        self.pushButtonSaveFile.move(600, 400)
        self.label_file = QtWidgets.QLabel(self)
        self.label_file.setText('脚本：无')
        self.label_file.setFixedWidth(500)
        self.label_file.move(100, 400)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.Bold=True
        font.setPointSize(30)
        self.pushButtonRecord.setFont(font)
        self.pushButtonRecord.setObjectName("pushButtonRecord")
        self.horizontalLayout.addWidget(self.pushButtonRecord)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonStart.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(30)
        font.Bold=True
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout.addWidget(self.pushButtonStart)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        global key_dic
        self.label_hot_key = QtWidgets.QLabel(self)
        self.label_hot_key.setText('请分别设置：\n录制启动热键：%s\n录制终止热键: %s\n脚本运行时终止热键: %s' % (
        str(key_dic[recordWindow.startKey]), str(key_dic[recordWindow.endKey]),str(key_dic[recordWindow.stopRunKey])))
        self.label_hot_key.move(50, 10)
        self.label_hot_key.setFont(QFont("黑体",9,QFont.Bold))
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Main):
        Main.setWindowTitle("MouseTranck  By.@DOCCA0  2947323341@qq.com")
        self.pushButtonRecord.setText("热键设置")
        self.pushButtonStart.setText("启动脚本")

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == recordWindow.startKey:
            print('开始录制')
            self.showMinimized()
            self.startRecord()




    def startRecord(self):
        global filename, f
        filename = str(time.time()) + '.txt'
        f = open(filename, 'w')
        f.write('[')
        self.last_time = time.clock()
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def endRecord(self):
        global f, choose_save_thread
        print('结束录制')
        self.showNormal()
        f.close()
        with open(filename, 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()
        with open(filename,'a') as filehandle:
            filehandle.write('\n]')
        # ######################删除最后一个“，”#########################

        self.label_file.setText("录制脚本成功：%s 请保存" % filename)

        self.mouse_listener.stop()
        del self.mouse_listener
        self.keyboard_listener.stop()
        del self.keyboard_listener

    # 鼠标监听函数
    def on_click(self, x, y, button, pressed):
        string_act = 'click ' + str(x) + ' ' + str(y) + ' ' + str(button) + ' ' + str(pressed)
        try:
            self.now_time = time.clock()
            f.write('\n{"time":"%.4f","action":"%s"},'%(self.now_time-self.last_time,string_act))
            self.last_time=self.now_time
            print(string_act)
        except:
            pass

    def on_scroll(self, x, y, dx, dy):
        string_act = 'scroll' + ' ' + str(x) + ' ' + str(y) + ' ' + str(dx) + ' ' + str(dy)
        try:
            self.now_time = time.clock()
            f.write('\n{"time":"%.4f","action":"%s"},' % (self.now_time - self.last_time, string_act))
            self.last_time = self.now_time
            print(string_act)
        except:
            pass

    def on_move(self,x,y):
        self.a=self.a+1
        if(self.a%20==0):
            try:
                string_act = 'move' + ' ' + str(x)+' '+str(y)
                self.now_time = time.clock()
                f.write('\n{"time":"%.4f","action":"%s"},' % (self.now_time - self.last_time, string_act))
                self.last_time = self.now_time
                print(string_act)
            except:
                pass
            self.a=1


    # 键盘监听函数
    def on_press(self, key):
        global key_dic, f, filename, file_choose_thread
        if key == key_dic[recordWindow.endKey]:
            self.endRecord()
        else:
            try:
                string_act = 'press' + ' ' + str(key)
                self.now_time = time.clock()

                f.write('\n{"time":"%.4f","action":"%s"},' % (self.now_time - self.last_time, string_act))
                self.last_time = self.now_time
                print(string_act)
            except:
                pass

    def on_release(self, key):
        string_act = 'release' + ' ' + str(key)
        try:
            self.now_time = time.clock()
            f.write('\n{"time":"%.4f","action":"%s"},' % (self.now_time - self.last_time, string_act))
            self.last_time = self.now_time
            print(string_act)
        except:
            pass
