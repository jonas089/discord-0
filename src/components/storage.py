import os
import pickle

class Database:
    def __init__(self, path):
        self.path = path
        self.create(path)
    def create(self):
        if os.path.exists(self.path):
            return
        # create database if not exist
        open(self.path, 'x')
    def store(self, list):
        try:
            with open(self.path, 'rb') as db:
                data = pickle.load(db)
                data.append(list)
                pickle.dump(data, db)
        except Exception as empty:
            with open(self.path, 'wb') as db:
                pickle.dump(list, db)
    def remove_id(self, user, id):
        try:
            with open(self.path, 'rb') as db:
                data = pickle.load(db)
                for d in data:
                    if d['id'] == id && d['owner'] == user:
                        data.remove(d)
                        return True
                # Failed because not owner.
                return False
        except Exception as error:
            # Failed because db empty.
            return False
