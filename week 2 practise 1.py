import datetime 

def add_expense():
    entered_name = input("Please enter the expenses name")
    while True:
            inputed_year = input("pleae enter the date yyyy-mm-dd")
            try:
                datetime.datetime.strptime(inputed_year, "%y-%m-d%")
                print("test succesful")
            except ValueError:
                 print("you entered an icorrect date")

add_expense()
