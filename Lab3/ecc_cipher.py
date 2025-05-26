import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow 

import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_newKeys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)  
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = 'http://127.0.0.1:5000/api/ecc/generate_keys'
        try: 
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", data['message'])
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Request Error", str(e))

    def call_api_sign(self):      
        url = 'http://127.0.0.1:5000/api/ecc/sign'
        payload = {'message': self.ui.txt_info.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data['signature'])
                QMessageBox.information(self, "Success", "Signed Successfully!")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Request Error", str(e))
    
    def call_api_verify(self):
        url = 'http://127.0.0.1:5000/api/ecc/verify'
        payload = {
            'message': self.ui.txt_info.toPlainText(),
            'signature': self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    QMessageBox.information(self, "Success", "Verified Successfully")
                else:
                    QMessageBox.warning(self, "Failed", "Verification Failed")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Request Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
