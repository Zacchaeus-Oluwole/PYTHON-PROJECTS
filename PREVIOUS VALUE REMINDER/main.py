# PRINT THE PREVIOUS VALUE --- LAST EVENT REMINDER
valueX = 0
while True:
    value = int(input('Enter'))
    if value == valueX:
        print("NaN")
    else:
        print(valueX)
    valueX = value