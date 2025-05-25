class MyIterator:

    def __iter__(self):
        self.num=1
        return self
    
    def __next__(self):
        if self.num<=5:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
        
number=MyIterator()
for i in number:
    print(i)