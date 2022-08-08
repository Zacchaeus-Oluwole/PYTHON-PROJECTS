def isValid(data):
    result = None
    data = [x for x in data]
    dataL = len(data)%2
    if dataL == 0:
        for i in range(len(data)):
            if data[i] == '(' and (data[-i] == ')' or data[i + 1] == ')'):
                result = True
            elif data[i] == '{' and (data[-i] == '}' or data[i + 1] == '}'):
                result = True
            elif data[i] == '[' and (data[-i] == ']' or data[i + 1] == ']'):
                result = True
    return result

if isValid('([])') == True:
    print("Valid")
else:
    print('Invalid')

# if isValid('()[]') == True:
#     print("Valid")
# else:
#     print('Invalid')