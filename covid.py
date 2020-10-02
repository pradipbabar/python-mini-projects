import random

print(" hello! , my name is Pradip Babar and i am a NCC officer")
print("today i will check whether you are having COVID 19 symbtoms or not")
print("so please answer my questions honestly")
print("so first tell me your name")
name = input()

print(f"{name} that is a nice name 😘 \n")
print("so without wasting time lets check you")

print("are you suffering from dry cough problem?")
ans = input()
if ans == 'yes':
  print("ohh")
elif ans != 'yes':
  print("okk")
  
print("are you suffering from high fever?")
ans = input()
if ans == 'yes':
  print("ohh🤔")
elif ans != 'yes':
  print("okk😊")
  
print("are you having running nose")
ans = input()
if ans == 'yes':
  print("ohh🤔")
elif ans != 'yes':
  print("okk😊")
  
print("are you feeling weakness or tiredness?")
ans = input()
if ans == 'yes':
  print("ohh🤔")
elif ans != 'yes':
  print("okk😊")

cough = str(input("\nSo,Do you feel dry cough?(y/n)\n - "))
fever = str(input("\nDo you have fever?(y/n)\n - "))
tired = str(input("\nDo you feel tiredness at all?(y/n)\n - "))
breath = str(input("\nDo you have difficulty in breathing?(y/n)\n - "))

if cough=="y" and fever=="y" and tired=="y" and breath=="y":
  print("\nhmm.. Don't engage with people.. Contact your doctor.. \nplease call _ 011-23978046 \nAnd follow some steps to avoid spreading it.")
elif cough=="n" and fever=="n" and tired=="n" and breath=="n":
    print(" \nPick up a pillow and jump to bed 🛌\n    No one is gonna harm you😅.")
else:
  print("\n          Ok, don't worry it's normal")
  
# if all the questions gives the answer ohh then you must concern to you doctor.
# if all the questions gives the answer okk then you dont need to worry.