from math import log2


def entropy(class0, class1):
    if class0 <=0 or class1<=0:
        return 0

    return -(class0 * log2(class0) + class1 * log2(class1))

def calculate_entropy(item,dict):
    # split of the main dataset
    num_of_trans = len(dict.keys())
    num_of_0 = 0
    num_of_1 = 0
    for k in dict.keys():
        if dict[k][1] == 0:
            num_of_0 += 1
        else:
            num_of_1 += 1
    class0 = num_of_0 / num_of_trans
    class1 = num_of_1 / num_of_trans
    s_entropy=entropy(class0,class1)

    # split 1&2 (split via value1)
    num_of_0_item_in = 0
    num_of_1_item_in = 0
    num_of_0_item_not = 0
    num_of_1_item_not = 0
    for k in dict.keys():
        if set(item).issubset(dict[k][0]) :
            if dict[k][1]==0:
                num_of_0_item_in+=1
            else:
                num_of_1_item_in+=1
        else:
            if dict[k][1] == 0:
                num_of_0_item_not += 1
            else:
                num_of_1_item_not += 1
    num1 = num_of_1_item_in+num_of_0_item_in
    if num1 == 0:
        s1_entropy = 0
    else:
        s1_entropy = entropy(num_of_0_item_in/num1,num_of_1_item_in/num1)
    num2 = num_of_0_item_not+num_of_1_item_not
    if num2 == 0:
        s2_entropy = 0
    else:
        s2_entropy = entropy(num_of_0_item_not / num2, num_of_1_item_not / num2)

    gain = s_entropy - (num1/num_of_trans * s1_entropy + num2/num_of_trans * s2_entropy)
    return gain,num_of_0_item_in,num_of_1_item_in

def delete(item,dict):
    trans_to_del=[]
    for k in dict.keys():
        if set(item).issubset(dict[k][0]) :
            trans_to_del.append(k)
    for trans in trans_to_del:
        del(dict[trans])

def dived_data(dict,dataSetList,num):#just five blocks regular
    length = len(dict.keys())
    a = int(length/num)
    keys = list(dict.keys())
    for i in range(0,num):
        dataSetList.append([])
    j = 0
    i = 0
    for k in dict.keys():
        dataSetList[i].append(dict[k][0])
        j+=1
        if j == a:
            if i == num-1:
                continue
            i+=1
            j = 0

