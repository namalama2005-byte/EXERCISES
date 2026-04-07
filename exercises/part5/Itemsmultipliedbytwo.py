def double_items(numbers: list):
    
    doubled = [num * 2 for num in numbers]
    return doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
