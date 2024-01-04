# https://www.w3schools.com/python/python_sets.asp

# set is collection of UNIQUE item

# usage: email recipients (to:), it make no sense sending to the same person twice (email server will only send once anyway)

uniqueUsers = {'John', 'Peter'}  # primitive type: string, int, float, bool
even_numbers = {1, 3, 5, 7, 9}
print(uniqueUsers)

unique2Users = {'Ann', 'Mary', 'Ann'}  # un-ordered list
print(unique2Users, 'Ann is shown ONCE only')