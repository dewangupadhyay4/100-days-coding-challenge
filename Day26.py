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

#-----------------------------------------------------------------------------

def even_number():
    for i in range(1,11):
        if i % 2 == 0:
            yield i

for num in even_number():
    print(num)