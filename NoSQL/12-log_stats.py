#!/usr/bin/env python3
"""Test script for MongoDB connection and basic operations."""

from pymongo import MongoClient

if __name__ == "__main__":
    """Simple test script to connect to MongoDB, insert a document, and retrieve it."""
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_database"]
    collection = db["test_collection"]

    # Insert a sample document
    sample_document = {"name": "Alice", "age": 30, "city": "New York"}
    insert_result = collection.insert_one(sample_document)
    print(f"Inserted document ID: {insert_result.inserted_id}")

    # Retrieve and print the document
    retrieved_document = collection.find_one({"name": "Alice"})
    print("Retrieved document:", retrieved_document)

    # Clean up by dropping the test database
    client.drop_database("test_database")
    print("Test database dropped.")
