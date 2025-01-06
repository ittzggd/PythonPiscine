def NULL_not_found(object: any) -> int:
    if object == None :
        print(f"Nothing: {object} {type(object)}")
    elif type(object) == float and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif type(object) == int and object == 0 :
        print(f"Zero: {object} {type(object)}")
    elif type(object) == str and not object:
        print(f"Empty: {type(object)}")
    elif type(object) == bool and object == False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
