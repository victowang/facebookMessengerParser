import pandas as pd
import bs4 as BeautifulSoup
import os


def getPage(name):
    with open(name) as fp:
        soup = BeautifulSoup.BeautifulSoup(fp, "html.parser")
    return soup.find_all("div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")

def getReceivedReactionsFromFile(dataframe, filename):
    page = getPage(filename)
    for message in page[1:]:
        name = message.div.string
        if not name in dataframe.columns:
            dataframe[name] = pd.Series(0, index=dataframe.index)
        dataframe[name]['nb_msg'] += 1
        for reaction in message.find_all("li"):
            emoji = reaction.string[0]
            if emoji in dataframe.index[1:7]:
                dataframe[name][emoji] += 1
                dataframe["Total"][emoji] += 1
            else:
                if (emoji == b'\xf0\x9f\x91\x8e'.decode()):
                    dataframe[name]['Thumb down'] += 1
                    dataframe["Total"]['Thumb down'] += 1
                elif (emoji == b'\xf0\x9f\x91\x8d'.decode()):
                    dataframe[name]['Thumb up'] += 1
                    dataframe["Total"]['Thumb up'] += 1
    return dataframe


def getReceivedReactionsFromDir(path):
    indexes = ['nb_msg', '😍', '😆', '😮', '😢', '😠', '❤', 'Thumb up', 'Thumb down']
    participant_list = ["Total"]
    dataframe = pd.DataFrame(0, index=indexes, columns=participant_list)

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.html' in file:
                files.append(os.path.join(r, file))
    files.sort()
    for f in files:
        print("Parsing : " + f)
        getReceivedReactionsFromFile(dataframe, f)
    return dataframe