# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My_Repos\PyQt_Socius\designer_files\pyqt_sorter_boiler_creator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_boiler_create_Dialog(object):
    def setupUi(self, boiler_create_Dialog):
        boiler_create_Dialog.setObjectName("boiler_create_Dialog")
        boiler_create_Dialog.resize(450, 650)
        boiler_create_Dialog.setMinimumSize(QtCore.QSize(450, 650))
        boiler_create_Dialog.setMaximumSize(QtCore.QSize(450, 650))
        self.gridLayout_3 = QtWidgets.QGridLayout(boiler_create_Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.variables_groupBox = QtWidgets.QGroupBox(boiler_create_Dialog)
        self.variables_groupBox.setMaximumSize(QtCore.QSize(425, 161))
        self.variables_groupBox.setObjectName("variables_groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.variables_groupBox)
        self.formLayout.setObjectName("formLayout")
        self.converted_ui_label = QtWidgets.QLabel(self.variables_groupBox)
        self.converted_ui_label.setObjectName("converted_ui_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.converted_ui_label)
        self.converted_ui_lineEdit = QtWidgets.QLineEdit(self.variables_groupBox)
        self.converted_ui_lineEdit.setFrame(False)
        self.converted_ui_lineEdit.setReadOnly(True)
        self.converted_ui_lineEdit.setObjectName("converted_ui_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.converted_ui_lineEdit)
        self.converted_class_label = QtWidgets.QLabel(self.variables_groupBox)
        self.converted_class_label.setAlignment(QtCore.Qt.AlignCenter)
        self.converted_class_label.setObjectName("converted_class_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.converted_class_label)
        self.converted_class_lineEdit = QtWidgets.QLineEdit(self.variables_groupBox)
        self.converted_class_lineEdit.setFrame(False)
        self.converted_class_lineEdit.setReadOnly(True)
        self.converted_class_lineEdit.setObjectName("converted_class_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.converted_class_lineEdit)
        self.line = QtWidgets.QFrame(self.variables_groupBox)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.new_class_label = QtWidgets.QLabel(self.variables_groupBox)
        self.new_class_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_class_label.setObjectName("new_class_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.new_class_label)
        self.new_class_lineEdit = QtWidgets.QLineEdit(self.variables_groupBox)
        self.new_class_lineEdit.setObjectName("new_class_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.new_class_lineEdit)
        self.gridLayout_3.addWidget(self.variables_groupBox, 0, 0, 1, 1)
        self.output_groupBox = QtWidgets.QGroupBox(boiler_create_Dialog)
        self.output_groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.output_groupBox.setMaximumSize(QtCore.QSize(425, 16777215))
        self.output_groupBox.setObjectName("output_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.output_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.output_pushButton = QtWidgets.QPushButton(self.output_groupBox)
        self.output_pushButton.setObjectName("output_pushButton")
        self.gridLayout_2.addWidget(self.output_pushButton, 0, 0, 1, 1)
        self.output_lineEdit = QtWidgets.QLineEdit(self.output_groupBox)
        self.output_lineEdit.setFrame(False)
        self.output_lineEdit.setReadOnly(True)
        self.output_lineEdit.setObjectName("output_lineEdit")
        self.gridLayout_2.addWidget(self.output_lineEdit, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.output_groupBox, 2, 0, 1, 2)
        self.methods_groupBox = QtWidgets.QGroupBox(boiler_create_Dialog)
        self.methods_groupBox.setMaximumSize(QtCore.QSize(425, 16777215))
        self.methods_groupBox.setObjectName("methods_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.methods_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.add_method_pushButton = QtWidgets.QPushButton(self.methods_groupBox)
        self.add_method_pushButton.setObjectName("add_method_pushButton")
        self.gridLayout.addWidget(self.add_method_pushButton, 0, 0, 1, 1)
        self.delete_method_pushButton = QtWidgets.QPushButton(self.methods_groupBox)
        self.delete_method_pushButton.setObjectName("delete_method_pushButton")
        self.gridLayout.addWidget(self.delete_method_pushButton, 0, 1, 1, 1)
        self.methods_listWidget = QtWidgets.QListWidget(self.methods_groupBox)
        self.methods_listWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.methods_listWidget.setObjectName("methods_listWidget")
        self.gridLayout.addWidget(self.methods_listWidget, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.methods_groupBox, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(boiler_create_Dialog)
        self.buttonBox.setMaximumSize(QtCore.QSize(425, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(boiler_create_Dialog)
        self.buttonBox.accepted.connect(boiler_create_Dialog.accept)
        self.buttonBox.rejected.connect(boiler_create_Dialog.reject)

    def retranslateUi(self, boiler_create_Dialog):
        _translate = QtCore.QCoreApplication.translate
        boiler_create_Dialog.setWindowTitle(_translate("boiler_create_Dialog", "Dialog"))
        self.variables_groupBox.setTitle(_translate("boiler_create_Dialog", "Variables"))
        self.converted_ui_label.setText(_translate("boiler_create_Dialog", "Converted Ui File:"))
        self.converted_class_label.setText(_translate("boiler_create_Dialog", "Converted Class:"))
        self.new_class_label.setText(_translate("boiler_create_Dialog", "New Class:"))
        self.output_groupBox.setTitle(_translate("boiler_create_Dialog", "Output"))
        self.output_pushButton.setText(_translate("boiler_create_Dialog", "Output File"))
        self.methods_groupBox.setTitle(_translate("boiler_create_Dialog", "Methods"))
        self.add_method_pushButton.setText(_translate("boiler_create_Dialog", "Add Method"))
        self.delete_method_pushButton.setText(_translate("boiler_create_Dialog", "Delete Method"))
        self.methods_listWidget.setSortingEnabled(True)
import pyqtsocius.ui_elements.pyqt_sorter_ressources_rc