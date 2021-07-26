# problem overview: https://www.hackerrank.com/challenges/crush/problem
# For this problem, I took the inspiration from youtube channel 'JAVAAID - Coding Interview Preparation'
# and implemented the algorithm in python
# the general idea of the algorithm is using +=value and -=value at starting and ending position to keep track of the changes made by each query

def arrayManipulation(n, queries):


    #Initiating the referece array with the size n+1 and returning value max_val
    ref_a = [0]*(n+1) # 1 extra element added to the array to increase performance
    max_val = 0
 
    for curr in queries:
        #initiating 3 variables to catch the starting point(st_pt), ending point(ed_pt), value(val) from the queries
        st_pt = curr[0] - 1
        ed_pt = curr[1]
        val = curr[2]
        ref_a[st_pt] += val
        ref_a[ed_pt] -= val
        
        #debugging code
        # print(ref_a)
    diff = 0
    for item_ref in ref_a:
        diff += item_ref
        item_ref = diff
        if item_ref > max_val:
            max_val = item_ref

    # debugging code
    # print(result)
    # print(ref_a)
    return max_val