from Tkinter import *

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.headerFont = ("Comic Sans", "16", "bold italic")
		
		self.title("SignUp Form")
		self.geometry("550x300+0+0")
		self.setInfo()

	def setInfo(self):
		Label(self, text = "Enter the details",
				font = self.headerFont).grid(columnspan = 6)
        
		#get user's First Name
                Label(self, text = "First Name").grid(row = 1, column = 0)
                self.txtFirstName = Entry(self)
                self.txtFirstName.grid(row = 1, column = 1)
                #using the insert function to default all fields to "0"
                self.txtFirstName.insert(0, "First Name")
		
		#get user's Last Name 
                Label(self, text = "Last Name").grid(row = 2, column = 0)
                self.txtLastName = Entry(self)
                self.txtLastName.grid(row = 2, column = 1)
       		self.txtLastName.insert(0,"Last Name")


		#get user's name
		Label(self, text = "UserName \n(keep same as email").grid(row = 3, column = 0)
		self.txtUserName = Entry(self)
		self.txtUserName.grid(row = 3, column = 1)
		self.txtUserName.insert(0, "User Name")
		
		#get users password 
		Label(self, text = "Password").grid(row = 4, column = 0)
		self.txtPassword = Entry(self)
		self.txtPassword.grid(row = 4, column = 1)
		self.txtPassword.insert(0,"Password")

		#get confirm password
		Label(self, text = "Confirm Password").grid(row = 5, column = 0)
		self.txtConfPass = Entry(self)
		self.txtConfPass.grid(row = 5, column = 1)
		self.txtConfPass.insert(0, "Confirm Password")

		#get Email address 
                Label(self, text = "Email Address").grid(row = 6, column = 0)
                self.txtEmailAdd = Entry(self)
                self.txtEmailAdd.grid(row = 6, column = 1)
		self.txtEmailAdd.insert(0, "Email @address")
               

		#label for value checks that have to be done
		
		self.label_FNE = Label(self)
		self.label_FNE.grid(row = 1, column = 4)
		self.label_LNE=Label(self)
		self.label_LNE.grid(row=2,column=4)
		self.label_show=Label(self)
		self.label_show.grid(row=5, column=4)
		self.label_emailCheck=Label(self)
                self.label_emailCheck.grid(row=6, column=4)

		#button OK info
		self.btnOk = Button(self, text = "OK")
		self.btnOk.grid(row = 7, columnspan = 5)
		self.btnOk["command"] = self.calcCheck

			  
	def calcCheck(self):
		#Check of the Values in the Form

		#Check for the values 
		FirstN=self.txtFirstName.get()
		LastN=self.txtLastName.get()
		Pass = self.txtPassword.get()
		Pass_conf = self.txtConfPass.get()
		email=self.txtEmailAdd.get()
		#check  if the informaiton if correct?? 
		if FirstN=="First Name" or FirstN=="":
			self.label_FNE["text"]="Please enter a First Name"
		if LastN=="Last Name" or LastN=="":
			self.label_LNE["text"]="Please enter a last Name"
		if  Pass!=Pass_conf:
			self.label_show["text"]="Passwords Don't Match !"
		if email=="Email @address" or email==" " :
			self.label_emailCheck["text"]="Enter the Email"

def main():
	a = App()
	a.mainloop()


if __name__ == "__main__":
	main()
