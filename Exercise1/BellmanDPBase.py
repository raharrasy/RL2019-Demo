from MDP import MDP

class BellmanDPSolver(object):
	def __init__(self):
		self.policy = {(1, 3): ['DRIBBLE_UP', 'SHOOT'], (3, 0): ['DRIBBLE_UP', 'SHOOT'], (2, 1): ['DRIBBLE_UP', 'SHOOT'], (0, 3): ['DRIBBLE_UP', 'SHOOT'], (4, 0): ['DRIBBLE_UP', 'SHOOT'], (1, 2): ['DRIBBLE_UP'], (3, 3): ['DRIBBLE_UP', 'SHOOT'], (4, 4): ['DRIBBLE_UP', 'SHOOT'], (2, 2): ['DRIBBLE_UP', 'SHOOT'], (4, 1): ['DRIBBLE_UP', 'SHOOT'], (1, 1): ['DRIBBLE_UP', 'SHOOT'], 'OUT': ['DRIBBLE_UP', 'SHOOT'], (3, 2): ['DRIBBLE_UP', 'SHOOT'], (0, 0): ['DRIBBLE_UP', 'SHOOT'], (0, 4): ['DRIBBLE_UP', 'SHOOT'], (1, 4): ['DRIBBLE_UP', 'SHOOT'], (2, 3): ['DRIBBLE_UP', 'SHOOT'], (4, 2): ['DRIBBLE_UP', 'SHOOT'], (1, 0): ['DRIBBLE_UP', 'SHOOT'], (0, 1): ['DRIBBLE_UP', 'SHOOT'], 'GOAL': ['DRIBBLE_UP', 'SHOOT'], (3, 1): ['DRIBBLE_UP', 'SHOOT'], (2, 4): ['DRIBBLE_UP', 'SHOOT'], (2, 0): ['DRIBBLE_UP', 'SHOOT'], (4, 3): ['DRIBBLE_UP', 'SHOOT'], (3, 4): ['DRIBBLE_UP', 'SHOOT'], (0, 2): ['DRIBBLE_UP', 'SHOOT']}
		self.vals = {(1, 3): 0, (3, 0): 0, (2, 1): 0, (0, 3): 0, (4, 0): 0, (1, 2): 0, (3, 3): 0, (4, 4): 0, (2, 2): 0, (4, 1): 0, (1, 1): 0, 'OUT': 0, (3, 2): 0, (0, 0): 0, (0, 4): 0, (1, 4): 0, (2, 3): 0, (4, 2): 0, (1, 0): 0, (0, 1): 0, 'GOAL': 0, (3, 1): 0, (2, 4): 0, (2, 0): 0, (4, 3): 0, (3, 4): 0, (0, 2): 0}
	def initVs(self):
		raise NotImplementedError
	def BellmanUpdate(self):
		return self.vals, self.policy

if __name__ == '__main__':
	solution = BellmanDPSolver()
	for i in range(20000):
		values, policy = solution.BellmanUpdate()
	print("Values : ", values)
	print("Policy : ", policy)
