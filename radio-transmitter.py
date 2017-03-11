#Note: This is not completed yet

from collections import Counter

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

xs=sorted(x)
x_map=Counter(x)

base_range=(k*2)
pos=-1
max_range=-1
mid_range=-1
trans=0

for c in xs:
    #print("Location:",c)
    if pos>=c:
        continue
    #print("New Tranmitter")
    mid_range=c+k
    pos=c
    
    #Check if Middle range is possible
    if mid_range in x_map:
        #print('Mid-range Found, moving to', mid_range)
        pos=mid_range
        
    else:
        #print('No max Mid-range found',mid_range)
        while mid_range not in x_map:
            mid_range-=1
            #print('trying', mid_range)
        
        pos=mid_range
        
    if pos==c:
        #print('No mid-range, staying at', pos)
        trans+=1
        continue
    
    #Check is max Range is possible
    max_range=pos+k

    if max_range in x_map:
        #print('Max-range Found, moving to', max_range)
        pos=max_range
    else:
        #print('No max max-range found', max_range)
        while max_range not in x_map:
            max_range-=1
            #print('trying', max_range)
            
        pos=max_range
    
    
    trans+=1

print(trans)