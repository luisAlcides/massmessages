# Form implementation generated from reading ui file '/home/heracle/code/massmessages/view/updatePersonalWindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dialogNewPersonal(object):
    def setupUi(self, dialogNewPersonal):
        dialogNewPersonal.setObjectName("dialogNewPersonal")
        dialogNewPersonal.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dialogNewPersonal.resize(760, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogNewPersonal.sizePolicy().hasHeightForWidth())
        dialogNewPersonal.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label.setGeometry(QtCore.QRect(60, 90, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_first_name = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_first_name.setGeometry(QtCore.QRect(220, 90, 401, 26))
        self.txt_first_name.setObjectName("txt_first_name")
        self.label_2 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 191, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_second_name = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_second_name.setGeometry(QtCore.QRect(220, 140, 401, 26))
        self.txt_second_name.setObjectName("txt_second_name")
        self.txt_salary = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_salary.setGeometry(QtCore.QRect(210, 340, 401, 26))
        self.txt_salary.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_salary.setText("")
        self.txt_salary.setObjectName("txt_salary")
        self.label_5 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_5.setGeometry(QtCore.QRect(90, 340, 101, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_6.setGeometry(QtCore.QRect(90, 290, 81, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txt_phone = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_phone.setGeometry(QtCore.QRect(210, 290, 401, 26))
        self.txt_phone.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_phone.setText("")
        self.txt_phone.setObjectName("txt_phone")
        self.btn_update = QtWidgets.QPushButton(parent=dialogNewPersonal)
        self.btn_update.setGeometry(QtCore.QRect(320, 690, 121, 41))
        self.btn_update.setObjectName("btn_update")
        self.txt_overtime = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_overtime.setGeometry(QtCore.QRect(210, 390, 401, 26))
        self.txt_overtime.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_overtime.setText("")
        self.txt_overtime.setObjectName("txt_overtime")
        self.label_7 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_7.setGeometry(QtCore.QRect(90, 390, 101, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txt_travelers = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_travelers.setGeometry(QtCore.QRect(210, 430, 401, 26))
        self.txt_travelers.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_travelers.setText("")
        self.txt_travelers.setObjectName("txt_travelers")
        self.label_8 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_8.setGeometry(QtCore.QRect(90, 430, 91, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txt_trips = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_trips.setGeometry(QtCore.QRect(210, 470, 401, 26))
        self.txt_trips.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_trips.setText("")
        self.txt_trips.setObjectName("txt_trips")
        self.label_9 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_9.setGeometry(QtCore.QRect(90, 470, 91, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txt_productive_bonus = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_productive_bonus.setGeometry(QtCore.QRect(270, 510, 401, 26))
        self.txt_productive_bonus.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_productive_bonus.setText("")
        self.txt_productive_bonus.setObjectName("txt_productive_bonus")
        self.label_10 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_10.setGeometry(QtCore.QRect(90, 510, 131, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txt_social_security = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_social_security.setGeometry(QtCore.QRect(270, 560, 401, 26))
        self.txt_social_security.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_social_security.setText("")
        self.txt_social_security.setObjectName("txt_social_security")
        self.label_11 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_11.setGeometry(QtCore.QRect(90, 560, 171, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txt_IR = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_IR.setGeometry(QtCore.QRect(270, 610, 401, 26))
        self.txt_IR.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.txt_IR.setText("")
        self.txt_IR.setObjectName("txt_IR")
        self.label_12 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_12.setGeometry(QtCore.QRect(90, 610, 171, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txt_second_surname = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_second_surname.setGeometry(QtCore.QRect(220, 240, 401, 26))
        self.txt_second_surname.setObjectName("txt_second_surname")
        self.txt_first_surname = QtWidgets.QLineEdit(parent=dialogNewPersonal)
        self.txt_first_surname.setGeometry(QtCore.QRect(220, 190, 401, 26))
        self.txt_first_surname.setObjectName("txt_first_surname")
        self.label_4 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(parent=dialogNewPersonal)
        self.label_13.setGeometry(QtCore.QRect(50, 240, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(dialogNewPersonal)
        QtCore.QMetaObject.connectSlotsByName(dialogNewPersonal)

    def retranslateUi(self, dialogNewPersonal):
        _translate = QtCore.QCoreApplication.translate
        dialogNewPersonal.setWindowTitle(_translate("dialogNewPersonal", "Actualizar Personal"))
        self.label.setText(_translate("dialogNewPersonal", "Primer Nombre"))
        self.label_2.setText(_translate("dialogNewPersonal", "Nuevo Personal"))
        self.label_3.setText(_translate("dialogNewPersonal", "Segundo Nombre"))
        self.label_5.setText(_translate("dialogNewPersonal", "Salario Base"))
        self.label_6.setText(_translate("dialogNewPersonal", "Telefono"))
        self.btn_update.setText(_translate("dialogNewPersonal", "Registrar"))
        self.label_7.setText(_translate("dialogNewPersonal", "Horas Extras"))
        self.label_8.setText(_translate("dialogNewPersonal", "Viaticos  "))
        self.label_9.setText(_translate("dialogNewPersonal", "Viajes"))
        self.label_10.setText(_translate("dialogNewPersonal", "Bono Productivo"))
        self.label_11.setText(_translate("dialogNewPersonal", "Seguro Social Laboral"))
        self.label_12.setText(_translate("dialogNewPersonal", "I.R. Del trabajo"))
        self.label_4.setText(_translate("dialogNewPersonal", "Primer Apellido"))
        self.label_13.setText(_translate("dialogNewPersonal", "Segundo Apellido"))
