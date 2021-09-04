class validator:

    
    def hasCorrectNumberofDigits(strNumber):
        if len(strNumber) < 5 and len(strNumber) > 0:
            return True
        else:
            return False
            
    def hasCorrectNumberOfParameters(parameters):
        if len(parameters) > 5:
            return False
        else:
            return True
        
    def hasCorrectOperation(operation):
        if operation == '+' or operation == '-':
            return True
        else:
            return False
        
    def parametersAreValid(parameters):
        if validator.hasCorrectNumberOfParameters(parameters):
            return True
        
    def hasCorrectOperation(operator):
        if operator == '+' or operator == '-':
            return True
        else:
            return False
        
    def problemIsValid(problem):
        problemValues = problem.split()
        if validator.hasCorrectNumberofDigits(problemValues[0]) and problemValues[0].isdigit() \
            and validator.hasCorrectNumberofDigits(problemValues[1]) and problemValues[1].isdigit() \
                and validator.hasCorrectOperation(problemValues[2]):
                return True
        else: 
            return False
            
