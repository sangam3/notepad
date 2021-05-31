#I am Sangam Prashar as @sangam3
#I am self python learner. If you help me in learning python, I will be thankful to you.
#You can contact me through E-mail: sangamprashar3@gmail.com 
# or throught linkedin by following this link: https://www.linkedin.com/in/sangam-prashar-519bb31aa/

#About Project: Notepad
"""I created this project while learning Tkinter. It is my third project.
 I used tkinter module to make GUI and os module to open and save file.
 tkinter.messagebox is used to display poped dialog box with message.

This is a Notebook which perform all basic operation of a word editor."""

#importing modules
from tkinter import*
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename


#creating function for all MENU BAR option
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
    if file =="":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0, END)
        f = open(file,"r")
        TextArea.insert(1.0, f.read())
        f.close()
def saveFile():
    #making global file so we can change name of file
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
        if file == "":
            file=None
# saving as new file
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close
# changing file name
        root.title(os.path.basename(file) + "-Notepad")

    else:
        #save the file
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close
def saveasFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])
        if file == "":
            file=None
# saving as new file
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close
# changing file name
        root.title(os.path.basename(file) + "-Notepad")

    else:
        #save the file
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def help():
    showinfo("Notepad", "If you need any help please contact me through e-mail:\n sangamprashar3@gmail.com")
def about():
    showinfo("Notepad", "this is my third project on Python GUI using tkinter.\n Hope you like it..")
def quit():
    root.destroy()



# Designing GUI
if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("644x788")

# add text Area
    TextArea =Text(root, font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH,expand=True)
    
#menu bar Start
    MenuBar = Menu(root)

    #file menu start
    FileMenu = Menu(MenuBar, tearoff=0)
    # to open new file
    FileMenu.add_command(label="New",command=newFile)
    # to open new file
    FileMenu.add_command(label="Open",command=openFile)
    FileMenu.add_separator()
    # to open new file
    FileMenu.add_command(label="Save",command=saveFile)
    # to open new file
    FileMenu.add_command(label="Save as",command=saveasFile)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    #file menu end

    #Edit menu start
    EditMenu = Menu(MenuBar, tearoff=0)
    # to cut
    EditMenu.add_command(label="Cut",command=cut)
    # to copy
    EditMenu.add_command(label="Copy",command=copy)
    # to paste
    EditMenu.add_command(label="Paste",command=paste)
    # to open new file
    #EditMenu.add_command(label="###",command=###)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    #edit menu end

    #Help menu start
    HelpMenu = Menu(MenuBar, tearoff=0)
    # for Help
    HelpMenu.add_command(label="Help",command=help)
    HelpMenu.add_command(label="About",command=about)
    HelpMenu.add_separator()
    # To Quit
    HelpMenu.add_command(label="Quit",command=quit)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    #Help menu end

    root.config(menu=MenuBar)
# Menu bar End


# adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
#scrollbar end

root.mainloop()# ending 