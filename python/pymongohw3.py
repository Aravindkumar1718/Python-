from pymongo import MongoClient
client= MongoClient("mongodb://localhost:27017")
DB = client.TYPES
col = DB.Items
data={"Type":"Ice-Cream","Flavor":["Vanilla","Black current","Cocololate","Butterscotch","Pista","Kulfi"]}
col.insert_one(data)
