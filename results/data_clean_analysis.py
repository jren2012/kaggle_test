import os
import re
from collections import defaultdict
import numpy as np
from matplotlib.pylab import plt
import matplotlib.ticker as ticker
import plotly as py
import plotly.graph_objs as go


def extractData(dataPath):
    # Open the file with read only permit
    f = open(dataPath, "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    result = []

    lines = f.readlines()
    # close the file after reading the lines.
    f.close()

    i = 1
    for line in lines:
        # 572/572 [=============] - 21207s 37s/step - loss: 2.4878 - acc: 0.4582 - val_loss: 12.0619 - val_acc: 0.1163
        # print(line)
        # [float(s) for s in re.findall(r'-?\d+\.?\d*', 'he33.45llo -42 I\'m a 32 string 30')]

        matchObj = re.match(r'.* loss: (\d.\d*) - acc: (\d.\d*) - val_loss: (\d.\d*) - val_acc: (\d.\d*)', line,
                            re.M | re.I)
        if matchObj:
            loss = matchObj.group(1)
            acc = matchObj.group(2)
            val_loss = matchObj.group(3)
            val_acc = matchObj.group(4)
            print(loss, acc, val_loss, val_acc)
            # print(matchObj.group(1), matchObj.group(2), matchObj.group(3), matchObj.group(4))
            i = i + 1
            result.append([loss, acc, val_loss, val_acc])

    print(result)
    loss = [item[0] for item in result]
    acc = [item[1] for item in result]
    val_loss = [item[2] for item in result]
    val_acc = [item[3] for item in result]
    print(loss)
    print(acc)
    print(val_loss)
    print(val_acc)


    # resultDict = defaultdict(list)
    #
    # for item in loss:
    #     resultDict['loss'].append(item)
    #
    # for item in acc:
    #     resultDict['acc'].append(item)
    #
    # for item in val_loss:
    #     resultDict['val_loss'].append(item)
    #
    # for item in val_acc:
    #     resultDict['val_acc'].append(item)

    resultDict = defaultdict(list)
    for i in range(len(loss)):
        resultDict['index'].append(i+1)
        resultDict['loss'].append(loss[i])
        resultDict['acc'].append(acc[i])
        resultDict['val_loss'].append(val_loss[i])
        resultDict['val_acc'].append(val_acc[i])

    print("=============")
    print(resultDict['index'])
    print(resultDict['loss'])
    print(resultDict['acc'])
    print(resultDict['val_loss'])
    print(resultDict['val_acc'])

    return resultDict


def getopts():
    from sys import argv
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts


def plot_train(result, outputfilename):
    trace0 = go.Scatter(
        x=result['index'],
        y=result['loss'],
        name='training_loss',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4)
    )
    trace2 = go.Scatter(
        x=result['index'],
        y=result['val_loss'],
        name='val_loss',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4,
            dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
    )

    data = [trace0, trace2]

    # Edit the layout
    layout = dict(title='The Loss of simple_cnn',
                  xaxis=dict(title='Epoch'),
                  yaxis=dict(title='Loss)'),
                  )

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, filename=outputfilename)


def plot_val(result, outputfilename):
    trace1 = go.Scatter(
        x=result['index'],
        y=result['acc'],
        name='training_acc',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4, )
    )
    trace3 = go.Scatter(
        x=result['index'],
        y=result['val_acc'],
        name='val_acc',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4,
            dash='dash')
    )

    data = [trace1, trace3]

    # Edit the layout
    layout = dict(title='The Accuracy of simple_cnn',
                  xaxis=dict(title='Epoch'),
                  yaxis=dict(title='Accuracy'),
                  )

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, filename=outputfilename)


if __name__ == "__main__":
    opts = getopts()
    dataPath = opts.get('--path', 'xxx.txt')
    outputfilename_tr = opts.get('--outputfilename', 'simple_cnn_loss.html')
    outputfilename_val = opts.get('--outputfilename', 'simple_cnn_acc.html')
    print(dataPath)
    result = extractData(dataPath)
    plot_train(result, outputfilename_tr)
    plot_val(result, outputfilename_val)

    # ax = plt.figure(figsize=(8, 6))
    # plt.plot(result['loss'], '-.', color="#333333", label="loss")
    # plt.plot(result['acc'], '-.', color="chocolate", label="acc")
    # plt.plot(result['val_loss'], '-.', color="red", label="val_loss")
    # plt.plot(result['val_acc'], '-.', color="green", label="val_acc")
    # plt.legend(loc='upper left')
    # plt.AutoLocator()
    # plt.title("The performance of VGG16 model", fontsize=16)
    # plt.xlabel("Number of Epochs")
    # plt.ylabel("Accuracy")
    # plt.show()






