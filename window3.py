
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form3(object):
    def setupUi(self, Form3):
        if not Form3.objectName():
            Form3.setObjectName(u"Form3")
        Form3.resize(681, 406)
        self.dockWidget = QDockWidget(Form3)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setGeometry(QRect(0, 9, 681, 391))
        self.dockWidget.setAutoFillBackground(False)
        self.dockWidget.setStyleSheet(u"")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 681, 361))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);\n"
"\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(0, 255,0);")
        self.textEdit.setFrameShape(QFrame.Shape.Box)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(Form3)

        QMetaObject.connectSlotsByName(Form3)
    # setupUi

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(QCoreApplication.translate("Form3", u"Syn Flood Monitoring", None))
#if QT_CONFIG(accessibility)
        self.dockWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.dockWidget.setWindowTitle(QCoreApplication.translate("Form3", u"                                                                        Suspicious Syn Flood List", None))
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("Form3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form3", u"Current Status: No Suspicion found", None))
    # retranslateUi

