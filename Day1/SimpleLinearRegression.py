def prediction(values_x, w0, w1):
	predict = []
	for i in range(len(values_x)):
		predict.append(w0 + w1*values_x[i])
	return predict

def mean(values):
	return sum(values)/float(len(values))

def variance(values,mean):
	diff = []
	for x in values:
		diff.append((x-mean)**2) 
	return (sum(diff))/float(len(values))

def covariance(values_x,mean_x,values_y,mean_y):
	diff = []
	for i in range(len(values_x)):
		diff.append((values_x[i]-mean_x)*(values_y[i]-mean_y))
	return (sum(diff))/float(len(values_x))	

#dataset
values_x = [1,2,4,3,5]
values_y = [1,3,3,2,5]

#Calculations
mean_x = mean(values_x)
mean_y = mean(values_y)
variance_x = variance(values_x,mean_x)
variance_y = variance(values_y,mean_y)
covariance = covariance(values_x,mean_x,values_y,mean_y) 

#coefficients
w1 = covariance / variance_x
w0 = mean_y - w1*mean_x

print("Observed Values Are: " , values_y)
print("Predicted Values Are: " , prediction(values_x,w0,w1))
