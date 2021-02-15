
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

        self.name_entry=Entry(self.questions)
        self.name_entry.grid(row=2,column=1)

        self.labels = ["name", "Last name"]
        for i in range(len(self.labels)):
            lab = Label(self.questions, text=self.labels[i], anchor="w",padx=35)
            lab.grid(row=1 + i,sticky="w")
            lab_mt=Label(self.questions,text=" ")
            lab_mt.grid(row=i+4)

        self.diff=["Easy","Medium","hard","Superhard"]
        self.diff_lvl=StringVar()
        self.diff_lvl.set(0)
        self.diff_btns=[]

        for i in range(len(self.diff)):
            rb=Radiobutton(self.questions, variable=self.diff_lvl,value=i,text=self.diff[i], anchor="w",padx=30)
            self.diff_btns.append(rb)
            rb.grid(row=i+5,column=0, sticky="w")

        self.homebutton = Button(self.questions,text="Home",anchor=W,command=self.show_frame1)
        self.homebutton.grid(row=50, column=0)


    #function for calling
    def show_frame2(self):
        self.welcome.grid_remove()
        self.questions.grid()

    def show_frame1(self):
        self.questions.grid_remove()
        self.welcome.grid()


if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("OOP")
    root.mainloop()
