#!/usr/bin/python3
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count

if __name__ == "__main__":
    my_list = [1, 2, 3, "hello", 4, 5]
    count = safe_print_list_integers(my_list, len(my_list))
    print("Number of integers:", count)
