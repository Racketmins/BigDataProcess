def counter(filename, m):
	try:
		f = open(filename)
		for line in f:
			info = line.strip().split("::")
			if info[2].find('|') == -1:
				if info[2] not in m:
					m[info[2]] = 1
				else:
					m[info[2]] += 1
			else:
				genre = info[2].strip().split('|')
				for i in genre:
					if i not in m:
						m[i] = 1
					else:
						m[i] += 1
		return m
	except FileNotFoundError:
		print("Not file from counter")
	finally:
		f.close()

def saveList(filename, m):
	try:
		f = open(filename, "wt")
		keyList = m.keys()
		for i in keyList:
			f.write("%s %d" % (i, m[i]))
	except FileNotFoundError:
		print("Not file from save")
	finally:
		f.close()

movies = dict()
inputFile  = input()
outputFile = input()
movies = counter(inputFile, movies)
saveList(outputFile, movies)
