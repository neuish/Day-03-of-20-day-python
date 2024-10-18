# 1. Print all even numbers from 1 to 100 using a loop.
def even_numbers():
    print("Even numbers from 1 to 100:")
    for x in range(1, 101):
        if x % 2 == 0:
            print(x)

# 2. Write a program that asks the user for a number and prints its factorial.
def factorial():
    num = int(input('Enter the number you wish to factorial: '))
    result = 1
    
    for x in range(1, num + 1):
        result *= x
    print(f'The result of the factorial is: {result}') 

# 3. Generate and print the first n Fibonacci numbers.
def fibonacci():
    num1 = 0
    num2 = 1

    num = int(input('Enter the number of Fibonacci terms you want: '))
    print('The Fibonacci series is:', end=' ')

    for _ in range(num):  # Use num to determine how many terms to print
        print(num1, end=' ')
        num1, num2 = num2, num1 + num2
    print()  # Print a newline at the end

# 4. Create a program that finds the largest number in a list.
def largest():
    numlist = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if len(numlist) == 0:
        print('The list is empty.')
    else: 
        largest_num = numlist[0]  # Initialize the largest number

        for x in numlist:
            if x > largest_num:
                largest_num = x  # Update the largest number

        print('The largest number is:', largest_num)

# 5. Create a program that calculates the sum of all numbers from 1 to a user-provided number.
def sum_numbers():
    num = int(input('Enter the number you wish to sum up to: '))
    total_sum = sum(range(1, num + 1))  # Use built-in sum function for simplicity
    print('The sum of numbers from 1 to', num, 'is:', total_sum)

def main_menu():
    while True:
        print('\n...main menu...')
        print('1. Even numbers')
        print('2. Factorial number')
        print('3. Fibonacci series')
        print('4. Largest number')
        print('5. Sum of numbers')
        print('0. Exit')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            even_numbers()
        
        elif choice == '2':
            factorial()  

        elif choice == '3':
            fibonacci()   

        elif choice == '4':
            largest()   
        
        elif choice == '5':
            sum_numbers()

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Start the program
main_menu()
