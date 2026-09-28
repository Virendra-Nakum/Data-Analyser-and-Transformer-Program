print("welcome to the data analayzer and transformer program! ")
data=[]
def input_data():
    """Take 1D array input from the user and store the data."""
    global data 
    print("Select option :")
    print("1. Input data for 1D array")
    print("2. Input data for 2D array")
    choice = int(input("Enter your choice: ")) 
    if choice == 1:
        values=input("enter data for a 1D array (separated by spaces)\n")
        data =list(map(int,values.split()))
        print("Data has been stored successfully")

    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        data = []

        for row in range(rows):
            row = []
            for col in range(cols):
                value = int(input("Enter value: "))
                row.append(value)
            data.extend(row)

        print("2D array stored successfully!")
 
def display_summary():
        """Display basic summary of the dataset using built-in functions."""
    
        print("\nData Summary")
        print(f"- Total Element :- {len(data)}")
        print(f"- Minimum Value :- {min(data)}")
        print(f"- Maximum Value :- {max(data)}")
        print(f"- Sum Of All Element :- {sum(data)}")
        print(f"- Average Value :- {sum(data) / len(data)}")

def fact(num):
    """Calculate factorial of a number using recursion."""
    if num <=1:
         return 1
    else:
         return num*fact(num-1)


def filter_data():
    """Filter data based on a threshold value using a lambda function."""
    if len(data) == 0:
        print("No data found!")
        return 
    
    threshold = int(input("Enter a threshold value to filer out the data: "))
    fil_data = list((filter(lambda i: i >=threshold,data)))
    print(f"Filtered Data (values >= {threshold}): {fil_data}")


def sort_data():
    """Sort the data in ascending or descending order based on user choice."""
    if data is None:
            print("Please input data first!")
            return
    
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        sorted_data = sorted(data)
    
        print("\nSorted Data in Ascending Order:")
        print(sorted_data)
    
    elif choice == 2:
        sorted_data = sorted(data, reverse=True)
    
        print("\nSorted Data in Descending Order:")
        print(sorted_data)
    
    else:
        print("Invalid sorting choice!")
    
def dataset_statistics(data):
    """Return minimum, maximum, sum and average as multiple values."""
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)
    return minimum, maximum, total, average

def display_dataset_statistics():
    """Display dataset statistics using the dataset_statistics function."""
    if len(data) == 0:
        print("No data found!")
        return
    
    minimum, maximum, total, average = dataset_statistics(data)
    
    print("\nDataset Statistics:")
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Sum of Values:", total)
    print("Average Value:", round(average, 2))

while True :
    print("\nSelect option :")
    print("1.Input data")
    print("2.Display data summary")
    print("3.Calculate factorial")
    print("4.Filter data by Threshold (Lambda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics (Return Multiple Values)")
    print("7.Exit")

    choice=int(input("enter your choicee :"))

    if choice == 1 :
        print(input_data.__doc__)
        input_data()

    elif choice == 2:
         print(display_summary.__doc__)
         display_summary()

    elif choice== 3:
        print(fact.__doc__)
        num = int(input("Enter a number: "))
        if num <0:
            print("Factorial is not possible!")

        else:
            result = fact(num)
            print(f"Factorial of {num} is: {result}")

    elif choice == 4:
         print(filter_data.__doc__)
         filter_data()

    elif choice == 5:
        print(sort_data.__doc__)
        sort_data()

    elif choice == 6:
        print(display_dataset_statistics.__doc__)
        display_dataset_statistics()
        
    elif choice == 7 :
        print("Exiting!\nThank You For Using Data Analyzer And Transformer Program")
        break
         
    else : 
        print("Invalid Choice")
