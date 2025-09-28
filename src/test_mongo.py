from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['highschool']
activities = db['activities']

# Print all activities
print("Activities in the database:")
for doc in activities.find():
    print(doc)