from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.widget import Widget

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """self.pizzas = [
            Pizza("4 Fromages", "chevre, emental, brie, comte", 9.5, True),
            Pizza("Chorizo", "Tomates, emental, bacon, oignon", 9.5, False),
            Pizza("Calzone", "fromage, oeuf, jambon, champignon", 9.5, False)
        ]"""

        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parent):
        # l = self.recycleView.data = [pizza.get_dictionnary() for pizza in self.pizzas]
        pizza_dict = StorageManager().load_data('pizzas')
        # if pizza_dict:                                # On peut soit faire ces deux lignes si on met None dans le stotag_manager.py
        #   self.recycleView.data = pizza_dict
        self.recycleView.data = pizza_dict              # Ou soit on peut faire ca si on met "" dans le stotag_manager.py

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data('pizzas', pizzas_dict)

    def on_server_error(self, error):
        print("Erreur:" + error)
        self.error_str = "Erreur:" + error


class PizzaApp(App):
    pass


PizzaApp().run()
