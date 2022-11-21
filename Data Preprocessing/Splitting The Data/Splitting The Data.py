#Splitting data as independent and dependent 
#removing index column in independent dataset 
x=ds.iloc[:,1:31].values 
y=ds.iloc[:, -1].values 
print(x,y)

#Splitting data into train and test 
from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=42)
