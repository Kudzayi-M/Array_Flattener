def makeFlat(ugArr):
    while True:
        for i in range(len(ugArr)):
            if type(ugArr[i]) == list:
                sepList = ugArr[i]
                ugArr.pop(i)
                w = i
                for j in range(len(sepList)):
                    ugArr.insert(w, sepList[j])
                    w += 1          
        pts = 0
        for i in range(len(ugArr)):
            if type(ugArr[i]) != list:
                pts += 1
        if pts == len(ugArr):
            break
    return ugArr