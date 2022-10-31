import pickle
def id():
    data = read()
    return len(data)

def read():
    data = []
    try:
        with open('data.xml', 'rb') as db:
            data = pickle.load(db)
    except Exception as fourOfour:
        pass
    return data

def write(data):
    try:
        with open('data.xml', 'wb') as db:
            pickle.dump(data, db)
        return True
    except Exception as error:
        return False

def push(data, element):
    data.append(element)
    return data

def edit(id, override):
    try:
        data = read()
        data[id] = override
        write(data)
        return True
    except Exception as error:
        return False
def delete(id):
    data = read()
    try:
        data.remove(data[id])
        write(data)
        return True
    except Exception as fourOfour:
        return False

def signup(id, user):
    data = read()
    if user in data[id]['participating']:
        return False
    try:
        data[id]['participating'].append(user)
        write(data)
        return True
    except Exception as fourOfour:
        return False

def ownerof(id):
    try:
        data = read()
        return data[id]['creator']
    except Exception as error:
        return False
def clear():
    write([])
