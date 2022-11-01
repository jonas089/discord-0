import time

# get timestamp for Event
def timestamp(date, time):
    datetime = '{} {}'.format(date, time)
    try:
        return time.mktime(time.strptime(datetime, "%d.%m.%Y %H:%M:%S"))
    except Exception as invalid:
        return None

# check if Event has expired
def expired(timestamp):
    if time.time() >= timestamp:
        return True
    return False
