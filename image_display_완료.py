# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_dispaly.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import glob
import os, shutil
global img_list, save_img, show_list
save_img = []
show_list = []
img_list = []

class Ui_Form(QWidget):
    global img_list, save_img, show_list

    def __init__(self):

        tmp_list = []
        QWidget.__init__(self)

        self.setupUi(self)
        self.show_img()
        # self.pushButton_2.clicked.connect(self.keyPressEvent(Qt.Key_S))
        self.pushButton_2.clicked.connect(self.Save_image)
        self.pushButton_3.clicked.connect(self.FolderOpenClicked)
        self.pushButton_4.clicked.connect(self.Del_image)


    def Save_image(self):

        global img_list, save_img, show_list
        self.status_print("Save")
        if len(img_list) == 0:
            self.status_print("완료")

            return
        tmp = img_list.pop()

        tmp_name = os.path.split(tmp)

        tmp_str = "파일 이름, 경로 ", tmp_name
        self.status_print(tmp_str)
        if tmp_name[1] == "none.jpg":
            self.status_print("저장 완료")
            return
        save_img.append(tmp)

        # print("save img 뒤에서 2개", save_img[-1],save_img[-2])
        if len(img_list) < 3:
            img_list.insert(0, "./none.jpg")
        show_list[4] = show_list[3]
        show_list[3] = tmp
        show_list[2] = img_list[-1]
        show_list[1] = img_list[-2]
        show_list[0] = img_list[-3]
        self.show_img()
        # if len(save_img) >= 1:
        #     self.label_2.setPixmap(QPixmap(save_img[0]))
        # if len(save_img) >= 1:
        # self.label_2.setPixmap(QPixmap(show_list[0]))
        # self.label_3.setPixmap(QPixmap(show_list[1]))
        # self.label_4.setPixmap(QPixmap(show_list[2]))
        # self.label_5.setPixmap(QPixmap(show_list[3]))
        # self.label_6.setPixmap(QPixmap(show_list[4]))

    def Del_image(self):
        global img_list, save_img, show_list


        self.status_print("delete")
        # 삭제 저장 장소
        dir_removed = "./removed"
        self.make_dir(dir_removed)

        if len(img_list) < 3:
            img_list.insert(0, "./none.jpg")

        # if len(img_list) == 0:
        #     print("완료")
        #     return
        tmp = img_list.pop()
        tmp_name = os.path.split(tmp)
        print("삭제파일: ", tmp)
        save_img.append(tmp)
        if len(img_list) < 3:
            img_list.insert(0, "./none.jpg")
        if tmp_name[1] == "none.jpg":
            self.status_print("삭제완료")
            return
        shutil.move(tmp, dir_removed + '\\' + tmp_name[1])
        tmp_str = tmp_name[0], " 파일 ",  tmp_name[1], " 으로 이동 완료"
        self.status_print(tmp_str)
        # print(tmp_name[0], " 파일 ",  tmp_name[1], " 으로 이동 완료")

        show_list[2] = img_list[-1]
        show_list[1] = img_list[-2]
        show_list[0] = img_list[-3]
        self.show_img()
        # for i in range(3):
        #     # show list 2, 3, 4   img_list -1 -2 -3
        #     show_list[i+2] = img_list[(i*(-1)) -1]









    def make_dir(self, dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
            tmp_str = "디렉토리 생성 "+ dirname
            self.status_print(tmp_str)


    def first_show_img(self):
        global show_list, img_list
        show_list[2] = img_list[-1]
        show_list[3] = img_list[-2]
        show_list[4] = img_list[-3]
        show_list[1] = img_list[0]
        show_list[0] = img_list[1]
        self.label_2.setPixmap(QPixmap(show_list[0]))
        self.label_3.setPixmap(QPixmap(show_list[1]))
        self.label_4.setPixmap(QPixmap(show_list[2]))
        self.label_5.setPixmap(QPixmap(show_list[3]))
        self.label_6.setPixmap(QPixmap(show_list[4]))
    def show_img(self):
        global show_list

        while (len(show_list)<5):
            show_list.insert(0, "./none.jpg")

        self.label_2.setPixmap(QPixmap(show_list[0]))
        self.label_3.setPixmap(QPixmap(show_list[1]))
        self.label_4.setPixmap(QPixmap(show_list[2]))
        self.label_5.setPixmap(QPixmap(show_list[3]))
        self.label_6.setPixmap(QPixmap(show_list[4]))

    def keyPressEvent(self, a0: QKeyEventTransition):

        if a0.key() == Qt.Key_D:

            self.Del_image()
        elif a0.key() == Qt.Key_S:

            self.Save_image()

            # # print("Key press")
            #
            # if self.pause:
            #     self.label_pause.setText("key test")
            # else:
            #     self.label_pause.clear()

    def FolderOpenClicked(self):
        global img_list
        fname = QFileDialog.getExistingDirectory(self)
        self.plainTextEdit.appendHtml(fname)
        image_dir = fname +"/*"
        file_list = glob.glob(image_dir)
        img_list = file_list
        for i in range(len(file_list)):
            print(file_list[i])
        # self.label_2.setPixmap(QPixmap(img_list[0]))
        self.first_show_img()
        # self.label_2.setPixmap(QPixmap(save_img[-1]))
        # self.label_3.setPixmap(QPixmap(save_img[-2]))
        # self.label_4.setPixmap(QPixmap(save_img[-3]))
        # self.label_5.setPixmap(QPixmap(save_img[-4]))
        # self.label_6.setPixmap(QPixmap(save_img[-5]))

    def status_print(self, msg_string):

        msg_string = str(msg_string)
        print("status print: ", msg_string)

        self.plainTextEdit.appendPlainText(msg_string)
        # self.lb_4.setText(msg_string)

        #커서 내리기
        cursor = self.plainTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.plainTextEdit.setTextCursor(cursor)





    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1009, 407)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")


        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")


        self.verticalLayout_6.addWidget(self.pushButton_4)






        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 150))
        self.label_2.setMaximumSize(QSize(150, 150))
        # self.label_2.setPixmap(QPixmap(u"image.jpg"))
        self.label_2.setPixmap(QPixmap(u"image.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 150))
        self.label_3.setMaximumSize(QSize(150, 150))
        self.label_3.setPixmap(QPixmap(u"image.jpg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 200))
        self.label_4.setMaximumSize(QSize(200, 200))
        self.label_4.setPixmap(QPixmap(u"image.jpg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 150))
        self.label_5.setMaximumSize(QSize(150, 150))
        self.label_5.setPixmap(QPixmap(u"image.jpg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 150))
        self.label_6.setMaximumSize(QSize(150, 150))
        self.label_6.setPixmap(QPixmap(u"image.jpg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(110, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.plainTextEdit = QPlainTextEdit(Form)
        # self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Open Dir", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Save_image", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"delete Image", None))

        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi

if __name__ ==  '__main__':
    import sys




    app = QApplication([])
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())