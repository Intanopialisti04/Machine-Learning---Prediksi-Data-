from sklearn.neighbors import NearestCentroid

# Dtabase : Gerbang logika AND
# x = Data, y = Target
x = [[2,0], [0,2], [0,0], [2,1], [1,3], [3,0], [3,2], [2,3], [2,2], [3,3], [4,3], [4,4]]
y = [0,0,0,0,0,0,0,0,1,1,0,1]

# Traininy and Classify
clf = NearestCentroid()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Nearest Neighbots")
print ("Logika = Prediksi")
print ("2 0 = ", clf.predict([[2,0]]))
print ("0 2 = ", clf.predict([[0,2]]))
print ("0 0 = ", clf.predict([[0,0]]))
print ("2 1 = ", clf.predict([[2,1]]))
print ("1 3 = ", clf.predict([[1,3]]))
print ("3 0 = ", clf.predict([[3,0]]))
print ("3 2 = ", clf.predict([[3,2]]))
print ("2 3 = ", clf.predict([[2,3]]))
print ("2 2 = ", clf.predict([[2,2]]))
print ("3 3 = ", clf.predict([[3,3]]))
print ("4 3 = ", clf.predict([[4,3]]))
print ("4 4 = ", clf.predict([[4,4]]))
