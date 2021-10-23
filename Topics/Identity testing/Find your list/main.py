def find_my_list(the_lists, my_list):
    for i, lst in enumerate(the_lists):
        # Change the next line
        if lst is my_list:
            return i
    return None
