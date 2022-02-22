import pandas as pd
import ants

filename = "data/graph5.txt"

def read_dataset(file):
	return pd.read_csv(file, sep = '\t',
			names = ['u', 'v', 'weight'], index_col = ['u', 'v'])

args = {
	'max_iter' : 1,
	'evaporation_rate': 0.02,
	'Q': .001,
	'alpha': 1,
	'beta': 1,
	'seed': 0,
	'ants': 20
}


edges = read_dataset(filename)
colony = ants.Colony(edges)
stats = colony.run(args)
longest_path = stats.loc[args['max_iter']-1,'gbest']
print()
print()
print('longest path cost: '+ str(longest_path[0]))

print('longest path: '+ str(longest_path[1]))	
print()