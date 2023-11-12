import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize, pyqtSignal
from PyQt6 import uic


class TaskWidget(QWidget):

    taskRemoved = pyqtSignal()

    def __init__(self, task_text, parent=None):
        super().__init__(parent)

        uic.loadUi('todo-item.ui', self)

        self.setFixedSize(375, 40)
        self.label.setText(task_text)

        self.closeButton.clicked.connect(self.remove_todo)
        self.checkBox.toggled.connect(self.task_toggele)

    def task_toggele(self):
        if self.checkBox.isChecked() == True:
            f = self.label.font()
            f.setStrikeOut(True)
            self.label.setFont(f)
        else:
            f = self.label.font()
            f.setStrikeOut(False)
            self.label.setFont(f)

    def remove_todo(self):
        self.taskRemoved.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('todo-ui.ui', self)

        self.setFixedSize(400, 500)
        self.setWindowTitle('TODO APP')

        self.addTask.clicked.connect(self.add_todo)
        self.listView.doubleClicked.connect(self.edit_task)

    def add_todo(self):
        todo, ok = QInputDialog.getText(
            self, 'Add Task', 'Enter Task')

        if ok:
            item_widget = TaskWidget(todo)
            item = QListWidgetItem()
            item.setSizeHint(QSize(375, 40))
            self.listView.addItem(item)
            self.listView.setItemWidget(item, item_widget)
            item_widget.taskRemoved.connect(lambda: self.remove_todo(item))

    def remove_todo(self, item):
        row = self.listView.row(item)
        self.listView.takeItem(row)

    def edit_task(self):
        row = self.listView.currentItem()
        print(row)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
