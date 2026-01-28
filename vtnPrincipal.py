# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(524, 397)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(30, 30, 81, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lblNombre.setFont(font)
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(30, 80, 91, 20))
        self.lblApellido.setFont(font)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(130, 30, 241, 20))
        self.txtNombre.setMaxLength(20)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(130, 80, 241, 20))
        self.txtApellido.setMaxLength(20)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(190, 290, 81, 31))
        self.lblcedula = QLabel(self.centralwidget)
        self.lblcedula.setObjectName(u"lblcedula")
        self.lblcedula.setGeometry(QRect(30, 120, 81, 20))
        self.lblcedula.setFont(font)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(130, 120, 121, 21))
        self.txtCedula.setMaxLength(10)
        self.txtCedula.setCursorPosition(0)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(290, 290, 91, 31))
        self.cbSexo = QComboBox(self.centralwidget)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(140, 210, 121, 21))
        self.lblSexo = QLabel(self.centralwidget)
        self.lblSexo.setObjectName(u"lblSexo")
        self.lblSexo.setGeometry(QRect(40, 210, 61, 20))
        self.lblSexo.setFont(font)
        self.lblemail = QLabel(self.centralwidget)
        self.lblemail.setObjectName(u"lblemail")
        self.lblemail.setGeometry(QRect(30, 160, 81, 20))
        self.lblemail.setFont(font)
        self.txtemail = QLineEdit(self.centralwidget)
        self.txtemail.setObjectName(u"txtemail")
        self.txtemail.setGeometry(QRect(130, 160, 231, 21))
        self.txtemail.setMaxLength(50)
        self.txtemail.setCursorPosition(0)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 524, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombre, self.txtApellido)
        QWidget.setTabOrder(self.txtApellido, self.txtCedula)
        QWidget.setTabOrder(self.txtCedula, self.txtemail)
        QWidget.setTabOrder(self.txtemail, self.cbSexo)
        QWidget.setTabOrder(self.cbSexo, self.btnGuardar)
        QWidget.setTabOrder(self.btnGuardar, self.btnLimpiar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema Administracion de Persona", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lblcedula.setText(QCoreApplication.translate("vtnPrincipal", u"Cedula:", None))
        self.txtCedula.setText("")
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.cbSexo.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero no Decirlo", None))

        self.lblSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo", None))
        self.lblemail.setText(QCoreApplication.translate("vtnPrincipal", u"Email:", None))
        self.txtemail.setText("")
    # retranslateUi

