import os


class Phonebook:

    def __init__(self):
        self.contacts = {}
        self.filename = "phonebook.txt"
        self.file_cache = open(self.filename, "w")
        self.consistent = True

    def add(self, name, number):
        self.contacts[name] = number

    def lookup(self, name):
        assert name is not None, "name parameter is required!"
        return self.contacts[name]

    def names(self):
        return set(self.contacts.keys())

    def is_consistent(self):
        return self.consistent

    def clear(self):
        self.contacts = {}
        self.file_cache.close()
        os.remove(self.filename)
