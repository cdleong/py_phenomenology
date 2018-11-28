"""ECE 595 Computer problem CIV-4.

'PUTTING IT ALL TOGETHER'
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import numpy.polynomial.polynomial as poly
import seaborn as sns
from sklearn.metrics import mean_squared_error
from pyphenom import atmosphere
sns.set()

dirname = os.path.dirname(__file__)


def load_data(final_problem_data_file=dirname + "/../data/Final Problem.xls",
              atmo_trans_file=dirname + "/../data/ECE 595 Lesson 13 Transmission to Space.xlsx"):
    """Load excel files to pandas dataframes."""
    qe_df = pd.read_excel(final_problem_data_file, sheet_name="Quantum Efficiencies")
    print("loaded QE sheet.")
    print(qe_df.head())
    print("dtypes:")
    print(qe_df.dtypes)

    tau_df = pd.read_excel(final_problem_data_file, sheet_name="Tau Optics")
    print("\nLoaded TO sheet")
    print(tau_df.head())
    print("dtypes:")
    print(tau_df.dtypes)

    atmo_trans_df = pd.read_excel(atmo_trans_file)
    print("\nloaded atmo trans sheet")
    units_row = 0

    # drop units row
    atmo_trans_df = atmo_trans_df.drop([units_row])

    # fix datatypes
    for column_name in atmo_trans_df:

        print("fixing dtype for column {}".format(column_name))
        atmo_trans_df[column_name] = atmo_trans_df[column_name].apply(float)

    print(atmo_trans_df.head())
    print("dtypes:")
    print(atmo_trans_df.dtypes)

    return qe_df, tau_df, atmo_trans_df


if __name__ == "__main__":
    qe_df, tau_df, atmo_trans_df = load_data()

    plt.show()
