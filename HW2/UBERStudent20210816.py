import sys
import calendar

weekDay = ["MON","TUE", "WED","THU","FRI","SAT","SUN"]
rfile = sys.argv[1]
wfile = sys.argv[2]
result = dict()

with open(rfile) as rf:
	for line in rf:
		info = line.strip().split(',')
		weeks = info[1].split('/')
		weekf = list(map(int, weeks))
		info[1] = weekDay[calendar.weekday(weekf[2],weekf[0],weekf[1])]
		region = info[0] + ',' + info[1]
		nums = [int(info[2]) , int(info[3])]
		if region not in result:
			result[region] = nums
		else:
			result[region][0] += nums[0]
			result[region][1] += nums[1]

with open(wfile, "wt") as wf:
	keyls = result.keys()
	for i in keyls:
		wf.write("%s %d,%d\n" % (i, result[i][0], result[i][1]))
