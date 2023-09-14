pkt = int(input("Pocket Number: "))
if pkt == 0:
   print("Green")
elif pkt >= 1 and pkt <=10:
   if pkt%2 == 0:
       print("Black")
   else:
       print("Red")
elif pkt >= 11 and pkt <=18:
   if pkt%2 == 0:
       print("Red")
   else:
       print("Black")
elif pkt >= 19 and pkt <=28:
   if pkt%2 == 0:
       print("Black")
   else:
       print("Red")
elif pkt >= 29 and pkt <=36:
   if pkt%2 == 0:
       print("Red")
   else:
       print("Black")
else:
   print("Error")
