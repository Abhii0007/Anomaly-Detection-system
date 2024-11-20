
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_Form2(object):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(1366, 749)
        Form2.setMinimumSize(QSize(500, 300))
        Form2.setMaximumSize(QSize(1366, 768))
        Form2.setBaseSize(QSize(1366, 768))
        Form2.setWindowOpacity(1.000000000000000)
        Form2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        Form2.setStyleSheet(u"")
        Form2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.background = QLabel(Form2)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1366, 768))
        self.background.setStyleSheet(u"\n"
"\n"
"font: 14pt \"Segoe UI\";\n"
"color: rgb(255, 85, 0);")
        self.background.setFrameShape(QFrame.Shape.NoFrame)
        self.background.setFrameShadow(QFrame.Shadow.Sunken)
        self.background.setPixmap(QPixmap(u"back.png"))
        self.background.setScaledContents(True)
        self.lineEdit_pid = QLineEdit(Form2)
        self.lineEdit_pid.setObjectName(u"lineEdit_pid")
        self.lineEdit_pid.setGeometry(QRect(527, 540, 151, 22))
        self.lineEdit_pid.setStyleSheet(u"")
        self.lineEdit_ipaddress = QLineEdit(Form2)
        self.lineEdit_ipaddress.setObjectName(u"lineEdit_ipaddress")
        self.lineEdit_ipaddress.setGeometry(QRect(526, 566, 241, 21))
        self.lineEdit_ipaddress.setClearButtonEnabled(False)
        self.close_btn = QPushButton(Form2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(1155, 70, 51, 24))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(84, 84, 84);")
        self.minimise_btn = QPushButton(Form2)
        self.minimise_btn.setObjectName(u"minimise_btn")
        self.minimise_btn.setGeometry(QRect(1119, 70, 31, 24))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.minimise_btn.setFont(font1)
        self.minimise_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimise_btn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(84, 84, 84);")
        self.progressBar = QProgressBar(Form2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(220, 580, 121, 21))
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setStyleSheet(u"color: rgb(0, 221, 255);")
        self.progressBar.setMaximum(20)
        self.progressBar.setValue(3)
        self.dockWidget = QDockWidget(Form2)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setGeometry(QRect(200, 153, 321, 190))
        self.dockWidget.setMaximumSize(QSize(321, 190))
        self.dockWidget.setAutoFillBackground(False)
        self.dockWidget.setStyleSheet(u"")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 321, 211))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 0,0);")
        self.textEdit.setFrameShape(QFrame.Shape.Box)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.dockWidget_3 = QDockWidget(Form2)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidget_3.setGeometry(QRect(524, 153, 312, 190))
        self.dockWidget_3.setMaximumSize(QSize(312, 190))
        self.dockWidget_3.setFloating(False)
        self.dockWidget_3.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.textEdit_2 = QTextEdit(self.dockWidgetContents_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 312, 211))
        self.textEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);\n"
"color: rgb(0, 255, 255);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"")
        self.textEdit_2.setFrameShape(QFrame.Shape.Panel)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(1)
        self.textEdit_2.setMidLineWidth(0)
        self.textEdit_2.setLineWrapColumnOrWidth(0)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        self.pushButton_terminate = QPushButton(Form2)
        self.pushButton_terminate.setObjectName(u"pushButton_terminate")
        self.pushButton_terminate.setGeometry(QRect(758, 540, 71, 24))
        self.pushButton_terminate.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_terminate.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_terminate.setStyleSheet(u"background-color: rgb(20, 20, 20);\n"
"\n"
"color: rgb(255, 0, 0);")
        self.pushButton_terminate.setCheckable(False)
        self.pushButton_getinfo = QPushButton(Form2)
        self.pushButton_getinfo.setObjectName(u"pushButton_getinfo")
        self.pushButton_getinfo.setGeometry(QRect(683, 540, 71, 24))
        self.pushButton_getinfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_getinfo.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_getinfo.setStyleSheet(u"background-color: rgb(52, 52, 52);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_getinfo.setCheckable(False)
        self.pushButton_refresh = QPushButton(Form2)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setGeometry(QRect(769, 566, 61, 24))
        self.pushButton_refresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_refresh.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_refresh.setStyleSheet(u"background-color: rgb(52, 52, 52);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_refresh.setCheckable(False)
        self.dockWidget_4 = QDockWidget(Form2)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidget_4.setGeometry(QRect(200, 347, 321, 190))
        self.dockWidget_4.setMaximumSize(QSize(321, 190))
        self.dockWidget_4.setAutoFillBackground(False)
        self.dockWidget_4.setFloating(False)
        self.dockWidget_4.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.textEdit_4 = QTextEdit(self.dockWidgetContents_4)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(0, 0, 321, 201))
        self.textEdit_4.setFont(font2)
        self.textEdit_4.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 255, 0);")
        self.textEdit_4.setFrameShape(QFrame.Shape.Box)
        self.textEdit_4.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        self.dockWidget_5 = QDockWidget(Form2)
        self.dockWidget_5.setObjectName(u"dockWidget_5")
        self.dockWidget_5.setGeometry(QRect(524, 347, 312, 190))
        self.dockWidget_5.setMaximumSize(QSize(312, 190))
        self.dockWidget_5.setFloating(False)
        self.dockWidget_5.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.textEdit_5 = QTextEdit(self.dockWidgetContents_5)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(0, 0, 312, 211))
        self.textEdit_5.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);\n"
