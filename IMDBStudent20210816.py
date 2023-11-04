def counter(filename, m):
	try:
		f = open(filename)
		for line in f:
			info = line.strip().split("::")
			genre = info[2].split('|')
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
			f.write(str(i) + " "  + str(m[i]) + "\n")
	except FileNotFoundError:
		print("Not file from save")
	finally:
		f.close()

movies = dict()
inputFile  = "movie.dat"
outputFile = "movieoutput.txt"
movies = counter(inputFile, movies)
saveList(outputFile, movies)
