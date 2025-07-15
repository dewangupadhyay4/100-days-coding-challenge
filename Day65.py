listing=[12,34,23,34,23,454,45,45,45,455,453,32,45,34]

def count_freq(lists):
    freq={}
    for i in lists:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

print("Frequencies: ", count_freq(listing))
