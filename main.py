#project_name: Intrusion anomaly Detection Program, Btech Cyber Security + AIML 7th Sem
#source Code: Python and Qt Framework

#Copyright (c) [2024] [Abhishek Verma] "Author/Developer"

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to use
#copy, modify, merge, publish, and distribute the Software, provided that the
#Software is **not sold** or distributed for profit or commercial use without
#explicit permission from the author. if developers want to contribute additional
#features, its must required that modified projects should <Opensource>.
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
#THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#Project Condition : Work in Progress...


print("Loading...")
import sys,time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal
import threading
import psutil
import csv
import requests
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QMovie
from PySide6.QtCore import QTimer
import platform

lock=0
notify_x=True

from scapy.all import sniff, IP, TCP
from collections import defaultdict
import socket
import time
import threading


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextEdit,QTableWidget,QTextBrowser,QFrame,
    QWidget)

class Ui_Form_table(object):
    def setupUi(self, Form_table):
        if not Form_table.objectName():
            Form_table.setObjectName(u"Form_table")
        Form_table.resize(948, 486)
        self.tableWidget = QTableWidget(Form_table)
        if (self.tableWidget.columnCount() < 18):
            self.tableWidget.setColumnCount(18)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(0, 0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 951, 491))
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(18)
        self.retranslateUi(Form_table)
        QMetaObject.connectSlotsByName(Form_table)
    def retranslateUi(self, Form_table):
        Form_table.setWindowTitle(QCoreApplication.translate("Form_table", u"Suspicious Programs Datasheet", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_table", u"Time", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_table", u"Process PID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_table", u"Program name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_table", u"Local Addr", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_table", u"Remote Addr", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_table", u"Local Port", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form_table", u"Remote Port", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form_table", u"Status", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form_table", u"Case", None));

class Ui_commander(object):
    def setupUi(self, commander):
        if not commander.objectName():
            commander.setObjectName(u"commander")
        commander.resize(820, 600)
        self.textBrowser = QTextBrowser(commander)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 820, 600))
        self.textBrowser.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 255);\n"
