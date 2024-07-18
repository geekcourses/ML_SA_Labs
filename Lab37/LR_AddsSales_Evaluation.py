import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression

from pprint import pprint


def load_data(path_to_file):
    return pd.read_csv(path_to_file, index_col=0)

def prepare_data():
    df = load_data('https://raw.githubusercontent.com/geekcourses/JupyterNotebooksExamples/master/datasets/various/Advertising.csv')

    X = df.drop(columns='sales')
    y = df['sales']

    return (X,y);

def perform_iteration(estimator, train_size ):
    # Separate data
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size)

    # Fit Model
    lm = estimator().fit(X_train,y_train)

    # Test and Evaluate
    y_pred = lm.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    return lm,mae

if __name__ == "__main__":
    iterations = []
    iterations_count = 3

    X,y = prepare_data()
    estimator = LinearRegression
    train_size = 0.5
    train_increment = 0.1

    for _ in range(iterations_count):
        lm,mae = perform_iteration(estimator=estimator, train_size=train_size)
        iterations.append({
            # 'estimator': estimator,
            'model':lm,
            'train_size':train_size,
            'mae':round(mae,4),
        })
        train_size+=train_increment


    iterations.sort(key=lambda d:d['mae'])
    pprint(iterations)

    best_model = iterations[0]['model']


    # Use our model:
    tv = 0.054809
    radio=1.000000
    newspaper = 0.354104

    # DONE: make it work
    predicted_sales = best_model.predict(pd.DataFrame({
        'TV':[tv],
        'radio':[radio],
        'newspaper':[newspaper]
    }))

    print(predicted_sales)




