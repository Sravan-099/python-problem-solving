'''list=[1,2,3,4,5,6,7,8,9,10]
list2 = []
for n in list :
    if n % 4 == 0 :
        list2.append(n)
print(list2)
'''
names = ["srinu","sravan","sai","vamshi", "aei"]
s=[]
for words in names :
    count=0
    for char in words :
        if char in "aeiou":
            count+=1
            if count==3:
                s.append(words)
print(s)        
