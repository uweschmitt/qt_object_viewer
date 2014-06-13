# qt_object_viewer

This Python package provides a Qt based widget and a dialog class for exploring a
nested object structure.

Example:

```python

from qt_object_viewer import ObjectTreeDialog

from PyQt4.QtGui import QApplication

app = QApplication([])
dlg = ObjectTreeDialog([1, 2, 3, dict(a=3, b=4, c=(1, 2, dict(d=(4, 5))))])
dlg.show()
app.exec_()
```

Or if you want to embed the widget:

```python
from qt_object_viewer import ObjectTreeWidget

from PyQt4.QtGui import QDialog, QVBoxLayout
from PyQt4.QtCore import Qt

class MyDialog(QDialog):

    def __init__(self, root_object, parent=None, f=Qt.WindowFlags()):
        QDialog.__init__(self, parent, f)
        self.resize(480, 640)
        self.vertical_layout = QVBoxLayout(self)
        self.tree_view = ObjectTreeWidget(self)
        self.tree_view.set_root_object(root_object)
        self.tree_view.expand_top_level()
        self.vertical_layout.addWidget(self.tree_view)

app = QApplication([])
dlg = MyDialog([1, 2, 3, dict(a=3, b=4, c=(1, 2, dict(d=(4, 5))))])
dlg.show()
app.exec_()
```
