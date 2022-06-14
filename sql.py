import sqlite3

conection = sqlite3.connect("main.db")
cursor = conection.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS xaridor(ism TEXT,yosh INTEGER, qarz REAL)")
#cursor.execute("INSERT INTO xaridor (qarz,ism,yosh) VALUES(520000,'karim',26)")
#cursor.execute("INSERT INTO xaridor (ism, yosh,qarz) VALUES('Aziz',35,350000)")
#cursor.execute("INSERT INTO xaridor (ism, yosh,qarz) VALUES('Karim',24,350000)")
#cursor.execute("INSERT INTO xaridor (ism, yosh,qarz) VALUES('Kamol',54,350000)")
#cursor.execute("DELETE FROM xaridor WHERE yosh='karim'")
#cursor.execute("UPDATE xaridor SET ism='sardoba',yosh=22 WHERE qarz<520000")
#cursor.execute("UPDATE xaridor SET yosh= 25 WHERE yosh==34")
#cursor.execute("SELECT * FROM xaridor WHERE qarz>200000 ORDER BY ism")
#cursor.execute("SELECT * FROM xaridor WHERE qarz>200000 ORDER BY ism DESC")
#cursor.execute("SELECT * FROM xaridor WHERE qarz>200000 ORDER BY qarz DESC")
#cursor.execute("SELECT * FROM xaridor WHERE qarz>200000 ORDER BY qarz DESC LIMIT 2")
#cursor.execute("SELECT * FROM xaridor WHERE qarz>200000 ORDER BY qarz  LIMIT 3")
#cursor.execute("SELECT * FROM xaridor WHERE qarz>200000 ORDER BY qarz LIMIT 0,2")
#print(cursor.fetchall())
#for result in cursor:
   # print(result)
 #    print(f"Xaridor: {result[0]}, qarzi: {result[2]}")
#cursor.execute("SELECT * FROM xaridor ORDER BY qarz DESC")
#print(cursor.fetchone())


#cursor.execute("SELECT * FROM xaridor ORDER BY qarz DESC")
#print(cursor.fetchmany(1))

#cursor.execute("SELECT * FROM xaridor WHERE ism LIKE 't%' OR ism LIKE'S%'")
#cursor.execute("SELECT * FROM xaridor WHERE(ism LIKE 't%' OR ism LIKE'S%') AND qarz >300000")
cursor.execute("SELECT * FROM xaridor WHERE ism LIKE '_a_d%'")
cursor.execute("SELECT * FROM xaridor WHERE ism LIKE '%rk%' ")

print(cursor.fetchall())
conection.commit()
conection.close()


#NUll - NULL (bo'sh) qiymat
#INEGER - butun son
#REAL - haqiqiy sonlar
#TEXT - matinlar
#BLOB - katta malumotlar