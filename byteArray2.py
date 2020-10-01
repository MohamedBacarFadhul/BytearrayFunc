#!/usr/bin/python3
#Bytearray impaire
def funcBytearrayParitePaire():

   arr=input("Enter your number:")
   trans=int(arr)
   array=bytearray(trans)
   a=format(trans, '08b')
   strA=a.split(",")
   print("Le nombre saisie en binnaire est ",strA)
   one_count=0
   for i in strA:
    	   if i=="1":
             one_count=+0

   if one_count%2==0:
        strA.append("0")

   full_str = ' '.join([str(elem) for elem in strA])
   print("Le parité paire de ",a , "est", full_str)
  


print (funcBytearrayParitePaire())
