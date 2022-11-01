from timelib import timestamp
from storage import Database
class Event:
    def __init__(self, id, owner, game, date, time):
        self.id = id
        self.owner = owner
        self.game = game
        self.date = date
        self.time = time
        self._timestamp = timestamp(date, time)
    def _dict(self):
        # invalid event if timestamp == None
        if self._timestamp == None:
            return None
        # return relevant event info
        return {
            'id':self.id,
            'owner':self.owner,
            'game':self.game,
            'date':self.date,
            'time':self.time
        }
    def _save(self):
