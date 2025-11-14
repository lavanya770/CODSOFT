print("SIMPLE CALCULATOR")
num1=int(input("Enter first number:"))
operator=(input("Enter operation (+,-,*,/,%):"))
num2=int(input("Enter second number:"))
if operator=="+":
  result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
      result=num1*num2
elif operator=="/":
        result=num1/num2
elif operator=="%":
    result=num1%num2
else:
  result="Invalid Operator"
print("Result:", result)
  

