def get_number_list():
  file = open("data/1_1_inputs.txt", "r")
  lines = file.readlines()
  return lines

number_list = get_number_list()
print(number_list)