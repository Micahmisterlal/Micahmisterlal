user_email = input("micahmisterlal4@gmail.com: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if  re.match(pattern, user_email):
    print("Valid email address.")