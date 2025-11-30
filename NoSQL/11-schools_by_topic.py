#!/usr/bin/env python3
"""Module for querying MongoDB for schools by topic."""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that offer a specific topic.

    Args:
        mongo_collection: The MongoDB collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents that offer the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
