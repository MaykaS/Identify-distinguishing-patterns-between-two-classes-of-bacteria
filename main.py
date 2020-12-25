# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_extract
import small_data_extract
import fpGrowth
import calculate_IG
import FP_algorithm


def print_info(item,ig,apoerance0,apperance1):
     print("the item:",item )
     print("have IG:", ig)
     print("apperce in habitat Human (label0):", apoerance0,"times")
     print("apperce in habitat Anima (label1):", apperance1,"times")

def rec(dict, max_item_set,max_ig,max_item):
    dataSet = []
    # dataSet_small =[]
    for k in dict.keys():
        dataSet.append(dict[k][0])
    dict1 = fpGrowth.createInitSet(dataSet)
    myFpTree, myHeaderTable = fpGrowth.createTree(dict1, 350)

    if myHeaderTable is None:
        print("len of myHeaderTable is 0")
        return max_item_set

    freqItemList = []
    fpGrowth.mineTree(myFpTree, myHeaderTable, 350, set([]), freqItemList)
    appearance_in_label1 = 0
    appearance_in_label0 = 0
    max_item_appearance_label0 = 0
    max_item_appearance_label1 = 0
    for item in freqItemList:
        ig,appearance_in_label0,appearance_in_label1 = calculate_IG.calculate_entropy(item, dict)
        if ig >= max_ig:
            max_ig = ig
            max_item = item
            max_item_appearance_label0 = appearance_in_label0
            max_item_appearance_label1 = appearance_in_label1
    print_info(max_item, max_ig, max_item_appearance_label0, max_item_appearance_label1)
    max_item_set.append(max_item)
    calculate_IG.delete(max_item,dict)

    if len(dict.keys())== 0:
        print("no more trans")
        return max_item_set

    rec(dict,max_item_set,max_ig,max_item)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     dict={}
     data_extract.func(dict)
     max_item_set =[]
     max_ig = 0
     max_item = ""
     rec(dict,max_item_set,max_ig,max_item)
     print("max item set:",max_item_set)





