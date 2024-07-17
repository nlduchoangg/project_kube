from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId


# MongoDB connection details
mongodb_uri = "mongodb://admin:password@localhost:27017"
database_name = "test"
collection_name = "user_db"

# Function to check MongoDB connection and insert sample data
def insert_sample_data():
    try:
        # Connect to MongoDB
        client = MongoClient(mongodb_uri)
        db = client[database_name]
        collection = db[collection_name]

        # Sample data to insert
        sample_data = [
            {"_id": str(ObjectId()), "name": "John Doe", "age": 30, "email": "john.doe@example.com"},
            {"_id": str(ObjectId()), "name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
            {"_id": str(ObjectId()), "name": "Michael Johnson", "age": 35, "email": "michael.johnson@example.com"}
        ]

        # Insert sample data into MongoDB
        result = collection.insert_many(sample_data)
        print(f"Inserted {len(result.inserted_ids)} documents")

        # Close MongoDB connection
        client.close()

        return True, "Data insertion successful"

    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
        return False, f"Failed to connect to MongoDB: {e}"

    except Exception as e:
        print(f"Error inserting data into MongoDB: {e}")
        return False, f"Error inserting data into MongoDB: {e}"

# Execute the function to insert sample data and handle results
success, message = insert_sample_data()
if success:
    print("Insertion successful")
else:
    print(f"Insertion failed: {message}")
