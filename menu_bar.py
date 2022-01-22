import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio
import sys


class Window(Gtk.ApplicationWindow):

    def __init__(self, app):
        super(Window, self).__init__(title="Application", application=app)

        grid = Gtk.Grid()

        menubar = Gtk.MenuBar()

        fmi = Gtk.MenuItem.new_with_label("Explore")
        cmi = Gtk.MenuItem.new_with_label("Contest")
        lmi = Gtk.MenuItem.new_with_label("Leave")


	
	#1
        menu = Gtk.Menu()
        
        pmi = Gtk.MenuItem.new_with_label("Problemset") 
        prmi = Gtk.MenuItem.new_with_label("Practice")
       
        menu.append(pmi)
        menu.append(prmi)
        
        fmi.set_submenu(menu)
   
   	#2     
        menu = Gtk.Menu()
        emi = Gtk.MenuItem.new_with_label("Exit")
        
        emi.connect("activate", self.quitApp)
        menu.append(emi)
        
        lmi.set_submenu(menu)
        
  	#3      
        menu = Gtk.Menu()
        
        wmi = Gtk.MenuItem.new_with_label("Weekly Contest") 
        bwmi = Gtk.MenuItem.new_with_label("Biweekly Contest")
        
        menu.append(wmi)
        menu.append(bwmi)
        
        cmi.set_submenu(menu)
        
        

             
        
        

        menubar.add(fmi)
        menubar.add(cmi)
        menubar.add(lmi)
        
        

        grid.attach(menubar, 0, 0, 1, 1)

        self.add(grid)

        self.set_default_size(280, 180)

    def quitApp(self, par):

        app.quit()
   

class Application(Gtk.Application):

    def __init__(self):
        super(Application, self).__init__()

    def do_activate(self):
    
        self.win = Window(self)
        self.win.show_all()

    def do_startup(self):

        Gtk.Application.do_startup(self)

app = Application()
app.run(sys.argv)
