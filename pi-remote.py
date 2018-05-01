from tkinter import *
from tkinter import ttk
from time import sleep
import subprocess
import os

bashcon = "irsend SEND_ONCE Soniq "

def irsend(str):
    #print(str)
    bashCommand = bashcon + str
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

root = Tk()
root.title("Pi IR Remote")
root.geometry("290x420")
gui = ttk.Style()
gui.configure('My.TFrame', bg='#993353')
mainframe = ttk.Frame(root, style = 'My.TFrame', padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="CH 1", command=lambda:irsend("KEY_1")).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="CH 2", command=lambda:irsend("KEY_2")).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="CH 3", command=lambda:irsend("KEY_3")).grid(column=3, row=1, sticky=W)

ttk.Button(mainframe, text="CH 4", command=lambda:irsend("KEY_4")).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="CH 5", command=lambda:irsend("KEY_5")).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="CH 6", command=lambda:irsend("KEY_6")).grid(column=3, row=2, sticky=W)

ttk.Button(mainframe, text="CH 7", command=lambda:irsend("KEY_7")).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="CH 8", command=lambda:irsend("KEY_8")).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="CH 9", command=lambda:irsend("KEY_9")).grid(column=3, row=3, sticky=W)

ttk.Button(mainframe, text="MUTE", command=lambda:irsend("KEY_MUTE")).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="CH 0", command=lambda:irsend("KEY_0")).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="MENU", command=lambda:irsend("KEY_MENU")).grid(column=3, row=4, sticky=W)

ttk.Button(mainframe, text="EXIT", command=lambda:irsend("KEY_EXIT")).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text="UP ▲", command=lambda:irsend("KEY_UP")).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="INFO", command=lambda:irsend("KEY_INFO")).grid(column=3, row=5, sticky=W)

ttk.Button(mainframe, text="◀ LEFT", command=lambda:irsend("KEY_LEFT")).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="OK", command=lambda:irsend("KEY_OK")).grid(column=2, row=6, sticky=W)
ttk.Button(mainframe, text="RIGHT ▶", command=lambda:irsend("KEY_RIGHT")).grid(column=3, row=6, sticky=W)

ttk.Button(mainframe, text="VOL+", command=lambda:irsend("KEY_VOLUMEUP")).grid(column=1, row=7, sticky=W)
ttk.Button(mainframe, text="DOWN ▼", command=lambda:irsend("KEY_DOWN")).grid(column=2, row=7, sticky=W)
ttk.Button(mainframe, text="CH ▲ ", command=lambda:irsend("KEY_CHANNELUP")).grid(column=3, row=7, sticky=W)

ttk.Button(mainframe, text="VOL-", command=lambda:irsend("KEY_VOLUMEDOWN")).grid(column=1, row=8, sticky=W)
ttk.Button(mainframe, text="LAST CH", command=lambda:irsend("KEY_")).grid(column=2, row=8, sticky=W)
ttk.Button(mainframe, text="CH ▼", command=lambda:irsend("KEY_CHANNELDOWN")).grid(column=3, row=8, sticky=W)

#▲ ▼ ◀ ▶ 
ttk.Button(mainframe, text="◀ REW", command=lambda:irsend("KEY_REWIND")).grid(column=1, row=9, sticky=W)
ttk.Button(mainframe, text="PLAY PAUSE", command=lambda:irsend("KEY_PLAYPAUSE")).grid(column=2, row=9, sticky=W)
ttk.Button(mainframe, text="FF ▶", command=lambda:irsend("KEY_FASTFORWARD")).grid(column=3, row=9, sticky=W)

ttk.Button(mainframe, text="◀◀ PREV", command=lambda:irsend("KEY_PREVIOUS")).grid(column=1, row=10, sticky=W)
ttk.Button(mainframe, text="POWER", command=lambda:irsend("KEY_POWER")).grid(column=2, row=10, sticky=W)
ttk.Button(mainframe, text="NEXT ▶▶", command=lambda:irsend("KEY_NEXT")).grid(column=3, row=10, sticky=W)

ttk.Button(mainframe, text="MEDIA", command=lambda:irsend("KEY_DVD")).grid(column=2, row=11, sticky=W)
ttk.Button(mainframe, text="REPEAT", command=lambda:irsend("KEY_MEDIA_REPEAT")).grid(column=3, row=11, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

imgicon = PhotoImage(file=os.path.join('/home/pi/workspace/FanSpeed/win4.py','/home/pi/Downloads/ir-icon.png'))
root.tk.call('wm', 'iconphoto', root._w, imgicon) 
root.mainloop()

