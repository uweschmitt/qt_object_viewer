from qt_object_viewer import ObjectTreeDialog

from PyQt4.QtGui import QApplication
app = QApplication([])
data = dict(name="configuraion",
            settings=dict(threshold=0.1,
                          iterations=3,
                          inner_loop_params=dict(iterations=5, threshold=.01)
                          )
            )
dlg = ObjectTreeDialog(data)
dlg.show()
app.exec_()
