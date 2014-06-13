from qt_object_viewer import ObjectTreeDialog

from PyQt4.QtGui import QApplication
app = QApplication([])
dlg = ObjectTreeDialog([1, 2, 3, dict(a=3, b=4, c=(1, 2, dict(d=(4, 5))))])
dlg.show()
app.exec_()
