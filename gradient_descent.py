import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(error,weights):
	weights-=0.1*error

def main():
	theta=np.random.rand(3)
	inp=np.random.rand(100,3)
	out=np.random.rand(100)
	inp[:,:1]=1
	for i in range(2000):
		grad=np.zeros(3)
		for vec in range(len(inp)):
			d=np.dot(theta.T,inp[vec])
			error=d-out[vec]
			grad+=(error)*inp[vec]
		gradient_descent(grad/100,theta)
	sample=np.linspace(1,0.01,100)
	line=theta[2]*sample+theta[1]*sample+np.repeat(theta[0],100)
	plt.plot(line,sample)
	plt.plot(out,inp[:,1:],'o')
	plt.show()
	print(error,theta,grad)

if __name__=="__main__":
	main()
