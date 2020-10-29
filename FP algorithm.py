import fpGrowth

rootNode = fpGrowth.treeNode('pyramid',9,None)
rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)
rootNode.disp()
rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix', 3, None)
rootNode.disp()




#reload(fpGrowth)
simpDat = fpGrowth.loadSimpDat()
print(simpDat)

initSet = fpGrowth.createInitSet(simpDat)
print(initSet)

#The FP-tree
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)
myFPtree.disp()

#reload(fpGrowth)
fpGrowth.findPrefixPath('x', myHeaderTab['x'][1])
fpGrowth.findPrefixPath('z', myHeaderTab['z'][1])
fpGrowth.findPrefixPath('r', myHeaderTab['r'][1])

reload(fpGrowth)
#Now create an empty list to store all the frequent itemsets
freqItems = []
fpGrowth.mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems)
freqItems

# TODO: Code to access the Twitter Python library - NEED?

