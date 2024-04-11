import pandas as pd
from train_models.train_rf import train_rf

test = pd.read_csv('data/heart_attack_prediction_dataset.csv')

data_type = None
while data_type == None:
    print('What would you like to diagnose:\n1: Heart Attack\n2: Heart Disease\n')
    user_input = input('Enter here: ')

    try:
        data_type = float(user_input)
        train_rf(data_type, test)
    except ValueError:
        data_type = None
        print('Please enter a number listed above :)\n')



