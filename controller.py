from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.logger import Logger
from model import TipModel

Builder.load_file('view.kv')

class TipCalculator(BoxLayout):
    bill_input = StringProperty('')
    tip_output = StringProperty(' ')
    num_people = StringProperty('')  
    split_output = StringProperty('')  
    
    __model: TipModel

    def __init__(self, model):
        super().__init__()    
        self.__model = model

    def btn_click_calc_tip(self, tip_percent):
        try:
            if not self.bill_input or self.bill_input.strip() == '':
                self.tip_output = "Please enter a bill amount first!"
                self.split_output = ""
                print("Error: No bill amount entered")
                return
            
            bill = float(self.bill_input)
            self.__model.bill_amount = bill
            self.__model.tip_percent = float(tip_percent)
            
            tip_amount = self.__model.tip_amount
            total_bill = bill + tip_amount
            
            self.tip_output = f"Tip Amount: ${tip_amount:.2f} (Total: ${total_bill:.2f})"
            print(f"Calculated: Tip=${tip_amount:.2f}, Total=${total_bill:.2f} for ${bill} at {tip_percent}%")
            
            self._calculate_split(total_bill)

        except ValueError as ex:
            self.tip_output = "Invalid input! Please enter numbers only."
            self.split_output = ""
            print(f"Error: {ex}")
    
    def _calculate_split(self, total_bill):
        """Calculate how much each person pays"""
        try:

            if not self.num_people or self.num_people.strip() == '':
                self.split_output = "Enter number of people to split"
                return

            num = int(self.num_people)

            if num <= 0:
                self.split_output = "Number of people must be greater than 0"
                return

            split_amount = total_bill / num
            
            self.split_output = f"Split {num} ways: ${split_amount:.2f} per person"
            print(f"Split: ${split_amount:.2f} per person for {num} people")
            
        except ValueError:
            self.split_output = "Please enter a valid whole number for people"
        except Exception as ex:
            self.split_output = f"Error calculating split: {ex}"