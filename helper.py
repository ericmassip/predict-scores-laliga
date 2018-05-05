import pickle

def save(data, dataFilename):
    pickle.dump(data, open(dataFilename, 'wb'))

def load(dataFilename):
    return pickle.load(open(dataFilename, mode='rb'))

def invert_dict(dic):
    return dict([ (value, key) for key, value in dic.items() ])
