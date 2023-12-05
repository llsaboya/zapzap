from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/home.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(986, 666)
        Home.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Home)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuUsers = QtWidgets.QFrame(parent=Home)
        self.menuUsers.setMinimumSize(QtCore.QSize(50, 0))
        self.menuUsers.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menuUsers.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menuUsers.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menuUsers.setObjectName("menuUsers")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuUsers)
        self.verticalLayout.setContentsMargins(5, 6, 5, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QVBoxLayout()
        self.menu.setContentsMargins(0, -1, 0, -1)
        self.menu.setSpacing(8)
        self.menu.setObjectName("menu")
        self.verticalLayout.addLayout(self.menu)
        self.line_2 = QtWidgets.QFrame(parent=self.menuUsers)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.btnHomeNewAccount = QtWidgets.QPushButton(parent=self.menuUsers)
        self.btnHomeNewAccount.setText("")
        self.btnHomeNewAccount.setObjectName("btnHomeNewAccount")
        self.verticalLayout.addWidget(self.btnHomeNewAccount)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnHomeNewChat = QtWidgets.QPushButton(parent=self.menuUsers)
        self.btnHomeNewChat.setText("")
        self.btnHomeNewChat.setObjectName("btnHomeNewChat")
        self.verticalLayout.addWidget(self.btnHomeNewChat)
        self.line = QtWidgets.QFrame(parent=self.menuUsers)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.btnHomeSetting = QtWidgets.QPushButton(parent=self.menuUsers)
        self.btnHomeSetting.setText("")
        self.btnHomeSetting.setObjectName("btnHomeSetting")
        self.verticalLayout.addWidget(self.btnHomeSetting)
        self.btnHomePerfil = QtWidgets.QPushButton(parent=self.menuUsers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHomePerfil.sizePolicy().hasHeightForWidth())
        self.btnHomePerfil.setSizePolicy(sizePolicy)
        self.btnHomePerfil.setMinimumSize(QtCore.QSize(0, 40))
        self.btnHomePerfil.setText("")
        self.btnHomePerfil.setFlat(False)
        self.btnHomePerfil.setObjectName("btnHomePerfil")
        self.verticalLayout.addWidget(self.btnHomePerfil)
        self.btnHomeSetting.raise_()
        self.btnHomePerfil.raise_()
        self.line.raise_()
        self.btnHomeNewChat.raise_()
        self.line_2.raise_()
        self.btnHomeNewAccount.raise_()
        self.horizontalLayout.addWidget(self.menuUsers)
        self.userStacked = QtWidgets.QStackedWidget(parent=Home)
        self.userStacked.setObjectName("userStacked")
        self.horizontalLayout.addWidget(self.userStacked)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        
        self.btnHomeNewAccount.setToolTip(_("New account"))
        self.btnHomeNewChat.setToolTip(_("New chat"))
        self.btnHomeSetting.setToolTip(_("Settings"))
        self.btnHomePerfil.setToolTip(_("Perfil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Home = QtWidgets.QWidget()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec())
