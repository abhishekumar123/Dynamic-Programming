import pandas as pd

class CoinChange:
	def __init__(self):
		self.set1 = []

	def create_matrix(self,summ,st):
		self.st = st
		for i in xrange(summ+1):
			self.set1.append(i)
		self.df = pd.DataFrame(index = st ,columns = self.set1)
		for i in range(0,self.df.shape[1]) :
			self.df.loc[0,i] = i
		for i in st:
			self.df.loc[i,0] = 0

		self.df.fillna(0)
	
		
				

	def get_matrix(self):
		for i in range(1,len(self.st)):
			for j in range(1,self.df.shape[1]) :
				if(self.st[i] > j):
					self.df.loc[self.st[i],j] = self.df.loc[self.st[i-1],j]
				else:
					self.df.loc[self.st[i],j]  = min(1 + self.df.loc[self.st[i],j-self.st[i]],self.df.loc[self.st[i-1],j])
					
				print i,self.st[i],j
					
					
					
					
