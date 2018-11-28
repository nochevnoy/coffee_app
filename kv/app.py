from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from screens.screenmanager import sm, screens
from kivy.uix.screenmanager import ScreenManagerException

from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'heigth', '512')

class CoffeeApp(App):
    title = 'Coffee app v1.0'
    screen_manager = None

    def initialize_app(self):
        self.screen_manager = sm
        self.switch_screen('main')

    def switch_screen(self, screen_name):
        if screen_name in screens.keys():
            screen = screens[screen_name](name = screen_name)
            self.screen_manager.switch_to(screen)
            return
        else:
            raise ScreenManagerException('Screen {} not found'.format(screen_name))

    def build(self):
        self.initialize_app()
        return self.screen_manager

if __name__ == '__main__':
    CoffeeApp().run()
