def hello():
    return 'hello'

print(hello())

# Basis of a test
# You'll be testing functions or methods, these need to be called or initialised
# Having controlled inputs for known outputs
    # And testing for these

def make_dough(arg1, arg2):
    pass

def bake_dough(arg1):
    pass

# Make test for make_dough
# To make dough it will take in water and flour to make dough
print("Testing make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough('water', 'flour') == 'dough')
print ('got:', make_dough('water', 'flour'))

# Make test for bake_dough
# Then, with the dough we should be able to put it in the oven and get out a naan
print("Testing bake_dough with 'dough'. Expected --> 'Naan'")
print(bake_dough('dough') == 'Naan')
print ('got:', bake_dough('dough'))


