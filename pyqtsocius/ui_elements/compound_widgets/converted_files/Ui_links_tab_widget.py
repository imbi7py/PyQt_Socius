# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Dropbox\hobby\Modding\Programs\Github\My_Repos\PyQt_Socius\designer_files\links_tab_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LinksTab(object):
    def setupUi(self, LinksTab):
        LinksTab.setObjectName("LinksTab")
        LinksTab.resize(1018, 1043)
        self.gridLayout = QtWidgets.QGridLayout(LinksTab)
        self.gridLayout.setObjectName("gridLayout")
        self.new_link_groupBox = QtWidgets.QGroupBox(LinksTab)
        self.new_link_groupBox.setMinimumSize(QtCore.QSize(500, 250))
        self.new_link_groupBox.setMaximumSize(QtCore.QSize(16777215, 250))
        self.new_link_groupBox.setObjectName("new_link_groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.new_link_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.new_link_name_lineEdit = QtWidgets.QLineEdit(self.new_link_groupBox)
        self.new_link_name_lineEdit.setObjectName("new_link_name_lineEdit")
        self.gridLayout_6.addWidget(self.new_link_name_lineEdit, 1, 1, 1, 1)
        self.new_link_description_label = QtWidgets.QLabel(self.new_link_groupBox)
        self.new_link_description_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.new_link_description_label.setObjectName("new_link_description_label")
        self.gridLayout_6.addWidget(self.new_link_description_label, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 2, 1, 1)
        self.new_link_lineEdit = QtWidgets.QLineEdit(self.new_link_groupBox)
        self.new_link_lineEdit.setObjectName("new_link_lineEdit")
        self.gridLayout_6.addWidget(self.new_link_lineEdit, 2, 1, 1, 2)
        self.new_link_label = QtWidgets.QLabel(self.new_link_groupBox)
        self.new_link_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.new_link_label.setObjectName("new_link_label")
        self.gridLayout_6.addWidget(self.new_link_label, 2, 0, 1, 1)
        self.new_link_name_label = QtWidgets.QLabel(self.new_link_groupBox)
        self.new_link_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.new_link_name_label.setObjectName("new_link_name_label")
        self.gridLayout_6.addWidget(self.new_link_name_label, 1, 0, 1, 1)
        self.insert_new_link_pushButton = QtWidgets.QPushButton(self.new_link_groupBox)
        self.insert_new_link_pushButton.setMaximumSize(QtCore.QSize(158, 16777215))
        self.insert_new_link_pushButton.setObjectName("insert_new_link_pushButton")
        self.gridLayout_6.addWidget(self.insert_new_link_pushButton, 4, 1, 1, 2, QtCore.Qt.AlignLeft)
        self.new_link_description_plainTextEdit = QtWidgets.QPlainTextEdit(self.new_link_groupBox)
        self.new_link_description_plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 75))
        self.new_link_description_plainTextEdit.setObjectName("new_link_description_plainTextEdit")
        self.gridLayout_6.addWidget(self.new_link_description_plainTextEdit, 3, 1, 1, 2)
        self.gridLayout.addWidget(self.new_link_groupBox, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.useful_links_tableView = QtWidgets.QTableView(LinksTab)
        self.useful_links_tableView.setMinimumSize(QtCore.QSize(1000, 0))
        self.useful_links_tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.useful_links_tableView.setAlternatingRowColors(True)
        self.useful_links_tableView.setGridStyle(QtCore.Qt.NoPen)
        self.useful_links_tableView.setObjectName("useful_links_tableView")
        self.useful_links_tableView.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.useful_links_tableView, 0, 0, 1, 2)

        self.retranslateUi(LinksTab)

    def retranslateUi(self, LinksTab):
        _translate = QtCore.QCoreApplication.translate
        LinksTab.setWindowTitle(_translate("LinksTab", "Form"))
        self.new_link_groupBox.setTitle(_translate("LinksTab", "Add New Link"))
        self.new_link_description_label.setText(_translate("LinksTab", "Description:"))
        self.new_link_label.setText(_translate("LinksTab", "Link:"))
        self.new_link_name_label.setText(_translate("LinksTab", "Name:"))
        self.insert_new_link_pushButton.setText(_translate("LinksTab", "Insert"))
import pyqtsocius.ui_elements.pyqt_sorter_ressources_rc