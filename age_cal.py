import time
#taking the birth date 
timestampt = time.strftime('%d/%m/%Y')
dayg = int(input("Enter your birth day :")) 
monthg = int(input("Enter your birth month in decimal :"))
yearg = int(input("Enter your birth year :"))

#stating the birth date 
dayt = int(time.strftime('%d')) 
montht = int(time.strftime('%m'))
yeart = int(time.strftime('%Y'))


if(dayt < dayg):      #math of birth day
    dayt = dayt + 30
    montht = montht - 1 
    aged = (dayt-dayg)
else:
    aged = (dayt-dayg)



if(montht < monthg):  #math of birth month 
    montht = montht + 12
    yeart = yeart - 1
    agem =(montht - monthg)
else :
    agem = (montht-monthg)


agey = (yeart-yearg)   #math of birth year

print("Your age is :" + str(agey) + "years" + " " + str(agem) + "months"+ " " + str(aged) +  "days")

if(agey>=18):
    print("\"You are an adult\"")

else: 
    print("You are not an adult")




