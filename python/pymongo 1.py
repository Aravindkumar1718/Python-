from pymongo import MongoClient
client = MongoClient ("mongodb://localhost:27017/")
db = client.MONGO
col = db.User
name = input("Enter your name : ")
col.insert_one({ "name": [name,name]})
col.insert_many ([{},{},{}])
{
question:"what is your name?"
options:["option1","option2","option3"]
answer:"option1"
}

