# python -m venv env
# env\scripts\activate
# pip install kivymd

from kivymd.app import MDApp
from task_classes import CreateTaskDialog, TodoItem
from kivy.lang import Builder
import os


class Main(MDApp):

    def build(self):
        # Load the .kv file layout
        return Builder.load_file('main.kv')


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
                       file.write(widget.text + "\n")

        print(f"File saved to: {file_path}")

#Read tasks when program opens
    def read_tasks_file(self):

        try:
            with open("todo_texts.txt", "r") as file:
                print("Reading previous tasks...")
                texts = file.readlines()

                for task_text in texts:
                    task_text = task_text.strip()
                    self.root.ids['container'].add_widget(TodoItem(text=task_text))
        except:
            print("Creating a new tasks file!")
        
    def on_stop(self):
        self.write_tasks_file()

    
    def on_start(self):
        self.read_tasks_file()

if __name__ == '__main__':
    Main().run()