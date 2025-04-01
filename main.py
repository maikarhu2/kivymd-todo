# python -m venv env
# env\scripts\activate
# pip install kivymd

from kivymd.app import MDApp
from task_classes import CreateTaskDialog, TodoItem
import os

class Main(MDApp):
    
    def show_create_task_dialog(self):
        self.task_dialog = CreateTaskDialog(title="CREATE TASK")
        self.task_dialog.open() 

    def close_dialog(self):
        self.task_dialog.dismiss()

    def add_task(self,task_textfield):
        #This adds new task to the todolist
        self.root.ids['container'].add_widget(TodoItem(text=task_textfield.text))
        self.close_dialog()

    #Write tasks into a text file when program closed
    def write_tasks_file(self): #read tasks, write tasks

        file_name = "todo_texts.txt"
        file_path = os.path.abspath(file_name)
        with open(file_name, "a") as file:
             for widget in self.root.ids['container'].children:
                  if isinstance(widget, TodoItem):
                       print(widget.text)
                       file.write(widget.text + "\n")

        print(f"File saved to: {file_path}")

#Read tasks when program opens
    def read_tasks_file():
        
#Ensure this is the last step...
    def on_stop(self):
        self.write_tasks_file()

if __name__ == '__main__':
    Main().run()