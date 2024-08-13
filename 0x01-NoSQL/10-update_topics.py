#!/usr/bin/env python3
""" Update mongo document """


def update_topics(mongo_collection, name, topics):
    """ method to update mongo doc """
    update_doc = mongo_collection.update_many({"name" : name}, 
            {'$set': {"topics": topics}});
    return update_doc
