from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem
from datetime import datetime

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):        
        super().__init__(**kwargs)
        
    def show_date_picker(self):
        date_picker = MDDatePicker()
        date_picker.open()
    
    def on_save(self):
        print("SAVING")
    
class TodoItem(TwoLineAvatarIconListItem):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #

class CreateTaskDialog(MDDialog):
    def __init__(self, **kwargs):
        self.type = "custom" # alert, confirmation, simple
        self.content_cls = DialogContent()
        super().__init__(**kwargs)