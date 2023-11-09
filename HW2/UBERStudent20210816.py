from datetime import datetime

def convertWeek(rfile, weekDay):
    try:
        rf = open(rfile)
        after = []
        for line in rf:
            info = line.strip().split(',')
            date = datetime.strptime(info[1], '%m/%d/%Y')
            weekday = date.strftime('%a')
            info[1] = weekDay[weekday]
            info_str = ",".join(info)
            after.append(info_str)
        after.sort()
    except FileNotFoundError:
        print("not file")
    finally:
        rf.close()
        return after

def saveFile(wfile, conv):
    try:
        wf = open(wfile, "wt")
        for i in conv:
            wf.write("%s\n" % i)
    except FileNotFoundError:
        print("we fail to save")
    finally:
        wf.close()

weekDay = {
    "Monday" : "MON",
    "Tuesday" : "TUE",
    "Wednesday" : "WED",
    "Thursday" : "THU",
    "Friday" : "FRI",
    "Saturday" : "SAT",
    "Sunday" : "SUN"
}

rfile = input()
wfile = input()
conv = convertWeek(rfile, weekDay)
saveFile(wfile, conv)