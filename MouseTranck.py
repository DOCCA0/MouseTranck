import json
import shutil
import sys
import threading
from time import sleep
import pynput
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pynput.keyboard import  Key
from pynput.mouse import Button
import First
import recordWindow

mouse_controller=pynput.mouse.Controller()
keyboard_controller=pynput.keyboard.Controller()
running=False
def end_listen(key):
    global running
    if key==First.key_dic[recordWindow.stopRunKey]:
        try:
            running=False
            keyboard_listener.stop()
        except:
            print('停止运行脚本失败')

keyboard_listener = pynput.keyboard.Listener(on_press=end_listen)
first: First.Ui_Main


# 更新label的slot
def change_hot_key():
    first.label_hot_key.setText('请分别设置：\n录制启动热键：%s\n录制终止热键: %s\n脚本运行时终止热键: %s' % (
        str(First.key_dic[recordWindow.startKey]), str(First.key_dic[recordWindow.endKey]),str(First.key_dic[recordWindow.stopRunKey])))


def savefile():
    try:
        fname = QFileDialog.getSaveFileName(first, '保存脚本', './%s' % First.filename, '*.txt', '*.txt')
        shutil.move('./%s' % First.filename, fname[0])
    except:
        pass


def openfile():
    try:
        fname = QFileDialog.getOpenFileName(first, '打开脚本', '', '*.txt', '*.txt')
        # 开始解析json
        with open(fname[0], 'r') as fileholder:
            time, action = [], []
            string_json = fileholder.read()
            json_objs = json.loads(string_json)
            for i in json_objs:
                time.append(float(i['time']))
                action.append(i['action'])
        first.showMinimized()
        global running
        running=True
        threading.Thread(target=start_run(time,action),daemon=True).start()



    except:
        pass


# 开始运行脚本
def start_run(time,action):
    global running,keyboard_listener
    keyboard_listener=pynput.keyboard.Listener(on_press=end_listen)
    keyboard_listener.start()
    for i in range(len(time)):
        if running:
            sleep(time[i])
            act=str.split(action[i],' ')
            if len(act)==5or len(act)==3:
                mouse_action(act)
            else:
                keyboard_action(act)

    msg=QtWidgets.QMessageBox(first)
    if running:
        msg.setWindowTitle("运行完成")
        msg.setText("您的脚本已经运行完成，你可以返回录制新的脚本")
        running=False
    else:
        msg.setWindowTitle("运行结束")
        msg.setText("您手动结束了进程，你可以返回录制新的脚本")
    first.showNormal()
    msg.show()
    try:
        keyboard_listener.stop()
    except:
        pass


def mouse_action(act):
    mouse_controller.position=(int(act[1]), int(act[2]))
    if act[0]=='click':
        if act[-1]=='True':
            if len(act[3])==11:
                mouse_controller.press(Button.left)
            else:
                mouse_controller.press(Button.right)
        else:
            if len(act[3]) == 11:
                mouse_controller.release(Button.left)
            else:
                mouse_controller.release(Button.right)
    elif act[0]=='move':
        mouse_controller.position=(act[1],act[2])
    else:
        mouse_controller.scroll(72*int(act[3]),72*int(act[4]))

def keyboard_action(act):
    key=act[1].replace("'",'')
    if len(act[1])!=3:
        key=key[4:]
        key=getattr(Key,key)
    if act[0]=='press':
        keyboard_controller.press(key)
    else:
        keyboard_controller.release(key)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    first = First.Ui_Main()
    r = recordWindow.RecordWindow()
    first.show()
    first.pushButtonRecord.clicked.connect(r.show)
    first.pushButtonSaveFile.clicked.connect(savefile)
    first.pushButtonStart.clicked.connect(openfile)
    r.comboBoxStart.activated.connect(change_hot_key)
    r.comboBoxEnd.activated.connect(change_hot_key)
    r.comboBoxStopRun.activated.connect(change_hot_key)
    sys.exit(app.exec_())

