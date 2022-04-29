import sys
import pandas as pd
from matplotlib import pyplot as plt
import os
from sklearn.linear_model import LinearRegression
sys.stdout = open("indentation graph sq.txt", "w")
for root, dirs, files in os.walk("C:\\Users\\Gebruiker\\Desktop\\SQ Testing"):
    dirs[:] = [d for d in dirs if d not in 'Calib']
    for f in files:
        if f.endswith(".txt"):
            file = f
            filepath = os.path.abspath(os.path.join(root, file))
            df = pd.read_csv(filepath,
                             skiprows=37, sep='\t', header=0)
            filename = file.replace(".txt", "")
            x = df[df.columns[0]]
            y1 = df[df.columns[1]]
            y2 = df[df.columns[2]]
            y3 = df[df.columns[3]]
            y4 = df[df.columns[4]]
            plt.plot(x, y2, label="Indentation (nm)")
            plt.plot(x, y4, label="Piezo (nm)")
            plt.xlabel = "Time"
            plt.legend()
            plt.rcParams["figure.figsize"] = [20, 10]
            plt.rcParams["figure.autolayout"] = True
            plt.savefig("{} indentation".format(filename))
            plt.clf()
            "plt.show()"

            xr = x.array.reshape(-1, 1)
            y2r = y2.array.reshape(-1, 1)

            linreg = LinearRegression(fit_intercept=True)
            linreg_rin = linreg.fit(xr, y2r)
            y_pred_r = linreg.predict(xr)
            sq_r = linreg.score(xr, y2r)

            plt.plot(xr, y2r)
            plt.plot(xr, y_pred_r, color='red')

            plt.rcParams["figure.figsize"] = [20, 10]
            plt.rcParams["figure.autolayout"] = True
            plt.savefig("{} indentation sq.png".format(filename))
            plt.clf()
            "plt.show()"
            print('coefficient of determination for indentation graph of {} :   '.format(filename), sq_r)
sys.stdout.close()
