# creating taxa files for our choices
file = open('bactTaxa_Habitat.txt', mode = 'r')
lines = file.readlines()
file.close()
f_human = open("Human_taxa.txt", "w")
f_animal = open("Animal_taxa.txt", "w")
#my_list = []
for line in lines:
   # print(line)
    line = line.split(';')
   # print(line[-1])
    word=line[-1].rstrip()
    #print(word)
    if word=="Human":
        #print("miao")
        f_human.write(line[1]+"\n")
    if word=="Animal":
        #print("miao2")
        f_animal.write(line[1]+"\n")

f_human.close()
f_animal.close()
print(f_animal)

# creating cog files for our choices
file = open('cog_words_bac.txt', mode = 'r')
f_human_cog = open("Human_cog.txt", "w")
f_animal_cog = open("Animal_cog.txt", "w")
lines = file.readlines()
file.close()
for line in lines:
    # print(line)
    line = line.split('\t')
    string = line[1:-1]
    name = line[0].split('#')
    name = name[3]
    #print(name)
    f_human = open("Human_taxa.txt", "r")
    f_animal = open("Animal_taxa.txt", "r")
    if name in f_animal.read():
        for item in string:
            f_animal_cog.write(item+ " ")
        f_animal_cog.write("\n")
    if name in f_human.read():
        for item in string:
            f_human_cog.write(item+" ")
        f_human_cog.write("\n")

f_animal.close()
f_human.close()
f_human_cog.close()
f_animal_cog.close()

#a + b - TO DO 

