from datetime import date, datetime

import arff
import numpy as np


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataset = arff.load(open('datosFict1.arff', 'rb'))
    data = np.array(dataset['data'])
    x = datetime(1975, 2, 17)
    print(calculate_age(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
