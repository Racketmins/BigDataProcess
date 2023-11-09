rfile = input()
wfile = input()
m = dict()

with open(rfile) as f:
    for line in f:
        info = line.strip.split('::')
        genre = info[2].split('|')
        for i in genre:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
    print(m)

with open(wfile, "wt") as wf:
    keyls = m.keys()
    for i in keyls:
        wf.write("%s %d\n" % (i, m[i]))