import mysql.connector

db= mysql.connector.connect(host='localhost', user='root', password='none', database='pacman')
c=db.cursor()
def get_data():
    run="select * from packages;"
    c.execute(run)
    data=c.fetchall()
    return data

def view():
    data = get_data()
    for i in data:
        print(i[0])