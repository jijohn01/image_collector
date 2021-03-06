



# import sys
# # from PySide2.QtWidgets import QApplication, QWidget, \
# #     QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
# from PySide2.QtWidgets import *
# from PySide2.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys
from time import sleep

from PySide2.QtGui import *

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
# import functions
import time
import os
import random
import threading
from tqdm import tqdm

class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setWindowTitle("Crawling")
        self.vb = QVBoxLayout()
        self.setLayout(self.vb)

        self.hb_1 = QHBoxLayout()
        self.hb_2 = QHBoxLayout()
        self.hb_3 = QHBoxLayout()
        self.hb_4 = QHBoxLayout()
        self.hb_5 = QHBoxLayout()
        self.hb_6 = QHBoxLayout()

        self.vb.addLayout(self.hb_1)
        self.vb.addLayout(self.hb_2)
        self.vb.addStretch()
        self.vb.addLayout(self.hb_3)
        self.vb.addStretch()
        self.vb.addLayout(self.hb_4)
        self.vb.addLayout(self.hb_5)
        self.vb.addLayout(self.hb_6)

        # self.vb.addLayout(self.hbTop)
        # self.vb.addLayout(self.hbMid)
        # self.vb.addStretch()
        # self.vb.addLayout(self.hbBot)

        # 버튼, line edit 기능들
            # label
        self.lb1 = QLabel("박스 레이아웃 예제")
        self.lb_1 = QLabel("검색어:")
        self.lb_2 = QLabel("추가 검색어:")
        self.lb_3 = QLabel()
        self.lb_4 = QLabel("현재 진행 상황")


            # 텍스트 입력창
        self.ln = QLineEdit("ln1")
        self.ln_1 = QLineEdit("", self)
        self.ln_2 = QLineEdit("", self)

        # self.ln_1.textChanged.connect(self.lineEditChanged(self.ln_1.text()))
        # self.ln_2.textChanged.connect(self.lineEditChanged(self.ln_2.text()))
        # self.ln_1.textChanged.connect(self.lineEditChanged)
        # self.ln_2.textChanged.connect(self.lineEditChanged)
        self.ln_1.returnPressed.connect(self.lineEditChanged)
        self.ln_2.returnPressed.connect(self.lineEditChanged)


            # 버튼
        self.btn1 = QPushButton("출력")
        self.btn2 = QPushButton("지우기")
        self.btn3 = QPushButton("출력하고 지우기")
        self.btn4 = QPushButton("저장 위치")
        self.btn5 = QPushButton("시작")
            #버튼 기능
        self.btn4.clicked.connect(self.FolderOpenClicked)
        self.btn5.clicked.connect(self.thread_crawl)

            # 텍스트 창
        self.text_line = QTextEdit()

        # 지정된 공간에 입력
            # 1 번째 줄
        self.hb_1.addWidget(self.lb_1)
        self.hb_1.addWidget(self.ln_1)
        self.hb_1.addWidget(self.lb_2)
        self.hb_1.addWidget(self.ln_2)
        self.hb_1.addWidget(self.btn4)

            # 2 번째 줄
        self.hb_2.addWidget(self.lb_3)

            # 3 번째 줄
        self.hb_3.addWidget(self.text_line)

            # 4 번째 줄
        # self.createStatusBar()
        self.pb1 = QProgressBar()
        self.pb1.setMinimum(0)
        self.pb1.setMaximum(100)
        self.pb1.setValue(0)
        self.hb_4.addWidget(self.lb_4)
        self.hb_4.addWidget(self.pb1)


            # 5 번째 줄
        self.hb_5.addWidget(self.btn5)

        # 폴더 str
        # self.folder_string



        # self.hbTop.addWidget(self.lbl)
        # self.hbMid.addWidget(self.ln)
        # self.hbMid.addWidget(self.btn1)
        # self.hbBot.addWidget(self.btn2)
        # self.hbBot.addStretch()
        # self.hbBot.addWidget(self.btn3)
        #
        # self.btn1.clicked.connect(self.prt_line)
        # self.btn2.clicked.connect(self.del_line)
        # self.btn3.clicked.connect(self.prt_del)
    def lineEditChanged(self):
        print("검색어: ", self.ln_1.text(), "부 검색어", self.ln_2.text())

        # self.text_line.append(msg_string)

        # self.statusBar.showMessage(self.lineEdit.text())

    def prt_line(self):
        print(self.ln.text())

    def del_line(self):
        self.ln.clear()

    def prt_del(self):
        self.prt_line()
        self.del_line()

    def FolderOpenClicked(self):
        fname = QFileDialog.getExistingDirectory(self)
        self.lb_3.setText(fname)
        # self.folder_string = frame
        # self.label.setText

    def createStatusBar(self):

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setValue(10)
        # self.setStatusBar(self.statusBar)
    def thread_crawl(self):
        t = threading.Thread(target=self.test_func)
        t.daemon = True
        t.start()
        # t.join()
    def status_print(self, msg_string):

        print("status print: ", msg_string)
        # self.text_line.append(msg_string)
        # self.lb_4.setText(msg_string)
        #
        # #커서 내리기
        # cursor = self.text_line.textCursor()
        # cursor.movePosition(QTextCursor.End)
        # self.text_line.setTextCursor(cursor)
        # self.text_line.moveCursor(self.text_line.cursor.left)
        # self.text_line.moveCursor()
        # self.statusBar.showMessage(msg_string)
    def statusbar_update(self, tmp):
        pass
        # self.pb1.setValue(tmp)
    def test_func(self):
        # self.statusBar.showMessage("self.lineEdit.text()")

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')            # Chrome internet not open
        # options.add_argument('disable-gpu')         # Chrome internet not open
        options.add_argument('window-size=1920x1080')


        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        action = webdriver.common.action_chains.ActionChains(driver)

        # f =functions.function(driver)

        # keyword =input("수집할 키워드 : ")
        # add = input("키워드 뒤에 덧붙일 키워드 : 예) 매장,강남점,왕십리점")

        # keyword = "맥도날드"


        #폴더 선택
        folder_string = self.lb_3.text()
        msg_string = "저장 위치: " + folder_string
        self.status_print(msg_string)
        print(folder_string)

        keyword = self.ln_1.text()

        tmp = self.ln_2.text()
        tmp = tmp.split()
        temp = ['']
        temp.extend(tmp)
        add_keywords = temp
        # add_keywords = ['', "매장"]
        # add_keywords = ['',"매장","간판","앞"]


        search_engines = ['naver', 'daum']
        search_address = {'naver': 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=',
                          'daum': 'https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q='}
        more_btn_css = {'naver': 'a.btn_more._more', 'daum': 'a.expender.open'}
        img_css = {'naver': 'img._img', 'daum': 'img.thumb_img'}
        img_list = []


        msg_string = "키워드 검색중..."
        self.status_print(msg_string)
        # self.statusBar.showMessage("키워드 검색중...")
        # print("키워드 검색중...")
        for search_engine in search_engines:

            # print('\n검색엔진 : {}'.format(search_engine))
            msg_string = '\n검색엔진 : {}'.format(search_engine)
            self.status_print(msg_string)
            for add_keyword in add_keywords:
                init_address = search_address[search_engine] + keyword + ' ' + add_keyword

                # print('\n{} {}'.format(keyword, add_keyword))
                msg_string = '\n{} {}'.format(keyword, add_keyword)
                self.status_print(msg_string)


                driver.get(init_address)

                # 페이지 다운목록 넓히기
                body = driver.find_element_by_css_selector('body')
                while (True):
                    for i in range(30):
                        body.send_keys(Keys.PAGE_DOWN)
                        time.sleep(0.1)
                    time.sleep(1)
                    try:
                        driver.find_element_by_css_selector(more_btn_css[search_engine]).click()
                    except:
                        break
                for i in range(10):
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.1)

                # 이미지 긁어오기
                imgs = driver.find_elements_by_css_selector(img_css[search_engine])
                time.sleep(1)


                num_max = len(imgs)

                self.pb1.setMaximum(num_max)


                for idx, img in enumerate(imgs):
                    # print("idx ", idx, " img: ", img)

                    if idx%20 == 0:
                        self.statusbar_update(idx)
                    elif idx == num_max:
                        self.statusbar_update(idx)

                    # t = threading.Thread(target=self.statusbar_update(idx))
                    # t.start()
                    if 'http' in img.get_attribute('src'):
                        img_list.append(img.get_attribute('src'))
                self.pb1.setValue(num_max)
                time.sleep(1)
                self.pb1.setValue(0)


        # print(img_list)
        # print('이미지 수집중...')
        msg_string = '이미지 수집중...'
        self.status_print(msg_string)

        driver.close()
        # save
        try:
            os.mkdir(folder_string + '/{}'.format(keyword))
        except:
            pass

        # print("개수 {}".format(len(img_list)))
        msg_string = "개수 {}".format(len(img_list))

        self.status_print(msg_string)

        # print("저장중....")
        msg_string = "저장중...."
        num_max = len(img_list)
        self.pb1.setMaximum(num_max)



        self.pb1.setMaximum(num_max)
        self.status_print(msg_string)
        for idx, link in enumerate(img_list):

            if idx % 20 == 0:
                self.statusbar_update(idx)
            elif idx == num_max:
                self.statusbar_update(num_max)

            # if idx%100 == 0:                  #업데이트 횟수 줄이기
            #     t = threading.Thread(target=self.statusbar_update(idx))
            #     t.start



            start = link.rfind('.')
            end = link.rfind('&')
            # print(link[start:end])
            file_type = link[start:end]
            # print(img_name)
            try:
                urlretrieve(link, folder_string + '/{}/{}_{}{}'.format(keyword, keyword, idx, ".jpg"))
                time.sleep(random.randrange(1, 10) / 100)
                if idx%100 == 0:
                    print(idx, "번째 저장중")
            except:
                print("네트워크 불안 저장 실패")

        # print("저장완료!! 갯수: {}".format(len(img_list)))
        msg_string = "저장완료!! 갯수: {}".format(len(img_list))
        time.sleep(1)
        self.statusbar_update(0)
        self.status_print(msg_string)



app = QApplication([])
form = Form()
form.show()
sys.exit(app.exec_())