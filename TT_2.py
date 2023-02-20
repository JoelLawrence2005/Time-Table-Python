def Convert(l):
    if int(l[0]) == 0:
        if int(l[1]) <= 7:
            l = "07:50"
            return(l)
        elif int(l[1]) in range(7,10):
            l = "09:10"
            return(1)
    if int(l[0]) == 1:   #1
        if int(l[1]) == 0: #1 or 0 - 0
            if int(l[4]) <= 5: # 3
                l = "10:30"
                return(l)
        elif int(l[1]) == 1:
            if int(l[3]) <= 5:
                l = "11:45"
                return(l)
        elif int(l[1]) == 2:
            if int(l[3]) <= 3:
                l = "12:25"
                return(l)
            else:
                if l[4] <= 5:
                    l = "13:05"
                    return(l)
        elif int(l[1]) == 3:
            if int(l[3]) >= 3:
                if int(l[4]) <= 9:
                    l = "13:45"
                    return(l)
        else:
            return(0)