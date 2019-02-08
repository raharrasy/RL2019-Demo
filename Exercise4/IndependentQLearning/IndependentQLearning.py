#!/usr/bin/env python3
# encoding utf-8

import random
import argparse
from DiscreteMARLUtils.Environment import DiscreteMARLEnvironment
from DiscreteMARLUtils.Agent import Agent
from copy import deepcopy
		
class IndependentQLearningAgent(Agent):
	def __init__(self, learningRate, discountFactor, epsilon, initVals=0.0):
		super(IndependentQLearningAgent, self).__init__()

	def setExperience(self, state, action, reward, status, nextState):
		return
	
	def learn(self):
		return

	def act(self):
		return self.possibleActions[random.randint(0,len(self.possibleActions)-1)]

	def toStateRepresentation(self, state):
		return str(state)

	def setState(self, state):
		return

	def setEpsilon(self, epsilon):
		return
		
	def setLearningRate(self, learningRate):
		return
		
	def computeHyperparameters(self, numTakenActions, episodeNumber):
		return 0.1, 0.1

if __name__ == '__main__':
	MARLEnv = DiscreteMARLEnvironment(numOpponents = 1, numAgents = 2, visualize = True)
	agents = []
	numAgents = 2
	for i in range(numAgents):
		agent = IndependentQLearningAgent(learningRate = 0.1, discountFactor = 0.9, epsilon = 1.0)
		agents.append(agent)

	numEpisodes = 50000
	numTakenActions = 0
	for episode in range(numEpisodes):	
		status = ["IN_GAME","IN_GAME","IN_GAME"]
		observation = MARLEnv.reset()
		totalReward = 0.0
		timeSteps = 0
					
		while status[0]=="IN_GAME":
			for agent in agents:
				learningRate, epsilon = agent.computeHyperparameters(numTakenActions, episode)
				agent.setEpsilon(epsilon)
				agent.setLearningRate(learningRate)
			actions = []
			stateCopies = []
			for agentIdx in range(numAgents):
				obsCopy = deepcopy(observation[agentIdx])
				stateCopies.append(obsCopy)
				agents[agentIdx].setState(agent.toStateRepresentation(obsCopy))
				actions.append(agents[agentIdx].act())
			numTakenActions += 1
			nextObservation, reward, done, status = MARLEnv.step(actions)
			print(nextObservation, reward, done, status)

			for agentIdx in range(numAgents):
				agents[agentIdx].setExperience(agent.toStateRepresentation(stateCopies[agentIdx]), actions[agentIdx], reward[agentIdx], 
					status[agentIdx], agent.toStateRepresentation(nextObservation[agentIdx]))
				agents[agentIdx].learn()
				
			observation = nextObservation
				
