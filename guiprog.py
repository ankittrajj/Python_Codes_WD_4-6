#gui ----> graphical user interface
#tkinter----> gui based module

#import
from tkinter import *
# object of tkinter
window = Tk()

# title
window.title('myfirstgui')

# function
def click():
    enter_text = textEntry.get()
    output.delete(0.0,END)
    try:
        define = my_dict[enter_text]
    except:
        define = 'not avaliable in dict'
    output.insert(END,define)

#make a background for our gui
# photo = PhotoImage(file = 'download (1).png')

# create a label
# Label(window,image=photo).grid(row=0,column=0,sticky=E)

#text label
Label(window,text="Enter something useful",bg='red',fg='black',font='none 12 bold').grid(row=1,column=0,sticky=W)

# text box
textEntry = Entry(window,width=30,bg='white')
textEntry.grid(row=1,column=1,sticky=W)

# submit button
Button(window,text='Submit',width=10,command=click,bg='red',fg='black').grid(row=3,column=0,sticky=W)

#another textlabel
Label(window,text='\nDefination',bg='red',fg='white',font='none 12 bold').grid(row=4,column=0,sticky=W)

#create a text box
output = Text(window,width=60,height=10,wrap=WORD,background='white')
output.grid(row=5,column=0,sticky=W)

# make a dict
my_dict={
    'animal':['dog','cat'],
    'bug':'some error while coding'
}



# this is our window loop which will run infinite time until you close the window!!
window.mainloop()
