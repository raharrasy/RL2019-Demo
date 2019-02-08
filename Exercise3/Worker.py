import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

from Networks import ValueNetwork
from torch.autograd import Variable
from Environment import HFOEnv
import random

def train():
	hfoEnv = HFOEnv(numTeammates=0, numOpponents=1, port=1234, seed=1234)
	hfoEnv.connectToServer()

	episodeNumber = 0
	while True:
		action = random.randint(0,3)
		act = hfoEnv.possibleActions[action]
		newObservation, reward, done, status, info = hfoEnv.step(act)
		print(newObservation, reward, done, status, info)
		if status == 5:
			hfoEnv.quitGame()
			break

		if done:
			episodeNumber += 1
		else:
			state = torch.Tensor([newObservation])
	

def computeTargets(reward, nextObservation, discountFactor, done, targetNetwork):
	raise NotImplementedError

def computePrediction(state, action, valueNetwork):
	raise NotImplementedError

if __name__ == '__main__':
	train()





