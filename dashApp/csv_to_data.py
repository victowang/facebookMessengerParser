import pandas as pd

def sent(filename):
    dataframe = pd.read_csv(filename)
    data = []
    users = list(dataframe.head())[2:]
    #indexes = sent_dataframe["Unnamed: 0"]
    indexes = ['Reactions sent', '😍', '😆', '😮', '😢', '😠', '❤', 'Thumb up', 'Thumb down']

    for name in users:
        userDict = {}
        userDict['x'] = indexes
        userDict['y'] = dataframe[name]
        userDict['type'] = 'bar'
        userDict['name'] = name
        data.append(userDict)
    return data

def received(filename):
    dataframe = pd.read_csv(filename)
    # print(sent_dataframe)
    data = []
    users = list(dataframe.head())[2:]
    #indexes = dataframe["Unnamed: 0"]
    #indexes = ['Messages sent', 'Reactions received', '😍', '😆', '😮', '😢', '😠', '❤', 'Thumb up', 'Thumb down']
    indexes = ['Reactions received', '😍', '😆', '😮', '😢', '😠', '❤', 'Thumb up', 'Thumb down']

    for name in users:
        userDict = {}
        userDict['x'] = indexes
        userDict['y'] = dataframe[name][1:]
        userDict['type'] = 'bar'
        userDict['name'] = name
        data.append(userDict)
    return data

def sent_radar_charts(filename):
    dataframe = pd.read_csv(filename)
    charts = []
    users = list(dataframe.head())[2:]
    theta = ['😍', '😆', '😮', '😢', '😠', '❤', 'Thumb up', 'Thumb down']
    for name in users:
        r = dataframe[name][1:].to_list()
        max = 0
        for val in r:
            if val >= max:
                max = val
        r = [val/max for val in r]
        charts.append({'name': name, 'r':r, 'theta': theta})
    return charts