import pandas 	as pd

class pldrm_sbsq:
	def __init__(self):
		self.str = ''
		self.set1 = []

	def create_matrix(self,str):
		self.str = str
		for i in range(-1,len(str)):
			self.set1.append(i)
		self.df = pd.DataFrame(index = self.set1 ,columns = self.set1)
		for i in range(-1,len(self.set1)-1) :
			self.df.loc[-1,i] = 1
			self.df.loc[i,-1] = 1



	
		
				

	def get_matrix(self):
		k = 0
		for i in range(1,len(self.str)+1):
			j = i-1
			while(j < len(self.str)):
				print k,j
				if self.str[j] != self.str[k]:
					self.df.loc[k,j] = max(self.df.loc[k,j-1],self.df.loc[k+1,j])
				else:
					if  i == 1:
						self.df.loc[k,j] = 1
					else:
						self.df.loc[k,j] = 2 + self.df.loc[k+1,j-1]
						
				j = j+1
				k = k+1
				
			k=0
			
						
			

				print i,self.st[i],j
					
					
					
					
