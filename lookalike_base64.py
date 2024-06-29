import random

sample = "MDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVohIiMkJSZcJygpKissLS4vOjs8PT4/QDAxMjM0NTY3ODlhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFla"
char_list = list(sample)

char_count = {}

for char in char_list:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

total_chars = len(char_list)

char_percentage = {}

for char, count in char_count.items():
    char_percentage[char] = (count / total_chars) * 100

characters = list(char_percentage.keys())
weights = list(char_percentage.values())

weights = [weight / 100 for weight in weights]

def generate(prefix="", length=20):
    digest = prefix + ''.join(random.choices(characters, weights, k=length))
    return digest

