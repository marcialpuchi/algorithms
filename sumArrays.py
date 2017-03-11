# Write a method that implements an integer adder. 
# Given two arrays of integers where each position 
# in the array contains an 0>= integer <= 9. Return an
# array with the result of the addition of the two.

def sumInvertedArray(a1, a2):
    a1=a1[::-1]
    a2=a2[::-1]
    d=len(a1)-len(a2)

    g = a1 if d>0 else a2 if d<0 else None

    i=0
    carry=0
    finalSum=[]

    while i<len(a1) and i<len(a2):
        tmpSum=a1[i]+a2[i]+carry
        carry=0

        if tmpSum>9:
            carry=1
            tmpSum-=10

        finalSum.append(tmpSum)
        i+=1

    if g is not None:
        #One is larger
        finalSum.append(g[i]+carry)
        finalSum += g[i+1:]

    elif carry>0:
        #They are equal, but there is a carrier.
        finalSum.append(carry)
        
    return finalSum[::-1]

tests=[
    [[1, 0], [5]],
    [[2, 5], [2, 5]],
    [[9, 9], [9, 9]]
]

for t in tests:
    print sumInvertedArray(t[0],t[1])