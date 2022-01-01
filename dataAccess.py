import sqlite3
import os
from sqlite3 import Error

class QrDataAccess:
    def __init__(self):
        self.dbFile = os.path.dirname(os.path.abspath(__file__)) 
        self.dbFile += '\\sqlite\\db\\QrDatabase'
        self.createTable()

    def createConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.dbFile)
        except Error as e:
            print(e)
        
        return connection

    def createTable(self):
        sql = '''create table if not exists QrCodes(
                id integer primary key,
                data text not null,
                unique(data)
            );'''
        connection = self.createConnection()
        
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def addQrCode(self, qrCode):
        sql = '''insert into QrCodes(data)
            values(?)'''
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql, (qrCode,))
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def getAllQrCodes(self):
        sql = 'select data from QrCodes'
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            result = [row[0] for row in rows]
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

        return result

    def deleteAllQrCodes(self):
        sql = 'delete from QrCodes'
        connection = self.createConnection()

        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
