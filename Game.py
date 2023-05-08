# Displaying the minefield.

from PyQt5.QtCore import QSize
from MinefieldContent import Field
from MinefieldContent import Empty
from MinefieldContent import Mine
from Scoreboard import Score
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QGridLayout, QMessageBox, QColorDialog
from PyQt5 import QtGui
import random
import sys

class Screen(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)        
        self.createScreen()

    def createScreen(self):

        # The resolution of our screen is 720*720.
        self.setGeometry(0,0,720,720)

        # The 5 different special colors are created for buttons and added into "buttonColorList".
        buttonColor1 = QtGui.QColor(176, 190, 197)
        buttonColor2 = QtGui.QColor(255, 255, 255)
        buttonColor3 = QtGui.QColor(255, 204, 188)
        buttonColor4 = QtGui.QColor(179, 157, 219)
        buttonColor5 = QtGui.QColor(179, 229, 252)
        buttonColorList = [buttonColor1, buttonColor2, buttonColor3, buttonColor4, buttonColor5]

        # The special color of buttons is chosen from the "buttonColorList" with its RGB code The color will appear randomly for every game.
        self.buttonColor = random.choice(buttonColorList)


        # The 5 special colors are created for background with their RGB codes.
        self.color1 = QtGui.QColor(236, 64, 122)   # Type of magenta
        self.color2 = QtGui.QColor(206, 147, 216)  # Type of lavander
        self.color3 = QtGui.QColor(79, 195, 247)   # Type of light blue
        self.color4 = QtGui.QColor(118, 255, 3)    # Type of lime green
        self.color5 = QtGui.QColor(244, 81, 30)    # Type of red-orange 

        # The colors are applied with order and size by the method "setStyleSheet".
        self.setStyleSheet("background-color: qlineargradient(x1:0, x2:1, x3:0, x4:1, x5:0, stop: 0.1 {color1}, stop: 0.4 {color2}, stop: 0.6 {color3}, stop: 0.8 {color4}, stop: 1 {color5});"
                           .format(color1=self.color1.name(), color2=self.color2.name(), color3=self.color3.name(), color4=self.color4.name(), color5=self.color5.name()))

        # Field is callable and usable.
        self.field = Field()
        print("The answer key:")
        print(self.field)

        # Empty is callable and usable.
        self.empty = Empty()

        # Mine is callable and usable.
        self.mine = Mine()

        # Score is callable and usable.
        self.score = Score()

        # Applying the buttons with grid layout type.
        self.buttonLayout = QGridLayout()

        # Applying the widgets with grid layout type.
        self.widgetLayout = QGridLayout()

        
        # The rows of buttons.
        for buttonRows in range(0, 10):
            # The columns of buttons.
            for buttonColumns in range(0, 10):
                    
                # The QToolButton function is used for creating the buttons.
                button = QToolButton()

                # The buttons special color is applied to game screen.
                button.setStyleSheet("background-color: {buttonColor};".format(buttonColor = self.buttonColor.name()))

                # The minimum size of buttons to 60*60.
                button.setMinimumSize(QSize(60, 60))

                button.setObjectName('{:02d}'.format(buttonRows * 10 + buttonColumns))

                # Buttons are connected to function buttonProperties.
                button.released.connect(self.buttonProperties)

                # Placement of the buttons on field.
                self.buttonLayout.addWidget(button, buttonRows, buttonColumns)

        
        # Placing the buttons on minefield with commands.
        label = QLabel(self)
        #pixmap = QPixmap('background1.png')
        #label.setPixmap(pixmap)
        self.widgetLayout.addItem(self.buttonLayout)
        self.widgetLayout.addWidget(label)
        self.setLayout(self.widgetLayout) 


    # The defining of the "buttonProperties" function.
    def buttonProperties(self):

        # Sending the buttons on the field with function "sender()".
        sendButtons = self.sender()

        # The values of buttons are converted to float variable.
        buttonName = float(sendButtons.objectName())

        # the buttonName variable are converted to string and splitted.
        buttonName = str(buttonName / 10).split(".")    

        # With dividing the row and column may be read.
        # With converting the string, it became list type.
        # So, the variables of rows and columns are created and they can be read.
        
        x = int(buttonName[0])
        y = int(buttonName[1])

        # Controlling the box if there is not a mine by clicking.
        if self.field[x][y] != "X":

            # The score will increase 100 points when clicking the non-mine button.
            self.score += 100
            
            # When non-mine button is clicked, the "O" symbol will appear.
            self.sender().setText("O")
            
            # The color of non-mine box is applied to game.
            self.nonMineColor = QtGui.QColor(83, 80, 255) 
            self.sender().setStyleSheet("background-color: {};".format(self.nonMineColor.name()))

            # The amount of non-mine boxes are decreased 1.
            self.empty -= 1


        # Controlling the box if there is a mine by clicking.
        elif self.field[x][y] == "X":

            # The score will decrease 200 points when clicking the mine button.
            self.score -= 200

            # The color of mine's box becomes red, text color is white and size is settled to 14..
            self.sender().setStyleSheet("background-color: rgba(255,0,0,1); color:white; font-size:14pt;")

            # X is assigned to inside of the mine's box.
            self.sender().setText("X")

            # The quota of clicking to mine will decrease clicking the mine button.
            self.mine -= 1


        # If there is not any empty boxes.
        if (self.empty == 0):
            
            # The "winMessage" is created for whe win message.
            winMessage = QMessageBox()

            # The icon is chosen for messagebox.
            winMessage.setIcon(QMessageBox.Information)

            # The text of win message.
            winMessage.setText("You WON the game!\nYour score: {scoore}\nYou can exit by click buttons 'X' or 'OK'.".format(scoore=self.score))
            
            #winMessage.setStandardButtons(QMessageBox.Ok)

            winMessage.exec_()
            sys.exit()  


        # If there is not any quota of mine boxes.
        elif (self.mine == 0):

            # The message box is created for ending message.
            LoseMessage = QMessageBox()

            # The icon is chosen for messagebox.
            LoseMessage.setIcon(QMessageBox.Critical)

            # The text of ending message.
            LoseMessage.setText("You LOST the game!\nYour score: {scoore}\nYou can exit by click buttons 'X' or 'OK'.".format(scoore=self.score))

            # The messagebox must be closed by just clicking with "exec_".
            LoseMessage.exec_()
            sys.exit()


# The game will displayed MAINLY with the function "main()".
def main():

    app = QApplication(sys.argv)
    app.setApplicationName("Minefield Game v1.0")
    display = Screen()
    display.show()
    sys.exit(app.exec_())

# Interface and Compile Commands
if __name__ == '__main__':
    main()