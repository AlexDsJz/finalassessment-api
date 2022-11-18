def get_minimum_value(l, i , j):
    if(i != len(l)):
        minimum_sum = l[i][j] + (min(get_minimum_value(l,i+1,j), 
                                            get_minimum_value(l,i+1,j+1),
                                            get_minimum_value(l,i+1,j+2)))
        return minimum_sum 
    else:
        return 0