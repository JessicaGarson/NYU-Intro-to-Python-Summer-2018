phone_number = '2022343259'

area_code = phone_number[0:3]
middle_part = phone_number[3:6]
last_part = phone_number[6:]

formatted_number = "({}){}-{}".format(area_code, middle_part, last_part)

print(formatted_number)
