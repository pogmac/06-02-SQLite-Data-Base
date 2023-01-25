import sqlite3

print('starting..')
cnn =None
filename = r"C:\projects\06-02-SQLite-Data-Base\time.db"
try:
    cnn =sqlite3.connect(filename)
    print('database connected..')
    cs = cnn.cursor()
    sql = ("Create Table if not exists MY_DATES ("
            " DateID int not null primary key,"
            " TextDate text,"
            " IntDate int,"
            " Comment text);")
    cs.execute(sql) #it does not require commit since its ddl it will create a table without a commmit
    print('created..')            
    sql = ("Insert into MY_DATES"
            " (DateID, textDate, IntDate, Comment)"
            " Values (1, date('2022-08-15'),"
            " unixepoch('2022-08-20'), 'Example 1');")# unixepoch returns the number of seconds from the ?1970.01.01 00:00?
    #cs.execute(sql)
    sql = ("Insert into MY_DATES"
            " (DateID, textDate, IntDate, Comment)"
            " Values (5, date('2022-08-16 14:34'),"
            " unixepoch('2022-08-20 23:15:01'), 'Example 4');")# unixepoch returns the number of seconds from the ?1970.01.01 00:00?
    #cs.execute(sql)
    sql = ("Insert into MY_DATES"
            " (DateID, textDate, IntDate, Comment)"
            " Values (3, date('2022-08-12 14:55:01'),"
            " unixepoch('2022-09-30 01:45:14'), 'Example 3');")# unixepoch returns the number of seconds from the ?1970.01.01 00:00?
    #cs.execute(sql)
    sql = ("Insert into MY_DATES"
            " (DateID, textDate, IntDate, Comment)"
            " Values (6, datetime('2022-08-12 14:55:01'),"
            " unixepoch('2022-09-30 01:45:14'), 'Example 6');")# unixepoch returns the number of seconds from the ?1970.01.01 00:00?
    #cs.execute(sql)
    cnn.commit()
    print('inserted..')
    sql = 'Select * From MY_DATES;'
    sql = "Select datetime(IntDate, 'unixepoch') MyUnixDate From MY_DATES;"
    sql = "Select date(IntDate, 'unixepoch') MyUnixDate From MY_DATES;"
    recs = cs.execute(sql)
    for rec in recs:
        print(rec)
except Exception as e:
    print(e)
finally:
    if cnn:
        cnn.close()            
        print('connection closed..')
print('done')        


