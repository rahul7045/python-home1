itemn=raw_input("enter the iten name : ")
itemq=int(raw_input("eneter the item quantity : "))
itemp=int(raw_input("enter the item price : "))
total=itemq*itemp
print("--------BILL--------")
print(format('Item name','>50'),format('Item quantity','^50'),format('Item Price','<50'))
print(format(itemn,'>50'),format(itemq,'^50'),format(itemp,'<50'))
print("*******************")
print(total)






