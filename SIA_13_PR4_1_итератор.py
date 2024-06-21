class MyIterator:
    def __init__(self, maxNum):
        self.maxNum = maxNum
        self.current = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.maxNum<0:
            if self.current > self.maxNum:
                self.current -= 1
                return self.current
            else:
                raise StopIteration
        else:
            if self.current < self.maxNum:
                self.current += 1
                return self.current
            else:
                raise StopIteration

iterator = MyIterator(7)
for num in iterator:
    print(num)