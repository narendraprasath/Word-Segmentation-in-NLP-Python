# Author Narendra Prasath B
# python 3.5.1

from __future__ import with_statement #with statement for reading file
import re   # Regular expression

words = []  #  corpus file words
testword = []   # test words   
ans = []    # words matches with corpus

print("MENU")
print("-----------")
print(" 1 . Hash tag segmentation ")
print(" 2 . URL segmentation ")
print("enter the input choice for performing word segmentation")
choice = int(input())
if choice == 1:
    text = "#whatismyname"         # hash tag test data to segment
    print("input with HashTag",text)
    pattern=re.compile("[^\w']")
    a = pattern.sub('', text)
elif choice == 2:
    text = "www.whatismyname.com"       # url test data to segment
    print("input with URL",text)
    a=re.split('\s|(?<!\d)[,.](?!\d)', text)
    splitwords = ["www","com","in"]      # remove the words which is containg in the list
    a ="".join([each for each in a if each not in splitwords])
    

else:
    print("wrong choice...try again")


print(a)
for each in a:
    testword.append(each)   #test word 
test_lenth = len(testword)       # lenth of the test data

    
# Reading the corpus
with open('words.txt', 'r') as f:
    lines = f.readlines()
    words =[(e.strip()) for e in lines]

def Seg(a,lenth):
    ans =[]
    for k in range(0,lenth+1):  # this loop checks char by char in the corpus
        
        if a[0:k] in words:
            print(a[0:k],"-appears in the corpus")
            ans.append(a[0:k])   
            break
    if ans != []:
        g = max(ans,key=len)
        return g

test_tot_itr = 0    #each iteration value
answer = []     # Store the each word contains the corpus
Score = 0   # initial value for score
N = 37    # total no of corpus
M = 0
C = 0
while test_tot_itr < test_lenth:    
    ans_words = Seg(a,test_lenth)
    if ans_words != 0:
        test_itr = len(ans_words)
        answer.append(ans_words)
        a = a[test_itr:test_lenth]
        test_tot_itr += test_itr

Aft_Seg = " ".join([each for each in answer])
# print segmented words in the list
print("output")
print("---------")
print(Aft_Seg)  # print After segmentation the input 

# Calculating Score
C = len(answer)
score = C * N / N       # Calculate the score
print("Score",score)        

