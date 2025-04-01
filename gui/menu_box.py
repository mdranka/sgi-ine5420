from gi.repository import Gtk
from .window_form import WindowForm
from .object_form import ObjectForm
from .object_list import ObjectList

class MenuBox():
    def __init__(self, grid):
        self.element = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=7)
        self.element.set_border_width(25)
        grid.attach(self.element, 0, 0, 1, 2)

        
        self.object_form = ObjectForm(self)
        self.object_list = ObjectList(self)
        self.window_form = WindowForm(self)

        self.element.set_hexpand(False)

    def add_element(self, new_element):
        self.element.pack_start(new_element, False, True, 0)
