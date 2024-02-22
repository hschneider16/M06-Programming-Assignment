import datetime

# 13.1
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
with open('today.txt', 'w') as file:
    file.write(current_date)

# 13.2
with open('today.txt', 'r') as file:
    today_string = file.read()

# 13.3
parsed_date = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()

print(parsed_date)