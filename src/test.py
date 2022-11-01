import sys
import pickle
import argparse
sys.path.append('./components')
from constants import db as path
from constants import id as id_path
from event import Event
from storage import Database, ID

def _test_event():
    _event = Event(0, 'jonas', 'GTA', '01.01.2000', '16:30')
    return _event

def _test_write_single():
    db = Database(path)
    _event = _test_event().export()
    db.store(_event)

def _test_read_db():
    try:
        with open(path, 'rb') as db:
            return pickle.load(db)
    except Exception as error:
        return error

def _test_kill_db():
    try:
        db = Database(path)
        db.kill()
    except Exception as error:
        return error

def _test_edit():
    id = 0
    db = Database(path)
    _event = _test_read_db()[0]
    _Event = Event(_event['id'], _event['owner'], _event['game'], _event['date'], _event['time'])
    _Event.edit_game('LOL')

    db.remove_id(id=_event['id'], user='jonas')
    db.store(_Event.export())

parser = argparse.ArgumentParser(
    prog = 'Jonas Discord Bot',
    description = 'Test discord bot functions and structs.',
    epilog = ''
)

def _test_id():
    id = ID(id_path, 0)
    id.incr()
    id.incr()
    id.incr()
    id.store()
    if int(id.read()) == 3:
        print("[info]: ID is ok.")
    else:
        print("[error]: ID incorrect.")
parser.add_argument('--action')
args = parser.parse_args()
if args.action == 'write':
    _test_write_single()
elif args.action == 'read':
    print(_test_read_db())
elif args.action == 'kill':
    _test_kill_db()
elif args.action == 'edit':
    _test_edit()
elif args.action == 'id':
    _test_id()
