from timelib import timestamp
class Event:
    def __init__(self, id, owner, game, date, time, participants):
        self.id = id
        self.owner = owner
        self.game = game
        self.date = date
        self.time = time
        self.participants = participants
        self._timestamp = timestamp(date, time)
    def export(self):
        # invalid event if timestamp == None
        if self._timestamp == None:
            return None
        # return relevant event info
        return {
            'id':self.id,
            'owner':self.owner,
            'game':self.game,
            'date':self.date,
            'time':self.time,
            'participants':self.participants
        }
    def join(self, user):
        self.participants.append(user)
    def edit_game(self, game):
        self.game = game
    def edit_date(self, date):
        self.date = date
        self._timestamp = timestamp(date, self.time)
    def edit_time(self, time):
        self.time = time
        self._timestamp = timestamp(self.date, time)
