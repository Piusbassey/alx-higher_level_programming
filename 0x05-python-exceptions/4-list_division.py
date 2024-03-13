#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check if division by 0 is going to happen
            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = element_1 / element_2
            result_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            pass

    return result_list

# Test cases
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

