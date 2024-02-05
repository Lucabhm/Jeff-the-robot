word = 'Hallo'
word = [i for i in word]
print(word)

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

one_list = [number for row in lists for number in row]
print(one_list)
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
newnbrs = [i for i in numbers if i % 2 == 0 and i >= 0]
print(newnbrs)
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
newnbr = [i for i in numbers if i > 0]
print(newnbr)
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_l = [nbr for sublist in list_of_lists for subsublist in sublist for nbr in subsublist]
print(one_l)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(output)