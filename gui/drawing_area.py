from gi.repository import Gdk, Gtk


class DrawingArea():

    def __init__(self, grid: Gtk.Grid, viewport_size):
        self._element = Gtk.DrawingArea()
        self._element.set_size_request(viewport_size, viewport_size)
        self._element.set_hexpand(True)
        self._element.set_vexpand(True)
        self._element.set_events(Gdk.EventMask.SCROLL_MASK)
        self._element.connect("draw", self._on_draw)

        grid.attach(self._element, 1, 0, 2, 2)

    def connect_on_draw(self, on_draw):
        self._external_on_draw = on_draw

    def queue_draw(self):
        self._element.queue_draw()

    def _on_draw(self, _, context):
        if self._external_on_draw:
            self._external_on_draw(context)

