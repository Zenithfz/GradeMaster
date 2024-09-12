# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: 20211594

# Date:13/12/2022

#REFERENCES
#https://www.codegrepper.com/code-examples/python/python+save+input+to+text+file
#https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python
#https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
#https://www.w3schools.com/python/python_variables_global.asp
#https://www.datacamp.com/community/tutorials/functions-python
#https://peps.python.org/pep-0498/

# Global variables
passCredits = 0
deferCredits = 0
failCredits = 0
creditsSum = 0
noErr = True
progressOutcome = ""
contStatus = 'y'
invalidStatus = True
countProgress = 0
countTrailer = 0
countRetriever = 0
countExclude = 0
listProgress = []
listTrailer = []
listRetriever = []
listExclude = []

print("\n\\\\\\University Progression Outcome At The End Of 2022\\\\\\\n\n")
# Function to calculate and return credits total
def return_credits_total(c_pass,c_defer,c_fail):
    c_total = c_pass + c_defer + c_fail
    return c_total

# Function to return the progression outcome based on the table defined by the University
def return_progression_outcome(c_pass,c_defer,c_fail):
    global countProgress
    global countTrailer
    global countRetriever
    global countExclude
    cList = [c_pass,c_defer,c_fail]
    if c_pass == 120:
        countProgress += 1
        listProgress.append(cList)
        return "Progress"
    if c_pass == 100 and (c_defer == 20 or c_fail == 20):
        countTrailer += 1
        listTrailer.append(cList)
        return "Progress (moduler trailer)"
    if c_pass == 80 or c_pass == 60 or (c_pass == 40 and c_defer != 0) or ((c_pass == 20 or c_pass == 0) and c_fail < 80):
        countRetriever += 1
        listRetriever.append(cList)
        return "Do not Progress - moduler retriever"
    if c_fail >= 80:
        countExclude += 1
        listExclude.append(cList)
        return "Exclude"
#Function to return the continue status,allowing the program to use multiple times until the user enters quit
def return_continue_status():
    print("Would you like to enter another set of data?\n")
    print("Enter 'y' for yes or 'q' to quit and view results:")
    cStatus = ''
    return input(cStatus)

#Function to display the horizontal histrogram after quiting the program
def display_horizontal_histogram():
    totalStudents = 0
    print("-"*90)
    print("\nHorizontal Histrogram\n")
    print("Progress " + str(countProgress) + " : " + '*'*countProgress)
    print("Trailer " + str(countTrailer) + " : " + '*'*countTrailer)
    print("Retriever "+ str(countRetriever) + " : "+ '*'*countRetriever)
    print("Excluded " + str(countExclude) + " : "+ '*'*countExclude)
    totalStudents = countProgress + countTrailer + countRetriever + countExclude
    print( totalStudents , " outcomes in total.")
    
#Function to display the stored credit data from the list 
def display_credits_list():
    print("-"*90)
    print("\nDisplay data from the list\n")      
    for item in listProgress:
        strItem = [str(i) for i in item]
        print("Progress  - ",', '.join(strItem), end = '\n')
    for item in listTrailer:
        strItem = [str(i) for i in item]
        print("Progress (module trailer)   - ",', '.join(strItem), end = '\n')
    for item in listRetriever:
        strItem = [str(i) for i in item]
        print("Module retriever - ",', '.join(strItem), end = '\n')
    for item in listExclude:
        strItem = [str(i) for i in item]
        print("Exclude   - ",', '.join(strItem), end = '\n') 
#Function to write the stored progression data to a text file
def write_progression_data():
    with open('prog_summary.txt', 'w') as f:
         for items in listProgress:
             f.write("\nProgress  - " +', '.join(map(str, items)))
         for items in listTrailer:
             f.write("\nProgress (module trailer)   - " +', '.join(map(str, items)))
         for items in listRetriever:
             f.write("\nModule retriever    - " +', '.join(map(str, items)))
         for items in listExclude:
             f.write("\nExclude   - "+ ', '.join(map(str,items)))     
    f.close()

#Function to read and print the progression data
def read_file_print():
    print("-"*90)
    print("\nDisplay the data read from the text file\n")      
    print(open('prog_summary.txt', 'r').read())    
#The main program
while contStatus == 'y':
    noErr = True
    while noErr and contStatus == 'y':
        try:
            passCredits = int(input("Please enter your credits at Pass: "))
            if passCredits not in range(0,140,20):
                print("out of range")
                noErr = False
                break
            deferCredits = int(input("Please enter your credits at Defer: "))
            if deferCredits not in range(0,140,20):
                print("out of range")
                noErr = False
                break
            failCredits = int(input("Please enter your credits at Fail: "))
            if failCredits not in range(0,140,20):
                print("out of range")
                noErr = False                
                break
        except:
            print("integer required")
            noErr = False
            break
        if return_credits_total(passCredits, deferCredits,failCredits) != 120:
            print("Total incorrect.")
            noErr = False
            break
        print (return_progression_outcome(passCredits, deferCredits,failCredits))
        invalidStatus = True
        while invalidStatus:
            contStatus = return_continue_status()
            if contStatus not in ['y', 'q']:
                print("Invalid input\n\n")
            else:
                invalidStatus = False
        if contStatus == 'q':
            display_horizontal_histogram()
            display_credits_list()
            write_progression_data()
            read_file_print()
    
        
              








         
       
            
    
   
