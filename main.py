import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('Book1.csv', header=0)
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[14]]))