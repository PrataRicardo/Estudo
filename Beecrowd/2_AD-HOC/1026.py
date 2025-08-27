while True:
    try:
        integer_value, integer_value2 = [int(x) for x in input().split(" ")]
        result1 = integer_value ^ integer_value2
        print(f"{result1}")
    
    except EOFError:
        break