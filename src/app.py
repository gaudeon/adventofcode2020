def get_number_list():
  file = open("data/1_1_inputs.txt", "r")
  lines = file.readlines()
  
  number_list = []
  for line in lines:
    number_list.append(int(line))

  return number_list

number_list = get_number_list()
print(number_list)