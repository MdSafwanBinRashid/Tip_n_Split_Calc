from kivy.config import Config

scale = 50
Config.set('graphics', 'width', str(8*scale))
Config.set('graphics', 'height', str(7*scale))

from kivy.app import App
from model import TipModel
from controller import TipCalculator

class TipCalculatorApp(App):
    def build(self):
        model = TipModel()
        controller = TipCalculator(model)
        return controller
    
if __name__ == "__main__":
    app = TipCalculatorApp()
    app.run()