def top_n_frequent(elements,n):
    frequency={}
    for element in elements:
        frequency[element]=frequency.get(element,0)+1
    sorted_elements=sorted(frequency, key=frequency.get,reverse=True)
    return sorted_elements[:n]
elements=[1,2,3,2,4,5,1,1,2]
n=int(input("Enter N:"))
print(top_n_frequent(elements,n))