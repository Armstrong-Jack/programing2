import datetime as dt
VALID_CATEGORIES = ['food', 'transport', 'utilities', 'entertainment', 'other']

def is_valid_category(cat):
    # Implement validation logic here
    pass
    test_piece = cat
    cleaned_test_piece = test_piece.lower()
    if cleaned_test_piece in VALID_CATEGORIES:
        return True
    else:
        return False

# Test
print(is_valid_category('Food')) # Should be True
print(is_valid_category('Car'))  # Should be False
try:
    user_input = input("please enter the date: (yyyy-mm-dd)")
except (EOFError, KeyboardInterrupt) as e:
    print("yay caught error")
date_format = "%Y-%m-%d"

try:
    valid_date = dt.datetime.strptime(user_input, date_format)
    print("yay succesful")
except ValueError:
    print("Value error")
