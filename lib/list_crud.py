def create_an_empty_list():
    return []

def create_a_list():
    return ['never', 'gonna', 'give_you', 'up']

def add_element_to_end_of_list(l : list, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l : list, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l : list):
    l.pop()
    return l

def remove_element_from_start_of_list(l : list):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l : list):
    return l[0]

def retrieve_element_from_index(l : list, index):
    return l[index]

def retrieve_last_element_from_list(l : list):
    return l[-1]
