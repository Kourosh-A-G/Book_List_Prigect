from DataAccessLayer.BookDAL import BookDALClass
from Model.BookModel import BookModelClass

class BookBLLClass:



    def registerBookFunction_BLL(self, bookModelObject:BookModelClass):
        bookDALObject = BookDALClass()
        bookDALObject.registerBookFunction(bookModelObject)

    def getBookGenreList(self):
        bookDALObject = BookDALClass()
        return bookDALObject.getBookGenreList()

    def deleteBook(self, bookID: int):
        bookDALObject = BookDALClass()
        bookDALObject.deleteBook(bookID)

    def updateBook(self, bookObject: BookModelClass):
        bookDALObject = BookDALClass()
        bookDALObject.updateBook(bookObject)