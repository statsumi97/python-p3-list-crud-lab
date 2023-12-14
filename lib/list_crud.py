def create_an_empty_list():
    return []

def create_a_list():
    return ['Phoebe Bridgers', 'Lucy Dacus', 'Julien Baker', 'MUNA']


my_list = ['Phoebe Bridgers', 'Lucy Dacus', 'Julien Baker']
new_element = 'MUNA'

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

add_element_to_start_of_list(my_list, new_element)

def remove_element_from_end_of_list(l):
    l.pop()
    return l

remove_element_from_end_of_list(my_list)


spotify_artists_list = ['Indigo de Souza', 'Samia', 'MUNA', 'boygenius', 'Fiona Apple']

def remove_element_from_start_of_list(l):
    del l[0]
    return l

remove_element_from_start_of_list(spotify_artists_list)


favorite_foods_list = ['Pho', 'Udon', 'Hot Pot', 'Tonkatsu', 'Kimchi Jjigae']

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
