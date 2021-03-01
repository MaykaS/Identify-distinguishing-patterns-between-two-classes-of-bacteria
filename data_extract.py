# creating taxa files for our choices
def func(dict):
    file = open('bactTaxa_Habitat.txt', mode = 'r')
    lines = file.readlines()
    file.close()
    f_human = open("Host_taxa.txt", "w")
    f_animal = open("Animal_taxa.txt", "w")
    i = 0
    for line in lines:
        line = line.split(';')
        word=line[-1].rstrip()
        if word=="Human":
            if i < 125: #we want that human and plant have the same amunt of trans
                f_human.write(line[1]+"\n")
                list =[[],0]
                dict[line[1]]=list
                i+=1
        if word=="Plant":
            f_animal.write(line[1]+"\n")
            list = [[],1]
            dict[line[1]] = list

    f_human.close()
    f_animal.close()
    #print(f_animal)

# creating cog files for our choices
    file = open('cog_words_bac.txt', mode = 'r')
    f_human_cog = open("Human_cog.txt", "w")
    f_animal_cog = open("Animal_cog.txt", "w")
    lines = file.readlines()
    file.close()
    f_human = open("Host_taxa.txt", "r")
    f_animal = open("Animal_taxa.txt", "r")
    for line in lines:
        # print(line)
        line = line.split('\t')
        string = line[1:-1]
        name = line[0].split('#')
        name = name[3]
   # print(name)
        if name in dict.keys():
            for item in string:
                if item != 'X':
                    if item not in dict[name][0]:
                    #f_animal_cog.write(item+ " ")
                        dict[name][0].append(item)
    key_to_del=[]
    for k in dict.keys():
        if len(dict[k][0]) == 0:
            key_to_del.append(k)
    for k in key_to_del:
        del dict[k]

    f_animal.close()
    f_human.close()
    f_human_cog.close()
    f_animal_cog.close()
#a + b - TO DO 

