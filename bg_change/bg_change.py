#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    
        
        #self.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(400, 400, 400))

        #self.first = GdkPixbuf.Pixbuf.new_from_file("first.jpeg")
        #self.second = GdkPixbuf.Pixbuf.new_from_file("two.jpeg")
        self.third = GdkPixbuf.Pixbuf.new_from_file("three.jpeg")
        
        #image1 = Gtk.Image()
        #image2 = Gtk.Image()
        image3 = Gtk.Image()
        
        #image1.set_from_pixbuf(self.first)
        #pythimage2.set_from_pixbuf(self.second)
        image3.set_from_pixbuf(self.third)
               
        fixed = Gtk.Fixed()
           
        #fixed.put(image1, 10, 10)
        #fixed.put(image2, 40, 160)
        fixed.put(image3, 170, 50)

        self.add(fixed)

        self.set_border_width(20)
        self.set_title("Fixed")
        
        self.connect("destroy", Gtk.main_quit)

win = MyWindow()
win.show_all()
Gtk.main()
