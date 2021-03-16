string = input("Enter text: ")

#replacing chars

charList = list(string)

for index in range(len(charList)):
    
    char = charList[index].lower()
    
    if char == "l":
        
        print("L -> 1")
        charList[index] = "7"
        
    elif char == "a":
        
        print("A -> 4")
        charList[index] = "4"
        
    elif char == "b":
        
        print("B -> 8")
        charList[index] = "8"
        
    elif char == "e":
        
        print("E -> 3")
        charList[index] = "3"
    
    elif char == "e":
        
        print("E -> 3")
        charList[index] = "3"
        
    elif char == "i":
        
        print("I -> 1")
        charList[index] = "1"
        
    elif char == "o":
        
        print("O -> 0")
        charList[index] = "0"
        
    elif char == "s":
        
        print("S -> 5")
        charList[index] = "5"
        
    elif char == "t":
        
        print("T -> 7")
        charList[index] = "7"
        
textFinalized = ""
for char in charList: textFinalized = textFinalized + char
        
print(textFinalized)
        
