import random

sample = "MDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVohIiMkJSZcJygpKissLS4vOjs8PT4/QFtcXF1eX2B7fH1+IDAxMjM0NTY3ODlhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaISIjJCUmXCcoKSorLC0uLzo7PD0+P0BbXFxdXl9ge3x9fiAwMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWiEiIyQlJlwnKCkqKywtLi86Ozw9Pj9AW1xcXV5fYHt8fX4gMDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVohIiMkJSZcJygpKissLS4vOjs8PT4/QFtcXF1eX2B7fH1+IDAxMjM0NTY3ODlhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaISIjJCUmXCcoKSorLC0uLzo7PD0+P0BbXFxdXl9ge3x9fiAjJCUmXCcoKSorLC0uLzo7PD0+P0BbXFxdXl9ge3x9fiB3eHl6QUJDQFtcXF1eX2B7fH1+IDAxMjM0NTY3ODlhYmNkZWZnaGlqa0RFRkdISUpLTE1OT1BRUlNUVVZXWHd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVW"

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

