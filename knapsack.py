import pandas as pd

class Knapsack:
	def __init__(self):
		self.set1 = []
		self.mapper = {}
		self.weight = []

	def create_matrix(self,summ,st,weight):
		self.st = st
		j = 0
		for i in self.st:
			self.mapper[i] = weight[j]
			j = j+1
			
		for i in xrange(summ+1):
			self.set1.append(i)
		self.df = pd.DataFrame(index = st ,columns = self.set1)
		for i in range(0,self.df.shape[1]) :
			self.df.loc[0,i] =  0
		for i in st:
			self.df.loc[i,0] = 0

	
		
				

	def get_matrix(self):
		for i in range(1,len(self.st)):
			for j in range(1,self.df.shape[1]) :
				if(self.st[i] > j):
					self.df.loc[self.st[i],j] = self.df.loc[self.st[i-1],j]
				else:
					self.df.loc[self.st[i],j]  = max(self.mapper[self.st[i]]+ self.df.loc[self.st[i-1],j-self.st[i]],self.df.loc[self.st[i-1],j])
					
				print i,self.st[i],j
