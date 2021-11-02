# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bayes.ui'
#
# Created by: PyQt5 UI code generator 5.12


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QCoreApplication
import sys
import os
from Bayes_classification import Classifier

class Ui_gui(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.resize(310, 250)
        self.label_meta = QtWidgets.QLabel(self)
        self.label_meta.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_meta.setObjectName("label_meta")
        self.comboBox_meta = QtWidgets.QComboBox(self)
        self.comboBox_meta.setGeometry(QtCore.QRect(109, 10, 191, 31))
        self.comboBox_meta.setObjectName("comboBox_meta")
        self.label_train = QtWidgets.QLabel(self)
        self.label_train.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.label_train.setObjectName("label_train")
        self.comboBox_train = QtWidgets.QComboBox(self)
        self.comboBox_train.setGeometry(QtCore.QRect(109, 50, 191, 31))
        self.comboBox_train.setObjectName("comboBox_train")
        self.label_test = QtWidgets.QLabel(self)
        self.label_test.setGeometry(QtCore.QRect(10, 90, 91, 31))
        self.label_test.setObjectName("label_test")
        self.comboBox_test = QtWidgets.QComboBox(self)
        self.comboBox_test.setGeometry(QtCore.QRect(109, 90, 191, 31))
        self.comboBox_test.setObjectName("comboBox_test")
        self.label_accuracy = QtWidgets.QLabel(self)
        self.label_accuracy.setGeometry(QtCore.QRect(10, 130, 91, 31))
        self.label_accuracy.setObjectName("label_accuracy")
        self.Label_evaluate = QtWidgets.QLabel(self)
        self.Label_evaluate.setGeometry(QtCore.QRect(110, 130, 120, 31))
        self.Label_evaluate.setObjectName("textEdit_evaluate")
        self.pushButton_accuracy = QtWidgets.QPushButton(self)
        self.pushButton_accuracy.setGeometry(QtCore.QRect(240, 130, 61, 31))
        self.pushButton_accuracy.setObjectName("pushButton_accuracy")
        self.label_predict = QtWidgets.QLabel(self)
        self.label_predict.setGeometry(QtCore.QRect(10, 170, 91, 31))
        self.label_predict.setObjectName("label_predict")
        self.lineEdit_predict = QtWidgets.QLineEdit(self)
        self.lineEdit_predict.setGeometry(QtCore.QRect(110, 170, 120, 31))
        self.lineEdit_predict.setObjectName("lineEdit_predict")
        self.pushButton_save = QtWidgets.QPushButton(self)
        self.pushButton_save.setGeometry(QtCore.QRect(240, 170, 61, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_classify = QtWidgets.QPushButton(self)
        self.pushButton_classify.setGeometry(QtCore.QRect(10, 210, 141, 34))
        self.pushButton_classify.setObjectName("pushButton_classify")
        self.pushButton_quit = QtWidgets.QPushButton(self)
        self.pushButton_quit.setGeometry(QtCore.QRect(160, 210, 141, 34))
        self.pushButton_quit.setObjectName("pushButton_quit")
        
        self.retranslateUi()
        self.show()
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.meta_path=self.comboBox_meta.currentText()
        self.train_path=self.comboBox_train.currentText()
        self.test_path=self.comboBox_test.currentText()
        self.comboBox_meta.currentIndexChanged.connect(self.meta_change)
        self.comboBox_train.currentIndexChanged.connect(self.train_change)
        self.comboBox_test.currentIndexChanged.connect(self.test_change)
        
        self.classifier=Classifier()
        self.pushButton_classify.clicked.connect(self.calculate)
        self.pushButton_accuracy.clicked.connect(self.evaluate)
        self.pushButton_save.clicked.connect(self.predict)
        self.pushButton_quit.clicked.connect(self.quit)

    def meta_change(self):
        self.meta_path=self.comboBox_meta.currentText()
            
    def train_change(self):
        self.train_path=self.comboBox_train.currentText()
            
    def test_change(self):
        self.test_path=self.comboBox_test.currentText()
            
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Bayes classification")
        self.label_meta.setText("meta:")
        self.label_train.setText("train:")
        self.label_test.setText("test:")
        self.label_accuracy.setText("accuracy")
        self.pushButton_accuracy.setText( "Test")
        self.label_predict.setText("Predict:")
        self.pushButton_save.setText("Save")
        self.pushButton_classify.setText("Train")
        self.pushButton_quit.setText("Quit")
        
        # set combobox
        i=0;
        for name in os.listdir('data'):
            self.comboBox_meta.addItems([name])
            self.comboBox_train.addItems([name])
            self.comboBox_test.addItems([name])
            
    
    def calculate(self):
        try:
            self.classifier.train(self.meta_path, self.train_path)
        except:
            self.display_file_error()
        
    def evaluate(self):
        try:
            acc=self.classifier.evaluate(self.test_path)
            self.Label_evaluate.setText(str(acc)[0:5])
        except:
            self.display_file_error()
            
    def predict(self):
        try:
            out_path=self.lineEdit_predict.text()
            self.classifier.predict(self.test_path,'data/'+out_path)
        except:
            self.display_file_error()
        
    def quit(self):
        self.close()
        QApplication.instance().quit
        
    def display_file_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Error')
        msg.setWindowTitle("Error")
        msg.exec_()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    Bayes = Ui_gui()                                           
    sys.exit(app.exec_())      