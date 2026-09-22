print("\nWelcome to The Data Analyser and Transformer Program")
print()

Data = []
    
def input_Data ():
    global Data 
    arr=input("Enter Data for a 1D array (Separated By Spaces) :- ")

    for i in arr.split():
        Data.append(i)
        Data = list(map(int,arr.split()))
    print("Data has been stored Successfully !")
    print()

    
def Data_summary():
    total =sum(Data)
    lenth =len(Data)
    print("Data Summary : ")
    print(f"- Total Elements : {len(Data)}")
    print(f"- Minimum Value  : {min(Data)}")
    print(f"- Maximum Value  : {max(Data)}")
    print(f"- Sum of all values: {sum(Data)}") 
    print(f"- Average Value  : {total/lenth:.2f}")
    print()

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
 

def Filter_Data ():

    value = int(input("Enter a threshold value:- "))
    a = filter(lambda x: x > value, Data )
    print(*a, sep=", ")
 
def sort_Data ():
    while True :

        print("1. Ascending.")
        print("2. Descending.")

        ch = int(input("Enter Your Choice:-"))
        if ch == 1 :
            print("Sorted Data in Ascending order:")
            Data .sort()
            print(Data )
            break
            
        elif ch == 2 :
            print("Sorted Data in descending order:")
            Data.sort()
            Data.reverse()
            print(Data)
            break
 

def Data_statistics():
    total = sum(Data)
    minimum = min(Data)
    maximum = max(Data)
    average = total / len(Data)

    return  minimum, maximum,  total, average
 
while True:
    print("Main Menu: ")
    print("1. Input Data  ")
    print("2. Data Summary (Built-in-Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda Function)")
    print("5. Sort Data ")
    print("6. Display Data Set Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()


    choice=int(input("Please Enter Your Choice :- "))
    print()

    if choice == 1 :
        input_Data()

    elif choice == 2 :
        Data_summary()

    elif choice == 3 :
        n = int(input("Enter a number to calculate its factorial :-"))
        result = factorial(n)
        print(f"Factorial of {n} is :", result)

    elif choice == 4 :
        Filter_Data()

    elif choice == 5 :
        sort_Data()

    elif choice == 6 :
        
        total, minimum, maximum, average = Data_statistics()

        print("Dataset Statistics:")
        print("Minimum value :", minimum)
        print("Maximum value :", maximum)
        print("Sum of all value :", total)
        print("Average value :", average)


    elif choice == 7 :
        print("Thank you for using The Data Analyser and Transformer Program. GoodBye!")
        break
    else:
        print("Enter Valid choice !")