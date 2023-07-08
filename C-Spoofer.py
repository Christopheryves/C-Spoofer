import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QInputDialog, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont, QDesktopServices
from PyQt5.QtCore import QUrl
import winreg
import shutil
import subprocess
from pypresence import Presence

client_id = "1126865889434800175"

rpc = Presence(client_id)
rpc.connect()

rpc.update(
        large_image="spoofer",
        small_image="small_image_key",
        large_text="HWID Spoofer",
        small_text="Small Image Text",
        buttons=[{"label": "Discord", "url": "https://discord.gg/YnnjSeuvAA"}])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Christopheryves Spoofer")
        self.setFixedSize(500, 150)

        self.label_HWID = QLabel("HWID:", self)
        self.label_GUID = QLabel("GUID:", self)
        self.label_MachineId = QLabel("MachineID:", self)

        self.label_HWID_value = QLabel(self.get_HWID(), self)
        self.label_GUID_value = QLabel(self.get_GUID(), self)
        self.label_MachineId_value = QLabel(self.get_MACHINEID(), self)

        self.button_HWID = QPushButton("Change HWID", self)
        self.button_HWID.clicked.connect(self.change_HWID)

        self.button_GUID = QPushButton("Change GUID", self)
        self.button_GUID.clicked.connect(self.change_GUID)

        self.button_MachineId = QPushButton("Change MachineID", self)
        self.button_MachineId.clicked.connect(self.change_MachineId)

        self.button_CopyHWID = QPushButton("Copy HWID", self)
        self.button_CopyHWID.clicked.connect(self.copy_HWID)

        self.button_CopyGUID = QPushButton("Copy GUID", self)
        self.button_CopyGUID.clicked.connect(self.copy_GUID)

        self.button_CopyMachineId = QPushButton("Copy MachineID", self)
        self.button_CopyMachineId.clicked.connect(self.copy_MachineId)

        self.button_LinkGUID = QPushButton("HWID/GUID Generator", self)
        self.button_LinkGUID.clicked.connect(self.open_GUID_link)

        self.button_CleanFiveM = QPushButton("Clean FiveM", self)
        self.button_CleanFiveM.clicked.connect(self.clean_FiveM)

        self.logged_in = True

        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        layout_HWID = QHBoxLayout()
        layout_HWID.addWidget(self.label_HWID)
        layout_HWID.addWidget(self.label_HWID_value)
        layout_HWID.addWidget(self.button_HWID)

        layout_GUID = QHBoxLayout()
        layout_GUID.addWidget(self.label_GUID)
        layout_GUID.addWidget(self.label_GUID_value)
        layout_GUID.addWidget(self.button_GUID)

        layout_MachineId = QHBoxLayout()
        layout_MachineId.addWidget(self.label_MachineId)
        layout_MachineId.addWidget(self.label_MachineId_value)
        layout_MachineId.addWidget(self.button_MachineId)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_CopyHWID)
        layout_buttons.addWidget(self.button_CopyGUID)
        layout_buttons.addWidget(self.button_CopyMachineId)
        layout_buttons.addWidget(self.button_LinkGUID)
        layout_buttons.addWidget(self.button_CleanFiveM)

        main_layout.addLayout(layout_HWID)
        main_layout.addLayout(layout_GUID)
        main_layout.addLayout(layout_MachineId)
        main_layout.addLayout(layout_buttons)

        self.setCentralWidget(main_widget)

    def change_HWID(self):
        if self.logged_in:
            choixProfile, okPressed = QInputDialog.getText(self, "Yves HWID", "Enter the new HWID:")
            if okPressed:
                choixProfile = "{" + choixProfile.strip("{}") + "}"
                if self.set_HWID(choixProfile):
                    QMessageBox.information(self, "Christopheryves Spoofer", "Successfully changed HWID!")
                else:
                    QMessageBox.warning(self, "Error", "Failed to change HWID!")
                self.label_HWID_value.setText(self.get_HWID())
        else:
            QMessageBox.warning(self, "Login Required", "Please log in to change HWID.")

    def change_GUID(self):
        if self.logged_in:
            choixMachine, okPressed = QInputDialog.getText(self, "Yves GUID", "Enter the new GUID:")
            if okPressed:
                choixMachine = "{" + choixMachine.strip("{}") + "}"
                if self.set_GUID(choixMachine):
                    QMessageBox.information(self, "Christopheryves Spoofer", "Successfully changed GUID!")
                else:
                    QMessageBox.warning(self, "Error", "Failed to change GUID!")
                self.label_GUID_value.setText(self.get_GUID())
        else:
            QMessageBox.warning(self, "Login Required", "Please log in to change GUID.")

    def change_MachineId(self):
        if self.logged_in:
            choixMachine, okPressed = QInputDialog.getText(self, "Yves MachineID", "Enter the new MachineID:")
            if okPressed:
                choixMachine = "{" + choixMachine.strip("{}") + "}"
                if self.set_MACHINEID(choixMachine):
                    QMessageBox.information(self, "Christopheryves Spoofer", "Successfully changed MachineID!")
                else:
                    QMessageBox.warning(self, "Error", "Failed to change MachineID!")
                self.label_MachineId_value.setText(self.get_MACHINEID())
        else:
            QMessageBox.warning(self, "Login Required", "Please log in to change MachineID.")

    def copy_HWID(self):
        current_HWID = self.get_HWID()
        QApplication.clipboard().setText(current_HWID)
        QMessageBox.information(self, "Christopheryves Spoofer", "Successfully copied HWID!")

    def copy_GUID(self):
        current_GUID = self.get_GUID()
        QApplication.clipboard().setText(current_GUID)
        QMessageBox.information(self, "Christopheryves Spoofer", "Successfully copied GUID!")

    def copy_MachineId(self):
        current_MachineId = self.get_MACHINEID()
        QApplication.clipboard().setText(current_MachineId)
        QMessageBox.information(self, "Christopheryves Spoofer", "Successfully copied MachineId!")

    def open_GUID_link(self):
        current_GUID = self.get_GUID()
        url = "https://www.guidgenerator.com/".format(current_GUID)
        QDesktopServices.openUrl(QUrl(url))


    def clean_FiveM(self):
        try:
            paths = [r"AppData\\Local\\FiveM"]

            for path in paths:
                if os.path.exists(path):
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        shutil.rmtree(path)
                    QMessageBox.information(self, "Christopheryves Spoofer", f"{path} başarıyla silindi!")
                else:
                    QMessageBox.warning(self, "Error", f"{path} Not Found!")
        except Exception as e:
            QMessageBox.warning(self, "Error", "Not Found!")
            print("Error:", e)




    def get_HWID(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001', 0, winreg.KEY_READ)
        (value, _) = winreg.QueryValueEx(key, 'HwProfileGuid')
        winreg.CloseKey(key)
        return value

    def get_MACHINEID(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\SQMClient', 0, winreg.KEY_READ)
        (value, _) = winreg.QueryValueEx(key, 'MachineId')
        winreg.CloseKey(key)
        return value

    def get_GUID(self):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Cryptography', 0, winreg.KEY_READ)
        (value, _) = winreg.QueryValueEx(key, 'MachineGuid')
        winreg.CloseKey(key)
        return value

    def set_HWID(self, choixProfile):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'HwProfileGuid', 0, winreg.REG_SZ, choixProfile)
            winreg.CloseKey(key)
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def set_GUID(self, choixMachine):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Cryptography', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'MachineGuid', 0, winreg.REG_SZ, choixMachine)
            winreg.CloseKey(key)
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def set_MACHINEID(self, choixMachineId):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\SQMClient', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'MachineId', 0, winreg.REG_SZ, choixMachineId)
            winreg.CloseKey(key)
            return True
        except Exception as e:
            print("Error:", e)
            return False


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
