import random
from collections import defaultdict

sample = "MDEyMzQ1Njc4OWFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVohIiMkJSZcJygpKissLS4vOjs8PT4/QDAxMjM0NTY3ODlhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFla"

nodes = [sample[i:i+2] for i in range(0, len(sample)-1, 2)]

node_count = defaultdict(int)
for node in nodes:
    node_count[node] += 1

total_nodes = len(nodes)
node_probabilities = {node: count / total_nodes for node, count in node_count.items()}

characters = list(node_probabilities.keys())
weights = list(node_probabilities.values())

def generate(prefix="", length=20):
    selected_nodes = random.choices(characters, weights=weights, k=length)
    
    result = prefix + ''.join(selected_nodes)
    
    return result
