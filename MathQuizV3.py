
from tkinter import*

class MathQuiz:
    def __init__(self, parent):

        #first Welcome frame
        self.welcome = Frame(parent)
        self.welcome.grid(row=0, column=0)
        self.Titlelabel = Label(self.welcome, bg="black", fg="white",width=20,padx=30,pady=10,
                                text="Welcome to Math Quiz",font=("times", "14", "bold italic"))
        self.Titlelabel.grid(columnspan=2)
        self.nextbutton = Button(self.welcome,text="Next",anchor=W, command=self.show_frame2)
        self.nextbutton.grid(row=8, column=1)
        
        #second frame made to for laved and choices
        self.questions = Frame(parent)
        self.questionsLabel = Label(self.questions,bg="black",fg="white",width=20,padx=30,pady=10,
                                    text="Answer Quiz Questions",font=("times", "14", "bold italic"))
        self.questionsLabel.grid(columnspan=2)
        self.labelempty=Label(self.questions, text="", padx=20, pady=5)
        self.labelempty.grid(row=1)

        self.labels = ["name", "Last name"]

        self.gettingvar=[]

        for i in range(len(self.labels)):
            self.lab = Label(self.questions, text=self.labels[i], anchor="w",padx=35)
            self.lab.grid(row=1 + i,sticky="w")
            for b in range(len(self.labels)):
                self.ent=Entry(self.questions)
                self.ent.grid(row=1+b,column=1)
                self.gettingvar.append(self.ent)

            #empty label for space
            self.lab_mt=Label(self.questions,text=" ")
            self.lab_mt.grid(row=4, columnspan=2)
            self.lab_diff = Label(self.questions, text=" Choose Difficulty")
            self.lab_diff.grid(row=5)

        self.diff=["Easy","Medium","hard","Superhard"]
        self.diff_lvl=StringVar()
        self.diff_lvl.set(0)
        self.diff_btns=[]

        for i in range(len(self.diff)):
            rb=Radiobutton(self.questions, variable=self.diff_lvl,value=i,text=self.diff[i], anchor="w",padx=30)
            self.diff_btns.append(rb)
            rb.grid(row=i+30,column=0, sticky="w")

        #Buttons for question frame
        self.homebutton = Button(self.questions,text="Home",anchor=W,command=self.show_frame1,padx=15)
        self.homebutton.grid(row=51, column=0, sticky=W)

        self.nextbutton_2=Button(self.questions,text="next", anchor=E, command=self.check_entries,padx=20)
        self.nextbutton_2.grid(row=51,column=1, sticky=E)

    #function for calling
    def show_frame2(self):
        self.welcome.grid_remove()
        self.questions.grid()

    def show_frame1(self):
        self.questions.grid_remove()
        self.welcome.grid()
    def check_entries(self):
        for i in range(len(self.gettingvar)):
            if self.gettingvar[i].get()=="":
                self.lab_mt.config(text="Do not leave any spaces empty")
            else:
                self.lab_mt.config(text="Thanks")

if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("OOP")
    root.mainloop()
