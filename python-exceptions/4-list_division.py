#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Attempt to divide corresponding elements, handle exceptions
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check if the elements are of numeric types
            if not isinstance(element_1, (int, float)) or not isinstance(element_2, (int, float)):
                raise TypeError("wrong type")

            # Check if the division by 0
            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = element_1 / element_2
            result_list.append(division_result)

        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except IndexError:
            print("out of range")
            break
        finally:
            pass
    return result_list
