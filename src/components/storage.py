import os
import pickle
from event import Event
class ID:
    def __init__(self, path, start):
        self.current = start
        self.path = path
        self.create()
    def create(self):
        if os.path.exists(self.path):
            return
        # create database if not exist
        open(self.path, 'a').close()
    def update(self, id):
        self.current = id
    def incr(self):
        self.current = self.current + 1
    def store(self):
        with open(self.path, 'w') as file:
            file.write(str(self.current))
    def read(self):
        with open(self.path, 'r') as file:
            self.current = int(file.read())
            return self.current
class Database:
    def __init__(self, path):
        self.path = path
        self.create()
    def create(self):
        if os.path.exists(self.path):
            return
        # create database if not exist
        open(self.path, 'a').close()
    def store(self, object):
        try:
            with open(self.path, 'rb') as db:
                data = pickle.load(db)
            with open(self.path, 'wb') as db:
                data.append(object)
                pickle.dump(data, db)
        except Exception as empty:
            with open(self.path, 'wb') as db:
                pickle.dump([object], db)
    def read(self):
        try:
            with open(self.path, 'rb') as db:
                data = pickle.load(db)
                return data
        except Exception as empty:
            return None
    def remove_id(self, user, id):
        try:
            with open(self.path, 'rb') as db:
                data = pickle.load(db)
                for d in data:
                    if (str(d['id']) == str(id)) and (d['owner'] == user):
                        data.remove(d)
                        break
                    return False
                # Failed because not owner.
            with open(self.path, 'wb') as db:
                pickle.dump(data, db)
                return True
        except Exception as error:
            # Failed because db empty.
            return False
    def override(self, _event):
        data = self.read()
        for i in range(0, len(data)):
            if str(data[i]['id']) == str(_event['id']):
                data[i] = _event
        with open(self.path, 'wb')as db:
            pickle.dump(data, db)
        return True
    def kill(self):
        try:
            os.remove(self.path)
            return True
        except Exception as error:
            return False
    def size(self):
        return len(self.read())
