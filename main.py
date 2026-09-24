print("Welcome to The Data Analyzer and Transformer Program")
print()

Data = []

def input_Data():
    """Take 1D or 2D array data from the user and store it."""
    global Data

    print("1. 1D Array")
    print("2. 2D Array")

    choice = int(input("Enter your Choice:-"))

    if choice == 1:
        arr = input("Enter Data for a 1D array (Separated By Spaces) :- ")

        for i in arr.split():
            Data.append(i)
            Data = list(map(int, arr.split()))

        print("Data has been stored Successfully!")
        print()

    elif choice == 2:
        row = int(input("Enter Number of Rows :- "))
        column = int(input("Enter Number of Columns :- "))

        for i in range(row):
            l = []
            for j in range(column):
                value = int(input("Enter Number Value :- "))
                l.append(value)

            Data.append(l)

        print("Data has been stored Successfully!")
        print("2D Data:", Data)
        print()

    else:
        print("Enter Valid Choice!")


def Data_summary():
    """Display summary information of the stored dataset."""

    print("1. 1D Array")
    print("2. 2D Array")
    ch = int(input("Enter Choice :- "))

    if ch == 1:

        print("Data Summary:")
        print(f"- Total Elements   : {len(Data)}")
        print(f"- Minimum Value    : {min(Data)}")
        print(f"- Maximum Value    : {max(Data)}")
        print(f"- Sum of all values: {sum(Data)}")
        print(f"- Average Value    : {sum(Data) / len(Data):.2f}")
        print()

    elif ch == 2:
        value = []
        for x in Data:
            for i in x:
                value.append(i)

        print("Data Summary For 2D:")
        print(f"- Total Elements   : {len(value)}")
        print(f"- Minimum Value    : {min(value)}")
        print(f"- Maximum Value    : {max(value)}")
        print(f"- Sum of all values: {sum(value)}")
        print(f"- Average Value    : {sum(value) / len(value):.2f}")
        print()

    else:
        print("Enter Valid Choice!")


def factorial(n):
    """Calculate the factorial of a number using recursion."""

    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def Filter_Data():
    """Filter and display values greater than the threshold."""

    print("1. 1D Array")
    print("2. 2D Array")
    choice = int(input("Enter Choice:-"))

    if choice == 1:
        value = int(input("Enter a threshold value:- "))
        a = filter(lambda x: x > value, Data)
        print(*a, sep=", ")

    elif choice == 2:

        value = int(input("Enter a threshold value:- "))
        result = []
        for row in Data:
            for x in row:
                if x > value:
                    result.append(x)
        print(*result, sep=", ")

    else:
        print("Enter Valid Choice!")


def sort_Data():
    """Sort the dataset in ascending or descending order."""

    print("1. 1D Array")
    print("2. 2D Array")
    choice = int(input("Enter Choice:-"))

    if choice == 1:

        print("1. Ascending")
        print("2. Descending")
        ch = int(input("Enter Your Choice:-"))

        if ch == 1:
            print("Sorted Data in Ascending order:")
            Data.sort()
            print(Data)

        elif ch == 2:
            print("Sorted Data in Descending order:")
            Data.sort()
            Data.reverse()
            print(Data)

        else:
            print("Enter Valid Choice!")

    elif choice == 2:
        value = []
        for x in Data:
            for i in x:
                value.append(i)

        print("1. Ascending")
        print("2. Descending")
        ch = int(input("Enter Your Choice:-"))

        if ch == 1:
            print("Sorted 2D Data in Ascending order:")
            value.sort()
            print(value)

        elif ch == 2:
            print("Sorted 2D Data in Descending order:")
            value.sort()
            value.reverse()
            print(value)

        else:
            print("Enter Valid Choice!")

    else:
        print("Enter Valid Choice!")


def Data_statistics():
    """Return multiple statistical values."""

    print("1. 1D Array")
    print("2. 2D Array")
    choice = int(input("Enter Choice:-"))

    if choice == 1:

        total = sum(Data)
        minimum = min(Data)
        maximum = max(Data)
        average = total / len(Data)

        return minimum, maximum, total, average

    elif choice == 2:

        value = []
        for i in Data:
            for j in i:
                value.append(j)

        total = sum(value)
        minimum = min(value)
        maximum = max(value)
        average = total / len(value)

        return minimum, maximum, total, average

    else:
        print("Enter Valid Choice!")

while True:

    print()
    print("Main Menu:")
    print("1. Input Data")
    print("2. Data Summary (Built-in-Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Data Set Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()

    choice = int(input("Please Enter Your Choice :- "))
    print()

    if choice == 1:
        input_Data()

    elif choice == 2:
        Data_summary()

    elif choice == 3:
        n = int(input("Enter a number to calculate its factorial :- "))
        result = factorial(n)
        print(f"Factorial of {n} is:", result)

    elif choice == 4:
        Filter_Data()

    elif choice == 5:
        sort_Data()

    elif choice == 6:
        minimum, maximum, total, average = Data_statistics()

        print("Dataset Statistics:")
        print(f"- Minimum Value  : {minimum}")
        print(f"- Maximum Value  : {maximum}")
        print(f"- Sum of all values: {total}")
        print(f"- Average Value  : {average:.2f}")

    elif choice == 7:
        print("Thank you for using The Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Enter Valid Choice!")