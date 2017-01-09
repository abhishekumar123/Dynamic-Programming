import pandas as pd

class Min_Ways_coin_change:

	def __init__(self):
		self.set1 = []

	def create_matrix(self,summ,st):
		self.st = st
		for i in xrange(summ+1):
			self.set1.append(i)
		self.df = pd.DataFrame(index = st ,columns = self.set1)
		self.df.fillna(0,inplace = True)
		for i in range(0,self.df.shape[1]) :
			self.df.loc[0,i] = 0
		for i in st:
			self.df.loc[i,0] = 1

		self.df.fillna(0)

	def get_matrix(self):
		for i in range(1,len(self.st)):
			for j in range(1,self.df.shape[1]) :
				if(self.st[i] > j):
					self.df.loc[self.st[i],j] = self.df.loc[self.st[i-1],j]
				else:
					
					self.df.loc[self.st[i],j]  = self.df.loc[self.st[i-1],j] + self.df.loc[self.st[i],j-self.st[i]]
					
				print i,self.st[i],j
					
	
		
				
