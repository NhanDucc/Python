def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def spilit_and_transfer(lst):
    sublist = {}
    for element in lst:
        if element not in sublist:
            sublist[element] = [element]
        else:
            sublist[element].append(element)
    return list(sublist.values())

file = "__blank__" #Enter the path to the file to split and count the elements into __blank__
data = read_file(file)
sublist = spilit_and_transfer(data)
for sublists in sublist:
    print(sublists,len(sublists))
