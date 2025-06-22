class ArrayList:
    def __init__(self, initial_capacity=10):
        self.arrayList = [None] * initial_capacity
        self.curIndex = -1 # derive number of elements from index
        self.loadFactor = 0.75
        pass

    def add(self, element):
        if ((self.curIndex + 1) / len(self.arrayList)) >= self.loadFactor:
            self._resize()
        self.curIndex += 1
        self.arrayList[self.curIndex] = element
        pass


    def insert(self, index, element):
        if (index != 0 and index > self.curIndex) or index < 0:
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
        if index > self.curIndex or index < 0:
            return -1
        return self.arrayList[index]
        pass

    def remove(self, index):
        if index < 0 or index > self.curIndex:
            return -1
        else:
            if self.arrayList[index + 1] != None:
                for i in range(index, self.curIndex + 1):
                    self.arrayList[i] = self.arrayList[i + 1]
        self.curIndex -= 1
        pass

    def size(self):
        return self.curIndex + 1
        pass

    def is_empty(self):
        return self.curIndex == -1
        pass

    def _resize(self):
        temp, prevSize = self.arrayList, len(self.arrayList)
        self.arrayList = [None] * (prevSize * 2)
        for i in range(prevSize):
            self.arrayList[i] = temp[i]
        pass

    def print(self):
        print(self.arrayList)

