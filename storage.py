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
