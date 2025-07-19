from tkinter import *
from tkinter import ttk
from BusinessLogicLayer.UserBLL import UserBLL
from Model.UserModel import  User



loginForm =Tk()
loginForm.title('Login Form')
loginForm.geometry('400x160')
loginForm.iconbitmap('images/loginicon.ico')
x = int(loginForm.winfo_screenwidth()/2 - (400/2))
y= int(loginForm.winfo_screenheight()/2 - (160/2))
loginForm.geometry('+{}+{}'.format(x,y))
loginForm.resizable(0,0)




def checkUserNamePassword():
    global counter
    userName = txtUserName.get().lower()
    password = txtPassword.get()
    userModelObject = User(userName=userName,password=password)
    userBLLObject = UserBLL()
    output = userBLLObject.getUserbyUserNamePassword(userModelObject)
    if len(output) > 0:
        userModelObject.FirstName = output[0][2]
        userModelObject.LastName = output[0][3]
        userModelObject.IsActive = output[0][4]
        loginForm.destroy()
        from UserInterfaceLayer.MainFormUI import MainUIClass
        mainUIObject = MainUIClass(userparam=userModelObject)
        mainUIObject.MainUI_formLoad()


lblUserName = Label(loginForm, text='UserName:')
lblUserName.grid(column=0, row=0, padx=10, pady=10)

txtUserName = StringVar()
entUserName = ttk.Entry(loginForm,textvariable=txtUserName ,width=40)
entUserName.grid(column=1 ,row=0, padx=10, pady=10)

lblPassword = Label(loginForm, text='Password:')
lblPassword.grid(column=0, row=1, padx=10, pady=10)

txtPassword =StringVar()
entPassword = ttk.Entry(loginForm,textvariable=txtPassword,show='*' ,width=40)
entPassword.grid(column=1 ,row=1, padx=10, pady=10)

btnLogin = ttk.Button(loginForm, text='Login', width=16, command=checkUserNamePassword)
btnLogin.grid(column=1, row=2, padx=10, pady=20, sticky='e')



loginForm.mainloop()