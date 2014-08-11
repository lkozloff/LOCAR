#!/bin/python
#taken from http://www.yolinux.com/TUTORIALS/PyGTK.html
#testing forks

import pygtk
import gtk

class MyProgram:
    def button_clicked(self, widget, data=None):
        print "button %s clicked" % data

    def __init__(self):

        #create a new window
        self.app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.app_window.fullscreen()
        self.app_window.set_title("LOCAR")

        #change color of window??
        #self.green = gtk.gdk.color_parse('green')
        #self.red = gtk.gdk.color_parse('red')
        #self.app_window.modify_bg(gtk.STATE_NORMAL,self.green)

        #add entry and search fields
        self.entry = gtk.Entry()
        self.button_search = gtk.Button("Search")
        self.button_search.connect("clicked", self.search_button_clicked, "3")
        self.button_search.set_size_request(50,50)

        #add image display area
        self.student_pic = gtk.EventBox()
        self.student_id= gtk.EventBox()

        spacer1 = gtk.EventBox()
        spacer2 = gtk.EventBox()

        self.label=gtk.Label("Enter a Student ID to begin:")
        init = '<span background="gray"><span size="128000">XXX</span>\n<span size="64000">Enter a SID to begin!</span></span>'
        self.label.set_markup(init)
        self.student_id.add(self.label)

        vbox = gtk.VBox()
        student_info = gtk.HBox()
        controls = gtk.VBox()
        bottom_area = gtk.HBox()

        controls.pack_start(self.entry,fill=False)
        controls.pack_start(self.button_search,fill=False)

        student_info.pack_start(self.student_pic,fill=False)
        student_info.pack_start(self.student_id,fill=False)
        
        bottom_area.pack_start(spacer1)
        bottom_area.pack_start(controls)
        bottom_area.pack_start(spacer2)

        vbox.pack_start(student_info)
        vbox.pack_start(bottom_area)
        self.app_window.add(vbox)

        image = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("resource/unknown.jpg")
        scaled_buf = pixbuf.scale_simple(300,350,gtk.gdk.INTERP_BILINEAR)
        image.set_from_pixbuf(scaled_buf)
        image.show()

        self.student_pic.add(image)

        self.button_search.set_flags(gtk.CAN_DEFAULT)
        self.button_search.grab_default()
        self.entry.set_activates_default(True)
        self.app_window.set_focus(self.entry)

        self.app_window.show_all()

        return

    def search_button_clicked(self, widget, data=None):
        #intersting stuff goes here
        #grab sid
        sid = self.entry.get_text()

        #do a lookup for the name
        if int(sid) < 100:
            name = 'Soup For You!'
        else:
            name = 'No Soup For You!'

        #display the result
        #successful result
        result = '<span background="green"><span size="128000">'+sid+'</span>\n<span size="64000">'+name+'</span></span>'

        if name == 'No Soup For You!':
            result = '<span background="red"><span size="128000">'+sid+'</span>\n<span size="64000">'+name+'</span></span>'
            #self.app_window.modify_bg(gtk.STATE_NORMAL, self.red)
        self.label.set_markup(result)
        self.label.show()

        #clear entry box and reset focus
        self.entry.set_text('')
        self.app_window.set_focus(self.entry)
        self.app_window.show()
def main():
    gtk.main()
    return 0

if __name__=="__main__":
    MyProgram()
    main()

