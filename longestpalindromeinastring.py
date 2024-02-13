# n = input("Enter a string: ")
# needle = input("Enter the word to search for: ")
# count = 0

# for word in n.split():
#     if word != needle:
#         count += 1

# if needle in n:
    
#     print(needle)
# print(count)
n = input("Enter a string: ")
needle = input("Enter the word to search for: ")

index = n.find(needle)

if index != -1:
    print(f"The word '{needle}' is found at index: {index}")
else:
    print(f"The word '{needle}' is not found in the string.")
