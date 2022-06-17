from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class HelloWorld(QMainWindow):
    def __init__(self):
        super().__init__()
        loader= QUiLoader()
        self.ui=loader.load('form.ui',None)
        self.ui.show()
        self.ui.btn_1.clicked.connect(self.function_num_1)
        self.ui.btn_2.clicked.connect(self.function_num_2)
        self.ui.btn_3.clicked.connect(self.function_num_3)
        self.ui.btn_4.clicked.connect(self.function_num_4)
        self.ui.btn_5.clicked.connect(self.function_num_5)
        self.ui.btn_6.clicked.connect(self.function_num_6)
        self.ui.btn_7.clicked.connect(self.function_num_7)
        self.ui.btn_8.clicked.connect(self.function_num_8)
        self.ui.btn_9.clicked.connect(self.function_num_9)
        self.ui.btn_0.clicked.connect(self.function_num_0)
        self.ui.btn_dot.clicked.connect(self.function_num_dot)
        self.ui.btn_Eq.clicked.connect(self.function_num_eq)
        self.ui.butn_sum.clicked.connect(self.function_num_sum)
        self.ui.butn_sub.clicked.connect(self.function_num_sub)
        self.ui.butn_mul.clicked.connect(self.function_num_mul)
        self.ui.butn_div.clicked.connect(self.function_num_div)
        self.ui.btn_ac.clicked.connect(self.function_num_ac)
    


    def function_num_1(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'1')
    def function_num_2(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'2')
    def function_num_3(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'3')
    def function_num_4(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'4')
    def function_num_5(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'5')
    def function_num_6(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'6')
    def function_num_7(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'7')
    def function_num_8(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'8')
    def function_num_9(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'9')
    def function_num_0(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'0')
    def function_num_dot(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'.')

    


    def function_num_ac(self):
            
        self.ui.textbox.setText(self.ui.textbox.text()+'ac')
        self.ui.textbox.setText("")




    def function_num_sum(self):
            
        self.num1=int(self.ui.textbox.text())
        self.ui.textbox.setText('')

            
    def function_num_sub(self):
            
        self.num1=int(self.ui.textbox.text())
        self.ui.textbox.setText('')




    def function_num_mul(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'*')
        self.num1=int(self.ui.textbox.text())
        self.ui.textbox.setText('')



    def function_num_div(self):
        self.ui.textbox.setText(self.ui.textbox.text()+'/')
        self.num1=int(self.ui.textbox.text())
        self.ui.textbox.setText('')
    def function_num_eq(self):
        if self.ui.textbox.setText(self.ui.textbox.text()+'+'):
            self.num2=int(self.ui.textbox.text())
            result=self.num1 + self.num2
            self.ui.texbox.setText(str(result))
        if self.ui.textbox.setText(self.ui.textbox.text()+'-'):
            self.num2=int(self.ui.textbox.text())
            result=self.num1 - self.num2
            self.ui.texbox.setText(str(result))
        if  self.ui.textbox.setText(self.ui.textbox.text()+'*'):
            self.num2=int(self.ui.textbox.text())
            result=self.num1 * self.num2
            self.ui.texbox.setText(str(result))

        if  self.ui.textbox.setText(self.ui.textbox.text()+'/'):

            self.num2=int(self.ui.textbox.text())
            result=self.num1 / self.num2
            self.ui.texbox.setText(str(result))
        



app=QApplication([])
window= HelloWorld()
app.exec()


