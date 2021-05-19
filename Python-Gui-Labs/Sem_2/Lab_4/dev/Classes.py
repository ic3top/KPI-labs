from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont

class QTableViewM(QTableView):
    def __init__(self):
        super().__init__()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers or
                             QAbstractItemView.DoubleClicked)

    def keyPressEvent(self, event = QKeyEventTransition):
        super().keyPressEvent(event)
        if event.key() == 16777220: self.enterPressEvent(event)

    def enterPressEvent(self, event = QKeyEventTransition):
        pass


class Table(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.items = []
        self.namev = []
        self.nameh = []



    def columnCount(self, parent=None, *args, **kwargs):
        if len(self.items) == 0:
            return 0
        else:
            return len(self.items[0])

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.items)


    def __getitem__(self, item):
        return self.items[item]

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole and role != Qt.EditRole:
            return QVariant()
        return QVariant(str(self.items[index.row()][index.column()]))

    def clear(self):
        self.beginResetModel()
        for i in range(len(self.items)):
            for j in range(len(self.items[0])):
                self.items[i][j] = 0
        self.endResetModel()


    def append_sqr(self):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.beginInsertColumns(QModelIndex(), self.rowCount(), self.rowCount())

        if len(self.items) != 0:
            for i in range(len(self.items)):
                self.items[i].append(0)
            self.items.append([0]*len(self.items[0]))

            self.nameh.append(str(self.columnCount()))
            self.namev.append(str(self.rowCount()))

        else:
            self.items = [[0]]
            self.nameh.append(str(self.columnCount()))
            self.namev.append(str(self.rowCount()))

        self.endInsertRows()
        self.endInsertColumns()

    def del_sqr(self):
        self.beginResetModel()
        self.beginRemoveRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.beginRemoveColumns(QModelIndex(), self.rowCount(), self.rowCount())

        if len(self.items) != 0:
            for i in range(len(self.items)-1):
                self.items[i].pop(-1)
            self.items.pop(-1)
            self.namev.pop(-1)
            self.nameh.pop(-1)

        else:
            pass

        self.endRemoveRows()
        self.endRemoveColumns()
        self.endResetModel()

    def append(self, item, name):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.items.append(item)
        self.endInsertRows()
        self.nameh.append(name)

    def appendname(self, name=[]):
        for i in name:
            self.beginInsertColumns(QModelIndex(), self.rowCount(), self.rowCount())
            self.namev.append(i)
            self.endInsertColumns()

    def headerData(self, index, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.namev[index])
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(self.nameh[index])
        return QVariant()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, QModelIndex, Any, p_int=None):

        self.items[QModelIndex.row()][QModelIndex.column()] = Any
        self.items[QModelIndex.column()][QModelIndex.row()] = Any
        return False

    def setIData(self, column, row, data):
        self.beginResetModel()
        self.items[row][column] = data
        self.items[column][row] = data
        self.endResetModel()

    def getItems(self):
        items = []
        k = -1
        for i in self.items:
            k += 1
            items.append([])
            for j in self.items[k]:
                items[k].append(j)
        return items

