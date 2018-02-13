from Tkinter import *
import tkFont
import sqlite3
import math
# from tkinter.font import Font

class records():
     #class created to see records that have been previously inputted#
    def __init__(self,master):
        self.master=master
        self.master.geometry('2500x2000+0+0')
        self.master.title('Realtime Vehicle Database')
        self.connection = sqlite3.connect('./test.db')
        self.cur = self.connection.cursor()
        self.heading = Label(self.master,
		 text="Realtime Database for Vehicals in parking lot",
		 fg = "white",
		 bg = "#0000ff",
         pady = "30px",
		 font=("Helvetica",30))
        self.heading.grid(row=0,columnspan=4)
        self.regNoLabel = Label(self.master,compound=CENTER ,borderwidth=2,relief = "solid",pady="20px", text="Reg_no", width=20, font=("Helvetica",20))
        self.regNoLabel.grid(row=1, column=0)
        self.entryTimeLabel = Label(self.master,borderwidth=2,relief = "solid",pady="20px", text="Entritime", width=20, font=("Helvetica",20))
        self.entryTimeLabel.grid(row=1, column=1)
        self.exitTimeLabel = Label(self.master,borderwidth=2,relief = "solid",pady="20px", text="Exittime", width=20, font=("Helvetica",20))
        self.exitTimeLabel.grid(row=1, column=2)
        self.costLabel = Label(self.master,borderwidth=2,relief = "solid",pady="20px", text = "Charge/Fare", width=20, font=("Helvetica",20))
        self.costLabel.grid(row=1, column = 3)
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            a,b= math.modf(round(2345678*0.000277778, 2))
            c,d =math.modf(round(5678907*0.000277778, 2))
            Label(self.master, text=dat[0],borderwidth=2,relief = "groove",width = 20,pady="20px", font=("Helvetica",20)).grid(row=index+2, column=0)
            Label(self.master, text=str(b) +"hrs "+  str(a*100)+"min",borderwidth=2,relief = "groove",width = 20,pady="20px", font=("Helvetica",20)).grid(row=index+2, column=1)
            Label(self.master, text=str(d) +"hrs "+  str(c*100)+"min",borderwidth=2,relief = "groove",width = 20,pady="20px", font=("Helvetica",20)).grid(row=index+2, column=2)
            Label(self.master, text=dat[3],borderwidth=2,relief = "groove",width = 20,pady="20px", font=("Helvetica",20)).grid(row=index+2, column=3)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM PARKING")
        return self.cur.fetchall()
#
# s = Style();
# s.configure(bg="blue")
root = Tk()
text = Text(root)
text.configure(font=("Times New Roman", 40, "bold"))
my_gui = records(root)
root.mainloop()