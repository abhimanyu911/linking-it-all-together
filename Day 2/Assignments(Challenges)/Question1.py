def poisonousPlants(array =  None):
    #dummy value at zero position
    array.insert(0,None)
    delete_ele =[]
    c=0
    while True:
        for i in range(2,len(array)):
            if array[i]>array[i-1]:
                delete_ele.append(array[i])
        
        if len(delete_ele)==0:
            break

        for ele in delete_ele:
            array.remove(ele)
        
        c+=1
        delete_ele = []
        
    return c

if __name__ == '__main__':

    print("Enter input in specified format:")
    n = int(input())
    if n>=1 and n<=10**5:
        arr = list(map(int, input().split()))
        flag = True
        for item in arr:
            if not(item>=1 and item<=10**9):
                flag = False
                break
        if flag:
            val = poisonousPlants(array = arr)
            print(val)
        else:
            print("Array element(s) out of bounds, start over")
    else:
        print("Mo of plants out of bounds, start over")





