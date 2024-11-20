
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(689, 461)
        Dialog.setStyleSheet(u"background-color: rgb(99, 99, 99);")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(4, 6, 681, 451))
        self.textEdit.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: rgb(78, 255, 196);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Project Information:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    <br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Project Name:        	 Anomaly Vigilance Intrusion Detection System),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Domain/Branch:    	 Btech 6th Sem Cyber Security,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    UI-Frontend:          	 </span><span style=\" color:#eaeaea;\">Abhii Verma,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Design:                                  </span><span style=\" color:#eaeaea;\">Abhii Verma,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    UX &amp; Backend Developer:    Abhii Verma,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#eaeaea;\">    IDEA:                      	 Anjali Verma,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Programming Used:    	Python , Apis Libraries,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Apis Framework Used:    	Qt Framework C++/Pyside,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    Dom"
                        "ain:        	Windows OS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12px; color:#eaeaea;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    License: OpenSource LGPL+GNU (Lesser General Public License) version 3.0,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">    <br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">Welcome to the Intrusion Detection Program, a collaborative project initiated by Anjali Verma and Abhii Verma. Developed as part of the B.Tech 6th Semester Cyber Securi"
                        "ty course, this program aims to enhance network security by detecting and preventing unauthorized access.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\">Anjali Verma conceived the idea and spearheaded the project's UI/frontend design, ensuring a user-friendly experience. With a focus on usability and aesthetics, Anjali's contributions have made the program accessible to users of all levels.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\"> Abhii Verma, our backend developer, leveraged Python and various API libraries to create a robust and efficient detection system. His expertise in backend development, coupled with his understanding of network security, has been instrumental in crafting the program's core functionalities.</span></p>\n"
""
                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\"> Utilizing the Qt Framework in C++/PySide, our team has crafted a cross-platform solution compatible with Windows OS. This choice ensures seamless integration into existing systems, maximizing accessibility and usability.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#eaeaea;\"> The Intrusion Detection Program is released under the Open Source LGPL+GNU License (Lesser General Public License) version 3.0, reflecting our commitment to transparency and collaboration within the cybersecurity community</span><span style=\" font-size:12px; color:#000000;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12p"
                        "x; color:#000000;\"> </span><span style=\" font-size:12px; color:#dfdfdf;\">We welcome your feedback and suggestions to help us improve and evolve the program further. Please feel free to reach out to us at:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12px; color:#dfdfdf;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px; color:#000000;\">        </span><span style=\" font-size:12px; color:#6af1a7;\">Feedback ID1</span><span style=\" font-size:12px; color:#000000;\">:  </span><span style=\" font-family:'Google Sans Text'; font-size:11pt; color:#0b57d0; background-color:#f0f4f9;\">anjaliverma19171@gmail.com</span><span style=\" font-size:12px; color:#000000;\"> </span></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" "
                        "font-size:12px; color:#000000;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12px;\">        </span><span style=\" font-size:12px; color:#53f0af;\">Feedback ID2</span><span style=\" font-size:12px;\">:  </span><span style=\" font-family:'Google Sans Text'; font-size:11pt; color:#0b57d0; background-color:#f0f4f9;\">abhi639679@gmail.com</span></li></ul></body></html>", None))
    # retranslateUi

