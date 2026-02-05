# Tuple
# A tuple is a collection that is ordered and unchangeable
# parentheses are used to define a tuple

counties = ("Nairobi", "Mombasa", "Kisumu", "Nakuru", "Uasin Gishu", "Kericho")
print(counties)
print(type(counties))

# slicing a tuple
print(counties[3:])

# accessing elements in a tuple using index
print(counties[5])

# Note below will raise an error since tuples are immutable
# AttributeError: 'tuple' object has no attribute 'append'
counties.append("Machakos")
print(counties)

