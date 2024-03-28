import pymongo

py_url = "mongodb://localhost:27017"
client = pymongo.MongoClient(py_url)



database_name = "questions"
collection_name = "newfile"
db = client[database_name]
collection = db[collection_name]


questions_list = []

for _ in range(2):
    q = input("Enter the question: ")
    op1 = input("Option 1: ")
    op2 = input("Option 2: ")
    op3 = input("Option 3: ")
    options = [op1, op2, op3]
    ansInput = int(input("Enter the option number for the answer (1, 2, or 3): "))
    answer = options[ansInput - 1]

    
    question_data = {
        "question": q,
        "answer": answer,
        "options": options
    }

    
    questions_list.append(question_data)

collection.insert_many(questions_list)


client.close()

print("Questions have been successfully added to the database.")
