#!/usr/bin/env python3
""" insert into collection using args"""


def insert_school(mongo_collection, **kwargs):
    """ insert into collection """
    new_col = mongo_collection.insert_one(kwargs)
    return new_col.inserted_id
