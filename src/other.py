from constants import id as id_path
import sys
sys.path.append('./components')
from storage import ID

def next():
    id = ID(id_path, 0)
    try:
        id.read()
    except Exception as empty:
        id.write()
    return id.current
def incr():
    id = ID(id_path, 0)
    id.read()
    id.incr()
    id.store()
def _format(data):
    string = ''
    for d in data:
        appendix = '**ID**: '+ str(d['id']) + '\n' + 'host: ' + d['owner'] + '\n' + 'game: ' + '**' + d['game'] + '**' + '\n' + 'date: ' + '**' + d['date'] + '**' + '\n' + 'time: ' + '**' + d['time'] + '**' + '\n' + 'participants: ' + '**' + str(len(d['participants'])) + '**' + '\n' + '**' + ':small_blue_diamond:'*10 + '**' + '\n'
        string += appendix
    return string
