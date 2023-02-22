def solution(common):
    #등차수열이면
    if (common[1]-common[0])==(common[2]-common[1]):
        return common[-1]+common[2]-common[1]
    #등비수열이면
    elif (common[0]/common[1])==(common[1]/common[2]):
        return common[-1]*(common[2]-common[1])