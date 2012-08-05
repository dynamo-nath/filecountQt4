""" Main part of the filecount program that creates the Qt4 GUI and calls
the relevant query from filecountQUERY. In theory it should run on Windows but the
 \ might cause an issue in the filepath.
 
N Waterman 04-Aug-2012
"""

import sys, os
import filecountQUERY
fcq=filecountQUERY
from PyQt4 import QtGui, QtCore
from filecountGUI import Ui_MainWindow

root_list=[]

class makeGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pbMakeList, QtCore.SIGNAL('clicked()'), self.search_path)
        QtCore.QObject.connect(self.ui.pbResults, QtCore.SIGNAL('clicked()'), self.call_filecount)
        
    def search_path(self):
        '''sets list of values for combobox'''
        
        b1=self.ui.lineEdit.text()
        mylist=self.directory_list(b1)
        self.ui.comboBox.addItems(mylist)
#        self.ui.txtResults.setText(b1)
#        c1=self.ui.chkSubFolders.isChecked()
#        print(c1)

    def call_filecount(self):
        mypath=self.ui.comboBox.currentText()
        c1=self.ui.chkSubFolders.isChecked()
        if c1==True:
            z1=fcq.create_doc_type(mypath)
            self.ui.txtResults.setText(z1)
        else:
            z2=fcq.ext_list_folder(mypath)
            self.ui.txtResults.setText(z2)
        
    def directory_list(self, mypath=''):
       '''creates the list of sub-directories from a given directory'''
       
       temp_list = list()
       cntFolder=0
       for root, name, files in os.walk(mypath):
          cntFolder+=1
          temp_list.append(root)
       return temp_list
        
if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    myapp=makeGUI()
    myapp.show()
    sys.exit(app.exec_())
