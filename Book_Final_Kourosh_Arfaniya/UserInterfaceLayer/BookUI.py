import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from BusinessLogicLayer.BookBLL import BookBLLClass
from Model.BookModel import BookModelClass
from Model.UserModel import User

class BookUIClass:

    def BookUI_formLoad(self, userObject:User):

        registerBookForm = Tk()
        registerBookForm.title('register Book')
        registerBookForm.geometry('580x670')
        registerBookForm.iconbitmap('images/RegisterBookForm.ico')
        registerBookForm.resizable(0,0)
        x = int(registerBookForm.winfo_screenwidth() / 2 - (580 / 2))
        y = int(registerBookForm.winfo_screenheight() / 2 - (670 / 2))
        registerBookForm.geometry('+{}+{}'.format(x, y))

        bookGenreList = dict()


        def getBookGenreList():
            from BusinessLogicLayer.BookBLL import BookBLLClass
            bookBLLObject = BookBLLClass()
            rows = bookBLLObject.getBookGenreList()

            if len(rows)>0:
                for row in rows:
                    if row[1] not in bookGenreList:
                        bookGenreList[row[1]] = row[0]

            return bookGenreList

        def showList(*args):
            trvBookList.delete(*trvBookList.get_children())
            commandText ='''select C.ID,C.BookName,C.Author,C.Publisher,CC.BookGenre   from Book as C inner join BookGenre as CC
                            on C.BookGenreID = CC.ID'''
            connectionString = 'DB/databasefolder.db'
            with sqlite3.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, )
                rows = cursor.fetchall()
                rowCount = 0
                if len(rows)>0:
                    for row in rows:
                        rowCount += 1
                        values = [rowCount]
                        for value in row:
                            if value == None:
                                values.append("")
                            else:
                                values.append(value)
                        trvBookList.insert("","end",values=values)

        def resetform():
            for widget in lblfrmBookInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0,END)
                txtBookGenre.set("")
                txtBookID.set("")
                lblBookImage.config(image=bookImage)

        def registerBookFunction():
            bookName = txtBookName.get()
            author = txtAuthor.get()
            publisher = txtPublisher.get()
            bookGenreID = bookGenreList[txtBookGenre.get()]
            bookModelObject = BookModelClass(bookName, author, publisher,bookGenreID)
            bookBLLObject = BookBLLClass()
            bookBLLObject.registerBookFunction_BLL(bookModelObject)

            with open(txtBookPhotoPath.get(), mode='rb') as sourceFile:
                with open('images/'+bookName+'.png', mode='wb') as bookFile:
                    bookFile.write(sourceFile.read())

            showList()
            resetform()

        def editBookFunction():
            from BusinessLogicLayer.BookBLL import BookBLLClass
            from Model.BookModel import BookModelClass

            book = BookModelClass(bookName=txtBookName.get(),
                                      author=txtAuthor.get(),
                                      publisher=txtPublisher.get(),
                                      bookGenreID=bookGenreList[txtBookGenre.get()],
                                      id=txtBookID.get())
            bookBLLObject = BookBLLClass()
            bookBLLObject.updateBook(book)
            showList()
            resetform()

        def deleteBookFunction():
            if txtBookID.get() is not None:
                bookBLLObject = BookBLLClass()
                bookBLLObject.deleteBook(txtBookID.get())
            showList()

        def backToMainFunction():
            registerBookForm.destroy()
            from UserInterfaceLayer.MainFormUI import MainUIClass
            mainUIObject = MainUIClass(userparam=userObject)
            mainUIObject.MainUI_formLoad()

        def getFilePath():
            photoPath = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('png files','*.png')
                                                                                                     ,('jpeg files','*.jpg')
                                                                                                     ,('all files','*.*')))
            if photoPath is not None:
                txtBookPhotoPath.set(photoPath)

        def onTreeSelect(event):
            resetform()
            index = trvBookList.selection()
            if index:
                selectedValues = trvBookList.item(index)["values"]
                txtBookID.set(selectedValues[1])
                txtBookName.set(selectedValues[2])
                txtAuthor.set(selectedValues[3])
                txtPublisher.set(selectedValues[4])
                txtBookGenre.set(selectedValues[5])
                bookImage2.config(file=f'images/{selectedValues[2]}.png')
                lblBookImage.config(image=bookImage2)

        def checkValidation(*args):
            if len(txtBookName.get()) > 40:
                txtBookName.set(txtBookName.get()[:len(txtBookName.get()) - 1])



        lblfrmBookInfo = LabelFrame(registerBookForm, text='Book Info')
        lblfrmBookInfo.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

        lblBookIDTitle = ttk.Label(lblfrmBookInfo, text='BookID: ', style="CustomLabel.TLabel")
        lblBookIDTitle.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        txtBookID = StringVar()
        lblBookID = ttk.Label(lblfrmBookInfo, textvariable=txtBookID)
        lblBookID.grid(row=0, column=0, padx=10, pady=5, sticky='e')

        lblBookName = ttk.Label(lblfrmBookInfo, text='BookName:', style="CustomLabel.TLabel")
        lblBookName.grid(row=1, column=0, padx=10, pady=5)

        txtBookName = StringVar()
        txtBookName.trace('w',checkValidation)
        entBookName = ttk.Entry(lblfrmBookInfo, width=40, textvariable=txtBookName)
        entBookName.grid(row=2, column=0, padx=10, pady=5)

        lblAuthor = ttk.Label(lblfrmBookInfo, text='Author:', style="MyLabel.TLabel")
        lblAuthor.grid(row=3, column=0, padx=10, pady=5)

        txtAuthor = StringVar()
        entAuthor = ttk.Entry(lblfrmBookInfo, width=40, textvariable=txtAuthor)
        entAuthor.grid(row=4, column=0, padx=10, pady=5)

        lblPublisher = ttk.Label(lblfrmBookInfo, text='Publisher:', style="MyLabel.TLabel")
        lblPublisher.grid(row=3, column=1, padx=10, pady=5)

        txtPublisher = StringVar()
        entPublisher = ttk.Entry(lblfrmBookInfo, width=40, textvariable=txtPublisher)
        entPublisher.grid(row=4, column=1, padx=10, pady=5)

        txtBookGenre = StringVar()
        lblBookGenre = ttk.Label(lblfrmBookInfo, text='Book Genre:', style="MyLabel.TLabel")
        lblBookGenre.grid(row=5, column=0, padx=10, pady=5)

        cmbBookGenre = ttk.Combobox(lblfrmBookInfo, textvariable=txtBookGenre, state='readonly',
                                         values=list(getBookGenreList().keys()), width=37)
        cmbBookGenre.grid(row=6, column=0, padx=10, pady=5)

        lblBookPhotoPath = ttk.Label(lblfrmBookInfo, text='PhotoPath: ', style="MyLabel.TLabel")
        lblBookPhotoPath.grid(row=5, column=1, padx=10, pady=5)

        txtBookPhotoPath = StringVar()
        entPhotoPath = ttk.Entry(lblfrmBookInfo, width=32, textvariable=txtBookPhotoPath)
        entPhotoPath.grid(row=6, column=1, padx=10, pady=5, sticky='w')

        btnFileDialog = ttk.Button(lblfrmBookInfo, text='...', width=6, command=getFilePath)
        btnFileDialog.grid(row=6, column=1, padx=10, pady=5, sticky='e')

        btnRegisterBook = ttk.Button(lblfrmBookInfo, text='register Book', width=60, command=registerBookFunction, style="MyButton.TButton")
        btnRegisterBook.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='S')

        btnEditBook = ttk.Button(lblfrmBookInfo, text='Edit Book', width=25, command=editBookFunction, style="MyRedButton.TButton")
        btnEditBook.grid(row=8, column=1, padx=10, pady=5, sticky='w')

        btnDeleteBook = ttk.Button(lblfrmBookInfo, text='delete Book', width=25,command=deleteBookFunction, style="MyRedButton.TButton")
        btnDeleteBook.grid(row=8, column=0, padx=10, pady=5, sticky='e')

        btnBackToMain = ttk.Button(lblfrmBookInfo, text='backToMain', width=25,command=backToMainFunction, style="MyRedButton.TButton")
        btnBackToMain.grid(row=9, column=1, padx=10, pady=5, sticky='w')

        btnClearForm = ttk.Button(lblfrmBookInfo, text='Clear Form', width=25, command=resetform, style="MyRedButton.TButton")
        btnClearForm.grid(row=9, column=0, padx=10, pady=5, sticky='e')


        bookImage = PhotoImage(file='images/Default image.png')
        bookImage2 = PhotoImage(file='images/Default image.png')
        lblBookImage = ttk.Label(lblfrmBookInfo, image=bookImage)
        lblBookImage.grid(row=0, column=1, rowspan=3, padx=20, pady=20)


        # Style Region

        style = ttk.Style()
        style.configure("MyButton.TButton", background="red", foreground="black", padding=2)
        style.map("MyButton.TButton",
                  background=[('active', 'cyan'), ('pressed', 'magenta')],
                  foreground=[('active', 'black'), ('pressed', 'darkred')])

        style_twe = ttk.Style()
        style_twe.configure("MyRedButton.TButton", background="green", foreground="black", padding=1)
        style_twe.map("MyRedButton.TButton",
                      background=[('pressed', '#8B0000')],
                      foreground=[('pressed', 'white')])

        style_three = ttk.Style()
        style_three.configure("MyLabel.TLabel", foreground="blue", padding=1)

        style = ttk.Style()
        style.configure("CustomLabel.TLabel", foreground="orange", padding=8)

        # End Style Region


        lblfrmBookList = LabelFrame(registerBookForm, text='Book List')
        lblfrmBookList.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        _columns = ["Index", "ID", "BookName", "Author", "Publisher", "BookGenre"]
        _displayColumns = ["Index", "BookName", "Author", "Publisher", "BookGenre"]
        trvBookList = ttk.Treeview(lblfrmBookList, columns=_columns, displaycolumns=_displayColumns,
                                     selectmode="browse", show="headings")
        trvBookList.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)

        trvBookList.bind('<<TreeviewSelect>>',onTreeSelect)
        trvBookList.column("#0", width=0)

        trvBookList.column("Index", width=30)
        trvBookList.heading("Index", text="#", anchor="n")

        trvBookList.column("ID", width=0)
        trvBookList.heading("ID", text="ID", anchor="n")

        trvBookList.column("BookName", width=160)
        trvBookList.heading("BookName", text="Book Name", anchor="n")

        trvBookList.column("Author", width=100)
        trvBookList.heading("Author", text="Author", anchor="n")

        trvBookList.column("Publisher", width=100)
        trvBookList.heading("Publisher", text="Publisher", anchor="n")

        trvBookList.column("BookGenre", width=160)
        trvBookList.heading("BookGenre", text="BookGenre", anchor="n")


        showList()
        registerBookForm.mainloop()
