from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from urllib.request import urlopen    #for web scraping
from bs4 import BeautifulSoup   #for beautification


def click():
    try:
        url = "https://en.wikipedia.org/wiki/" + e.get()
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        global text_box
        text_box=Text(MidViewForm,height=60,width=100,padx=3,pady=5,font=("helvetica",14))
        text_box.insert(1.0,text)
        text_box.grid()

        """scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = Scrollbar(MidViewForm,column=2,selectmode="extended", height=100, yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)"""

    except Exception:
        messagebox.showwarning("error", "You have entered invalid input")

#remove previous search results
def clearb():
    text_box.destroy()


display_screen = Tk()                   #creating window
display_screen.geometry("900x800")      #setting width and hight
display_screen.title("The Astronomical Metadata")
TopViewForm=Frame(display_screen,width=600,bd=1,relief=SOLID)   #topview frame for heading
TopViewForm.pack(side=TOP,fill=X)

#first left frame for search menu
LFrom = Frame(display_screen, width=350)
LFrom.pack(side=LEFT, fill=Y)

# mid frame for displaying data
MidViewForm = Frame(display_screen, width=900)
MidViewForm.pack(side=TOP,padx=0,pady=25)

# label for heading
lbl_text = Label(TopViewForm, text="The Astronomical Metadata", font=('verdana', 18), width=600, bg="#20bebe",fg="white")
lbl_text.pack(fill=X)
Label(LFrom, text="Planet  ", font=("Arial", 12)).pack(side=TOP)
e=Entry(LFrom,font=("Arial",14,"bold"))


e.pack(side=TOP, padx=10, fill=X)



#creating search button
btn_search = Button(LFrom, text="Search",bg="#FFA500",command=click)
btn_search.pack(side=TOP, padx=10, pady=10, fill=X)


btn_clear = Button(LFrom, text="refresh",bg="#FF7F50",command=clearb)
btn_clear.pack(side=TOP, padx=10, pady=10, fill=X)

display_screen.mainloop()
