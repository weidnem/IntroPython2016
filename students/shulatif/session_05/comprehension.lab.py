
# Count Even Numbers
def count_evens(nums):
    return len([n for n in nums if n % 2 == 0])

# Tests
print(count_evens([2, 1, 2, 3, 4]) == 3)
print(count_evens([2, 2, 0]) == 3)
print(count_evens([1, 3, 5]) == 0)

# Dicts and Sets
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print('{name} is from {city} and he likes {cake} cake, {fruit}, {salad} salad, and {pasta}'.format(**food_prefs))


test = [prefs for prefs in food_prefs]
print(test)

