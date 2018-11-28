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
    print(qe_df.head())

    tau_df = pd.read_excel(final_problem_data_file, sheet_name="Tau Optics")
    print(tau_df.head())

    atmo_trans_df = pd.read_excel(atmo_trans_file)
    print(atmo_trans_df.head())

    return qe_df, tau_df, atmo_trans_df


if __name__ == "__main__":
    qe_df, tau_df, atmo_trans_df = load_data()

    plt.show()
