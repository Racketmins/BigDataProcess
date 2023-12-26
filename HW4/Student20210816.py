import sys
import os
import numpy as np
from collections import Counter

def load_data(folderName):
    data = []
    labels = []
    for filename in os.listdir(folderName):
        if filename.endswith(".txt"):
            label = int(filename.split("_")[0])
            filepath = os.path.join(folderName, filename)
            with open(filepath, 'r') as file:
                content = file.read().replace('\n', '')
                data.append(list(map(int, content)))
                labels.append(label)
    return np.array(data), np.array(labels)

def calculate_distance(a, b):
    return np.sqrt(np.sum((a - b)**2))

def classify0(input_data, training_data, training_labels, k):
    distances = [calculate_distance(input_data, i) for i in training_data]
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = training_labels[nearest_indices]
    return Counter(nearest_labels).most_common(1)[0][0]

train_folder = sys.argv[1]
test_folder = sys.argv[2]

train_data, train_labels = load_data(train_folder)
test_data, test_labels = load_data(test_folder)

for k in range(1, 21):
    error_count = 0
    total_len = len(test_data)
    for i in range(total_len):
        prediction = classify0(test_data[i], train_data, train_labels, k)
        if prediction != test_labels[i]:
            error_count += 1
    print(int((error_count / total_instances) * 100))
