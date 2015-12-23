# -*- coding: utf-8 -*-

#
# GUI and Layout created by: Qt Designer 4.8.7
# Code for UI-Elements generated by: PyQt4 UI code generator 4.11.4
#

import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx

from tsp_worker import Problem

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PROBLEMS_DIR = os.path.join(ROOT_DIR, 'problems')

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


class Ui_Tsp(QtGui.QWidget):
    def __init__(self):
        self.problem = None
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, TSP):
        TSP.setObjectName(_fromUtf8("TSP"))
        TSP.resize(1072, 761)

        ten_font = QtGui.QFont()
        ten_font.setPointSize(10)

        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        bold_font.setWeight(75)

        bold_ten_font = QtGui.QFont()
        bold_ten_font.setPointSize(10)
        bold_ten_font.setBold(True)
        bold_ten_font.setWeight(75)

        self.verticalLayout_3 = QtGui.QVBoxLayout(TSP)
        self.verticalLayout_3.setMargin(5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QtGui.QWidget(TSP)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setMargin(5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.commentLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commentLabel.sizePolicy().hasHeightForWidth())
        self.commentLabel.setSizePolicy(sizePolicy)
        self.commentLabel.setFont(bold_font)
        self.commentLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.commentLabel.setObjectName(_fromUtf8("commentLabel"))
        self.gridLayout_4.addWidget(self.commentLabel, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(140, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 7, 1, 1)
        self.dimensionText = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dimensionText.sizePolicy().hasHeightForWidth())
        self.dimensionText.setSizePolicy(sizePolicy)
        self.dimensionText.setObjectName(_fromUtf8("dimensionText"))
        self.gridLayout_4.addWidget(self.dimensionText, 0, 6, 1, 1)
        self.dimensionLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dimensionLabel.sizePolicy().hasHeightForWidth())
        self.dimensionLabel.setSizePolicy(sizePolicy)
        self.dimensionLabel.setFont(bold_font)
        self.dimensionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dimensionLabel.setObjectName(_fromUtf8("dimensionLabel"))
        self.gridLayout_4.addWidget(self.dimensionLabel, 0, 5, 1, 1)
        self.fileComboBox = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileComboBox.sizePolicy().hasHeightForWidth())
        self.fileComboBox.setSizePolicy(sizePolicy)
        self.fileComboBox.setObjectName(_fromUtf8("fileComboBox"))
        self.gridLayout_4.addWidget(self.fileComboBox, 0, 0, 1, 1)
        self.commentText = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commentText.sizePolicy().hasHeightForWidth())
        self.commentText.setSizePolicy(sizePolicy)
        self.commentText.setObjectName(_fromUtf8("commentText"))
        self.gridLayout_4.addWidget(self.commentText, 0, 3, 1, 1)
        self.runTsp_btn = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runTsp_btn.sizePolicy().hasHeightForWidth())
        self.runTsp_btn.setSizePolicy(sizePolicy)
        self.runTsp_btn.setObjectName(_fromUtf8("runTsp_btn"))
        self.gridLayout_4.addWidget(self.runTsp_btn, 0, 8, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.infoLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setFont(bold_ten_font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.gridLayout.addWidget(self.infoLabel, 0, 4, 1, 1)
        self.iterText = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iterText.sizePolicy().hasHeightForWidth())
        self.iterText.setSizePolicy(sizePolicy)
        self.iterText.setFont(ten_font)
        self.iterText.setObjectName(_fromUtf8("iterText"))
        self.gridLayout.addWidget(self.iterText, 0, 1, 1, 1)
        self.runtimeText = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runtimeText.sizePolicy().hasHeightForWidth())
        self.runtimeText.setSizePolicy(sizePolicy)
        self.runtimeText.setFont(ten_font)
        self.runtimeText.setObjectName(_fromUtf8("runtimeText"))
        self.gridLayout.addWidget(self.runtimeText, 0, 3, 1, 1)
        self.infoText = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoText.sizePolicy().hasHeightForWidth())
        self.infoText.setSizePolicy(sizePolicy)
        self.infoText.setFont(ten_font)
        self.infoText.setObjectName(_fromUtf8("infoText"))
        self.gridLayout.addWidget(self.infoText, 0, 5, 1, 1)
        self.runtimeLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runtimeLabel.sizePolicy().hasHeightForWidth())
        self.runtimeLabel.setSizePolicy(sizePolicy)
        self.runtimeLabel.setFont(bold_ten_font)
        self.runtimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.runtimeLabel.setObjectName(_fromUtf8("runtimeLabel"))
        self.gridLayout.addWidget(self.runtimeLabel, 0, 2, 1, 1)
        self.iterLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iterLabel.sizePolicy().hasHeightForWidth())
        self.iterLabel.setSizePolicy(sizePolicy)
        self.iterLabel.setFont(bold_ten_font)
        self.iterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iterLabel.setObjectName(_fromUtf8("iterLabel"))
        self.gridLayout.addWidget(self.iterLabel, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(TSP)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(TSP)
        QtCore.QMetaObject.connectSlotsByName(TSP)

    def retranslateUi(self, TSP):
        TSP.setWindowTitle(_translate("TSP", "Python TSP Heuristic", None))
        self.commentLabel.setText(_translate("TSP", "Comment:", None))
        self.dimensionLabel.setText(_translate("TSP", "Nodes:", None))
        self.runTsp_btn.setText(_translate("TSP", "Run!", None))
        self.infoLabel.setText(_translate("TSP", "Info:", None))
        self.runtimeLabel.setText(_translate("TSP", "Runtime:", None))
        self.iterLabel.setText(_translate("TSP", "Iterations:", None))

        for problem in collect_problems():
            self.fileComboBox.addItem(_fromUtf8(problem))
        self.problem_changed()

        self.runTsp_btn.clicked.connect(self.run_tsp)
        self.fileComboBox.currentIndexChanged.connect(self.problem_changed)

    def problem_changed(self):
        if self.problem and self.problem.isRunning():
                QtGui.QMessageBox.information(self, "Warning!", "Solver is still running!", QtGui.QMessageBox.Ok)
        else:
            problem = self.fileComboBox.currentText()
            file_path = os.path.join(PROBLEMS_DIR, str(problem))
            try:
                self.problem = Problem(file_path)
                self.commentText.setText(self.problem.meta['comment'])
                self.dimensionText.setText(self.problem.meta['dimension'])
                self.infoText.setText("ready...")
            except Exception as e:
                print e
                self.commentText.setText("Error")
                self.dimensionText.setText("Error")
                self.infoText.setText("Error while reading problem.")

    def run_tsp(self):
        self.infoText.setText("Solving TSP '{0}'...".format(self.problem.meta['name']))
        self.infoText.repaint()
        self.iterText.setText("")
        self.iterText.repaint()
        self.runtimeText.setText("")
        self.runtimeText.repaint()

        self.connect(self.problem, SIGNAL("finished()"), self.done)
        self.problem.start()

    def done(self):
        self.runtimeText.setText(str(self.problem.runtime))
        self.iterText.setText(str(self.problem.iterations))
        self.infoText.setText("Trip-Distance: " + str(self.problem.trip_distance))
        self.draw_solution(self.problem.tsp_solution)

    def draw_solution(self, tsp_solution):
        ax = self.figure.add_subplot(111)
        ax.hold(False)

        G = nx.DiGraph()
        G.add_nodes_from(range(0, len(self.problem.data)))
        G.add_edges_from(tsp_solution)
        nx.draw_networkx_nodes(G, self.problem.data, node_size=20, node_color='k')
        nx.draw_networkx_edges(G, self.problem.data, width=0.5, arrows=True, edge_color='r')

        plt.title(self.problem.meta['name'])
        plt.xlim(0)
        plt.ylim(0)
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        self.canvas.draw()


def collect_problems():
    for file in os.listdir(PROBLEMS_DIR):
        if file.endswith('.tsp'):
            yield file


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Tsp()
    ui.show()
    sys.exit(app.exec_())
