import sys
import os
import numpy as np
import operator

def load_data(folderName):
	data = []
	labels = []
	for filename in os.listdir(folderName):
		label = int(filename.split('_')[0])
		with open(os.path.join(folderName, filename)) as f:
			content = f.read()
			data.append([int(i) for i in content if i != '\n'])
		labels.append(label)
	return np.array(data), np.array(labels)

def classify0(inX, group, labels, k):
	m = group.shape[0]
	diffMat = np.tile(inX, (m,1))- group
	sqDiffMat = diffMat**2
	sqDistance = sqDiffMat.sum(axis = 1)
	distance = sqDistance ** 0.5
	sortedDistance = distances.argsort()
	classCount = {}
	for i in range(k):
		voteI = labels[sortedDistance[i]]
		classCount[voteI] = classCount.get(voteI, 0) + 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

train_folder = sys.argv[1]
test_folder = sys.argv[2]

train_data, train_labels = load_data(train_folder)
test_data, test_labels = load_data(test_folder)

for k in range(1, 21):
	rate = 0
	indx = 0
	for i in test_data:
		answer = classify0(i, train_data, train_labels, k)
		if answer == test_labels[indx]:
			rate += 1
		indx += 1
	print(rate / indx)
