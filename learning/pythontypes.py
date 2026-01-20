# Function with type hints
def add1(fname:str | list[int] ,lname:str | None):
    # fname can be str or list[int]
    # lname is optional
    # fname.capitalize()  # This does nothing (result not used)
    return fname # +lname

fname="navas"
lname="Sana"
name=add1(fname.capitalize(),lname)
print(name)  # NavasSana


# Function without type hints
def add2(fname,lname):
    # fname.  # Incomplete line
    return fname+lname

fname="navas"
lname="Sana"
name=add2(fname.capitalize(),lname)
print(name)  # NavasSana


# What I learned:
# - Type hints show what types parameters expect (: str, : int)
# - Union types (str | list[int]) allow multiple types
# - Default values (= None) make parameters optional
# - Type hints help with code readability
# - Type hints are optional in Python but recommended