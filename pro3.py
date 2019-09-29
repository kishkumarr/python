def stringfun():
	print("Methods in string")
	string1 = "Hello world"
	print("Printing string1 ",string1)
	print("Accessing characters in string ",string1[2:6])
	string2 = string1.replace('world','everyone')
	print("Replacing a word in the string ",string2)
	print("Upper case of a string ",string2.upper())
	print("Lower case of a string ",string1.lower())
	print("Join in string ",string1.join("!!!!"))
  
stringfun()
