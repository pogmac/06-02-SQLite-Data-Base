import sqlite3

print('starting..')
conn = None
filename = r"C:\projects\06-02-SQLite-Data-Base\database-progress.db"
try:
    conn = sqlite3.connect(filename)
    print('database connected..')
    cs = conn.cursor()

    sql = ("CREATE TABLE IF NOT EXISTS STUDY_LOG("
            "id INT NOT NULL PRIMARY KEY,"
            "textdate TEXT," 
            "hours REAL," 
            "topic TEXT," 
            "details TEXT," 
            "comment TEXT);")
    cs.execute(sql)

    sql = ("CREATE TABLE IF NOT EXISTS COACH_LOG("
            "id INT NOT NULL PRIMARY KEY,"
            "textdate TEXT);")
    cs.execute(sql)

    sql = "ALTER TABLE STUDY_LOG ADD IntDate INT" # ALTER
    #cs.execute(sql)            
    sql = "DROP TABLE STUDY_LOG" # DROP
    #cs.execute(sql)            
    sql = ("UPDATE STUDY_LOG SET textdate = date('2022-12-06') WHERE id = 2") # UPDATE
    #cs.execute(sql)            

    sql = ("INSERT INTO STUDY_LOG" 
           "(id,textdate, hours, topic, details, comment)"
          "VALUES(13,date('2022-12-30'), 6, 'mod 03_03,04,05 GitHub Repository push pull, mod 02 Coach review', 'pro','three solutions of the dice task');")
#    cs.execute(sql)

    sql = ("INSERT INTO COACH_LOG" 
           "(id,textdate)"
          "VALUES(2,date('2022-12-30'));")
#    cs.execute(sql)

    conn.commit()
    print("inserted..")
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()
        print('connection closed..')    
print('done')