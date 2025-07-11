from math import sqrt

listing=[12,34,543,3,3,323,232,12,121,344]

def find_lar_small(listing):
    largest=max(listing)
    smallest=min(listing)
    return largest, smallest

print(find_lar_small(listing))

def reverse(listing):
    reversed=[]
    for i in range(len(listing)-1,-1,-1):
        reversed.append(listing[i])
    return reversed

print(list(reversed(listing)))

def count(listing):
    count={}
    for i in listing:
        if i in count:
            count[i]+=1
        else:
            count[i]=1

    return count

print(count(listing))

def isPrime(n):
    if n < 1:
        return False
    if n==2:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
def sum(listing):
    sum=0
    for i in range(len(listing)):
        if isPrime(listing[i]):
            sum=sum+listing[i]
    return sum
        
summ=sum(listing)
print(summ)
        
