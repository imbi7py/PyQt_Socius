# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Projects\[Py_base]_PyQt-Sorter\pyqt_sorter\pyqt_sorter_widget_info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_info_Dialog(object):
    def setupUi(self, widget_info_Dialog):
        widget_info_Dialog.setObjectName("widget_info_Dialog")
        widget_info_Dialog.resize(895, 719)
        widget_info_Dialog.setMinimumSize(QtCore.QSize(662, 500))
        self.gridLayout = QtWidgets.QGridLayout(widget_info_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.notes_label = QtWidgets.QLabel(widget_info_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes_label.sizePolicy().hasHeightForWidth())
        self.notes_label.setSizePolicy(sizePolicy)
        self.notes_label.setMinimumSize(QtCore.QSize(50, 21))
        font = QtGui.QFont()
        font.setFamily("Fira Code Retina")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.notes_label.setFont(font)
        self.notes_label.setObjectName("notes_label")
        self.gridLayout.addWidget(self.notes_label, 4, 0, 1, 1)
        self.widget_info_buttonBox = QtWidgets.QDialogButtonBox(widget_info_Dialog)
        self.widget_info_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.widget_info_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.widget_info_buttonBox.setObjectName("widget_info_buttonBox")
        self.gridLayout.addWidget(self.widget_info_buttonBox, 6, 2, 1, 1)
        self.widget_name_label = QtWidgets.QLabel(widget_info_Dialog)
        font = QtGui.QFont()
        font.setFamily("Fira Code Retina")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.widget_name_label.setFont(font)
        self.widget_name_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.widget_name_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widget_name_label.setLineWidth(2)
        self.widget_name_label.setMidLineWidth(1)
        self.widget_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.widget_name_label.setObjectName("widget_name_label")
        self.gridLayout.addWidget(self.widget_name_label, 0, 0, 1, 3)
        self.notes_textEdit = QtWidgets.QTextEdit(widget_info_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes_textEdit.sizePolicy().hasHeightForWidth())
        self.notes_textEdit.setSizePolicy(sizePolicy)
        self.notes_textEdit.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.notes_textEdit.setObjectName("notes_textEdit")
        self.gridLayout.addWidget(self.notes_textEdit, 5, 0, 1, 3)
        self.frame = QtWidgets.QFrame(widget_info_Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.doc_url_label = QtWidgets.QLabel(self.frame)
        self.doc_url_label.setMinimumSize(QtCore.QSize(146, 0))
        self.doc_url_label.setObjectName("doc_url_label")
        self.gridLayout_2.addWidget(self.doc_url_label, 0, 0, 1, 1)
        self.doc_url_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.doc_url_lineEdit.setObjectName("doc_url_lineEdit")
        self.gridLayout_2.addWidget(self.doc_url_lineEdit, 0, 1, 1, 1)
        self.open_site_pushButton = QtWidgets.QPushButton(self.frame)
        self.open_site_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ressources/icons/get_info.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_site_pushButton.setIcon(icon)
        self.open_site_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.open_site_pushButton.setCheckable(False)
        self.open_site_pushButton.setAutoDefault(True)
        self.open_site_pushButton.setDefault(True)
        self.open_site_pushButton.setFlat(False)
        self.open_site_pushButton.setObjectName("open_site_pushButton")
        self.gridLayout_2.addWidget(self.open_site_pushButton, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 3)
        self.description_textBrowser = QtWidgets.QTextBrowser(widget_info_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_textBrowser.sizePolicy().hasHeightForWidth())
        self.description_textBrowser.setSizePolicy(sizePolicy)
        self.description_textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.description_textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.description_textBrowser.setAutoFillBackground(True)
        self.description_textBrowser.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.description_textBrowser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.description_textBrowser.setLineWidth(10)
        self.description_textBrowser.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.description_textBrowser.setLineWrapColumnOrWidth(0)
        self.description_textBrowser.setReadOnly(True)
        self.description_textBrowser.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.description_textBrowser.setObjectName("description_textBrowser")
        self.gridLayout.addWidget(self.description_textBrowser, 2, 0, 1, 3)

        self.retranslateUi(widget_info_Dialog)
        self.widget_info_buttonBox.accepted.connect(widget_info_Dialog.accept)
        self.widget_info_buttonBox.rejected.connect(widget_info_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(widget_info_Dialog)

    def retranslateUi(self, widget_info_Dialog):
        _translate = QtCore.QCoreApplication.translate
        widget_info_Dialog.setWindowTitle(_translate("widget_info_Dialog", "Dialog"))
        self.notes_label.setText(_translate("widget_info_Dialog", "Notes:"))
        self.widget_name_label.setText(_translate("widget_info_Dialog", "TextLabel"))
        self.doc_url_label.setText(_translate("widget_info_Dialog", "Documentation URL:"))
        self.description_textBrowser.setHtml(_translate("widget_info_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:\'Fira Code Retina\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


import pyqt_sorter_ressources_rc