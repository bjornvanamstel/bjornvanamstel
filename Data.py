import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
file = input("Enter indentation name: ")
df = pd.read_csv("C:\\Users\\Gebruiker\\Desktop\\50Nm 500um\\{}\\Indentations\\{} Indentation_001.txt".format(file,file), skiprows=37, sep='\t', header=0)

x = df[df.columns[0]]
y1 = df[df.columns[1]]
y2 = df[df.columns[2]]
y3 = df[df.columns[3]]
y4 = df[df.columns[4]]
plt.plot(x, y3, label = "Cantilever (nm)")
plt.plot(x, y4, label = "Piezo (nm)")
plt.xlabel="Time"
plt.legend()
plt.rcParams["figure.figsize"]=[20,10]
plt.rcParams["figure.autolayout"]= True
plt.savefig(file)
plt.show()

xr = x.array.reshape(-1,1)
y3r = y3.array.reshape(-1,1)

xrup = xr[540:2550]
y3rup = y3r[540:2550]

linreg = LinearRegression()
linreg_rup = linreg.fit(xrup,y3rup)
y_pred_rup = linreg.predict(xrup)
sq_rup = linreg.score(xrup,y3rup)

plt.plot(xrup, y3rup)
plt.plot(xrup,y_pred_rup, color='red')

xrss = xr[2551:3556]
y3rss = y3r[2551:3556]

linreg_rss = linreg.fit(xrss,y3rss)
y_pred_rss = linreg.predict(xrss)
sq_rss = linreg.score(xrss,y3rss)

plt.plot(xrss, y3rss)
plt.plot(xrss,y_pred_rss, color='red')

xrdn = xr[3556:5566]
y3rdn = y3r[3556:5566]

linreg_rdn = linreg.fit(xrdn,y3rdn)
y_pred_rdn = linreg.predict(xrdn)
sq_rdn = linreg.score(xrdn,y3rdn)

plt.plot(xrup, y3rup, label = "Cantilever (nm)")
plt.plot(xrss, y3rss)
plt.plot(xrdn, y3rdn)
plt.plot(xrdn,y_pred_rdn, color='red')
plt.plot(xrss,y_pred_rss, color='red')
plt.plot(xrup,y_pred_rup, color='red')
plt.xlabel="Time"
plt.legend()
plt.rcParams["figure.figsize"]=[20,10]
plt.rcParams["figure.autolayout"]= True
plt.savefig("{} sq.png".format(file))
plt.show()
print('coefficient of determination before D-max:', sq_rup)
print('coefficient of determination during steady state:', sq_rss)
print('coefficient of determination after D-max:', sq_rdn)

