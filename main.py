#using PEP8 coding standards


class Model:

    #Creates the model. We take an integer that dictates the size of each feature of our data
    def __init__(self, n_features):
        #self.num_features is the number of features that we will be taking into account
        #t represents a table/list of each of our weights for our model. This is basically a linear model
        #self.data stores each data point that we have currently trained our data with

        self.num_features = n_features
        self.t = []
        self.data = set()
        for i in range(n_features):
            #it is a design choice that we've decided to start all our weights at the same value, and at 1/n_features.
            self.t.append(1 / n_features)

    #Calculates the probability that the customer will pay the given loan
    #feature param is the data about our customer (customer is the person who is taking the loan)
    def predict(self, feature):
        if len(feature) != self.num_features:
            raise ValueError(
                "Data point provided does not have correct number of features")
        return sum(self.t[i] * feature[i] for i in range(self.num_features))

    #Trains our model given a data point
    #feature param is the data about our customer (customer is the person who is taking the loan)
    #b is whether our customer was able to pay back their loan. 1 represents yes, -1 represents a no.
    def train_with_data(self, feature, b):
        self.data.add(feature)
        s = max(sum(feature), 0.001)
        for i in range(self.num_features):
            self.t[i] += feature[i] / s * b

    #Determines if the customer is allowed to take a loan based only on their given situation. True = give loan, False = Do not give a loan
    def give_loan(self, feature, amount, interest, time_period):
        expected_returns = self.predict(
            feature) * amount * interest**time_period

        #if expected return on investment is more than the amount given, then we proceed to give our customer a loan.
        if expected_returns > amount:
            return True
        else:
            return False

    #Determines if the customer is allowed to take a loan based on their given siutation + the gain in information if their data is given into a model
    def give_loan_with_improved(
            self, feature, amount, interest, time_period,
            num_people_in_popupation_with_similar_characteristics):

        if self.give_loan(feature, amount, interest, time_period):
            return True

        #One way of deciding if a customer should be given a loan is to factor in the number of people who are in a similar situation to that of the person whom we are giving a loan to.
        p = self.predict(feature)
        if p > 0.5 and p * num_people_in_popupation_with_similar_characteristics > amount:
            return True
        else:
            return False

        #An alternative way of deciding if an customer should be provided a loan, is to test how different their financial situation is from our existing customers. This allows us to try out new customers (give loans out to different customers) whom we may have neglected in the past.
        """  
    if len(self.data) == 0:
      raise ValueError("Model has no data, please train")
  
    s = sorted([
        sum((f[i] - feature[i])**2 for i in range(self.num_features))
        for f in self.data
    ])

    #we will test whether 25% of the data lie within a distance of "a" from us.
    #we will test whether 50% of the data lie within a distance of "b" from us.
    #we will test whether 75% of the data lie within a distance of "c" from us.
    #we are essentially, trying to mimic some sort of normal distribution behavior here.
    a = (0.25**2 * self.num_features)**0.5
    b = (0.5**2 * self.num_features)**0.5
    c = (0.75**2 * self.num_features)**0.5
  
    if s[len(s) // 4] < a and s[len(s) // 2] < b and s[3 * len(s) //
                                                       4] < c:
        return False
  
  
    return True"""


#Let us test out the code:
m = Model(5)  #we make a model with 5 features

p1 = (1, 0, 0, 1, 1
      )  #let p1 be a tuple representing the characterstics of person 1
p2 = (0, 0, 0, 0, 0
      )  #let p2 be a tuple representing the characterstics of person 2
p3 = (1, 1, 1, 1, 1
      )  #let p be a tuple representing the characterstics of person 1
p4 = (1, 1, 1, 0, 0
      )  #let p be a tuple representing the characterstics of person 1

print("Person 1 able to pay back loan, prediction: " +
      str(m.give_loan(p1, 10, 1.01, 5)))
print("Person 2 able to pay back loan, prediction: " +
      str(m.give_loan(p2, 10, 1.01, 5)))
print("Person 3 able to pay back loan, prediction: " +
      str(m.give_loan(p3, 10, 1.01, 5)))
print("Person 4 was able to pay back loan, prediction: " +
      str(m.give_loan(p4, 10, 1.01, 5)))

#we see that person 1 failed to give back loan.
#To show that our model "learns" I'm going to train our model 100 times using person 4 as the trainining data (YOU NEVER EVER TRAIN YOUR MODELS LIKE THIS IN THE WILD)
for i in range(100):
  m.train_with_data(p4, 1)

print("After Training...")
#we now see that our model says that person 4 will pay back the loan
print("Person 4 was able to pay back loan, prediction: " +
      str(m.give_loan(p4, 10, 1.01, 5)))

#we also see that the model thinks person 1 will be able to give back his loan, assuming he takes a similar amount. To show that our model at least learns to determine which features are better than others, I'm going to train our model to recognise that person 1 cannot give back loan.
print("Person 1 was able to pay back loan, prediction: " +
      str(m.give_loan(p1, 10, 1.01, 5)))

print("Training to recognise that person 1 cannot pay back loan")
for i in range(100):
  m.train_with_data(p1, -1)

#we now see that our model says that person 1 will not be able to pay back the loan, whilst still ensuring that person 4 can give back his loan
print("Person 1 was able to pay back loan, prediction: " +
      str(m.give_loan(p1, 10, 1.01, 5)))

print("Person 4 was able to pay back loan, prediction: " +
      str(m.give_loan(p4, 10, 1.01, 5)))

#let's say that a new individual: person 5, comes along.... say his characteristics are: (0.2, 0.7, -0.2, 4, 1). Does our model want to give this individual a loan? let's see...
p5 = (0, 0, 0.023, 0, 0)
print("Person 5 able to pay back loan, prediction: " +
      str(m.give_loan(p5, 10, 1.01, 5)))

#we clearly see that our model thinks we shouldn't loan out any money to person 5... however, what if there's a million different users in a similar financial state as 5... should we now give person 5 a loan... since if person 5 can pay back the loan, that opens up a whole new market of customers....!
print("Person 5 able to pay back loan, prediction - improved, if there's one million people in the market to that of 5: " +
      str(m.give_loan_with_improved(p5, 10, 1.01, 5, 1000000)))

#As can be seen our model thinks that since there's a million people in the market with similar characteristics its worth taking the risk and providing person 5 with a loan.

#what if there were fewer people in the market with a similar siutation to that of 5? let's say.. only 10? Is it worth it now?
print("Person 5 able to pay back loan, prediction - improved, if there's only 10 people in the market with a similar situation to that of 5: " +
      str(m.give_loan_with_improved(p5, 10, 1.01, 5, 10)))

#what about person 6, whose financial situation is that of: p6 = (0, 0, 0.013, 0, 0)
p6 = (0, 0, 0.013, 0, 0)

#we can see that our model still decided not to give person 6 a loan... even though there are a million people in the market with a similar financial situation to that of person 6. Our model said "False", because it thinks that the probability of person 6 paying back is so low, that it just isn't worth it.
print("Person 6 able to pay back loan, prediction - improved: " +
      str(m.give_loan_with_improved(p6, 10, 1.01, 5, 1000000)))

#This is just a quick example of such a model that could accomodate for the idea of providing someone a loan based not only based on their financial situation, but also on the gain in knowledge to our model if such a person were to pay back their loan (or maybe not). We could have used a NN/SVM or whatver, but chose not to time constrains/wanting to use vanilla python making it easier to experiment with/removing the black box -- alowing for easier understanding...