"\n"
"font: 12pt \"Segoe UI\";\n"
"")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.retranslateUi(commander)
        QMetaObject.connectSlotsByName(commander)
    def retranslateUi(self, commander):
        commander.setWindowTitle(QCoreApplication.translate("commander", u"Admin OS Commands", None))
        self.textBrowser.setHtml(QCoreApplication.translate("commander", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">attrib                = display file attributes                       	     tree                = display folder structure graphically</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">call                   = calls a batch file from another one        "
                        "              pause             = pauses the execution of a batch file and shows a message</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">cd                     = change directory                                        	    runas             = start a program as another user</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">cls                    = clear screen                                                 	    rmdir / rd      = delete directory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">cmd                = start command prompt                         	    replace          = replace files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">copy/xcopy   = copy files                                           	    rename          = rename files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">compact        = display/change file compression     	    reg                  = add/read/import/export registry entries</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">comp             = compare file contents                            	    route              = display network routing table, add static routes/type route print for print</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">chkntfs          = d"
                        "isplay/change volume check at startup             shutdown       = shutdown the computer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">chkdsk           = check volumes                                 	    sort                 = sort the screen output</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">driverquery   = display installed devices and their properties  	    systeminfo    = displays computer-specific properties and configurations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">diskpart         = volume management                              	    tracert            = trace routes similar to patchping</span></p>\n"
"<p style=\" margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">defrag            = defragment media                               	    taskkill            = terminate a process or a application</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">diskcopy       = copy floppy disc to another one                            tasklist            = display applications and related task</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">diskcomp     = compare content of two floppy disks                    time                = display/edit the system time</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">dir          "
                        "        = list directory content                                                timeout          = wait any time</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">echo              = text output                                    	    title                 = set title for prompt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">expand          = extract files                                   	    type                = display content of text files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">erase / del     = delete one or more files                       	    pause             = pauses the execution of a batch file and shows a message</span></p>\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">exit                 = exits the command prompt or a batch file     	    tftp                 = transfer files to a TFTP server</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">find                = find files                                    		    telnet              = establish Telnet connection</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">format           = format volumes                               	    ver                   = display operating system version</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt"
                        ";\">ftp                  = transfer files to a FTP server                	    verify              = monitoring whether volumes are written correctly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">fc                   = copare files and display the differences                 vol                  = show volume description and serial numbers of the HDDs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">ftype             = display file type and mapping                  	    w32tm            = setting time synchronisation/time server/time zone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">for                 = for loop                                       		 "
                        "   move              = move/rename files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">gpresult        = display group policies                         	    mkdir              = create a new directory </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">getmac         = display MAC address                           	    netsh              = configure/control/display network components</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">gpupdate     = update group policies                         	    netstat            = display TCP/IP connections and status</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">hostname     = display host name                              	    nslookup        = query the DNS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">ipconfig        = display IP network settings                    	    pathping         = test the connection to a specific IP address </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">label              = change volume name                             	    ping                 = pings the network</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">mountvol     = assign/delete drive mountpoints                            perfmon         = start performance m"
                        "onitor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">mode            = configure interfaces/devices                                   prompt            = change command prompt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">ncpa.cpl       = To open adapter properties                    	    network           = show all network adapters</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">nslookup      = for Dns Lookup &amp; server IP check        	    wifi                   = for checking wifi passwords </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-si"
                        "ze:9pt;\">tracert           = tracing the IP and Ping of website         	    arp /arp -a       = it will show you the table ARP Poisioning</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">_______________________________________________________________________________________________________________________</span></p></body></html>", None))
# This Python file uses the following encoding: utf-8


from window1 import Ui_Form
class window_name(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        print('Started')
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.8)
        self.new7 = QMovie("av1.gif")
        self.form.movie7.setMovie(self.new7)
        self.new7.start()

        self.new2 = QMovie("trans0.gif")
        self.form.movie.setMovie(self.new2)
        self.new2.start()
        self.form.lineEdit_2.returnPressed.connect(self.login)
        self.form.close_btn0.clicked.connect(self.exit0)
    def exit0(self):
        QApplication.quit()
    def login(self):
        global widget2,widget,lock
        if self.form.lineEdit_2.text()=='abhi':
            widget2 = window_name2()
            widget2.show()
            del widget
        else:
            self.form.label_3.setText('Access Denied!')
            self.form.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")


from window4 import Ui_Dialog
class window_about(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form = Ui_Dialog()
        self.form.setupUi(self)
        
        


class UpdateThread(QThread):
    # Define a signal to update data in the main thread
    update_signal = Signal()

    def run(self):
        while True:
            # Sleep for 5 seconds
            time.sleep(10)
            # Emit signal to update data
            self.update_signal.emit()




from window2 import Ui_Form2
class window_name2(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form2 = Ui_Form2()
        self.form2.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.form2.close_btn.clicked.connect(self.exit1)
        self.form2.close_btn.enterEvent = self.close_btn_enter_event
        self.form2.close_btn.leaveEvent = self.close_btn_leave_event

        self.form2.minimise_btn.clicked.connect(self.min1)
        self.form2.lineEdit_ipaddress.returnPressed.connect(self.explore_ip)
        self.form2.pushButton_refresh.clicked.connect(self.explore_ip)
        self.form2.lineEdit_pid.returnPressed.connect(self.process_info)
        self.form2.pushButton_getinfo.clicked.connect(self.process_info)
        self.form2.pushButton_get_ip.clicked.connect(self.get_ip)
        self.form2.pushButton_showallprocess.clicked.connect(self.showall)
        self.form2.pushButton_terminate.clicked.connect(self.terminated)
        self.form2.pushButton_command.clicked.connect(self.commander1)
        self.form2.pushButton_open.clicked.connect(self.data_viewer)
        self.form2.background.mousePressEvent = self.mousePressEvent
        self.form2.background.mouseMoveEvent = self.mouseMoveEvent
        self.form2.dockWidget.setWindowOpacity(0.9)
        self.form2.pushButton_adv.clicked.connect(self.network1)
        self.form2.pushButton_about.clicked.connect(self.about)
        self.update_data()

        self.thread1 = UpdateThread()
        # Connect the signal to the update_data function
        self.thread1.update_signal.connect(self.update_data)
        # Start the thread
        self.thread1.start()

        # Create a QTimer to update the progress bar value
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.update_data)
        #self.timer.start(5000)  # Update every 5000=5 sec

        self.new4 = QMovie("alert55.gif")
        self.form2.movie3.setMovie(self.new4)
        self.new4.start()
        #-------------------------backgrounds animated----------------------
        self.new70 = QMovie("red1.gif")
        self.form2.movie70.setMovie(self.new70)
        self.new70.start()

        self.new72 = QMovie("green.gif")
        self.form2.movie70_2.setMovie(self.new72)
        self.new72.start()

        self.new73 = QMovie("cyber_.gif")
        self.form2.movie70_3.setMovie(self.new73)
        self.new73.start()

        self.new74 = QMovie("blue.gif")
        self.form2.movie70_4.setMovie(self.new74)
        self.new74.start()
        #------------------------End----------------------------------------
        self.new3 = QMovie("radar5.gif")
        self.form2.movie2.setMovie(self.new3)
        self.new3.start()

        self.system_info()
    def about(self):
        global form_about 
        form_about = window_about()
        form_about.show()

    def network1(self):
        
        os.system('start python main2.py')


    def close_btn_enter_event(self,event):
        self.form2.close_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n""background-color: rgb(255, 0, 0);")
    def close_btn_leave_event(self,event):
        self.form2.close_btn.setStyleSheet(u"color: rgb(255, 0, 0);\n""background-color: rgb(84, 84, 84);")
    def commander1(self):
        global widget5
        widget5=window_name5()
        widget5.setWindowOpacity(0.9)
        widget5.show()
        os.system('start cmd')
    def data_viewer(self):
        global widget4
        widget4=window_name4()
        widget4.show()
    def update_data(self):
        self.explore_ip()
        self.showall()

    def mrindia(self):
        self.form2.alert.hide()

    def terminated(self):
        term1=int(self.form2.lineEdit_pid.text())
        try:
            process = psutil.Process(term1)
            process.terminate()
            self.form2.textEdit_4.insertPlainText(f"{process.name()}     {term1} terminated successfully.\n")
        except psutil.NoSuchProcess:
            self.form2.textEdit_4.insertPlainText(f"No process found with PID {term1}.\n")
        except psutil.AccessDenied:
            self.form2.textEdit_4.insertPlainText(f"Access denied to terminate process with PID {term1}.\n")
        #self.showall()
    def process_info(self):
        try:
            pid1=int(self.form2.lineEdit_pid.text())
            self.form2.textEdit_5.setText('\n')
            process = psutil.Process(pid1)
            self.form2.textEdit_5.insertPlainText(f"Process Information for PID {pid1}:\n")
            self.form2.textEdit_5.insertPlainText(f"Name: {process.name()}\n")
            self.form2.textEdit_5.insertPlainText(f"CPU Usage: {process.cpu_percent(interval=1)}%\n")
            memory_info = process.memory_info()
            self.form2.textEdit_5.insertPlainText(f"Memory Used: {memory_info.rss / (1024 * 1024):.2f} MB\n")
            self.form2.textEdit_5.insertPlainText(f"Memory Used Percentage: {process.memory_percent()}%\n")
        except psutil.NoSuchProcess:
            self.form2.textEdit_5.insertPlainText(f"No process found with PID {pid1}.\n")
        except psutil.AccessDenied:
            self.form2.textEdit_5.insertPlainText(f"Access denied to access information for process with PID {pid1}.\n")

    def showall(self):
        self.form2.textEdit_6.setText('PID\tProgram Name\tPort(s)')
        processes = sorted(psutil.process_iter(), key=lambda p: p.name().lower())
       
        for proc in processes:
            pid = proc.pid
            name = proc.name()
            connections = proc.net_connections()
            ports = [conn.laddr.port for conn in connections if conn.status == 'LISTEN']
            if ports:
                self.form2.textEdit_6.insertPlainText(f"{pid}\t{name}\t{ports}\n")
            else:
                self.form2.textEdit_6.insertPlainText(f"{pid}\t{name}\t-\n")

    def notifier(self,proc,conn):
        print('No Telegram api connection')
        #Your can create your own telegram channel bot and use it here
        #You can use python-telegram-bot library to create a bot and send alert messages directly to telegram channel


        #Here is a simple example of how you can do it:



        '''TOKEN = '56465465SDFKJLAKSDJFKJLKJSADFLKJLKWERWERWER-XYZA'
        CHAT_ID = '654625466565'
        MESSAGE =f'[!] Unauthorized access detected!\nProcess PID:{proc.pid:<5} {proc.name():<20} is using sockets\nLocal Address:  {(conn.laddr)[0]}    Port:{(conn.laddr)[1]}\nRemote Address: {(conn.raddr)[0]}    Port:{(conn.raddr)[1]}\nStatus: {conn.status}'

        data1 = {"chat_id": CHAT_ID,"text": MESSAGE}
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        response = requests.post(url, json=data1)
        if response.ok:
            #print("Notified to Owner")
            pass
        else:
            print("Failed to Notified. Error:", response.status_code)'''

                            
        pass
    def explore_ip(self):
        global notify_x
        
        def write_to_csv(data, filename='suspicious_programs.csv'):
            
            # Check if the file exists
            file_exists = os.path.isfile(filename)
            # Write data to CSV
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header if the file is newly created
                if not file_exists:
                    writer.writerow(['Time','Process PID','Program name', 'local addr', 'remote addr','local port','remote port', 'status','Case'])  # Replace 'Column1', 'Column2' with your actual column names
                # Write data
                writer.writerow(data)
        ip_address = self.form2.lineEdit_ipaddress.text()
        self.form2.textEdit.setText("")
        self.form2.textEdit_3.setText("")
        self.form2.label_status.setText('Normal')
        self.form2.label_status.setStyleSheet(u"color: rgb(0, 255, 0);\n""font: 16pt \"Segoe UI\";\n""background-color: rgba(26, 26, 26,0);")
        #print('Search Query:', ip_address)
        local_host_native="127.0.0.1"
        default_ip_address="192.168.0.1"
        #ip_address=input("Type the Network IP address to Monitor|Press 1 for Localhost: ")
        Unauthorized_ports=[]
        if ip_address=='':
            ip_address=local_host_native
        
        # Get all running processes
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Get process connections
                connections = proc.net_connections()
                if connections:
                    #print(f"Process PID: {proc.pid:<5} {proc.name():<20} is using sockets")
                    self.form2.textEdit_3.insertPlainText(f"Process PID: {proc.pid:<5} {proc.name():<20} is using sockets\n")
                    
                    for conn in connections:
                        #print(f"- Local Address: {conn.laddr}, Remote Address: {conn.raddr}, Status: {conn.status}")
                        # Check for unauthorized access (for demonstration purposes)
                        
                        if str((ip_address)) in conn.raddr:
                            
                            Unauthorized_ports.append((conn.raddr)[1])

                            process_id=proc.pid
                            process_name=proc.name()
                            local_addr=(conn.laddr)[0]
                            local_port=(conn.laddr)[1]
                            remote_addr=(conn.raddr)[0]
                            remote_port=(conn.raddr)[1]
                            process_status=conn.status
                            case_1='Suspicious'

                            self.form2.textEdit.insertPlainText("\n")
                            self.form2.textEdit.insertPlainText(f"Process PID:{proc.pid:<5} {proc.name():<20} is using sockets\n")
                            self.form2.textEdit.insertPlainText(f"Local Address:  {(conn.laddr)[0]}    Port:{(conn.laddr)[1]}\n")
                            self.form2.textEdit.insertPlainText(f"Remote Address: {(conn.raddr)[0]}    Port:{(conn.raddr)[1]}\n")
                            self.form2.textEdit.insertPlainText(f"Status: {conn.status}")
                            self.form2.textEdit.insertPlainText("[!] Unauthorized access detected!\n")
                            self.form2.textEdit.insertPlainText("----------+-----------/\n")
                            
                            if notify_x==True:
                                
                                a12=threading.Thread(target=self.notifier,args=(proc,conn))
                                a12.start()
                                notify_x=False

                            import datetime
                            current_datetime = datetime.datetime.now()
                            current_time = current_datetime.strftime("%H:%M:%S %d/%m/%Y")
                            data_to_write = [current_time,process_id,process_name,local_addr,local_port,remote_addr,remote_port,process_status,case_1]
                            #print(data_to_write)
                            write_to_csv(data_to_write)
                            self.form2.alert.raise_()
                            self.form2.movie3.raise_()
                            self.form2.label_status.setText('Found!')
                            self.form2.label_status.setStyleSheet(u"color: rgb(255, 0, 0);\n""font: 16pt \"Segoe UI\";\n""background-color: rgba(26, 26, 26,0);")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


    def system_info(self):
        system_info = platform.uname()
        self.form2.textEdit_2.insertPlainText("System Information:\n\n")
        self.form2.textEdit_2.insertPlainText(f"System: {system_info.system}\n")
        self.form2.textEdit_2.insertPlainText(f"Node Name: {system_info.node}\n")
        self.form2.textEdit_2.insertPlainText(f"Release: {system_info.release}\n")
        self.form2.textEdit_2.insertPlainText(f"Version: {system_info.version}\n")
        self.form2.textEdit_2.insertPlainText(f"Machine: {system_info.machine}\n")
        self.form2.textEdit_2.insertPlainText(f"Processor: {system_info.processor}\n")


    def get_ip(self):
        import psutil
        import socket

        def get_ip_addresses():
            addresses = {}
            for interface, snics in psutil.net_if_addrs().items():
                ip_list = []
                for snic in snics:
                    # Only add IPv4 addresses
                    if snic.family == socket.AF_INET:
                        ip_list.append(snic.address)
                if ip_list:
                    addresses[interface] = ip_list
            return addresses
        
        # Display all IP addresses
        ip_addresses = get_ip_addresses()
        print("IP Addresses of all network interfaces:")
        for interface, ips in ip_addresses.items():
            print(f"Interface: {interface} | IP Address(es): {', '.join(ips)}")



        
    def min1(self):
        widget2.showMinimized()
    def mousePressEvent(self, event):
        from PySide6.QtCore import Qt
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        from PySide6.QtCore import Qt
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.dragPos)
            event.accept()

    def exit1(self):
        QApplication.quit()


from window3 import Ui_Form3
class window_name3(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form3 = Ui_Form3()
        self.form3.setupUi(self)
        self.annu()

    def annu(self):
        # Detection thresholds
        PORT_SCAN_THRESHOLD = 10  # Number of ports accessed in a short time for port scan detection
        SYN_FLOOD_THRESHOLD = 100  # Number of SYN packets for SYN flood detection

        # Define the port you want to monitor
        MONITOR_PORT = 80  # Replace with the port you want to monitor

        # Tracking dictionaries
        port_access_count = defaultdict(set)
        syn_packet_count = defaultdict(int)

        # Suspicious IP and Port records
        suspicious_ips = defaultdict(list)

        # Function to fetch the current IP address dynamically

        detected = False
        def get_current_ip():
            try:
                # Connect to a public server to determine the current IP
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.connect(("8.8.8.8", 80))  # Google's public DNS
                    return s.getsockname()[0]
            except Exception:
                return "No Network"

        # Analyze each captured packet
        def analyze_packet(packet):
            global detected
            while not detected:

                # Dynamically fetch the current IP address
                monitor_ip = get_current_ip()

                # Debugging: Print packet info to confirm capture
                if packet.haslayer(IP):
                    print(f"Captured packet from {packet[IP].src} to {packet[IP].dst}")
                
                # Check if the packet is an IP packet with a TCP layer
                if packet.haslayer(IP) and packet.haslayer(TCP):
                    ip_src = packet[IP].src
                    ip_dst = packet[IP].dst
                    dport = packet[TCP].dport
                    tcp_flags = packet[TCP].flags

                    # Detect SYN packets (indicates potential SYN flood or port scan)
                    if tcp_flags == "S":
                        syn_packet_count[ip_src] += 1
                        # Check for SYN Flood
                        if syn_packet_count[ip_src] > SYN_FLOOD_THRESHOLD:

                            print(f"[ALERT] Possible SYN Flood detected from IP: {ip_src}")
                            suspicious_ips[ip_src].append("Possible SYN Flood")
                            detected = True

                    
                        # Track accessed ports for port scan detection
                        port_access_count[ip_src].add(dport)
                        if len(port_access_count[ip_src]) > PORT_SCAN_THRESHOLD:
                            print(f"[ALERT] Possible Port Scan detected from IP: {ip_src} (accessed ports: {len(port_access_count[ip_src])})")
                            suspicious_ips[ip_src].append(f"Possible Port Scan (accessed {len(port_access_count[ip_src])} ports)")

                    # Check for specific IP address alert
                    if ip_src == monitor_ip or ip_dst == monitor_ip:
                        print(f"[ALERT] Traffic involving monitored IP {monitor_ip} detected!")

                    # Check for specific port alert
                    if dport == MONITOR_PORT:
                        print(f"[ALERT] Traffic involving monitored port {MONITOR_PORT} detected!")

        # Function to reset tracking dictionaries periodically
        def reset_counts():
            global port_access_count, syn_packet_count
            while not detected:
                time.sleep(3)  # Reset every 60 seconds
                port_access_count.clear()
                syn_packet_count.clear()
                print("Counters reset")

        # Function to display suspicious IPs and ports
        def display_suspicious_ips():
            global detected

            
            while not detected:
                time.sleep(1)  # Display suspicious IPs every 10 seconds
                if suspicious_ips:
                    print("\nSuspicious IPs and Activities Detected:")
                    detected = True
                    for ip, activities in suspicious_ips.items():
                        print(f"IP: {ip} - Activities: {', '.join(activities)}")
                    if detected:
                        break

                else:
                    print("No suspicious activity detected.")
                time.sleep(10)

                if detected:
                    break

        # Main function to start IDS
        def start_ids(interface=None):
            print("Starting Intrusion Detection System...")
            # Sniff packets on the specified network interface
            sniff(iface=interface, prn=analyze_packet, store=False)

        # Specify the interface you want to sniff on, e.g., 'Wi-Fi' or 'Ethernet'
        network_interface = "Wi-Fi"  # Replace with your active network interface name

        # Start the reset thread
        reset_thread = threading.Thread(target=reset_counts, daemon=True)
        reset_thread.start()

        # Start the display thread for suspicious IPs
        display_thread = threading.Thread(target=display_suspicious_ips, daemon=True)
        display_thread.start()

        # Start the IDS on the specified interface
        start_ids(interface=network_interface)













from PySide6.QtWidgets import QTableWidgetItem
import pandas as pd
class window_name4(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form4 = Ui_Form_table()
        self.form4.setupUi(self)
        self.load_csv("suspicious_programs.csv")

    def load_csv(self, file_path):
        # Read the CSV file using pandas
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return
        except pd.errors.EmptyDataError:
            print(f"Empty file: {file_path}")
            return

        # Set the number of rows and columns in the table widget
        self.form4.tableWidget.setRowCount(df.shape[0])
        self.form4.tableWidget.setColumnCount(df.shape[1])
        # Populate the table widget with data
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[i, j]))
                self.form4.tableWidget.setItem(i, j, item)

class window_name5(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form5 = Ui_commander()
        self.form5.setupUi(self)
        from PySide6.QtCore import Qt
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window_name()
    widget.show()
    sys.exit(app.exec())
        




        

           
          
            
            
            
           
        
        
        
        
        
        
        

    



        
                

        

                                

                           


                                
                            

                           
                                
                              
                             
                                


                            
                       
                        
    
       



        
        
        


       

    

        


    
    


    
    