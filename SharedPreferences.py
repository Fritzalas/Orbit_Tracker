import shelve

# Function to save a preference
def set_preference(key, value):
    with shelve.open('preferences.db') as prefs:
        prefs[key] = value

# Function to get a preference
def get_preference(key, default=None):
    with shelve.open('preferences.db') as prefs:
        return prefs.get(key, default)

# Function to remove a preference
def remove_preference(key):
    with shelve.open('preferences.db') as prefs:
        if key in prefs:
            del prefs[key]