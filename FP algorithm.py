import fpGrowth

print("start of Listing 12.2")
rootNode = fpGrowth.treeNode('pyramid',9,None)
rootNode.children['eye'] = fpGrowth.treeNode('eye',13,None)
rootNode.disp()
rootNode.children['phoenix'] = fpGrowth.treeNode('phoenix', 3, None)
rootNode.disp()
print("end of Listing 12.2")
print("\n")
print("start of Listing 12.3")
simpDat = fpGrowth.loadSimpDat()
for i in simpDat:
   print(simpDat)
print("\n")
initSet = fpGrowth.createInitSet(simpDat)
print(initSet)
print("\n")
#The FP-tree
myFPtree, myHeaderTab = fpGrowth.createTree(initSet, 3)
myFPtree.disp()
print("end of Listing 12.3")
print("\n")
print("start of Listing 12.4")
print(fpGrowth.findPrefixPath('x', myHeaderTab['x'][1]))
print(fpGrowth.findPrefixPath('z', myHeaderTab['z'][1]))
print(fpGrowth.findPrefixPath('r', myHeaderTab['r'][1]))
print("end of Listing 12.4")
print("\n")
print("start of Listing 12.5") 
#Now create an empty list to store all the frequent itemsets
freqItems = []
print(fpGrowth.mineTree(myFPtree, myHeaderTab, 3, set([]), freqItems))
print(freqItems)

print("end of Listing 12.5")
# TODO: Code to access the Twitter Python library - NEED?

