from pymongo import MongoClient


mongoClient = MongoClient('localhost',27017)

db = mongoClient.taller5

collection = db.libros

linea = 0
for line in open("historico.txt",encoding="UTF-8"):

    if linea !=0:
        #print(line)
        line = line.replace("\n","")
        titulo,autores,isbn,calificacionprom= line.split("|")[0:4]
        #print(inc_numb,offence_code,off_group,descript,distric,report,shott,occurred,year)
        item1={"titulo":titulo,"autores":autores,"isbn":isbn,"calificacionprom":calificacionprom}
        #print(item1)
        rec_id1 = collection.insert_one(item1)




    linea += 1

cursor = collection.find()

for record in cursor:
    print(record)








