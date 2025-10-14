#fucntion to check whetether 
#first and last character of words atch
def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)

    print("list of words iwth first and last character same\n",lst)
    return ctr has
count=match_words(['aba','cfc','xyz','abc','1221'])
print("numbers of wrods having first and last characyer same:",count)


