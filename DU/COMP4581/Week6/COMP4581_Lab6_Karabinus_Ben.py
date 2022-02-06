"""
Ben Karabinus
University of Denver
COMP 4581, Winter Quarter 2022
Lab 6
"""


class MyHashtable:

    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(self.size)]
        self.status = ["empty" for i in range(self.size)]

    def insert(self, elem):
        hash = ord(elem[0]) % self.size  # (ASCII#(firstLetter) mod hashTableSize) for idx
        while not self.status[hash] == "empty":
            hash = (hash+1) % self.size
        self.table[hash] = elem
        self.status[hash] = "filled"

    def member(self, elem):
        hash = ord(elem[0]) % self.size  # (ASCII#(firstLetter) mod hashTableSize) for idx
        while not self.status[hash] == "empty":
            if self.table[hash] == elem:
                return elem in self.table[hash]
            else:
                hash = (hash+1) % self.size
        return elem == self.table[hash]

    def delete(self, elem):
        hash = ord(elem[0]) % self.size  # (ASCII#(firstLetter) mod hashTableSize) for idx
        while not self.status[hash] == "empty":
            if self.table[hash] == elem:
                self.table[hash] = None
                self.status[hash] = "deleted"
                break
            else:
                hash = (hash+1) % self.size

    def __str__(self):
        return str(self.table)


def main():

    s = MyHashtable(10)
    s.insert("amy") #97
    #print(s)
    s.insert("chase") #99
    #print(s)
    s.insert("chris") #99
    #print(s)
    print(s.member("amy"))
    print(s.member("chris"))
    print(s.member("alyssa"))
    s.delete("chase")
    print(s.member("chris"))


if __name__ == '__main__':
    main()
