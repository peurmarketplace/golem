# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created: Fri Mar 28 01:11:08 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NodesManagerWidget(object):
    def setupUi(self, NodesManagerWidget):
        NodesManagerWidget.setObjectName(_fromUtf8("NodesManagerWidget"))
        NodesManagerWidget.resize(992, 637)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(NodesManagerWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(NodesManagerWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.nodeTableWidget = QtGui.QTableWidget(NodesManagerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeTableWidget.sizePolicy().hasHeightForWidth())
        self.nodeTableWidget.setSizePolicy(sizePolicy)
        self.nodeTableWidget.setMinimumSize(QtCore.QSize(681, 0))
        self.nodeTableWidget.setFrameShape(QtGui.QFrame.Box)
        self.nodeTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.nodeTableWidget.setShowGrid(True)
        self.nodeTableWidget.setRowCount(1)
        self.nodeTableWidget.setColumnCount(4)
        self.nodeTableWidget.setObjectName(_fromUtf8("nodeTableWidget"))
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.nodeTableWidget.setItem(0, 3, item)
        self.nodeTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.nodeTableWidget.horizontalHeader().setDefaultSectionSize(166)
        self.nodeTableWidget.horizontalHeader().setMinimumSectionSize(27)
        self.nodeTableWidget.verticalHeader().setDefaultSectionSize(22)
        self.horizontalLayout_4.addWidget(self.nodeTableWidget)
        self.frame = QtGui.QFrame(NodesManagerWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_5 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.endpointInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endpointInput.sizePolicy().hasHeightForWidth())
        self.endpointInput.setSizePolicy(sizePolicy)
        self.endpointInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.endpointInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endpointInput.setReadOnly(True)
        self.endpointInput.setObjectName(_fromUtf8("endpointInput"))
        self.gridLayout_2.addWidget(self.endpointInput, 0, 1, 1, 1)
        self.noPeersInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noPeersInput.sizePolicy().hasHeightForWidth())
        self.noPeersInput.setSizePolicy(sizePolicy)
        self.noPeersInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.noPeersInput.setReadOnly(True)
        self.noPeersInput.setObjectName(_fromUtf8("noPeersInput"))
        self.gridLayout_2.addWidget(self.noPeersInput, 1, 1, 1, 1)
        self.noTasks = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noTasks.sizePolicy().hasHeightForWidth())
        self.noTasks.setSizePolicy(sizePolicy)
        self.noTasks.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.noTasks.setReadOnly(True)
        self.noTasks.setObjectName(_fromUtf8("noTasks"))
        self.gridLayout_2.addWidget(self.noTasks, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.lastMsgInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastMsgInput.sizePolicy().hasHeightForWidth())
        self.lastMsgInput.setSizePolicy(sizePolicy)
        self.lastMsgInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lastMsgInput.setReadOnly(True)
        self.lastMsgInput.setObjectName(_fromUtf8("lastMsgInput"))
        self.gridLayout_2.addWidget(self.lastMsgInput, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.label_6 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.timeLeftInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLeftInput.sizePolicy().hasHeightForWidth())
        self.timeLeftInput.setSizePolicy(sizePolicy)
        self.timeLeftInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeLeftInput.setReadOnly(True)
        self.timeLeftInput.setObjectName(_fromUtf8("timeLeftInput"))
        self.gridLayout.addWidget(self.timeLeftInput, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cpuPowerInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpuPowerInput.sizePolicy().hasHeightForWidth())
        self.cpuPowerInput.setSizePolicy(sizePolicy)
        self.cpuPowerInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cpuPowerInput.setReadOnly(True)
        self.cpuPowerInput.setObjectName(_fromUtf8("cpuPowerInput"))
        self.gridLayout.addWidget(self.cpuPowerInput, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.remoteTaskProgressBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remoteTaskProgressBar.sizePolicy().hasHeightForWidth())
        self.remoteTaskProgressBar.setSizePolicy(sizePolicy)
        self.remoteTaskProgressBar.setMinimumSize(QtCore.QSize(160, 0))
        self.remoteTaskProgressBar.setProperty("value", 50)
        self.remoteTaskProgressBar.setObjectName(_fromUtf8("remoteTaskProgressBar"))
        self.gridLayout.addWidget(self.remoteTaskProgressBar, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_11 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_2.addWidget(self.label_11)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(10, 0, -1, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.totalTasks = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalTasks.sizePolicy().hasHeightForWidth())
        self.totalTasks.setSizePolicy(sizePolicy)
        self.totalTasks.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalTasks.setReadOnly(True)
        self.totalTasks.setObjectName(_fromUtf8("totalTasks"))
        self.gridLayout_3.addWidget(self.totalTasks, 0, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.localTaskProgressBar = QtGui.QProgressBar(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localTaskProgressBar.sizePolicy().hasHeightForWidth())
        self.localTaskProgressBar.setSizePolicy(sizePolicy)
        self.localTaskProgressBar.setMinimumSize(QtCore.QSize(160, 0))
        self.localTaskProgressBar.setProperty("value", 50)
        self.localTaskProgressBar.setObjectName(_fromUtf8("localTaskProgressBar"))
        self.gridLayout_3.addWidget(self.localTaskProgressBar, 5, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)
        self.totalChunksCalculatedInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalChunksCalculatedInput.sizePolicy().hasHeightForWidth())
        self.totalChunksCalculatedInput.setSizePolicy(sizePolicy)
        self.totalChunksCalculatedInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalChunksCalculatedInput.setReadOnly(True)
        self.totalChunksCalculatedInput.setObjectName(_fromUtf8("totalChunksCalculatedInput"))
        self.gridLayout_3.addWidget(self.totalChunksCalculatedInput, 1, 1, 1, 1)
        self.activeTasksInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activeTasksInput.sizePolicy().hasHeightForWidth())
        self.activeTasksInput.setSizePolicy(sizePolicy)
        self.activeTasksInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.activeTasksInput.setReadOnly(True)
        self.activeTasksInput.setObjectName(_fromUtf8("activeTasksInput"))
        self.gridLayout_3.addWidget(self.activeTasksInput, 2, 1, 1, 1)
        self.activeChunksInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activeChunksInput.sizePolicy().hasHeightForWidth())
        self.activeChunksInput.setSizePolicy(sizePolicy)
        self.activeChunksInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.activeChunksInput.setReadOnly(True)
        self.activeChunksInput.setObjectName(_fromUtf8("activeChunksInput"))
        self.gridLayout_3.addWidget(self.activeChunksInput, 3, 1, 1, 1)
        self.chunksLeftInput = QtGui.QLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chunksLeftInput.sizePolicy().hasHeightForWidth())
        self.chunksLeftInput.setSizePolicy(sizePolicy)
        self.chunksLeftInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chunksLeftInput.setReadOnly(True)
        self.chunksLeftInput.setObjectName(_fromUtf8("chunksLeftInput"))
        self.gridLayout_3.addWidget(self.chunksLeftInput, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.stopNodePushButton = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopNodePushButton.sizePolicy().hasHeightForWidth())
        self.stopNodePushButton.setSizePolicy(sizePolicy)
        self.stopNodePushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.stopNodePushButton.setObjectName(_fromUtf8("stopNodePushButton"))
        self.horizontalLayout_5.addWidget(self.stopNodePushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.fireNewPushButton = QtGui.QPushButton(NodesManagerWidget)
        self.fireNewPushButton.setMinimumSize(QtCore.QSize(220, 0))
        self.fireNewPushButton.setObjectName(_fromUtf8("fireNewPushButton"))
        self.horizontalLayout_2.addWidget(self.fireNewPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(NodesManagerWidget)
        QtCore.QMetaObject.connectSlotsByName(NodesManagerWidget)

    def retranslateUi(self, NodesManagerWidget):
        NodesManagerWidget.setWindowTitle(_translate("NodesManagerWidget", "Node manager", None))
        self.label.setText(_translate("NodesManagerWidget", "Local nodes", None))
        item = self.nodeTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("NodesManagerWidget", "Node", None))
        item = self.nodeTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("NodesManagerWidget", "Last seen", None))
        item = self.nodeTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("NodesManagerWidget", "Remote Task", None))
        item = self.nodeTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("NodesManagerWidget", "Local task", None))
        __sortingEnabled = self.nodeTableWidget.isSortingEnabled()
        self.nodeTableWidget.setSortingEnabled(False)
        item = self.nodeTableWidget.item(0, 0)
        item.setText(_translate("NodesManagerWidget", "UID", None))
        item = self.nodeTableWidget.item(0, 1)
        item.setText(_translate("NodesManagerWidget", "00:00:00.00", None))
        self.nodeTableWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("NodesManagerWidget", "Node (UID)", None))
        self.label_8.setText(_translate("NodesManagerWidget", "No. peers", None))
        self.label_7.setText(_translate("NodesManagerWidget", "Endpoint", None))
        self.endpointInput.setText(_translate("NodesManagerWidget", "127.0.0.1 : 4067", None))
        self.noPeersInput.setText(_translate("NodesManagerWidget", "0", None))
        self.noTasks.setText(_translate("NodesManagerWidget", "0", None))
        self.label_9.setText(_translate("NodesManagerWidget", "No. tasks", None))
        self.label_10.setText(_translate("NodesManagerWidget", "Last msg.", None))
        self.lastMsgInput.setText(_translate("NodesManagerWidget", "None", None))
        self.label_6.setText(_translate("NodesManagerWidget", "Active remote task (ID)", None))
        self.label_4.setText(_translate("NodesManagerWidget", "Time left", None))
        self.timeLeftInput.setText(_translate("NodesManagerWidget", "INF", None))
        self.label_2.setText(_translate("NodesManagerWidget", "CPU power", None))
        self.cpuPowerInput.setText(_translate("NodesManagerWidget", "0.0", None))
        self.label_3.setText(_translate("NodesManagerWidget", "Progress", None))
        self.label_11.setText(_translate("NodesManagerWidget", "Active local task (ID)", None))
        self.label_12.setText(_translate("NodesManagerWidget", "Total tasks", None))
        self.label_13.setText(_translate("NodesManagerWidget", "Total chunks", None))
        self.label_14.setText(_translate("NodesManagerWidget", "Active tasks", None))
        self.label_15.setText(_translate("NodesManagerWidget", "Active chunks", None))
        self.label_16.setText(_translate("NodesManagerWidget", "Chunks left", None))
        self.stopNodePushButton.setText(_translate("NodesManagerWidget", "Stop node", None))
        self.fireNewPushButton.setText(_translate("NodesManagerWidget", "Run new local node", None))

