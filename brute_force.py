#input and lowercase
need= input()
statement=need.lower()

#silly silly...I am just having fun here :) :) :)
if statement=='i love you':
    print('I love you too')
    print('but I am only an AI so this isnt real')
    quit()

#unessecary word database
pronouns= ['i','you','he','she','it','we','they','a','one','my']
link_verbs = ['be','am','is','are','were','been','being','to','with']
com_verbs = ['would','like','have','want','need','make','has','needs']
excess = ['can','help','something','some','little','really','can']
eliminations = [pronouns,link_verbs,com_verbs,excess]

#removal of unnecessary words
j=0
while j<len(eliminations):
    statement = ' '.join(i for i in statement.split() if i not in eliminations[j])
    j=j+1

#split statement
splitstate=statement.split()

#database for descriptions#
cup = ['cup of water','thirsty','water','drink','pour']
block = ['block','play','build','fun','bored']
scissor =['pair of scissors','cut','sharp','clip','trim','trimmed']
screwdriver = ['screwdriver','fix','screw','tool','unscrew']
pen =['pen','write','draw','jot']
phone = ['phone','call','text','google']
food =['croissant','food','hungry','eat','starving','peckish']
flower =['flower','gift','floral','smell','sweet','pretty']
sunglasses =['pair of sun glasses','sun','bright','protection','sunny']

#all possible objects
possible = [cup,block,scissor,screwdriver,pen,phone,food,flower,sunglasses]

#if there are no indicator words (null function)
if len(splitstate)==0:
    print('I cant help you there')
    quit()

#assigning object to leftover possible words
z=-1
while z<(len(splitstate)-1):
    z=z+1
    y=0
    while y<len(possible):
        obj=possible[y]
        y=y+1
        x=1
        while x<len(obj):
            if splitstate[z] == obj[x]:
                print ("I got you a " + obj[0] + "!")
                quit()
            else:
                x=x+1
print ('I dont know that there is anything I could get you')
