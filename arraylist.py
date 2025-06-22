class ArrayList:
    def __init__(self, initial_capacity=10):
        """
        Initialize the ArrayList with an initial capacity.
        """
        self.arrayList = [None] * initial_capacity
        self.curIndex = -1 # derive number of elements from index
        self.loadFactor = 0.75
        pass

    def add(self, element):
        """
        Add an element to the end of the ArrayList.
        """
        if ((self.curIndex + 1) / len(self.arrayList)) >= self.loadFactor:
            self._resize()
        self.curIndex += 1
        self.arrayList[self.curIndex] = element
        pass


    def insert(self, index, element):
        """
        Insert an element at the specified index.
        input: specific index and value
        output: modififed array
        cases: 
            - index > curIndex: return -1
            - index < 0: return -1
            - normal: add and shift right
        ex: [1, 2, 3, 4, 5] insert 7 @ index 2
            1. shift everthing after index 2 to the right
                - [1, 2, _, 3, 4, 5]
                temp = None
                i from index to curIndex
                    i = temp
                [1, 2, 3, 4, 5]

                prev = None
                temp = 3

                [i] = prev
                prev = temp
                temp = [i + 1]

                iter 1
                [1, 2, None, 4, 5]
                prev = 3
                temp = 4

                iter 2
                [1, 2, None, 3, 5]
                prev = 4
                temp = 5

                iter 3
                [1, 2, None, 3, 4]
                prev = 5
                temp = None

                iter 4
                [1, 2, None, 3, 4, 5]
                prev = None
                temp = None

            2. insert element at index (index)
            - expected: [1, 2, 7, 3, 4, 5]

            input: [1, 2, 3]
            output: [1, 2, 2, 3]

            prev = 3
            temp = None
        """
        if index > self.curIndex or index < 0:
            return -1
        if ((self.curIndex + 1) / len(self.arrayList)) >= self.loadFactor:
            self._resize()
        prev = element
        temp = self.arrayList[index]
        for i in range(index, self.curIndex + 2):
            self.arrayList[i] = prev
            prev = temp
            temp = self.arrayList[i + 1]
        self.curIndex += 1
        pass

    def get(self, index):
        """
        Retrieve the element at the specified index
        """
        if index > self.curIndex or index < 0:
            return -1
        return self.arrayList[index]
        pass

    def remove(self, index):
        """
        Remove the element at the specified index.
        input: index
        output: modified array
        Edge: index < 0 or index > curIndex (empty handled)
            -> return -1
        Normal: 
            - remove element by setting to None
            - if elements to right (!= None)
                * shift left
            - Never at end because of loadFactor
        [1, 2, 3, 4, 5]
        [1, 2, 4, 4, 5]
        [1, 2, 4, 5, 5]
        [1, 2, 3, 4, None]
        """
        if index < 0 or index > self.curIndex:
            return -1
        else:
            if self.arrayList[index + 1] != None:
                for i in range(index, self.curIndex + 1):
                    self.arrayList[i] = self.arrayList[i + 1]
        self.curIndex -= 1
        pass

    def size(self):
        """
        Return the current number of elements in the ArrayList.
        """
        return self.curIndex + 1
        pass

    def is_empty(self):
        """
        Check if the ArrayList is empty.
        """
        return self.curIndex == -1
        pass

    def _resize(self):
        """
        Resize the internal array when capacity is reached.
        """
        temp, prevSize = self.arrayList, len(self.arrayList)
        self.arrayList = [None] * (prevSize * 2)
        for i in range(prevSize):
            self.arrayList[i] = temp[i]
        pass

    def print(self):
        """
        For debugging
        """
        print(self.arrayList)

# Example Usage (for testing)
arr_list = ArrayList()
arr_list.add(5)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.add(6)
arr_list.insert(0, 11)
arr_list.insert(5, 12)
print(arr_list.size())
arr_list.remove(5)
arr_list.print()
