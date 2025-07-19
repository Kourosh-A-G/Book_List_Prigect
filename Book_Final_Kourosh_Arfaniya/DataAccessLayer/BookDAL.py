import sqlite3
from Model.BookModel import BookModelClass



class BookDALClass:

    def registerBookFunction(self, bookModelObject:BookModelClass):

        connectionString = 'DB/databasefolder.db'
        commandText = 'insert into Book (BookName,Author,Publisher,BookGenreID) VALUES(?,?,?,?)'

        sqlConnection = sqlite3.connect(connectionString)
        sqlcursor =sqlConnection.cursor()
        sqlcursor.execute(commandText,(bookModelObject.BookName,bookModelObject.Author,bookModelObject.Publisher,bookModelObject.BookGenreID))
        sqlConnection.commit()
        sqlConnection.close()

    def getBookGenreList(self):
        connection = 'DB/databasefolder.db'
        commandText = 'select ID,BookGenre from BookGenre'
        sqlConnection = sqlite3.connect(connection)
        sqlcursor = sqlConnection.cursor()
        sqlcursor.execute(commandText, )
        rows = sqlcursor.fetchall()
        return rows

    def deleteBook(self, BookID: int):
        commandText = 'DELETE FROM Book WHERE id=?'
        connection = 'DB/databasefolder.db'
        sqlConnection = sqlite3.connect(connection)
        sqlcursor = sqlConnection.cursor()
        sqlcursor.execute(commandText, (BookID, ))
        sqlConnection.commit()
        sqlConnection.close()

    def updateBook(self, bookObject:BookModelClass):
        commandText ="update Book set BookName=? , Author=? , Publisher=? , BookGenreID=? where id=?"
        params = (bookObject.BookName, bookObject.Author, bookObject.Publisher,bookObject.BookGenreID, bookObject.ID)
        connection = 'DB/databasefolder.db'
        sqlConnection = sqlite3.connect(connection)
        sqlcursor = sqlConnection.cursor()
        sqlcursor.execute(commandText, params)
        sqlConnection.commit()
        sqlConnection.close()