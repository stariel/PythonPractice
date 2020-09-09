#!/usr/bin/python3

# 1) Set the users variable to be an empty list
users = []
# 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
users.append('kevin')
users.append('bob')
users.append('alice')
print(users)
# 3) Remove 'bob' from the `users` list without reassigning the variable.
del users[1]
print(users)

# 4) Reverse the users list and assign the result to `rev_users`
rev_users = list(reversed(users))
print(rev_users)

# 5) Add the user 'melody' to users where 'bob' used to be.

users.insert(1, 'melody')

# 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command

users += ['andy', 'wanda', 'jim']

# 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`

center_users = users[2:4]