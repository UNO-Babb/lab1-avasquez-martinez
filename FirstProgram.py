#FirstProgram.py
#Name:
#Date:
#Assignment:

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name 
name=input("enter your name:")
  #Use the user's name in the program.
print("nice to meet you", name)
  #Ask the user for their age.
age=input("enter your age")
age=int(age)
  #Tell the user what year they were born in.
born=2024 - age 
  #Assume that they have not had their birthday yet this year.
print("you were born in", born)
#Call the main function if this is the file being run.
if __name__ == '__main__':      
    main()
