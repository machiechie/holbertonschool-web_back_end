#!/usr/bin/python3
"""Module that defines a function to list all documents in a MongoDB collection."""

def list_all(mongo_collection):
    """Returns a list of all documents in a collection."""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
