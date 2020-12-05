def get_number_list():
  file = open("data/1_1_inputs.txt", "r")
  lines = file.readlines()

  new_number_list = []
  for line in lines:
    new_number_list.append(int(line))

  return new_number_list
# end of get_number_list

def filter_number_list(the_number_list, criteria_def):
  filtered_number_list = []
  # go through all numbers, store in first variable
  for first_pos in range(0, len(the_number_list)):
    # go through all numbers, store in second variable
    for second_pos in range(0, len(the_number_list)):
      if first_pos == second_pos:
          continue

      # go through all numbers, store in third variable
      for third_pos in range(0, len(the_number_list)):
        if second_pos == third_pos or first_pos == third_pos:
          continue

        first_number = the_number_list[first_pos]
        second_number = the_number_list[second_pos]
        third_number = the_number_list[third_pos]
        
        is_true = criteria_def(first_number, second_number, third_number)

        print(first_number, second_number, third_number, is_true)

        if is_true:
          filtered_number_list.append(first_number)
          filtered_number_list.append(second_number)
          filtered_number_list.append(third_number)
          break

      if len(filtered_number_list) > 0:
        break
    
    if len(filtered_number_list) > 0:
      break

  return filtered_number_list
# end of filter_number_list

def is_sum_2020(the_first_number, the_second_number, the_third_number):
  # add numbers stored in first and second variable
  the_sum = the_first_number + the_second_number + the_third_number
  if the_sum == 2020:
    return True
  return False
# end of is_sum_2020

# main

number_list = get_number_list()
print(number_list)

results = filter_number_list(number_list, is_sum_2020)
print(results)

answer = results[0] * results[1] * results[2]
print("The answer is: ", answer)