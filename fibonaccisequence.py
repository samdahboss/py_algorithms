def sumFibs(numOfFibs):
    prevNum=0
    currentNum=1
    sum=0
    fibArr=[]
    while(len(fibArr)<numOfFibs):
        fibArr.append(currentNum)
        prevNum+=currentNum
        fibArr.append(prevNum)
        currentNum=prevNum+currentNum
    return(fibArr)

print(sumFibs(10))
    