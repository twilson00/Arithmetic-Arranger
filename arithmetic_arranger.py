from validator import *
from print_formatter import *

def arithmetic_arranger(problems, displayAnswers = False):

  formatter = PrintFormatter()

  if not validator.hasCorrectNumberOfParameters(problems):
    return "Error: Too many problems."

  for problem in problems:

    try:
      problemValues = problem.split()
      
      if not validator.hasCorrectNumberofDigits(problemValues[0]) or not validator.hasCorrectNumberofDigits(problemValues[2]):
        return "Error: Numbers cannot be more than four digits."
      
      if not problemValues[0].isdigit() or not problemValues[2].isdigit():
        return "Error: Numbers must only contain digits."
    
      if not validator.hasCorrectOperation(problemValues[1]):
        return "Error: Operator must be '+' or '-'."
      else:
        answer = getAnswer(problemValues[0], problemValues[2], problemValues[1])

      longestOperandLength = len(str(problemValues[0])) if len(str(problemValues[0])) > len(str(problemValues[2])) else len(str(problemValues[2]))
      numberOfDashes = longestOperandLength + 2
      
      topOperand = formatter.formatTopOperand(problemValues[0], problemValues[2], longestOperandLength, numberOfDashes)
      bottomOperand = formatter.formatBottomOperand(problemValues[0], problemValues[2], longestOperandLength)
      
      formatter.addToTopLine(topOperand)
      formatter.addToOperatorLine(bottomOperand, problemValues[1])
      formatter.addToDividerLine(numberOfDashes)
      
      if(displayAnswers):
        numberOfDashes = (longestOperandLength + 2) - len(str(answer))
        formatter.addToAnswerLine((" " * numberOfDashes) + str(answer))

    except(Exception) as e:
      print(e)
          
  return formatter.formatProblems()

def getAnswer(firstOperand, secondOperand, operator):
  if operator == '+':
    return int(firstOperand) + int(secondOperand) 
  else:
    return int(firstOperand) - int(secondOperand)