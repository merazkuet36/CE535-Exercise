from posixpath import split


def login(n:str, pin:str)-> bool: 
    success= False 
    # Check the user number is a string. 
    # # Check the pin number is a string. 
    # # Check the pin number has four digits. 
    if not isinstance(n, str): 
        return False 
    if not isinstance(pin, str): 
        return False 
    if len(pin)!=4: 
        return False 
    with open('pins.csv', 'r') as input_stream: 
        data = input_stream.read() 
        for line in data,split('\n'): 
            info = line.split(',') 
            current_pin=info[0] 
            current_user=info[1] 
            if n==current_user and pin==current_pin: 
                success= True 
                break 
            return success 
        print(f"login('60', '9430') == {login('60', '9430')}")