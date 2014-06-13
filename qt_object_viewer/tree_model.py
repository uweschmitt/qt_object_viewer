from PyQt4.QtCore import QVariant, QAbstractItemModel, QModelIndex, Qt
from PyQt4.QtGui import QTreeView

from tree import Leaf, Node


class _TreeModel(QAbstractItemModel):

    def __init__(self, root_object, parent=None):
        super(_TreeModel, self).__init__(parent)
        self.root_node = Node.from_("root", root_object)

    def top_level_indices(self):
        for i in range(self.root_node.get_num_children()):
            idx = self.index(i, 0)
            if idx.isValid():
                yield idx

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role != Qt.DisplayRole:
            return QVariant()

        item = index.internalPointer()
        if index.column() == 0:
            return item.name
        else:
            if isinstance(item, Leaf):
                return str(item.value)
            return ""

    def flags(self, index):
        if not index.isValid():
            return 0
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            child_item = self.root_node.children[row]
        else:
            parent_item = parent.internalPointer()
            child_item = parent_item.children[row]

        return self.createIndex(row, column, child_item)

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.get_parent()
        if parent_item == self.root_node:
            return QModelIndex()
        return self.createIndex(parent_item.get_index(), 0, parent_item)

    def rowCount(self, parent=QModelIndex()):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parent_item = self.root_node
        else:
            parent_item = parent.internalPointer()
        return parent_item.get_num_children()

    def columnCount(self, parent=QModelIndex()):
        return 2

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return ["Node", "Value"][section]
        return QVariant()


class ObjectTreeWidget(QTreeView):

    def __init__(self, *a, **kw):
        super(ObjectTreeWidget, self).__init__(*a, **kw)
        self.setAlternatingRowColors(True)
        self.setAutoExpandDelay(0)
        self.setIndentation(20)
        self.setRootIsDecorated(True)
        self.setUniformRowHeights(True)
        self.setAnimated(True)
        self.setHeaderHidden(False)

    def set_root_object(self, root_object):
        self.setModel(_TreeModel(root_object))

    def expand_top_level(self):
        for idx in self.model().top_level_indices():
            self.setExpanded(idx, True)


if __name__ == "__main__":

    from PyQt4.QtGui import QApplication, QDialog, QVBoxLayout
    from PyQt4.QtCore import Qt
    from MainWindow_ui import MainWindow

    class Dialog(QDialog):

        def __init__(self, root_object, parent=None, f=Qt.WindowFlags()):
            QDialog.__init__(self, parent, f)
            self.resize(480, 640)
            self.vertical_layout = QVBoxLayout(self)
            self.tree_view = ObjectTreeWidget(self)
            self.tree_view.set_root_object(root_object)
            self.tree_view.expand_top_level()
            self.vertical_layout.addWidget(self.tree_view)

    app = QApplication([])
    dlg = Dialog([1, 2, 3, dict(a=3, b=4, c=(1, 2, dict(d=(4, 5))))])
    dlg.show()
    app.exec_()
