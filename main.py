import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = addEditCoffeeForm()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT * FROM coffee""").fetchall()
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
                # self.dialog.lineEdit(f'  Id: {i[0]}')
                self.dialog.lnd(i)
                break


class addEditCoffeeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButtond.clicked.connect(lambda x: self.close())
        self.pushButton_2d.clicked.connect(self.save)

    def save(self):
        new_list = []
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        text = self.lineEditd.text()
        new_list.append(self.lineEdit_2d.text())
        new_list.append(self.lineEdit_3d.text())
        new_list.append(self.lineEdit_4d.text())
        new_list.append(self.textBrowserd.toPlainText())
        new_list.append(self.lineEdit_5d.text())
        new_list.append(self.lineEdit_6d.text())
        new_list.append(self.lineEditd.text())
        if not self.isHidden():
            cur.execute(
                """UPDATE coffee SET Name = ? AND obz = ? AND zer = ? AND text = ? AND price = 
                ? AND ob = ? WHERE id = ?""", new_list)
            con.commit()
            self.close()

    def lnd(self, k):
        self.lineEditd.setText(str(k[0]))
        self.lineEdit_2d.setText(str(k[1]))
        self.lineEdit_3d.setText(str(k[2]))
        self.lineEdit_4d.setText(str(k[3]))
        self.textBrowserd.setPlainText('    ' + k[4])
        self.lineEdit_5d.setText(str(k[5]))
        self.lineEdit_6d.setText(str(k[6]))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())