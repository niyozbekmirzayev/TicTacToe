from PyQt5.QtWidgets import QPushButton, QLabel

class MyButton(QPushButton):
    def __init__(self,position):
        super().__init__()
        #saving all values to by order
        self.position = position
      
        #giving default name
        self.setText(" ")
        #using polymorphism to get bool instead of string
    def setText(self,text: bool) -> None:
        if text == True:
            #calling original setText and telling to print x
            super().setText("X")
            #this function disables the given button
            self.setDisabled(True)
            return "X"
        elif text == False:
            super().setText("⭕️")
            self.setDisabled(True)
            return "⭕️"
        else:
            super().setText(" ")
        
   

        

    
    
       

