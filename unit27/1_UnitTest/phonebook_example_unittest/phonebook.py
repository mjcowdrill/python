class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        if (not self.entries or len(self.get_numbers) <= 0):
            return True
        ln1 = len(self.get_numbers)
        s   = sorted(set(self.get_numbers))
        ln2 = len(s)
        if (ln1 != ln2):
            return False
        for i in range(ln2-1):
            ln3 = len(s[i])
            if (s[i] == s[i+1][:ln3]):
                return False
        return True



    @property
    def get_names(self):
        return self.entries.keys()

    @property
    def get_numbers(self):
        return self.entries.values()
