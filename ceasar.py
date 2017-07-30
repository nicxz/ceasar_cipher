# Caesar Cipher
# based on: http://inventwithpython.com/hacking (BSD Licensed)

from PyQt5 import QtGui, QtCore, QtWidgets
import mainwindow


def ceasar(mode, message, key):
    # the string to be encrypted/decrypted
    #message = 'This is my secret message.'

    # the encryption/decryption key
    #key = 7

    # tells the program to encrypt or decrypt
    #mode = 'encrypt'  # set to 'encrypt' or 'decrypt'

    # every possible symbol that can be encrypted
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # stores the encrypted/decrypted form of the message
    translated = ''

    # capitalize the string in message
    message = message.upper()

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol)  # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # print the encrypted/decrypted string to the screen
    print(translated)
    return translated

def handleButton(self):
    outputText = "Hello World"
    if ui.encryptButton.isChecked():
        outputText = ceasar('encrypt', ui.inputText.toPlainText(), ui.keyInput.value())
    else:
        outputText = ceasar('decrypt', ui.inputText.toPlainText(), ui.keyInput.value())

    ui.outputText.clear()
    ui.outputText.insertPlainText (outputText)


def handleClearButton(self):
    ui.outputText.clear()
    ui.inputText.clear()

def handleSwitchButton(self):
    tempInput = ui.inputText.toPlainText()
    tempOutput = ui.outputText.toPlainText()
    handleClearButton(self)
    ui.inputText.insertPlainText (tempOutput)
    ui.outputText.insertPlainText (tempInput)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(handleButton)
    ui.clearButton.clicked.connect(handleClearButton)
    ui.switchButton.clicked.connect(handleSwitchButton)

    sys.exit(app.exec_())
