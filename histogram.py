def largest_histogram(histogram):
    
    result = len(histogram) #default lowest area
    col = 0
    width = 0 #initialise variables
    while col < len(histogram):
        for height in range(histogram[col], 2, -1): #check greatest number of sucessive rows with -1 height, store area (iterate until height 2)
            x = col #set counter for following while loop to current index
            while height <= histogram[x]: #increments width by 1 for each successive column with minimum height i
                width += 1
                if x < len(histogram)-1:
                    x += 1
                else:
                    break
            if result < width*height: 
                result = width*height
        col += 1        
  
    return result

print(largest_histogram([5,3]))