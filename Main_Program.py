import datetime
import TT_2
x = str(datetime.datetime.now().time())
w = datetime.datetime.now().weekday()

# Dictionary
Day = {
    0 : {
        "07:50" : "CS",
        "09:10" : "Physics",
        "10:30" : "Break",
        "11:45" : "Free",
        "12:25" : "Maths",
        "13:45" : "School",
        0 : "End"
    },
    1 : {
        "07:50" : "Physics",
        "09:10" : "Free",
        "10:30" : "Break",
        "11:45" : "CS",
        "12:25" : "Maths",
        "13:45" : "School",
        0 : "End"
    },
    2 : {
        "07:50" : "Physics",
        "09:10" : "Free",
        "10:30" : "Break",
        "11:45" : "Maths",
        "12:25" : "CS",
        "13:45" : "School",
        0 : "End"
    },
    3 : {
        "07:50" : "CS",
        "09:10" : "Maths",
        "10:30" : "Break",
        "11:45" : "Free",
        "12:25" : "Physics",
        "13:45" : "School",
        0 : "End"
    },
    4 : {
        "07:50" : "Physics",
        "09:10" : "Free",
        "10:30" : "Break",
        "11:45" : "Maths",
        "12:25" : "CS",
        "13:45" : "School",
        0 : "End"
    },
    5 : "Weekend",
    6 : "Weekend"
}
# End of Dictionary

# Day dict
Nday = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday",
}

print("Time:",x,"Day:",Nday[w])
# End of day dict
i = 0
l = []
while (i < 5):
    l.append(x[i])
    i = i + 1
# Main Timetable Function
def Get(w, l):
    l = l[0] + l[1] + l[2] + l[3] + l[4]
    if w == 0:
        l = TT_2.Convert(l)
        if l in Day[w]:
            print(Day[w][l])
            print(Nday[w])
    elif w == 1:
        l = TT_2.Convert(l)
        if l in Day[w]:
            print(Day[w][l])
            print(Nday[w])
    elif w == 2:
        l = TT_2.Convert(l)
        if l in Day[w]:
            print(Day[w][l])
            print(Nday[w])
    elif w == 3:
        l = TT_2.Convert(l)
        if l in Day[w]:
            print(Day[w][l])
            print(Nday[w])
    elif w == 4:
        l = TT_2.Convert(l)
        if l in Day[w]:
            print(Day[w][l])
            print(Nday[w])
    elif w == 5:
        print("Weekend", Nday[w])
    elif w == 6:
        print("Church/Weekend", Nday[w])
# End
Get(w,l)
