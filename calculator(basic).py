#Functions for arithmetic operations-----------------------------------------
def add(num1,num2):
    return num1 + num2
    
def subtract(num1,num2):
    return num1 - num2
    
def multiply(num1,num2):
    return num1 * num2
    
def divide(num1,num2):
        return num1 / num2
        
def power(num1,num2):
    return num1 ** num2
    
def remainder(num1,num2):
    return num1 % num2
#----------------------------------------------------------------------------

def msg_add(num1,num2):
    return print(num1,"+",num2,"=",add(num1,num2))
    
def msg_subtract(num1,num2):
    return print(num1,"-",num2,"=",subtract(num1,num2))
    
def msg_multiply(num1,num2):
    return print(num1,"*",num2,"=",multiply(num1,num2))
    
def msg_divide(num1,num2):
    if num2 != 0:
        return print(num1,"/",num2,"=",divide(num1,num2))
    else:
        return "Something went wrong!"
    
def msg_power(num1,num2):
    return print(num1,"*",num2,"=",power(num1,num2))
    
def msg_remainder(num1,num2):
    return print(num1,"%",num2,"=",remainder(num1,num2))

#----------------------------------------------------------
#TODO: Write the select_op(choice) function here

def select_op(choice,num1,num2):
            if choice == "+":
                return msg_add(num1,num2)
            elif choice == "-":
                return msg_subtract(num1,num2)
            elif choice == "*":
                return msg_multiply(num1,num2)
            elif choice == "/":
                return msg_divide(num1,num2)
            elif choice == "^":
                return msg_power(num1,num2)
            elif choice == "%":
                return msg_remainder(num1,num2)
         

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)  
  if choice == "#":
    #program ends here
    print("Done. Terminating")
    exit()
  elif choice == "$":
      continue  
  elif choice not in ("+","-","*","/","^","%"):
      print("Unrecognized Operation")
  else:
      try:
            while True:
                 num1 = input("Enter First Number: ")
                 if "$" not in num1:
                     num1 = float(num1)
                     break
                 
            while True:        
                 num2 = input("Enter Second Number: ")
                 if "$" not in num2:
                     num2 = float(num2)
                     break
            
            print(select_op(choice,num1,num2))
      except:
            print("Not a valid number,please enter again")

            