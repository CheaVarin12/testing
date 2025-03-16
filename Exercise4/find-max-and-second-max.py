def find_max_and_second_max(arr):
    if len(arr) < 2:
        print("List must have at least two distinct numbers.")
        return
    
    max_num = second_max = float('-inf')  

    for num in arr:
        if num > max_num:
            second_max = max_num  
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num  

    if second_max == float('-inf'):
        print("No second maximum found")
    else:
        print("Maximum number:", max_num)
        print("Second maximum number:", second_max)

find_max_and_second_max([5, 1, 8, 3, 8, 2])
