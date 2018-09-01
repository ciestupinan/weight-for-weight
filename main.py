def order_weight(s):

    lst = s.split()
    tupe_lst = []    # should be [(actual, weight)]
    
    # create weights for each number in the list
    for i in range(len(lst)):
        item = lst[i]
        weight = 0
        
        for j in range(len(item)):    # go through all characters in each item
            weight = weight + int(item[j])
        
        tupe_lst.append((int(item), weight))
    
    
    # sort list by weight
    sorted_lst = modifiedBubbleSort(tupe_lst)
    
    sorted_str = ''
    for item in sorted_lst:
        sorted_str = sorted_str + str(item[0]) + ' '
    
    return sorted_str[:-1]
        
        

def modifiedBubbleSort(l):
    
    sorted = False
    
    while not sorted:
        sorted = True
        
        for i in range(len(l)-1):
            if l[i][1] > l[i+1][1]:    # if weight0 > weight1, swap
                sorted = False
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
            
            if l[i][1] == l[i+1][1]:        # if weights are the same, compare the first digit
                strActual1 = str(l[i][0])
                strActual2 = str(l[i+1][0])
                
                if int(strActual1[0]) > int(strActual2[0]):    # if digit0 > digit1, swap
                    sorted = False
                    temp = l[i]
                    l[i] = l[i+1]
                    l[i+1] = temp
    return l
            
        
        
        
