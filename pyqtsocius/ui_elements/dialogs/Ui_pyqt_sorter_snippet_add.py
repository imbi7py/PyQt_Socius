# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My_Repos\PyQt_Socius\designer_files\pyqt_sorter_snippet_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_snippet_Dialog(object):
    def setupUi(self, add_snippet_Dialog):
        add_snippet_Dialog.setObjectName("add_snippet_Dialog")
        add_snippet_Dialog.resize(500, 750)
        add_snippet_Dialog.setMinimumSize(QtCore.QSize(500, 750))
        self.gridLayout = QtWidgets.QGridLayout(add_snippet_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.snippet_buttonBox = QtWidgets.QDialogButtonBox(add_snippet_Dialog)
        self.snippet_buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.snippet_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.snippet_buttonBox.setObjectName("snippet_buttonBox")
        self.gridLayout.addWidget(self.snippet_buttonBox, 0, 2, 4, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.snippet_label = QtWidgets.QLabel(add_snippet_Dialog)
        self.snippet_label.setObjectName("snippet_label")
        self.verticalLayout.addWidget(self.snippet_label)
        self.snippet_data_textEdit = QtWidgets.QTextEdit(add_snippet_Dialog)
        self.snippet_data_textEdit.setStyleSheet("background-image: url(:/backgrounds/ressources/backgrounds/mytry2.png);\n"
"color: rgb(255, 255, 255);")
        self.snippet_data_textEdit.setObjectName("snippet_data_textEdit")
        self.verticalLayout.addWidget(self.snippet_data_textEdit)
        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_label = QtWidgets.QLabel(add_snippet_Dialog)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_2.addWidget(self.name_label)
        self.snippet_name_lineEdit = QtWidgets.QLineEdit(add_snippet_Dialog)
        self.snippet_name_lineEdit.setObjectName("snippet_name_lineEdit")
        self.verticalLayout_2.addWidget(self.snippet_name_lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(add_snippet_Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(add_snippet_Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.color_label = QtWidgets.QLabel(add_snippet_Dialog)
        self.color_label.setObjectName("color_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.color_label)
        self.color_comboBox = QtWidgets.QComboBox(add_snippet_Dialog)
        self.color_comboBox.setObjectName("color_comboBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.color_comboBox)
        self.gridLayout.addLayout(self.formLayout_3, 5, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.icon_label = QtWidgets.QLabel(add_snippet_Dialog)
        self.icon_label.setObjectName("icon_label")
        self.verticalLayout_4.addWidget(self.icon_label)
        self.icon_listView = QtWidgets.QListView(add_snippet_Dialog)
        self.icon_listView.setViewMode(QtWidgets.QListView.IconMode)
        self.icon_listView.setObjectName("icon_listView")
        self.verticalLayout_4.addWidget(self.icon_listView)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(add_snippet_Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.description_label = QtWidgets.QLabel(add_snippet_Dialog)
        self.description_label.setObjectName("description_label")
        self.verticalLayout_3.addWidget(self.description_label)
        self.snippet_description_lineEdit = QtWidgets.QLineEdit(add_snippet_Dialog)
        self.snippet_description_lineEdit.setObjectName("snippet_description_lineEdit")
        self.verticalLayout_3.addWidget(self.snippet_description_lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 2)

        self.retranslateUi(add_snippet_Dialog)
        self.snippet_buttonBox.accepted.connect(add_snippet_Dialog.accept)
        self.snippet_buttonBox.rejected.connect(add_snippet_Dialog.reject)

    def retranslateUi(self, add_snippet_Dialog):
        _translate = QtCore.QCoreApplication.translate
        add_snippet_Dialog.setWindowTitle(_translate("add_snippet_Dialog", "Dialog"))
        self.snippet_label.setText(_translate("add_snippet_Dialog", "Snippet:"))
        self.name_label.setText(_translate("add_snippet_Dialog", "Name:"))
        self.color_label.setText(_translate("add_snippet_Dialog", "Color:"))
        self.icon_label.setText(_translate("add_snippet_Dialog", "Icon:"))
        self.description_label.setText(_translate("add_snippet_Dialog", "Description:"))
import pyqtsocius.ui_elements.pyqt_sorter_ressources_rc