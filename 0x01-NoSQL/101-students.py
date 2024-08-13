#!/usr/bin/env python3
""" Top STudents """


def top_students(mongo_collection):
    """ aggregate function """
    agg = mongo_collection.aggregate([{"$project": {
        "name": 1,
        "averageScore": {"$avg": "$scores" }}},
        { "$sort": {"averageScore": -1}}])
    return agg
