import sys 
from PyQt5.QtWidgets import  QApplication, QWidget, QMessageBox , QGridLayout
from PyQt5.QtGui import *
from My_Button import MyButton
import os

class MainWindow(QWidget):
    def __init__(self):
        super(). __init__()

        #giving easier names to methods
        #game starts with x
        self.setStyleSheet('.MyButton { font-size: 13pt;}')
        self.gamer = True
        self.tabel_box = QGridLayout()
    
        #creating buttons
        self.buttons = [MyButton(i) for i in range(9)]

        #creating table for interface
        cot = [(i, j) for i in range(3) for j in range(3)]

        #zip help us to use two elaments at the same time
        for btn, btn2 in zip(self.buttons, cot):
            btn.setFixedHeight(50)
            btn.setFixedWidth(100)
            self.tabel_box.addWidget(btn, *btn2)
            btn.clicked.connect(self.act)
            btn.setStyleSheet("background-color: cyan")

        #showing it to user
        self.msgBox = QMessageBox()
        self.setLayout(self.tabel_box)
        self.setGeometry(500, 240, 200, 200)
        self.setWindowTitle("Tic tac toe")
        self.show()

    def act (self):
        #finding which number choosen self.sender() helps us to get which button is pressed
        btn = self.sender()
        #sending gamer position and number which is choosen to modul
        btn.setText(self.gamer)

        #checking if player won
        if self.buttons[0].text() == self.buttons[1].text() == self.buttons[2].text() and  not self.buttons[0].text() == " ":
            winner = self.buttons[0].text()
            self.winner_check(winner)
            self.setDisabled(True)

        elif self.buttons[3].text() == self.buttons[4].text() == self.buttons[5].text() and not self.buttons[3].text() == " ":
            winner = self.buttons[3].text()
            self.winner_check(winner)
            self.setDisabled(True)

        elif self.buttons[6].text() == self.buttons[7].text() == self.buttons[8].text() and not self.buttons[6].text() == " ":
            winner = self.buttons[6].text()
            self.winner_check(winner)
            self.setDisabled(True)

        elif self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() and not self.buttons[0].text() == " ":
            winner = self.buttons[0].text()
            self.winner_check(winner)
            self.setDisabled(True)

        elif self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text() and not self.buttons[2].text() == " ":
            winner = self.buttons[2].text()
            self.winner_check(winner)
            self.setDisabled(True)
        
        elif self.buttons[0].text() == self.buttons[3].text() == self.buttons[6].text() and not self.buttons[0].text() == " ":
            winner = self.buttons[0].text()
            self.winner_check(winner)
            self.setDisabled(True)

        elif self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() and not self.buttons[1].text() == " ":
            winner = self.buttons[1].text()
            self.winner_check(winner)
            self.setDisabled(True)

        elif self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() and not self.buttons[2].text() == " ":
            winner = self.buttons[2].text()
            self.winner_check(winner)
            self.setDisabled(True)
        elif self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() and not self.buttons[0].text() == " ":
            winner = self.buttons[0].text()
            self.winner_check(winner)
            self.setDisabled(True)
        #checking if draw
        elif not self.buttons[0].text() == " " and not self.buttons[1].text() == " " and not self.buttons[2].text() == " " and not self.buttons[3].text() == " " and  not self.buttons[4].text() == " " and not self.buttons[5].text() == " " and  not self.buttons[6].text() == " " and not self.buttons[7].text() == " " and not self.buttons[8].text() == " ":
            fact = "DRAW!"
            self.show_result(fact)

        else:
            #giving position to next gamer
            self.gamer = not self.gamer


        #showing result in antoher message box
    def show_result(self,fact):
        self.msgBox.setIcon(QMessageBox.Question)
        self.msgBox.setText(f"""{fact}
Do you want to play again ? """)
        self.msgBox.setWindowTitle("Result")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.show()
        self.msgBox.buttonClicked.connect(self.msgButtons)
    
    #checking if players want to play again
    def msgButtons(self, i):
        if i.text() == 'OK' :
            #this method helps us to replay
            os.execl(sys.executable, sys.executable, *sys.argv)   
        elif i.text() == "Cancel":
            sys.exit()
        

            
        #checking who is winner
    def winner_check(self,winner):
        if winner == "X":
            fact = "X is winner"
            self.show_result(fact)
        elif winner == "⭕️":
            fact = "⭕️ is winner"
            self.show_result(fact)
       

if __name__ ==  "__main__":
    app = QApplication([])
    a = MainWindow()
    sys.exit(app.exec_())
