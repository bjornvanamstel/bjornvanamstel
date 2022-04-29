import sys
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats as st
import os
sys.stdout = open("Variance data indentation graph.txt", "w")
for root, dirs, files in os.walk("C:\\Users\\Bjorn\\Desktop\\Data"):
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
            # compute indentation graph variance
            var_indent = st.tvar(y2)
            # compute indentation graph variance
            # compute cantilever-piezo graph correlation
            corrcant = st.pearsonr(y3,y4)
            # compute cantilever-piezo graph correlation
            if corrcant[1]>0.0:
                plt.plot(x, y2, label="Indentation (nm)", color="red")
                plt.plot(x, y4, label="Piezo (nm)", color="blue")
                plt.xlabel = "Time"
                plt.legend()
                plt.rcParams["figure.figsize"] = [20, 10]
                plt.rcParams["figure.autolayout"] = True
                plt.savefig("Faulty {} indentation".format(filename))
                plt.clf()
                print('FAULTY variation of indentation graph {}:    '.format(filename), var_indent)
            else:
                if 0.9 > corrcant[0]:
                    plt.plot(x, y2, label="Indentation (nm)", color="red")
                    plt.plot(x, y4, label="Piezo (nm)", color="blue")
                    plt.xlabel = "Time"
                    plt.legend()
                    plt.rcParams["figure.figsize"] = [20, 10]
                    plt.rcParams["figure.autolayout"] = True
                    plt.savefig("NG {} indentation".format(filename))
                    plt.clf()
                    print('NG variation of indentation graph {}:    '.format(filename), var_indent)
                else:
                    plt.plot(x, y2, label="Indentation (nm)", color="red")
                    plt.plot(x, y4, label="Piezo (nm)", color="blue")
                    plt.xlabel = "Time"
                    plt.legend()
                    plt.rcParams["figure.figsize"] = [20, 10]
                    plt.rcParams["figure.autolayout"] = True
                    plt.savefig("{} indentation".format(filename))
                    plt.clf()
                    print('variation of indentation graph {}:    '.format(filename), var_indent)
sys.stdout.close()
sys.stdout = open("Piezo-Cantilever correlation.txt", "w")
for root, dirs, files in os.walk("C:\\Users\\Bjorn\\Desktop\\Data"):
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
            # compute cantilever-piezo graph correlation
            corrcant = st.pearsonr(y3,y4)
            # compute cantilever-piezo graph correlation
            if corrcant[1]>0.0:
                plt.plot(x, y3, label="Cantilever (nm)", color="green")
                plt.plot(x, y4, label="Piezo (nm)", color="blue")
                plt.xlabel = "Time"
                plt.legend()
                plt.rcParams["figure.figsize"] = [20, 10]
                plt.rcParams["figure.autolayout"] = True
                plt.savefig("Faulty {} cantilever-piezo".format(filename))
                plt.clf()
                print('FAULTY correlation of cantilever-piezo movement {}:    '.format(filename), corrcant)
            else:
                if 0.9 > corrcant[0]:
                    plt.plot(x, y3, label="Cantilever (nm)", color="green")
                    plt.plot(x, y4, label="Piezo (nm)", color="blue")
                    plt.xlabel = "Time"
                    plt.legend()
                    plt.rcParams["figure.figsize"] = [20, 10]
                    plt.rcParams["figure.autolayout"] = True
                    plt.savefig("NG {} cantilever-piezo".format(filename))
                    plt.clf()
                    print('NG correlation of cantilever-piezo movement {}:    '.format(filename), corrcant)
                else:
                    plt.plot(x, y3, label="Cantilever (nm)", color="green")
                    plt.plot(x, y4, label="Piezo (nm)", color="blue")
                    plt.xlabel = "Time"
                    plt.legend()
                    plt.rcParams["figure.figsize"] = [20, 10]
                    plt.rcParams["figure.autolayout"] = True
                    plt.savefig("{} cantilever-piezo".format(filename))
                    plt.clf()
                    print('correlation of cantilever-piezo movement {}:    '.format(filename), corrcant)
sys.stdout.close()