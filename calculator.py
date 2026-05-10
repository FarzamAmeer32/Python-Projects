def calculator(num1,num2,operand):
  try:
    if operand=='+':
      return num1+num2
    elif operand=='-':
      return num1-num2
    elif operand=='*':
      return num1*num2
    elif operand=='/':
      return num1/num2
    elif operand=='//':
      return num1//num2
    elif operand=='**':
      return num1**num2
    elif operand=='%':
      return num1%num2
    else:
      return 'Incorrect operand'
  except Exception as e:
    return f'Error Occured {e}'

def make_calculation():
  while True:
    try:
      num1=float(input('Enter first number: '))
      num2=float(input('Enter second number: '))
      operand=input('Enter operand: (+,-,*,/,//,**,%) ')
    except ValueError:
      print('Invalid Input')
      continue #skip current iteration
    except Exception as e:
      print(f'Error Occured {e}')
      continue

    result=calculator(num1,num2,operand)

    print(f' The Result is {result}')

    choice=input('Do you want to contine Yes/No?')
    if choice.lower()=='no':
      break


