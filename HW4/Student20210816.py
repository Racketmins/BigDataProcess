import sys
import os
import numpy as np
import operator
from collections import Counter

def load_data(folderName):
	data = []
	labels = []
	for filename in os.listdir(folderName):
		label = int(filename.split('_')[0])
		with open(os.path.join(folderName, filename)) as f:
			content = f.read().replace('\n', '')
			data.append([int(i) for i in content if i != '\n'])
		labels.append(label)
	return np.array(data), np.array(labels)

def calDistance(a, b):
	return np.sqrt(np.sum((a - b)**2))

def classify0(inX, group, labels, k):
	distances = [calDistance(inX, i) for i in group]
	nearest = np.argsort(distances)[:k]
	nearest_labels = labels[nearest]
	return Counter(nearest_labels).most_common(1)[0][0]

train_folder = sys.argv[1]
test_folder = sys.argv[2]

train_data, train_labels = load_data(train_folder)
test_data, test_labels = load_data(test_folder)

for k in range(1, 21):
	rate = 0
	leng = len(test_data)
	for i in range(leng):
		answer = classify0(test_data[i], train_data, train_labels, k)
		if answer != test_labels[i]:
			rate += 1
	print(int((rate / leng)*100))
