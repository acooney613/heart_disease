import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

class train_rf:
    def __init__(self, name, data):
        print(name)
        print(data)