# python -m venv env
# env\scripts\activate
# pip install kivymd

from kivymd.app import MDApp
from task_classes import CreateTaskDialog, TodoItem

class Main(MDApp):
    
    def show_create_task_dialog(self):
        self.task_dialog = CreateTaskDialog(title="CREATE TASK")
        self.task_dialog.open() 

    def close_dialog(self):
        self.task_dialog.dismiss()

    def add_task(self,task_textfield):
        #print(task_textfield.text)
        self.root.ids['container'].add_widget(TodoItem(text=task_textfield.text))
        self.close_dialog()

if __name__ == '__main__':
    Main().run()