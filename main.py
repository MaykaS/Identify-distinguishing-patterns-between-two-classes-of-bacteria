# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_extract
import fpGrowth
import calculate_IG
import operator
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


import FP_algorithm



def act(min_sup,num):
    dict = {}
    data_extract.func(dict)
    # dict- key:bac_name , value:[transaction][label0\1]

    # sperate data by 0/1
    dict0 = {}
    dict1 = {}
    for k in dict.keys():
        if dict[k][1] == 0:
            dict0[k] = dict[k]
        else:
            dict1[k] = dict[k]

    dataSetList0 = []
    dataSetList1 = []
    calculate_IG.dived_data(dict0, dataSetList0, num)
    calculate_IG.dived_data(dict1, dataSetList1, num)

    initSet0 = []
    initSet1 = []
    for i in range(0, num):
        initSet0.append(fpGrowth.createInitSet(dataSetList0[i]))
        initSet1.append(fpGrowth.createInitSet(dataSetList1[i]))


    myFpTreeList0 = []
    myHeaderTableList0 = []
    myFpTreeList1 = []
    myHeaderTableList1 = []

    for i in range(0, num):
        tree, table = fpGrowth.createTree(initSet0[i], min_sup)
        myFpTreeList0.append(tree)
        myHeaderTableList0.append(table)

        tree1, table1 = fpGrowth.createTree(initSet1[i], min_sup)
        myFpTreeList1.append(tree1)
        myHeaderTableList1.append(table1)

    for i in range(0, num):
        if myHeaderTableList0[i] is None:
            print(i, "my 0 headr table len is 0")
        if myHeaderTableList1[i] is None:
             print(i, "my 1 headr table len is 0")



    freqItemList0 = []
    freqItemList1 = []
    for i in range(0, num):
        freqItemList0.append([])
    for i in range(0, num):
        freqItemList1.append([])

    for i in range(0, num):
         if myHeaderTableList0[i] is not None:
            fpGrowth.mineTree(myFpTreeList0[i], myHeaderTableList0[i], min_sup, set([]), freqItemList0[i])
         if myHeaderTableList1[i] is not None:
             fpGrowth.mineTree(myFpTreeList1[i], myHeaderTableList1[i], min_sup, set([]), freqItemList1[i])

    freeItem = []
    for i in range(0, num):
        for word in freqItemList0[i]:
            if word not in freeItem:
                freeItem.append(word)
        for word in freqItemList1[i]:
            if word not in freeItem:
                freeItem.append(word)


    item_dict = {}
    best_words = []
    for item in freeItem:
        ig, appearance_in_label0, appearance_in_label1 = calculate_IG.calculate_entropy(item, dict)
        item_dict[str(item)] = []
        item_dict[str(item)].append(ig)
        item_dict[str(item)].append(appearance_in_label0)
        item_dict[str(item)].append(appearance_in_label1)


    average_sorted = sorted(item_dict.items(), key=operator.itemgetter(1))
    for i in range(0, 10):
        best_words.append(average_sorted[len(average_sorted) - i - 1][0])

    for word in best_words:
        print("the word:", word, " with ig of: ", item_dict[str(word)][0],
              " label0: ", item_dict[str(word)][1], " label1: ", item_dict[str(word)][2])



def graphs():
    time_list = [12.46,5.9,4.92]
    sup_list = [24,25,26]
    # data
    df = pd.DataFrame({'x': sup_list, 'y': time_list})

    # plot
    plt.ylabel("run time")
    plt.xlabel("min sup")
    plt.plot('x', 'y', data=df, linestyle='-', marker='o')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     num = 3  # to how many group to split the data
     min_sup = 24
     start_time = time.time()
     act(min_sup,num)
     end_time = time.time()
     print("the time with min_supp of: ", min_sup, " was: ", end_time - start_time)

     #graphs()


