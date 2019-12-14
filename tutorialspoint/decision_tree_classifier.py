#!/usr/bin/env python3
import pydotplus
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
#from sklearn import cross_validation
from sklearn.model_selection import train_test_split
import collections

X = [[165,19],[175,32],[136,35],[174,65],[141,28],[176,15],[131,32],
        [166,6],[128,32],[179,10],[136,34],[186,2],[126,25],[176,28],[112,38],
        [169,9],[171,36],[116,25],[196,25]]

Y = ['Man','Woman','Woman','Man','Woman','Man','Woman','Man','Woman',
        'Man','Woman','Man','Woman','Woman','Woman','Man','Woman','Woman','Man']
data_feature_names = ['height','length of hair']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.40, random_state=5)

#After providing the dataset, we need to fit the model which can be done as follows −

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

#Predict
prediction = clf.predict([[133,37]])
print(prediction)

#We can visualize the decision tree with the help of the following Python code −

dot_data = tree.export_graphviz(clf,feature_names = data_feature_names,
                    out_file = None,filled = True,rounded = True)
graph = pydotplus.graph_from_dot_data(dot_data)
colors = ('orange', 'yellow')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

    for edge in edges: edges[edge].sort()

    for i in range(1): dest = graph.get_node(str(edges[edge][i]))[0]
    dest.set_fillcolor(colors[i])
    graph.write_png('Decisiontree16.png')
