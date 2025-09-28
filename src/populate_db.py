from pymongo import MongoClient

# Initial activities data
initial_activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball with fellow students",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["noah@mergington.edu", "isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ethan@mergington.edu", "charlotte@mergington.edu"]
    },
    "Mathletes": {
        "description": "Compete in math competitions and solve challenging problems",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["alex@mergington.edu", "zoe@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific topics",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["ben@mergington.edu", "lily@mergington.edu"]
    }
}

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['highschool']
activities_collection = db['activities']

# Clear existing data
activities_collection.delete_many({})

# Insert initial data
for name, details in initial_activities.items():
    activities_collection.insert_one({"_id": name, **details})

print("Database populated with initial activities:")
for doc in activities_collection.find():
    print(f"\n{doc['_id']}:")
    print(f"  Description: {doc['description']}")
    print(f"  Participants: {len(doc['participants'])}")