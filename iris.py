#!/usr/bin/env/python3

from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("iris_dataset의 키: \n{}".format(iris_dataset.keys()))
print("iris_dataset의 data shape: \n{}".format(iris_dataset['data'].shape))