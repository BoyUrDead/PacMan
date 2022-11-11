import imports
db= imports.mysql.connector.connect(host='localhost', user='root', password='admin', database='pacman')
c=db.cursor()
def view():
    run="select * from packages;"
    c.execute(run)
    data=c.fetchall()
    for i in data:
        return i
    if i[1] == 'Eterm':
        print("OK")
    else:
        print("NO")