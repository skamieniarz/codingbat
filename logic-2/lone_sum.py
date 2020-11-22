''' Given 3 int values, a b c, return their sum. However, if one of the values
is the same as another of the values, it does not count towards the sum. '''


def lone_sum(a, b, c):
  lone_sum = 0
  ints_list = [a, b, c]
  for item in ints_list:
    if ints_list.count(item) == 1:
      lone_sum += item
  return lone_sum
