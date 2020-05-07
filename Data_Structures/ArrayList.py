# An array that resizes itself as needed while still providing O(1) access.
# A typical implementation is that when the array is full, the array doubles in size.
# Each doubling takes O(n) time, but happens so rarely that it's amortized unsertion time is still O(1)

RESIZING_FACTOR = 2

class ArrayList:
    elements = []
    size = 1
    def __init__(self, initial_size = 1):
        self.size = initial_size
        
    def append(self, element):
        if len(self.elements) >= self.size:
            self.increase_in_size()
        self.elements += [element]

    def increase_in_size(self):
        print(f"Increasing in size from {self.size} to {RESIZING_FACTOR * self.size}")
        new_elements = [x for x in self.elements] # simulate copy
        self.size *= RESIZING_FACTOR
        self.elements = new_elements


def main():
    x = ArrayList()
    x.append(1)
    x.append(2)
    x.append(3)
    x.append(4)
    return x


if __name__ == '__main__':
    x = main()
