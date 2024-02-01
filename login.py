# play list to show user what he is do
#user enter user name and password to log in
#when is't enter a correct user and password he is cant log in
#func to log in
def log_in(user_name,password):
 try:
  if user_name==user_name_1 and password==password_1:
   print("log in is correct")
  else:
   print("log in is not correct \nplease try again")
 except:
   print("there aren't account with his name")
def sign_up():
 print("sign in is done")
def forget_password():
  check=input("please enter your mobile phone:\n")
  global user_name_1
  global password_1
  if check==forget_pass:
    user_name_1=input("please enter a new user name:\n")
    password_1=input("please enter your new password:\n")
    print("the edit is done")

   
while True:
  print("""welcome to the program
      1-log in
      2-sign up
      3-forget password
      4-exit """)
  choice=input("please enter a choice: ").strip()
  if choice=="1":
    user_name=input("please enter your user name:\n").strip()
    password=input("please enter your password:\n").strip()
    log_in(user_name,password)
  if choice=="2":
    user_name_1=input("please enter your user name:\n").strip()
    password_1=input("please enter your password:\n").strip()
    forget_pass=input("please ener your mobile phone because if you forget your password:\n").strip()
    sign_up()
  if choice=="3":
    forget_password()
  if choice=="4":
    break
print("end ,bye bye")

    
