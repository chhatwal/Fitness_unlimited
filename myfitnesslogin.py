import myfitnesspal
import datetime

from Tkinter import *

root=Tk()
root.title("Login Screen")
root.geometry("400x300+0+0")

#creating the labels 
label_1=Label(root, text="Username")
label_2=Label(root, text="Password")
label_1.grid(row=3,column=0,sticky=E)
label_2.grid(row=4,column=0,sticky=E)

# text boxes declaration 
entry_1=Entry(root)
entry_2=Entry(root)
entry_1.grid(row=3,column=1)
entry_2.grid(row=4,column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)


# button declaration and grid  allocation 
button_ok=Button(root,text="OK")
button_cancel=Button(root,text="Cancel")
button_ok.grid(row=7,column=1,sticky=W)
button_cancel.grid(row=7, column=1,sticky=E)

# forgot password and sign up button

button_fgp=Button(root, text="Forgot Password")
button_fgp.grid(row=9, column= 1)
button_signup=Button(root, text="Sign Up!")
button_signup.grid(row=10, column=1)
root.mainloop()
