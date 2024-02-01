#make the part of choicess
#the chociess is 
#1-the book of plane
#2-the search of air plane
#3-packup of ticket
#4- exist the application
#create the book func
import random
def info (x):
    global credit_num
    global your_name
    global num_trip
    while True:
                 
                  
     credit_num=int(input("please enter your credit card number: "))
     your_name=input("please enter your name: ").strip().lower()
     num_trip=random.randrange(15984856)
     print(f"""the booking is done the trip date is '2024:10:{random.randrange(1,31)}'
*trip information is:
        -your name is:{your_name}
        -the number of trip:{num_trip}
        -the price is:{x}
        -your credit card number is:{credit_num}
         (you must save this information)""" )
     break
                 
                    
def book():
    
    while True:
        to_country=input("please enter the country the plane over:").strip()
        from_country=input("please enter the country that plane fly from here:").strip()
        print(f"\n[your fly is been from '{from_country}' to '{to_country}']\n")
        certian=input("if you want to continue please enter '1'\nif you want to back the choice any number except '1': ").strip()
        if certian=="1":
            break
    while True:
        the_class=input("""
                    1-the first class booking
                    2-the second class booking
                    3-the third class booking
                    4-information for each class:
                    please enter the number: """).strip()
        if the_class=="1":
            price=random.randrange(2000,3001)
            rank_class=input(f"""wlcome to the first class the cost of plane is {price}$
                          if you want to continue please enter '1' if you want rechoice enter any number except '1': """).strip()
            if rank_class=="1":
                info(price)
                
        elif the_class=="2":
            price=random.randrange(1200,1501)
            rank_class=input(f"""wlcome to the secound class the cost of plane is {price}$
                          if you want to continue please enter '1' if you want rechoice enter any number except '1': """).strip()
            if rank_class=="1":
                info(price)
        elif the_class=="3":
            price=random.randrange(800,1001)
            rank_class=input(f"""wlcome to the third class the cost of plane is {price}$
                          if you want to continue please enter '1' if you want rechoice enter any number except '1': """).strip()
            if rank_class=="1":
                info(price)
        elif the_class=="4":
            print("""&&&&&&&&&&information&&&&&&&&&""")
        else:
            print("please enter the correct choice")
        


    
        

print("welcome to the our application")
while True:
    print("""\t  1-the book of plane
          2-the search of air plane
          3-packup of ticket
          4-exist the application""" )
    the_choice=input("please enter the number:").strip()
    if the_choice=="1":
            book()
    elif the_choice=="2":
        def search():
            pass
    elif the_choice=="3":
        def packup():
            pass
    elif the_choice=="4":
        break
    else:
        print("please enter the correct choices")