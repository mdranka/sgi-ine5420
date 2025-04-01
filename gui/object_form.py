from gi.repository import Gtk
from global_vars import ObjectType

class ObjectForm:
    def __init__(self, menu_box):
        self.object_radio = ObjectRadio()
        self.name_input = Gtk.Entry()
        self.coordinate_input = Gtk.Entry()
        self.coordinate_input.set_placeholder_text("(x1,y1),(x2,y2),...")
        self.submit_button = Gtk.Button.new_with_label("Criar objeto")
        self.submit_button.connect("clicked", self.on_add)

        menu_box.add_element(Gtk.Label(label="Novo objeto"))
        menu_box.add_element(self.object_radio.element)
        menu_box.add_element(self.create_form_label("Descrição"))
        menu_box.add_element(self.name_input)
        menu_box.add_element(self.create_form_label("Coordenadas *"))
        menu_box.add_element(self.coordinate_input)
        menu_box.add_element(self.submit_button)

    def create_form_label(self, name):
        form_label = Gtk.Label()
        form_label.set_markup(f"<b>{name}</b>")
        form_label.set_xalign(0)
        return form_label

    def set_on_submit(self, function):
        self.on_submit = function

    def on_add(self, _):
        if self.on_submit:
            self.on_submit(
                self.object_radio.selected_type,
                self.name_input.get_text(),
                self.coordinate_input.get_text(),
            )
        self.clear_form() # Limpar campos após inserir

    def clear_form(self):
        self.name_input.set_text("")
        self.coordinate_input.set_text("")


class ObjectRadio:
    def __init__(self):
        self.element = Gtk.Box(spacing=7)
        self.selected_type = ObjectType.POINT
        self.buttons = []
        first_button = Gtk.RadioButton.new_with_label_from_widget(
            None, "Ponto")
        first_button.connect("toggled", self.on_toggle, self.selected_type)
        self.buttons.append(first_button)

        self.add_button("Reta", ObjectType.LINE)
        self.add_button("Polígono", ObjectType.POLYGON)

        for button in self.buttons:
            self.element.pack_start(button, False, False, 0)

    def add_button(self, name, object_type):
        button = Gtk.RadioButton.new_with_label_from_widget(
            self.buttons[0], name)
        button.connect("toggled", self.on_toggle, object_type)
        self.buttons.append(button)

    def on_toggle(self, button, type):
        if button.get_active():
            self.selected_type = type
