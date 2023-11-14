from motor.motor_asyncio import AsyncIOMotorClient

# MONGO_DETAILS = "mongodb://mongodb:27017"
MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["My_database"]
forms_collection = database["forms_collection"]
# database = client.your_database_name
# forms_collection = database.get_collection("forms_collection")


async def connect_to_mongo():
    print("Connected to MongoDB")


async def close_mongo_connection():
    client.close()
    print("Disconnected from MongoDB")
