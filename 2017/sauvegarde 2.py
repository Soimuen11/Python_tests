Python 3.2.5 (default, May 15 2013, 23:06:03) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("a=",a, "b=", b)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print("a=",a, "b=", b)
NameError: name 'a' is not defined
>>> print("a=", a, "et b=",b)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("a=", a, "et b=",b)
NameError: name 'a' is not defined
>>> b=5
>>> a=10
>>> print("a=", a, "et b=",b)
a= 10 et b= 5
>>> perfect
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    perfect
NameError: name 'perfect' is not defined
>>> "perfect"
'perfect'
>>> print("hello world!")
hello world!
>>> #premier exemple de condition
>>> a=5
>>> if a>0:#Si a est supérieur à 0
	print("a est supérieur à 0.")

	
a est supérieur à 0.
>>> if a>0
SyntaxError: invalid syntax
>>> 
>>> if a>0:
	print("a est supérieur à 0")

	
a est supérieur à 0
>>> a=5
>>> b=8
>>> if a>0:
	#on incrémente la valeur de b
	b+=1
	#on affiche les valeurs des variables
	print("a=", a' et b=", b)
	      
SyntaxError: EOL while scanning string literal
>>> 
>>> if a>0:
	#on incrémente la valeur de b
	b+=1
	#on affiche les valeurs des variables
	print("a=", a, "et b=", b)

	
a= 5 et b= 9
>>> a=5
>>> if aif a>0:
	#on incrémente la valeur de b
	b+=1
	#on affiche les valeurs des variables
	print("a=", a' et b=", b)
	      
SyntaxError: invalid syntax
>>> a=5
>>> if a>0: # Si a est positif
	print("a est positif")
    if a< 0: # Si est a est inférieur à 0
	    
SyntaxError: unindent does not match any outer indentation level
>>> if a>0: # Si a est positif
	print("a est positif")
    if a< 0: # a est négatif
	    
SyntaxError: unindent does not match any outer indentation level
>>> if a>0: # Si a est positif
	print("a est positif")
    if a<0: # a est négatif
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>>  if a>0: # Si a est positif
	print("a est positif")
if a<0: # a est négatif
	
SyntaxError: unexpected indent
>>> SyntaxError: unexpected indent
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> age =21
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")

	
vous êtes majeur
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")
	else: # sinon (age inférieur à 18)
		
SyntaxError: invalid syntax
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")
     else
     
SyntaxError: unindent does not match any outer indentation level
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")
	else:
		
SyntaxError: invalid syntax
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")
	elif
	
SyntaxError: invalid syntax
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")
	else
	
SyntaxError: invalid syntax
>>> if age>=18:# si age est supérieur ou égal à 18
	print("vous êtes majeur")
	else print("vous êtes mineur")
	
SyntaxError: invalid syntax
>>> if a=5
SyntaxError: invalid syntax
>>> a=5
>>> if a>0:
	print("a est supérieur à 0")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
