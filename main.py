import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QTableWidgetItem


class AddEditForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        print('ok')
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT id FROM coffee''').fetchall()
        id = int(result[-1][0]) + 1
        con.close()
        print(id)
        name_variety = self.lineEdit_2.text()
        degree_roasting = self.lineEdit_3.text()
        ground_grains = self.lineEdit_4.text()
        taste_description = self.lineEdit_5.text()
        price = self.lineEdit_6.text()
        packing_volume = self.lineEdit_7.text()
        try:
            con = sqlite3.connect('coffee.sqlite')
            cur = con.cursor()
            result = cur.execute(f'''INSERT INTO coffee VALUES('{id}', '{name_variety}',
                 '{degree_roasting}', '{ground_grains}', '{taste_description}', '{price}', '{packing_volume}')''').fetchall
            con.close()
        except Exception as e:
            print(e)



class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.show_new_window)
        self.select_data()
        self.w = AddEditForm()

    def select_data(self):
        query = "SELECT * FROM coffee"
        res = self.connection.cursor().execute(query).fetchall()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute('''SELECT id FROM coffee''').fetchall()
        self.id = result[-1][0]
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(self.id - 1)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()

    def show_new_window(self):
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())