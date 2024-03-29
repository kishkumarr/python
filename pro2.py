s = open('test.txt','r').read()  
num_chars = len(s)
num_lines = s.count('\n')
words = s.split()
d = {}
for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w],w) for w in d]
lst.sort()
lst.reverse()
print('Your input file has characters = '+str(num_chars))
print('Your input file has lines = '+str(num_lines))
print('Your input file has the following words = '+str(num_words))

print('\n The most frequent words are /n')

i = 1
for count, word in lst[:5]:
    print('%2s. %s %s' %(i,count,word))
    i+= 1



test.txt: 

Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.
Python is a MUST for students and working professionals to become a great Software Engineer specially when they are working in Web Development Domain.

Output:

Your input file has characters = 425
Your input file has lines = 2
Your input file has the following words = 61

 The most frequent words are /n
 1. 3 is
 2. 3 and
 3. 3 a
 4. 3 Python
 5. 2 working
