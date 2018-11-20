import sys
import platform
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

class CutesZeugExample(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif",10))

        self.setToolTip("This is a <b>QWidget</b> widget")

        #Sample button
        btn=QPushButton('Button', self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(10, 10)

        #Quit button
        qbtn=QPushButton('Quit',self)
        qbtn.setToolTip("this button will close the window")
        qbtn.clicked.connect(QCoreApplication.instance().quit())
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(10, 40)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("My Qt5 window on " + platform.system())

        self.center()
        self.show()

        #central framework on screen
        def center(self):
            #Specify geometry of the main window
            qr= self.frameGeometry()
            #QDesktopWidget provides info about Desctop
            #Figure screen res out and give back center
            cp=QDesktopWidget().availableGeometry().center()
            #center of rectangle to center of window
            qr.moveCenter(cp)
            #top left point to top left window to center window on screen
            self.move(qr.topleft())

        def closeEvent(self, event):
            reply=QMessageBox.question(self, "Message", "Sure you want to quit=", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply==QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
#
#Check if this script is run as the main module
#     if __name__=="__main__":
#         app=QApplication(sys.argv)
#         ex=CutesZeugExample()
#         sys.exit(app.exec_())
#
#CutesZeugExample()
