# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_extract
import fpGrowth
import FP_algorithm
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    dict={}
    data_extract.func(dict)
    #print(dict)
    #FP_algorithm.func(dict)
    dataSet =[]
    for k in dict.keys():
        dataSet.append(dict[k][0])
    #fpGrowth.createTree(dataSet)
    print(len(dataSet))
    dict1=fpGrowth.createInitSet(dataSet)
    myFpTree,myHeaderTeble = fpGrowth.createTree(dict1,200)
    #myFpTree.disp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
