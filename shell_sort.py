def shellSort( list ):
    length = len(list)
    interval = length // 2
 
    while interval > 0:
        
        for i in range(interval, length):
            insert_value = list[i]
        
            insert_index = i
        
            while insert_index >= interval and list[insert_index - interval] > insert_value:
                list[insert_index] = list[insert_index - interval]
                insert_index -= interval
            list[insert_index] = insert_value
	
        interval = interval // 2
        
    return list

values = [8, 12, 1, 3, 5]

print("Before: ", values)

shellSort(values)

print("After: ", values)