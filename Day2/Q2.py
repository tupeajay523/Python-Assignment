# Q2. Python program to take user input to add multiple elements to an array, then print the final array

arr = []


num_ele = int(input("How many elements do you want to add to the array? ")) # Quantity


for _ in range(num_ele):
    ele = int(input("Enter a number to add to the array: "))
    arr.append(ele)

print("Final array:", arr) 
