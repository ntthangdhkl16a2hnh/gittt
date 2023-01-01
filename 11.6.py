Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 23 2018, 23:31:17) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[74,74,72,72,73,69,69,71,76,71]
>>> list1=list[:3]
>>> list2=list[3:]
>>> print(list1)
[74, 74, 72]
>>> print(list2)
[72, 73, 69, 69, 71, 76, 71]
>>> m=sum(list)/len(list)
>>> print('trung bình:',rond(m,2))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('trung bình:',rond(m,2))
NameError: name 'rond' is not defined
>>> print('trung bình:' ,m)
trung bình: 72.1
>>> print(max(list))
76
>>> print(min(list))
69
>>> list.sort()
>>> print(list)
[69, 69, 71, 71, 72, 72, 73, 74, 74, 76]
>>> list.sort()
>>> list.reverse()
>>> print('\nAfter reverse:', list)

After reverse: [76, 74, 74, 73, 72, 72, 71, 71, 69, 69]
>>> 
