import random
import numpy as np

# Sample function to split a dataset based on an attribute and attribute value
def split_dataset(dataset, feature_index, threshold):
    left = []
    right = []
    for row in dataset:
        if row[feature_index] < threshold:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            proportion = [row[-1] for row in group].count(class_val) / size
            score += proportion * proportion
        gini += (1.0 - score) * (size / n_instances)
    return gini

# Select the best split point for a dataset
def get_best_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    best_index, best_value, best_score, best_groups = 999, 999, 999, None
    for feature_index in range(len(dataset[0])-1):
        for row in dataset:
            groups = split_dataset(dataset, feature_index, row[feature_index])
            gini = gini_index(groups, class_values)
            if gini < best_score:
                best_index, best_value, best_score, best_groups = feature_index, row[feature_index], gini, groups
    return {'index': best_index, 'value': best_value, 'groups': best_groups}

# Create a terminal node
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_best_split(left)
        split(node['left'], max_depth, min_size, depth+1)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_best_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_best_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

# Build a random forest
def random_forest(train, max_depth, min_size, n_trees):
    forest = []
    for _ in range(n_trees):
        sample = random.sample(train, len(train))  # Random sample with replacement
        tree = build_tree(sample, max_depth, min_size)
        forest.append(tree)
    return forest

# Make a prediction with a random forest
def random_forest_predict(forest, row):
    predictions = [predict(tree, row) for tree in forest]
    return max(set(predictions), key=predictions.count)

# Evaluate algorithm accuracy
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Random Forest Algorithm
def random_forest_algorithm(train, test, max_depth, min_size, n_trees):
    forest = random_forest(train, max_depth, min_size, n_trees)
    predictions = [random_forest_predict(forest, row) for row in test]
    actual = [row[-1] for row in test]
    accuracy = accuracy_metric(actual, predictions)
    return accuracy

# Example usage with a toy dataset (last column is the label)
dataset = [
    [2.771244718, 1.784783929, 0],
    [1.728571309, 1.169761413, 0],
    [3.678319846, 2.812813571, 0],
    [3.961043357, 2.61995032, 0],
    [2.999208922, 2.209014212, 0],
    [7.497545867, 3.162953546, 1],
    [9.00220326, 3.339047188, 1],
    [7.444542326, 0.476683375, 1],
    [10.12493903, 3.234550982, 1],
    [6.642287351, 3.319983761, 1]
]

# Split dataset into train and test
train = dataset[:8]
test = dataset[8:]

# Train random forest and evaluate accuracy
max_depth = 4
min_size = 1
n_trees = 6
accuracy = random_forest_algorithm(train, test, max_depth, min_size, n_trees)
print(f"Accuracy: {accuracy}%")
