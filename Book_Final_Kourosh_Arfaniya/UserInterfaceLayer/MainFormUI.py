from tkinter import *
from Model.UserModel import User



class MainUIClass:
    def __init__(self, userparam:User):
        self.User = userparam

    def MainUI_formLoad(self):

        MainFormUI = Tk()
        MainFormUI.title('register Book')
        MainFormUI.geometry('330x540')
        x = int(MainFormUI.winfo_screenwidth() / 2 - (330 / 2))
        y = int(MainFormUI.winfo_screenheight() / 2 - (540 / 2))
        MainFormUI.geometry('+{}+{}'.format(x, y))
        MainFormUI.resizable(0, 0)
        MainFormUI.iconbitmap('images/mainFormicon.ico')
        bg_image = PhotoImage(file='images/books_PNG_transparency.png')
        bg_label = Label(MainFormUI, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)


        #region Function
        def exitForm(*args):
            MainFormUI.destroy()

        def setClock():
            from datetime import datetime
            currentDateTime = datetime.today()
            currentDateTime = currentDateTime.strftime('%Y-%m-%d %H:%M:%S')
            txtCurrentDateTime.set('today: ' + currentDateTime)
            MainFormUI.after(1000, setClock)

        def bookCRUD():
            from UserInterfaceLayer.BookUI import BookUIClass
            MainFormUI.destroy()
            bookUIObject = BookUIClass()
            bookUIObject.BookUI_formLoad(userObject=self.User)

        def authorList():

            pass

        def publisherList():
            pass





        lblWelcaomMessage = Label(MainFormUI, text=f'welcome {self.User.FirstName} {self.User.LastName} !'
                                  , bg='#D3D3D3', fg='black')
        lblWelcaomMessage.grid(row=0, column=0, padx=10, pady=11, sticky='w')

        txtCurrentDateTime = StringVar()
        lblCurrentDateTime = Label(MainFormUI, textvariable=txtCurrentDateTime, bg='#D3D3D3', fg='black')
        lblCurrentDateTime.grid(row=0, column=1, padx=10, pady=11, sticky='w')

        lblForShowX = Label(MainFormUI, text='Press X Button On Your Keyboard For Exit!'
                            , bg='#D3D3D3', fg='black')
        lblForShowX.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 11), sticky=NSEW)

        bookPhoto = PhotoImage(file='images/Book.png')
        btnBook = Button(MainFormUI, text='Book CRUD', width=280, height=140,
                         image=bookPhoto, command=bookCRUD, compound=LEFT, relief='groove'
                         , bg='#D3D3D3', fg='black')
        btnBook.grid(row=2, column=0, columnspan=2, padx=10, pady=3, sticky='S')

        authorPhoto = PhotoImage(file='images/Author.png')
        btnAuthor = Button(MainFormUI, text='Author List', width=280, height=140,
                            image=authorPhoto, command=authorList, compound=LEFT, relief='groove'
                           , bg='#D3D3D3', fg='black')
        btnAuthor.grid(row=3, column=0, columnspan=2,padx=10, pady=3, sticky='S')

        publisherPhoto = PhotoImage(file='images/Publisher.png')
        btnPublisher = Button(MainFormUI, text='Publisher List', width=280, height=140,
                            image=publisherPhoto, command=publisherList, compound=LEFT, relief='groove'
                            , bg='#D3D3D3', fg='black')
        btnPublisher.grid(row=4, column=0,columnspan=2, padx=10, pady=3, sticky='S')







        MainFormUI.after(0, setClock)
        MainFormUI.bind('x', exitForm)
        MainFormUI.mainloop()