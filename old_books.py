searching_book = input()
command = input()
counter = 0
isFound = False

while command != "No More Books":
    if searching_book == command:
        isFound = True
        break
    else:
        command = input()
        counter += 1
if isFound:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
