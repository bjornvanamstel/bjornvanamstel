import sys
import pandas as pd
from matplotlib import pyplot as plt
import os
from sklearn.linear_model import LinearRegression
sys.stdout = open("data graph sq.txt", "w")
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
            plt.savefig("{} 3seg indentation".format(filename))
            plt.clf()
            "plt.show()"

            xr = x.array.reshape(-1, 1)
            y3r = y3.array.reshape(-1, 1)

            xrup = xr[540:2550]
            y3rup = y3r[540:2550]

            linreg = LinearRegression()
            linreg_rup = linreg.fit(xrup, y3rup)
            y_pred_rup = linreg.predict(xrup)
            sq_rup = linreg.score(xrup, y3rup)

            plt.plot(xrup, y3rup)
            plt.plot(xrup, y_pred_rup, color='red')

            xrss = xr[2551:3556]
            y3rss = y3r[2551:3556]

            linreg_rss = linreg.fit(xrss, y3rss)
            y_pred_rss = linreg.predict(xrss)
            sq_rss = linreg.score(xrss, y3rss)

            plt.plot(xrss, y3rss)
            plt.plot(xrss, y_pred_rss, color='red')

            xrdn = xr[3556:5566]
            y3rdn = y3r[3556:5566]

            linreg_rdn = linreg.fit(xrdn, y3rdn)
            y_pred_rdn = linreg.predict(xrdn)
            sq_rdn = linreg.score(xrdn, y3rdn)

            plt.plot(xrup, y3rup, label="Cantilever (nm)")
            plt.plot(xrss, y3rss)
            plt.plot(xrdn, y3rdn)
            plt.plot(xrdn, y_pred_rdn, color='red')
            plt.plot(xrss, y_pred_rss, color='red')
            plt.plot(xrup, y_pred_rup, color='red')
            plt.xlabel = "Time"
            plt.legend()
            plt.rcParams["figure.figsize"] = [20, 10]
            plt.rcParams["figure.autolayout"] = True
            plt.savefig("{} sq 3 seg.png".format(filename))
            plt.clf()
            print('coefficient of determination {} before D-max:    '.format(filename), sq_rup)
            print('coefficient of determination {} during steady state: '.format(filename), sq_rss)
            print('coefficient of determination {} after D-max: '.format(filename), sq_rdn)
sys.stdout.close()