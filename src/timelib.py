import time

# get timestamp for Event
def timestamp(date, _time):
    datetime = '{} {}'.format(date, _time)
    try:
        _t = time.mktime(time.strptime(datetime, "%d.%m.%Y %H:%M"))
        if time.time() >= _t:
            return None
        return _t
    except Exception as invalid:
        print("[Error]: Timestamp invalid: ", invalid)
        return None

# check if Event has expired
def expired(timestamp):
    if time.time() >= timestamp:
        return True
    return False
