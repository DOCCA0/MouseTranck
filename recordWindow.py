# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

startKey: QtGui.QKeyEvent.key=16777264
endKey: QtGui.QKeyEvent.key=16777265
stopRunKey:QtGui.QKeyEvent.key=16777266

class RecordWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('ico.ico'))
        self.setObjectName("RecordWindow")
        self.setFixedSize(611, 326)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(70, 80, 468, 142))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelStart = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelStart.setFont(font)
        self.labelStart.setObjectName("labelStart")
        self.horizontalLayout.addWidget(self.labelStart)
        self.comboBoxStart = QtWidgets.QComboBox(self.widget)
        self.comboBoxStart.setObjectName("comboBoxStart")
        self.comboBoxStart.addItems(['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'])
        self.comboBoxStart.activated.connect(self.choose_start)
        self.horizontalLayout.addWidget(self.comboBoxStart)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacer_item = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacer_item)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3=QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.labelEnd = QtWidgets.QLabel(self.widget)
        self.labelStopRun=QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelEnd.setFont(font)
        self.labelEnd.setObjectName("labelEnd")
        self.horizontalLayout_2.addWidget(self.labelEnd)
        self.labelStopRun.setFont(font)
        self.labelStopRun.setObjectName("labelStopRun")
        self.horizontalLayout_3.addWidget(self.labelStopRun)
        self.comboBoxEnd = QtWidgets.QComboBox(self.widget)
        self.comboBoxEnd.setObjectName("comboBoxEnd")
        self.comboBoxEnd.addItems(['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'])
        self.comboBoxEnd.activated.connect(self.choose_end)
        self.horizontalLayout_2.addWidget(self.comboBoxEnd)
        self.comboBoxStopRun=QtWidgets.QComboBox(self.widget)
        self.comboBoxStopRun.setObjectName("comboBoxStopRun")
        self.comboBoxStopRun.addItems(['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'])
        self.comboBoxStopRun.activated.connect(self.choose_stop_run)
        self.horizontalLayout_3.addWidget(self.comboBoxStopRun)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslate_ui(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, RecordWindow):
        _translate = QtCore.QCoreApplication.translate
        RecordWindow.setWindowTitle("热键设置")
        self.labelStart.setText("开始录制热键：")
        self.labelEnd.setText("结束录制热键：")
        self.labelStopRun.setText("停止脚本运行：")

    def choose_start(self):
        global startKey
        if self.comboBoxStart.currentText() == 'F1':
            startKey = 16777264
        elif self.comboBoxStart.currentText() == 'F2':
            startKey = 16777265
        elif self.comboBoxStart.currentText() == 'F3':
            startKey = 16777266
        elif self.comboBoxStart.currentText() == 'F4':
            startKey = 16777267
        elif self.comboBoxStart.currentText() == 'F5':
            startKey = 16777268
        elif self.comboBoxStart.currentText() == 'F6':
            startKey = 16777269
        elif self.comboBoxStart.currentText() == 'F7':
            startKey = 16777270
        elif self.comboBoxStart.currentText() == 'F8':
            startKey = 16777271
        elif self.comboBoxStart.currentText() == 'F9':
            startKey = 16777272


    def choose_end(self):
        global endKey
        if self.comboBoxEnd.currentText() == 'F1':
            endKey = 16777264
        elif self.comboBoxEnd.currentText() == 'F2':
            endKey = 16777265
        elif self.comboBoxEnd.currentText() == 'F3':
            endKey = 16777266
        elif self.comboBoxEnd.currentText() == 'F4':
            endKey = 16777267
        elif self.comboBoxEnd.currentText() == 'F5':
            endKey = 16777268
        elif self.comboBoxEnd.currentText() == 'F6':
            endKey = 16777269
        elif self.comboBoxEnd.currentText() == 'F7':
            endKey = 16777270
        elif self.comboBoxEnd.currentText() == 'F8':
            endKey = 16777271
        elif self.comboBoxEnd.currentText() == 'F9':
            endKey = 16777272

    def choose_stop_run(self):
        global stopRunKey
        if self.comboBoxStopRun.currentText() == 'F1':
            stopRunKey = 16777264
        elif self.comboBoxStopRun.currentText() == 'F2':
            stopRunKey = 16777265
        elif self.comboBoxStopRun.currentText() == 'F3':
            stopRunKey = 16777266
        elif self.comboBoxStopRun.currentText() == 'F4':
            stopRunKey = 16777267
        elif self.comboBoxStopRun.currentText() == 'F5':
            stopRunKey = 16777268
        elif self.comboBoxStopRun.currentText() == 'F6':
            stopRunKey = 16777269
        elif self.comboBoxStopRun.currentText() == 'F7':
            stopRunKey = 16777270
        elif self.comboBoxStopRun.currentText() == 'F8':
            stopRunKey = 16777271
        elif self.comboBoxStopRun.currentText() == 'F9':
            stopRunKey = 16777272

