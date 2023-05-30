def binary_search(list,req):
    start = 0
    end = len(list)
    middle = 0
    required = req
    steps = 0
    while(start<=end+1):
        print("Step",steps,list[start:end+1])
        middle = (start+end)//2
        steps+=1
        print(list[middle])
        if list[middle]==req:
            print("found it")
            break
        elif list[middle]<req:
            start = middle+1
        elif list[middle]>req:
            end = middle-1
list1 = [1,2,3,4,5,6,7,8]
binary_search(list1,8)
        



