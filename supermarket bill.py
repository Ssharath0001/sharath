
print("welcome to sharath super market")
name=input("enter the name:")
list='''
oil      Rs:100/ltr
sugar    Rs:25/kg
biscuit  Rs:10/pack
tomato   Rs:10/kg
boost    Rs:13/pac
magie    Rs:10/pac
soap     Rs:15/item
kurkure  Rs:10/packet
'''
#declaration
price=0
ilist=[]
plist=[]
qlist=[]
pricelist=[]
intialprice=0
totalprice=0

items={'oil':100,'sugar':25,'biscuit':10,'boost':13,'tomato':10,'magie':10,'kurkure':10,'soap':15}


while True:
    option=input("enter 1 is continue the shoping.2 is exit the shoping: ")
 
    if option=='2':
        print("thank you for visiting super market")
        break
    elif option=='1':
        print(list)
        while True:
            input1=input("enter 1 is continue the shoping.2 is exit the shoping:")
            if input1=='2':
                print("thank you for visiting")
                break
            elif input1=='1':
                item=input("enter the item:")
                while True:
                    quantityinput=input("enter the quatity:")
                
                    if quantityinput.isdigit():
                        quantity = int(quantityinput)
                        break
                    else:
                        print("in valid digit")
                          
                if item in items:
                    price= quantity *items[item]
                    pricelist.append((item,quantity,items[item],price))
                    totalprice+=price  
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                    
                else:
                    print("this item is not available ")
        if totalprice>0:
            tax=(totalprice *12)/100
            finalamount=totalprice-tax


            print(25*"=","sharath supermarket",25*"=")
            print(28*"=","hyderabad",28*"=")
            print(" customar name",name,30*" ")
            print(75*"-")
            print("sno",10 * " ", 'item', 8 * " ", 'quantity',8 * " ",'price',8 * " ")
            for i in range(len(pricelist)):
                print(i,10*" ",ilist[i],10*" ",qlist[i],10*" ",plist[i],15*" ")
            print(75*"-")
            print(55*" ","total amount",totalprice)
            print(55*" ","  gst tax  12%",tax)
            print(75*"-")
            print(55*" ","final amount",finalamount)
            print(75*"-")
            print(20*" ","thankyou & visit again")
            print(75*"-")
            break

    

            
        




