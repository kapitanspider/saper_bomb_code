from sklearn.datasets import load_digits
import pylab as pl
import random
from sklearn import tree

digits = load_digits()

#Define variables
n_samples = len(digits.images)
x_dig = digits.images.reshape((n_samples, -1))
y_dig = digits.target

#Create random indices
sample_index = random.sample(range(int(len(x_dig))), int(len(x_dig)/5)) #20-80
valid_index=[i for i in range(len(x_dig)) if i not in sample_index]

#Sample and validation images
sample_images=[x_dig[i] for i in sample_index]
valid_images=[x_dig[i] for i in valid_index]

#Sample and validation targets
sample_target=[y_dig[i] for i in sample_index]
valid_target=[y_dig[i] for i in valid_index]

#Using the Random Forest Classifier
classifier = tree.DecisionTreeClassifier()

#Fit model with sample data
classifier.fit(sample_images, sample_target)

#Attempt to predict validation data
score=classifier.score(valid_images, valid_target)
#tree.export_graphviz(classifier, out_file='tree.doc')
print("dokładność uczenia: "+str(score))

#for i in range(0, len(digits.images)):
i=122
pl.gray()
pl.matshow(digits.images[i])
#pl.savefig('liczba.png')
photo = x_dig[i].reshape(1, -1)
#pl.show()
wyn = classifier.predict(photo)
print(wyn);
filename = str(wyn)+" liczba numer "+str(i)+".png"
#filename = "data\ "+str(i)
pl.savefig(filename)
pl.close()

