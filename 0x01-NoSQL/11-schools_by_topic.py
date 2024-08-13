#!/usr/bin/env python3
""" select data given condition """


def schools_by_topic(mongo_collection, topic):
    """ fetch data from collection """
    n_list = [doc for doc in mongo_collection.find({"topics": topic})]
    return ni_list
