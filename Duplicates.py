list = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana' , 'fig', 'grape', 'cherry', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla bean', 'watermelon', 'xigua', 'yellow passion fruit', 'zucchini']

duplicates = []
for value in list:
    if list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print( duplicates)