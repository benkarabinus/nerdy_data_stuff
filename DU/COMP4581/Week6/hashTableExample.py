# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table

class MyHashtable(object):

    def __init__(self, size):

        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append([])
    
    def __str__(self):
        return str(self.table)
    
    def insert(self, elem): # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].append(elem)
    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]
    def delete(self, elem): # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].remove(elem)


def main():

    s = MyHashtable(10)
    s.insert("amy") #97
    s.insert("chase") #99
    s.insert("chris") #99
    print(s.member("amy"))
    print(s.member("chris"))
    print(s.member("alyssa"))
    s.delete("chase")
    print(s.member("chris"))
    #You can use print(s) at any time to see the contents
    # of the table for debugging
    # print(s)


if __name__ == '__main__':
    main()