def get_number_list():
  file = open("data/1_1_inputs.txt", "r")
  lines = file.readlines()

  new_number_list = []
  for line in lines:
    new_number_list.append(int(line))

  return new_number_list
# end of get_number_list

def filter_number_list(the_number_list, criteria_def):
  # go through all numbers, store in first variable
  for first_pos in range(0, len(the_number_list)):
    # go through all numbers, store in second variable
    for second_pos in range(0, len(the_number_list)):
        if first_pos == second_pos:
          continue

        first_number = the_number_list[first_pos]
        second_number = the_number_list[second_pos]
        
        is_true = criteria_def(first_number, second_number)

        print(first_pos, second_pos, is_true)
        pass
  
  # if a pair equals 2020 then keep them
  # if a pair doesn't equal 2020 continue 
  pass
# end of filter_number_list

def is_sum_2020(the_first_number, the_second_number):
  # add numbers stored in first and second variable
  the_sum = the_first_number + the_second_number
  if the_sum == 2020:
    return True
  return False
# end of is_sum_2020

# main

number_list = get_number_list()
print(number_list)

filter_number_list(number_list, is_sum_2020)