a=['a','b',1,2]
a.append(3)
print(a)

a=['a','b',1,2]
a.insert(2,3)
print(a)

a1 = [1, 2, 3] 
a2 = [2, 3, 4, 5] 
a1.extend(a2)         
print(a1)  
a2.extend(a1)  
print(a2) 

a = [1, 2, 3, 4, 5] 
print(sum(a)) 

b = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(b.count(3))

c1 = [0.3, 2.1, 3.2, 5.1, 1, 2.5] 
print(min(c1)) 
c2 = [2.3, 4.4, 3, 5.3, 1, 2.5] 
print(max(c2))  