from naan_factory_functions import *
# Tests go here for separation of concerns

# Make test for make_dough
# To make dough it will take in water and flour to make dough
print("Testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough('water', 'flour') == 'dough')
print("got:", make_dough('water', 'flour'))

#When I pass in cement and water, or anything else... I should get: 'Not dough'
print("My tests")
print("Testing make_dough with 'cement' and 'water'. Expected --> 'not_dough'")
print(make_dough('cement', 'water') == 'not_dough')
print("got:", make_dough('cement', 'water'))

print("Testing make_dough with 'egg' and 'flour'. Expected --> 'not_dough'")
print(make_dough('egg', 'flour') == 'not_dough')
print("got:", make_dough('egg', 'flour'))

# Make test for bake_dough
# Then, with the dough we should be able to put it in the oven and get out a naan
print("Testing bake_dough with 'dough'. Expected --> 'Naan'")
print(bake_dough('dough') == 'Naan')
print("When calling bake_dough, got:", bake_dough('dough'))

# When bake_dough is passed something other than 'dough' it should output 'not_Naan'
print("My test")
print("Testing bake_dough with 'chicken'. Expected --> 'Naan'")
print(bake_dough('chicken') == 'not_Naan')
print("When calling bake_dough, got:", bake_dough('chicken'))

