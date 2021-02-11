import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = addEditCoffeeForm(self.x)
        uic.loadUi('main.ui', self)
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        self.result = cur.execute("""SELECT * FROM coffee""").fetchall()
        names = [i[1] for i in self.result]
        self.comboBox.setPlaceholderText("Выберете вид кофе")
        self.pushButton.clicked.connect(self.ShowSecondForm)
        self.x = ''

        self.id_label.hide()
        self.name_label.hide()
        self.so_label.hide()
        self.z_label.hide()
        self.textBrowser.hide()
        self.price_label.hide()
        self.o_label.hide()
        self.label_3.hide()
        self.label_2.hide()
        self.label_5.show()
        self.pushButton.hide()
        self.pushButton_2.hide()

        for i in names[::-1]:
            self.comboBox.addItem(i)

        self.comboBox.currentIndexChanged.connect(self.on_combobox_func)

    def ShowSecondForm(self):
        self.dialog.show()


    def on_combobox_func(self):
        name = self.comboBox.currentText()
        self.id_label.show()
        self.name_label.show()
        self.so_label.show()
        self.z_label.show()
        self.textBrowser.show()
        self.price_label.show()
        self.o_label.show()
        self.label_3.show()
        self.label_2.show()
        self.label_5.hide()
        self.pushButton.show()
        self.pushButton_2.show()
        for i in self.result:
            if name == i[1]:
                self.id_label.setText(f'  Id: {i[0]}')
                self.name_label.setText(f'  Название: {i[1]}')
                self.so_label.setText(f'  Степень обжарки: {i[2]}')
                self.z_label.setText(f'  молотый/в зернах: {i[3]}')
                self.textBrowser.setPlainText('    ' + i[4])
                self.price_label.setText(f'  Цена: {i[5]}')
                self.o_label.setText(f'  Объем упаковки: {i[6]}')
                self.x = i[0]
                break


class addEditCoffeeForm(QWidget):
    def __init__(self, main):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.lineEdit.setText(main)
        self.lineEdit_2.setText()
        self.lineEdit_3.setText()
        self.lineEdit_4.setText()
        self.lineEdit_5.setText()
        self.lineEdit_6.setText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())