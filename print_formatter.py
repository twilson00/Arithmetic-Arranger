class PrintFormatter:

    def __init__(self):
        self.__topLine = ""
        self.__operatorLine = ""
        self.__dividerLine = ""
        self.__answerLine = ""
    
    def addToTopLine(self, operand):
        if(self.__topLine == ""):
            self.__topLine += operand
        else:
            self.__topLine += f"    {operand}"
    
    def addToOperatorLine(self, operand, operator):
        if(self.__operatorLine == ""):
            self.__operatorLine += f"{operator} {operand}"
        else:
            self.__operatorLine += f"    {operator} {operand}"
     
    def addToDividerLine(self, numberOfDashes):
        dashes = "-" * numberOfDashes
        if(self.__dividerLine == ""):
            self.__dividerLine += dashes
        else:
            self.__dividerLine += f"    {dashes}"
      
    def addToAnswerLine(self, answer):
        if(self.__answerLine == ""):
            self.__answerLine += answer
        else:
            self.__answerLine += f"    {answer}"  
            
    #If top operand is the longest, add spaces to line up the shorter bottom operand
    #Only needs longest operand to format spaces since the operator will also be adding a space after 
    def formatBottomOperand(self, topOperand, bottomOperand, longestOperandLength):
        if len(str(topOperand)) == longestOperandLength:
            numberOfSpacesToAdd = longestOperandLength - len(str(bottomOperand)) 
            bottomOperand = (" " * numberOfSpacesToAdd) + bottomOperand   
        return bottomOperand

    #If bottom operand is the longest, add spaces to line up the shorter top operand  
    #Uses numberOfDashes minus the top operand to line up with the bottom operand and the operator  
    def formatTopOperand(self, topOperand, bottomOperand, longestOperandLength, numberOfDashes):
        if len(str(bottomOperand)) == longestOperandLength:
            numberOfSpacesToAdd = numberOfDashes - len(str(topOperand))
            topOperand = (" " * numberOfSpacesToAdd) + topOperand
        else:
            #Add two spaces to right align with operator 
            topOperand = (" " * 2) + topOperand
        return topOperand
        
    def formatProblems(self):
        return(f'{self.__topLine}\n{self.__operatorLine}\n{self.__dividerLine}\n{self.__answerLine}'.rstrip())