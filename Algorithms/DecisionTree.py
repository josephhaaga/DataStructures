# Decision Tree implementation
# CART Method; inspired by https://www.youtube.com/watch?v=LDRbO9a6XPU
# Joseph Haaga 12/17/2018

class Question:
    def __init__(self, feature, value):
        self.feature = feature # 'color'
        self.value = value # 'red'
    def ask(self, example):
        if (type(self.value) == str):
            return example[self.feature] == self.value
        else:
            return example[self.feature] >= self.value
    def __repr__(self):
        if (type(self.value) == str):
            return "Is "+str(self.feature)+" == "+str(self.value)
        else:
            return "Is "+str(self.feature)+" >= "+str(self.value)
    def __str__(self):
        if (type(self.value) == str):
            return "Is "+str(self.feature)+" == "+str(self.value)
        else:
            return "Is "+str(self.feature)+" >= "+str(self.value)

def get_value_counts(data):
    # data = [{'label': "Apple"}, {'label': "Orange"}, {'label': "Apple"}]
    labels = [d['label'] for d in data] # ['Apple', 'Orange', 'Apple']
    unique_labels = list(set(labels)) # ['Apple', 'Orange']
    return dict(zip(unique_labels, [labels.count(z) for z in unique_labels]))


class Node:
    def __init__(self, data, depth = 1):
        self.data = data
        self.impurity = self.calc_gini_impurity(self.data)
        self.level = depth
        if self.level <= 4: # LIMIT DEPTH OF TREE
            self.partition()
    def partition(self):
        # Given some data, determine the best Question to ask
        features = list(set(self.data[0].keys()) - set(['label'])) # ['color', 'diameter']
        possible_questions = list(set([(f, m[f]) for m in self.data for f in features]))
        information_gains = []
        for question in possible_questions:
            q = Question(question[0], question[1])
            trues = []; falses = [];
            for d in self.data:
                if q.ask(d):
                    trues.append(d)
                else:
                    falses.append(d)
            true_gini = len(trues) * self.calc_gini_impurity(trues)
            false_gini = len(falses) * self.calc_gini_impurity(falses)
            info_gain = self.impurity - (true_gini + false_gini)
            information_gains.append((q, info_gain))
        information_gains = sorted(information_gains, key=lambda x: x[1])
        if len(falses) > 0 and len(trues) > 0:
            self.question = information_gains[-1][0]
            self.false_branch = Node(falses, self.level+1)
            self.true_branch = Node(trues, self.level+1)
        return True

    def print_question(self):
        print(self.question)

    def calc_gini_impurity(self, data):
        impurity = 1
        label_counts = get_value_counts(data)
        for label in label_counts.keys():
            impurity -= (label_counts[label]/len(data))**2 # nrows
        return impurity

    def print_tree(self):
        print("")
        if hasattr(self, 'question'):
            print((self.level*" "), end=' ')
            print("Level "+str(self.level)+" ", end='')
            print((self.level*" "), end='')
            print(self.question)
            if hasattr(self, 'false_branch'):
                if hasattr(self.false_branch, 'question'):
                    print((self.level*" "), end=' ')
                    print("if False...")
                    self.false_branch.print_tree()
            if hasattr(self, 'true_branch'):
                if hasattr(self.true_branch, 'question'):
                    print((self.level*" "), end=' ')
                    print("if True...")
                    self.true_branch.print_tree()

def run():
    data = [
        {'color': 'green', 'diameter': 3, 'label': 'Apple'},
        {'color': 'yellow', 'diameter': 3, 'label': 'Apple'},
        {'color': 'red', 'diameter': 1, 'label': 'Grape'},
        {'color': 'red', 'diameter': 1, 'label': 'Grape'},
        {'color': 'yellow', 'diameter': 3, 'label': 'Lemon'}
    ]

    tree = Node(data)
