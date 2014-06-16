# qt_object_viewer

This Python package provides a Qt based widget and a dialog class for exploring a
nested object structure.

Example:

![Image](https://github.com/uweschmitt/qt_object_viewer/raw/master/screenshot.png)

```python

from qt_object_viewer import ObjectTreeDialog

from PyQt4.QtGui import QApplication

app = QApplication([])
data = dict(name="configuration",
            settings=dict(threshold=0.1,
                          iterations=3,
                          inner_loop_params=dict(iterations=5, threshold=.01)
                          )
            )
dlg = ObjectTreeDialog(data)
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
data = dict(name="configuration",
            settings=dict(threshold=0.1,
                          iterations=3,
                          inner_loop_params=dict(iterations=5, threshold=.01)
                          )
            )
dlg = MyDialog(data)
dlg.show()
app.exec_()
```
