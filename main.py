# python -m venv env
# env\scripts\activate
# pip install kivymd

from kivymd.app import MDApp
from task_classes import CreateTaskDialog

class Main(MDApp):
    
    def show_create_task_dialog(self):
        self.task_dialog = CreateTaskDialog(title="CREATE TASK")
        self.task_dialog.open() 

    def close_dialog(self):
        self.task_dialog.dismiss()

        

if __name__ == '__main__':
    Main().run()