"color: rgb(0, 255, 255);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"")
        self.textEdit_5.setFrameShape(QFrame.Shape.Panel)
        self.textEdit_5.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_5.setLineWidth(1)
        self.textEdit_5.setMidLineWidth(0)
        self.textEdit_5.setLineWrapColumnOrWidth(0)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        self.label = QLabel(Form2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 549, 101, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 14pt \"Segoe UI\";\n"
"background-color: rgba(26, 26, 26,0);")
        self.label_status = QLabel(Form2)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setEnabled(True)
        self.label_status.setGeometry(QRect(647, 96, 101, 31))
        self.label_status.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"\n"
"background-color: rgba(26, 26, 26,0);\n"
"font: 16pt \"Segoe UI\";")
        self.pushButton_showallprocess = QPushButton(Form2)
        self.pushButton_showallprocess.setObjectName(u"pushButton_showallprocess")
        self.pushButton_showallprocess.setGeometry(QRect(719, 593, 111, 24))
        self.pushButton_showallprocess.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_showallprocess.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_showallprocess.setStyleSheet(u"background-color: rgb(52, 52, 52);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_showallprocess.setCheckable(False)
        self.alert = QLabel(Form2)
        self.alert.setObjectName(u"alert")
        self.alert.setEnabled(True)
        self.alert.setGeometry(QRect(349, 534, 141, 91))
        self.alert.setFrameShape(QFrame.Shape.NoFrame)
        self.alert.setTextFormat(Qt.TextFormat.AutoText)
        self.alert.setPixmap(QPixmap(u"alert.png"))
        self.alert.setScaledContents(True)
        self.alert.setWordWrap(False)
        self.tabWidget = QTabWidget(Form2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(840, 100, 371, 521))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.East)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textEdit_3 = QTextEdit(self.tab)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QRect(0, 0, 349, 515))
        self.textEdit_3.setFont(font2)
        self.textEdit_3.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 255, 0);")
        self.textEdit_3.setFrameShape(QFrame.Shape.Box)
        self.textEdit_3.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.movie2 = QLabel(self.tab)
        self.movie2.setObjectName(u"movie2")
        self.movie2.setGeometry(QRect(250, 410, 81, 81))
        self.movie2.setScaledContents(True)
        self.label_scanning = QLabel(self.tab)
        self.label_scanning.setObjectName(u"label_scanning")
        self.label_scanning.setEnabled(True)
        self.label_scanning.setGeometry(QRect(250, 480, 81, 31))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_scanning.setFont(font4)
        self.label_scanning.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgba(26, 26, 26,0);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textEdit_6 = QTextEdit(self.tab_2)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setEnabled(True)
        self.textEdit_6.setGeometry(QRect(0, 0, 349, 515))
        self.textEdit_6.setFont(font2)
        self.textEdit_6.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 0, 127);")
        self.textEdit_6.setFrameShape(QFrame.Shape.Box)
        self.textEdit_6.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.tabWidget.addTab(self.tab_2, "")
        self.movie3 = QLabel(Form2)
        self.movie3.setObjectName(u"movie3")
        self.movie3.setGeometry(QRect(399, 556, 41, 41))
        self.movie3.setScaledContents(True)
        self.pushButton_about = QPushButton(Form2)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setGeometry(QRect(471, 72, 61, 24))
        self.label_2 = QLabel(Form2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(193, 104, 81, 51))
        self.label_2.setPixmap(QPixmap(u"logo_front.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(Form2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(218, 108, 361, 41))
        self.label_3.setPixmap(QPixmap(u"123.png"))
        self.label_3.setScaledContents(True)
        self.pushButton_command = QPushButton(Form2)
        self.pushButton_command.setObjectName(u"pushButton_command")
        self.pushButton_command.setGeometry(QRect(336, 72, 71, 24))
        self.pushButton_open = QPushButton(Form2)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setGeometry(QRect(212, 72, 61, 24))
        self.pushButton_adv = QPushButton(Form2)
        self.pushButton_adv.setObjectName(u"pushButton_adv")
        self.pushButton_adv.setGeometry(QRect(408, 72, 61, 24))
        self.pushButton_save = QPushButton(Form2)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(274, 72, 61, 24))
        self.movie70 = QLabel(Form2)
        self.movie70.setObjectName(u"movie70")
        self.movie70.setGeometry(QRect(200, 177, 321, 165))
        self.movie70.setAutoFillBackground(False)
        self.movie70.setStyleSheet(u"background-color: rgba(0, 0, 0,0.8);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 0,0);")
        self.movie70.setFrameShape(QFrame.Shape.WinPanel)
        self.movie70.setScaledContents(True)
        self.movie70_2 = QLabel(Form2)
        self.movie70_2.setObjectName(u"movie70_2")
        self.movie70_2.setGeometry(QRect(200, 372, 321, 165))
        self.movie70_2.setAutoFillBackground(False)
        self.movie70_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0.8);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 255,0);")
        self.movie70_2.setFrameShape(QFrame.Shape.WinPanel)
        self.movie70_2.setScaledContents(True)
        self.movie70_3 = QLabel(Form2)
        self.movie70_3.setObjectName(u"movie70_3")
        self.movie70_3.setGeometry(QRect(524, 178, 312, 165))
        self.movie70_3.setAutoFillBackground(False)
        self.movie70_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0.8);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 255,255);")
        self.movie70_3.setFrameShape(QFrame.Shape.WinPanel)
        self.movie70_3.setScaledContents(True)
        self.movie70_4 = QLabel(Form2)
        self.movie70_4.setObjectName(u"movie70_4")
        self.movie70_4.setGeometry(QRect(524, 371, 312, 165))
        self.movie70_4.setAutoFillBackground(False)
        self.movie70_4.setStyleSheet(u"background-color: rgba(0, 0, 0,0.8);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 255,255);")
        self.movie70_4.setFrameShape(QFrame.Shape.WinPanel)
        self.movie70_4.setScaledContents(True)
        self.pushButton_get_ip = QPushButton(Form2)
        self.pushButton_get_ip.setObjectName(u"pushButton_get_ip")
        self.pushButton_get_ip.setGeometry(QRect(609, 595, 100, 20))
        self.pushButton_get_ip.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_get_ip.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_get_ip.setStyleSheet(u"background-color: rgb(52, 52, 52);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton_get_ip.setCheckable(False)
        self.background.raise_()
        self.lineEdit_pid.raise_()
        self.lineEdit_ipaddress.raise_()
        self.pushButton_terminate.raise_()
        self.pushButton_getinfo.raise_()
        self.pushButton_refresh.raise_()
        self.label_status.raise_()
        self.pushButton_showallprocess.raise_()
        self.minimise_btn.raise_()
        self.close_btn.raise_()
        self.pushButton_about.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_command.raise_()
        self.pushButton_open.raise_()
        self.pushButton_adv.raise_()
        self.pushButton_save.raise_()
        self.movie70.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        self.alert.raise_()
        self.movie3.raise_()
        self.dockWidget.raise_()
        self.tabWidget.raise_()
        self.movie70_2.raise_()
        self.dockWidget_4.raise_()
        self.movie70_3.raise_()
        self.movie70_4.raise_()
        self.dockWidget_3.raise_()
        self.dockWidget_5.raise_()
        self.pushButton_get_ip.raise_()

        self.retranslateUi(Form2)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"Intrusion Detection Program", None))
        self.background.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_pid.setToolTip(QCoreApplication.translate("Form2", u"type the Program ID", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_pid.setPlaceholderText(QCoreApplication.translate("Form2", u"Enter PID to get Info...", None))
        self.lineEdit_ipaddress.setText("")
        self.lineEdit_ipaddress.setPlaceholderText(QCoreApplication.translate("Form2", u"Enter the IP Address |Default: Localhost...", None))
        self.close_btn.setText(QCoreApplication.translate("Form2", u"X", None))
        self.minimise_btn.setText(QCoreApplication.translate("Form2", u"-", None))
#if QT_CONFIG(accessibility)
        self.dockWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.dockWidget.setWindowTitle(QCoreApplication.translate("Form2", u"                         Suspicious Variants List", None))
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("Form2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form2", u"Current Status: No Suspicion found", None))
        self.dockWidget_3.setWindowTitle(QCoreApplication.translate("Form2", u"                           System Information", None))
#if QT_CONFIG(tooltip)
        self.textEdit_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit_2.setHtml(QCoreApplication.translate("Form2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("Form2", u"System Info", None))
#if QT_CONFIG(tooltip)
        self.pushButton_terminate.setToolTip(QCoreApplication.translate("Form2", u"terminate using pid", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_terminate.setText(QCoreApplication.translate("Form2", u"Terminate", None))
#if QT_CONFIG(tooltip)
        self.pushButton_getinfo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_getinfo.setText(QCoreApplication.translate("Form2", u"Get Info", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Form2", u"Refresh", None))
        self.dockWidget_4.setWindowTitle(QCoreApplication.translate("Form2", u"                              Terminated Programs", None))
#if QT_CONFIG(tooltip)
        self.textEdit_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit_4.setHtml(QCoreApplication.translate("Form2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("Form2", u"No Terminated Programs", None))
        self.dockWidget_5.setWindowTitle(QCoreApplication.translate("Form2", u"                                       Program Info", None))
#if QT_CONFIG(tooltip)
        self.textEdit_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit_5.setHtml(QCoreApplication.translate("Form2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_5.setPlaceholderText(QCoreApplication.translate("Form2", u"No Suspicion found", None))
        self.label.setText(QCoreApplication.translate("Form2", u"Risk %", None))
        self.label_status.setText(QCoreApplication.translate("Form2", u"Normal", None))
#if QT_CONFIG(tooltip)
        self.pushButton_showallprocess.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_showallprocess.setText(QCoreApplication.translate("Form2", u"Show all Processes", None))
        self.alert.setText("")
#if QT_CONFIG(tooltip)
        self.textEdit_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit_3.setHtml(QCoreApplication.translate("Form2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Programs using Networks and ports</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("Form2", u"Prorgams using Networks Ports", None))
        self.movie2.setText(QCoreApplication.translate("Form2", u"TextLabel", None))
        self.label_scanning.setText(QCoreApplication.translate("Form2", u"Scanning...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form2", u"Sockets", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("Form2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ALL Currently Running Processes</p></body></html>", None))
        self.textEdit_6.setPlaceholderText(QCoreApplication.translate("Form2", u"Prorgams using Networks Ports", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form2", u"Running Processes", None))
#if QT_CONFIG(tooltip)
        self.movie3.setToolTip(QCoreApplication.translate("Form2", u"Threat Found", None))
#endif // QT_CONFIG(tooltip)
        self.movie3.setText("")
        self.pushButton_about.setText(QCoreApplication.translate("Form2", u"About", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form2", u"Project Logo", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText("")
        self.pushButton_command.setText(QCoreApplication.translate("Form2", u"Command", None))
#if QT_CONFIG(tooltip)
        self.pushButton_open.setToolTip(QCoreApplication.translate("Form2", u"Showing the Datalog sheet", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_open.setText(QCoreApplication.translate("Form2", u"Open", None))
        self.pushButton_adv.setText(QCoreApplication.translate("Form2", u"Adv", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form2", u"Save", None))
        self.movie70.setText("")
        self.movie70_2.setText("")
        self.movie70_3.setText("")
        self.movie70_4.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_get_ip.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_get_ip.setText(QCoreApplication.translate("Form2", u"Get All IP", None))
    # retranslateUi

