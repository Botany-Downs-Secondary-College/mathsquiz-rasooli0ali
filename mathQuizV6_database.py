
from tkinter import*
from random import*
import sqlite3


conn = sqlite3.connect('BDSC_Students.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Student (firstname text, age text, score text)")
conn.commit()
conn.close()

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

        self.diff=["Easy","Medium","hard","superhard"]
        self.diff_lvl=StringVar()
        self.diff_lvl.set(0)
        self.diff_btns=[]

        for i in range(len(self.diff)):
            rb=Radiobutton(self.questions, variable=self.diff_lvl,value=i,text=self.diff[i], anchor="w",padx=30)
            self.diff_btns.append(rb)
            rb.grid(row=i+30,column=0, sticky="w")
            print(i)

        #Buttons for question frame
        self.homebutton = Button(self.questions,text="Home",anchor=W,command=self.show_frame1,padx=15)
        self.homebutton.grid(row=51, column=0, sticky=W)

        self.nextbutton_2=Button(self.questions,text="next", anchor=E, command=self.check_entries,padx=20)
        self.nextbutton_2.grid(row=51,column=1, sticky=E)


        #third Frame where the questions are:
        self.questions_1 = Frame(parent)
        self.questionsLabel_1 = Label(self.questions_1, bg="black", fg="white", width=20, padx=30, pady=10,
                                    text="Answer Quiz Questions", font=("times", "14", "bold italic"))
        self.questionsLabel_1.grid()

        #question frame
        self.index=0
        self.score=0

        self.Question=Frame(parent)
        self.QuestionsLabel = Label(self.Question,bg="black",fg="white",width=20,padx=30,pady=10,
                                    text="Answer Quiz Questions",font=("times", "14", "bold italic"))
        self.QuestionsLabel.grid(columnspan=3)

        self.problem=Label(self.Question, text="")
        self.problem.grid(row=1,column=0)

        self.AnswerEntry=Entry(self.Question, width=20)
        self.AnswerEntry.grid(row=1,column=1)
        #create ScoreLabel
        self.Scorelabel=Label(self.Question, text="")
        self.Scorelabel.grid(row=1,column=2)

        self.FeedBack=Label(self.Question, text="")
        self.FeedBack.grid(row=2,columnspan=3)

        self.HomeButton=Button(self.Question, text="Home", command=self.show_frame1)
        self.HomeButton.grid(row=3,column=0)

        self.checkanswer=Button(self.Question, text="check answer", command=self.question_check)
        self.checkanswer.grid(row=3,column=1)
        self.next_question()
        self.AnswerButton=Button(self.Question, text="next question", command=self.next_question)
        self.AnswerButton.grid(row=3,column=2)

    #function for calling
    def show_frame2(self):
        self.welcome.grid_remove()
        self.questions.grid()

    def show_frame1(self):
        self.questions.grid_remove()
        self.welcome.grid()
        
    def show_frame3(self):
        self.questions.grid_remove()
        self.welcome.grid_remove()
        self.Question.grid()

    def check_entries(self):
        poop=0
        for i in self.gettingvar:
            if i.get()=="":
                self.lab_mt.config(text="Do not leave any spaces empty")
            elif i.get().isalpha() == False:
                self.lab_mt.config(text="dont use digits or space")
            else:
                poop=poop+1

            if poop==2:
                username=self.gettingvar[0].get()
                Age=self.gettingvar[1].get()
                Username=self.gettingvar[0].get()

                conn = sqlite3.connect('BDSC_Students.db')
                c = conn.cursor()
                finduser = "SELECT * FROM Student WHERE firstname = ?"
                c.execute(finduser, [(Username)])  # Checks existence of username in database
                if c.fetchall():
                    self.lab_mt.configure(text="username taken", bg="red")
                else:
                    insertData = ('''INSERT INTO Student (firstname text, age text)
                                    VALUES(?,?)''')  # Inserts new account into database
                    c.execute(insertData, [username, Age])
                    
                    conn.commit()
                    conn.close()
                    self.show_frame3()
                    
    def next_question(self):
        x=randrange(10)
        y=randrange(10)
        self.answer=x+y
        self.index+=1

        question_text=str(x)+" + "+str(y)+" = "
        self.problem.config(text=question_text)
        self.QuestionsLabel.config(text="Quiz Question "+str(self.index)+"/5")
        if self.index >=6:
            self.Question.grid_remove()
            self.welcome.grid()
        
    def question_check(self):
        try:
            ans=int(self.AnswerEntry.get())
            if ans==self.answer:
                self.FeedBack.config(text="Correct", fg="green")
                self.score +=1
                score_text="Score = " +str(self.score)
                self.Scorelabel.config(text=score_text)
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
            else:
                self.FeedBack.config(text="incorrect", fg="red")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()
        except ValueError:
            self.FeedBack.config(text="enter number")
            self.AnswerEntry.delete(0,END)
            self.AnswerEntry.focus()
        

if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("OOP")
    root.mainloop()
