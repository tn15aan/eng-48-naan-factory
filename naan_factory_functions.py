# Here we run the factory

def make_dough(arg1, arg2):
    if arg1 != 'water' and arg2 != 'water':
        return 'not_dough'
    elif arg1 != 'flour' and arg2 != 'flour':
        return 'not_dough'
    elif 'water' in [arg1, arg2] and 'flour' in [arg1, arg2]:
        return 'dough'

def bake_dough(arg1):
    if arg1 == 'dough':
        return 'Naan'
    else:
        return 'not_Naan'