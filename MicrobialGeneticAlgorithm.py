#!/usr/bin/env python

#Author: Pratik M Tambe <enthusiasticgeek@gmail.com>
#Converted the following article code to Python
#https://www.codeproject.com/Articles/16286/AI-Simple-Genetic-Algorithm-GA-to-solve-a-card-pro
#Well, GAs can be used to solve many problems. In fact, GAs have been used to grow new mathematical syntax trees, train multi-layer neural networks, to name but a few instances.
#
#However, for this example, I have used a simple card splitting excercise, which is as detailed here:
#
#    You have 10 cards numbered 1 to 10
#    You have to divide them into two piles so that:
#        The sum of the first pile is as close as possible to 36.
#        And the product of all in the second pile is as close as possible to 360. 

import os,sys
import random
import math

class MicrobialGeneticAlgorithm(object):
	"""
		blueprint Microbial Genetic Algorithm - Card Problem
	"""

	def __init__(self):

                #population
                self.POP = 30
                #geneotype
                self.LEN = 10
                #mutation rate, change it have a play
                self.MUT = 0.1
                #recomination rate
                self.REC = 0.5
                #how many tournaments should be played
                self.END = 1000
                #the sum pile, end result for the SUM pile
                #card1 + card2 + card3 + card4 + card5, MUST = 36 for a good GA
                self.SUMTARG = 36
                #the product pile, end result for the PRODUCT pile
                #card1 * card2 * card3 * card4 * card5, MUST = 360 for a good GA
                self.PRODTARG = 360
                #the genes array, 30 members, 10 cards each
                self.gene = [[0 for x in range(self.LEN)] for y in range(self.POP)] 
                #used to create randomness (Simulates selection process in nature)
                #randomly selects genes

        #initialize population iterating over 30 members sets and 10 cards each set
	def init_pop(self):
                for i in range(len(self.gene)):
                    for j in range(len(self.gene[i])):
                        #print self.gene[i][j]
                        if random.uniform(0.0, 1.0) < 0.5:
                           self.gene[i][j]=0
                        else:
                           self.gene[i][j]=1

	def display_pop(self):
		print("populating gene")
                for i in range(len(self.gene)):
                    for j in range(len(self.gene[i])):
                        print self.gene[i][j]

	def print_pop(self):
            for i in range(len(self.gene)):
                print self.gene[i]          


        #evaluate the the nth member of the population
        #@param n : the nth member of the population
        #@return : the score for this member of the population.
        #If score is 0.0, then we have a good GA which has solved
        #the problem domain
        def evaluate(self, n):
        
            #initialise field values
            sum = 0
            prod = 1

            scaled_sum_error = 0
            scaled_prod_error = 0
            combined_error = 0
            #loop though all genes for this population member
            for i in range(self.LEN):
                if self.gene[n][i] == 0:       
                   #if the gene value is 0, then put it in the sum (pile 0), and calculate sum
                   sum += (1 + i)
                else:
                   #if the gene value is 1, then put it in the product (pile 1), and calculate sum
                   prod *= (1 + i)
            
            #work out how food this population member is, based on an overall error
            #for the problem domain
            #NOTE : The fitness function will change for every problem domain.
            scaled_sum_error = (sum - self.SUMTARG) / self.SUMTARG
            scaled_prod_error = (prod - self.PRODTARG) / self.PRODTARG
            combined_error = math.fabs(scaled_sum_error) + math.fabs(scaled_prod_error)

            return combined_error
        
 
        #Runs the Microbial GA to solve the problem domain
        #Where the problem domain is specified as follows
        #
        #You have 10 cards numbered 1 to 10.
        #You have to divide them into 2 piles so that:
        #
        #The sum of the first pile is as close as possible to 36
        #And the product of all in second pile is as close as poss to 360
        def run(self):
            #declare pop member a,b, winner and loser
            a=0
            b=0
            Winner, Loser = 0,0
            #initialise the population (randomly)
            self.init_pop();
            #start a tournament
            for tournamentNo in range(self.END):
                #pull 2 population members at random
                a = int((self.POP * random.uniform(0.0, 1.0)))
                b = int((self.POP * random.uniform(0.0, 1.0)))
                #have a fight, see who has best genes
                if self.evaluate(a) < self.evaluate(b):
                    Winner = a
                    Loser = b
                else:
                    Winner = b
                    Loser = a
                #Possibly do some gene jiggling, on all genes of loser
                #again depends on randomness (simulating the natural selection
                #process of evolutionary selection)
                for i in range(self.LEN):
                    #maybe do some recombination
                    if random.uniform(0.0, 1.0) < self.REC:
                        self.gene[Loser][i] = self.gene[Winner][i]
                    #maybe do some mutation
                    if random.uniform(0.0, 1.0) < self.MUT:
                        self.gene[Loser][i] = 1 - self.gene[Loser][i]
                    #then test to see if the new population member is a winner
                    if self.evaluate(Loser) == 0.0:
                        self.display(tournamentNo, Loser)


        #Display the results. Only called for good GA which has solved
        #the problem domain
        #@param tournaments : the current tournament loop number
        #@param n : the nth member of the population. 
        def display(self, tournaments, n):
            print("\r\n==============================\r\n")
            print("After " + str(tournaments) + " tournaments, Solution sum pile (should be 36) cards are : ")
            for i in range(self.LEN):
              if self.gene[n][i] == 0: 
                  print(i + 1)
            print("\r\nAnd Product pile (should be 360)  cards are : ")
            for i in range(self.LEN):
              if self.gene[n][i] == 1:
                  print(i + 1)
 

mga = MicrobialGeneticAlgorithm()
mga.run()
