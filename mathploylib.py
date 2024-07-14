import matplotlib.pyplot as plt

# creating a basic plot
x=[1,2,3,4,5]
y=[10,20,30,40,50]
# plt.plot(x,y) #plots x and y axis on graph based onthe points given
# plt.xlabel('x-axis') #x-axis name
# plt.ylabel('y-axis') #y-axis name
# plt.title('Bar Graph');
# plt.show()

# creating a scatter plot
# plt.scatter(x,y,color='red')
# plt.show()

#creating a bar chart
# subjects=['maths','physics','chemistry','computers']
# marks=[100,50,76,80]
# plt.bar(subjects,marks,color='pink')
# plt.show()

#creating a histogram
# import numpy as np
# data=np.random.randn(1000)
# plt.hist(data,bins=30,edgecolor='black')
# plt.show()

#creating a piechart
brands=['apple','one plus','samsung','vivo','oppo']
sizes=[15,30,45,10,9]
plt.pie(sizes,labels=brands,autopct='%1.1f%%',startangle=140)
plt.axis('equal')
plt.show()

#creating subplots
x1=[1,2,3,4,5]
y1=[2,3,5,7,11]
y2=[1,4,6,8,10]
fig,axis=plt.subplots(2)
axis[0].plot(x,y1)