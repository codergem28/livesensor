from dataclasses import dataclass
import os
import pymongo

@dataclass  ##decorator to store data

class Environmentvariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URl")


env_var = Environmentvariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)