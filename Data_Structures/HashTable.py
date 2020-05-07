# Maps keys to values for highly-efficient lookup.

from LinkedList import LinkedList


class HashMap:
    def __init__(self, number_of_partitions = 2):
        self.partitions = [LinkedList()] * number_of_partitions

    def insert(self, key, value):
        hashkey = self._compute_hash_code(key)
        index = self._compute_index(hashkey)
        self.partitions[index].Insert(value)

    def retrieve(self, key):
        hashkey = self._compute_hash_code(key)
        index = self._compute_index(hashkey)
        return self.partitions[index].Search(key)

    def _compute_hash_code(self, key):
        return key.__hash__()

    def _compute_index(self, keyhash):
        return keyhash % len(self.partitions)

def main():
    x = HashMap(9)
    x.insert("somekey", "some value")
    x.insert("anotherkey", "a different value")
    return x

if __name__ == '__main__':
    x = main()
