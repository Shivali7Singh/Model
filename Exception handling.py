#Predict the output:
try:
    print("Befor error")
    print(5/0)
except:
    print("Something went wrong")

#Find and coorect the error:
try:
    print("Hello")
except:
    print("Error")
#Predict the output:
try:
    num=int("10a")
except ValueError:
    print("ValueError occurred")
finally:
    print("End of program")
    
#What will be printed:
try:
    a=[10,20,30]
    print(a[3])
except IndexError:
    print("Index out of range!")
else:
    print("All good!")
finally:
    print("Program completed")


#Find and explain the mistek:
try:
    age=int(input("Enter age:"))
    if age<18:
        raise"Too young!"
except:
    print("Error handled.")

def main():
    try:
      print("1.Addition")
      print("2.subtrection")
      print("3.multiply")
      print("4.division")
      choice=int(input("enter your choice(1/2/3/4):"))
      x=int(input("enter number1:"))
      y=int(input("enter number2:"))
      if choice==1:
          result1= x+y
          print(result1)
      elif choice==2:
         result2= x-y
         print(result2)
      elif choice==3:
         result3=x*y
         print(result3)
      elif choice==4:
         if y!=0:
          return x/y
      else:
        print("can't divide")
    except ZeroDivisionError:
        print("can't divide by 0")
    except ValueError:
       print("enter valid number:")
    else:
        print("Number are:",x,y) 
    finally:
      print("Calculate created!")
if __name__=="__main__":
      main()
