#!/user/bin/python3
from openpyxl import load_workbook

def calTotal(fn):
	try:
		wb = load_workbook(filename = fn)
		ws = wb.active
		for row in range(2, 76):
			mid = ws.cell(row = row, column = 3).value * 0.3
			fin = ws.cell(row = row, column = 4).value * 0.35
			hw = ws.cell(row = row, column = 5).value * 0.34
			att = ws.cell(row = row, column = 6).value
			total = mid + fin + hw + att
			ws.cell(row = row, column = 7, value = total)
		wb.save(filename = fn)
	except FileNotFoundError:
		print("We can't find that file")
	finally:
		wb.close()

def rank(fn):
	try:
		wb = load_workbook(filename = fn)
		ws = wb.active
		score = [ws.cell(row = row, column = 7).value for row in range(2, 76)]
		score.sort()
		score.reverse()
					
		A = int(74 * 0.3) - 1
		Ap = int((A + 1) * 0.5) -1
		B = int(74 * 0.7) - 1
		Bp = int((B - A) * 0.5) + A
		F = 0
		for i in range(2, 76):
			if ws.cell(row = i, column = 7).value < 40:
				ws.cell(row = i, column = 8, value = 'F')
				F -= 1
		Cp = int((73 + F - B) * 0.5) + B

		for i in range(2, 76):
			flag = ws.cell(row = i, column = 7).value
			if ws.cell(row = i, column = 7).value >= 40:
				if flag >= score[Ap]:
					ws.cell(row = i, column = 8, value = 'A+')
				elif flag >= score[A]:
					ws.cell(row = i, column = 8, value = 'A')
				elif flag >= score[Bp]:
					ws.cell(row = i, column = 8, value = 'B+')
				elif flag >= score[B]:
					ws.cell(row = i, column = 8, value = 'B')
				elif flag >= score[Cp]:
					ws.cell(row = i, column = 8, value = 'C+')
				else:
					ws.cell(row = i, column = 8, value = 'C')
		wb.save(filename = fn)
	except FileNotFoundError:
		print("Not File")
	finally:
		wb.close()


fileName = "student.xlsx"
calTotal(fileName)
rank(fileName)
