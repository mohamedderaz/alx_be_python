def perform_operation(num1,num2,operation):
    if operation =='add':
        return num1+num2
    elif operation =='subtract':
        return num2-num1
    elif operation =='multiply':
        return num1*num2
    elif operation =='divide':
        if num2==0:
            print("cannot divid by zero")
        else:return num1/num2
perform_operation(5,1,'add')    

 