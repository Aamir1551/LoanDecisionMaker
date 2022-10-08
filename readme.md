Typlically, loans are provided to individuals based on their personal details and characteristics. In this VERY brief demonstration, we examine a more far-sighted approach. We achieve this by not only examining an individuals ability to pay back their loan, but also the gain in information to our model by knowing if the user was able to pay back their loan. 


Example,
Say we have person A. Let D be the data collected (may be a tuple/list or whatever) of person A. We can feed D into decision algorithm.

Now their are two options:
1. Either our decision algorithms say's that we should provide person A a loan. Hurray!!!
2. Or, our decision algorithm say's that we should not provide person A a loan, as they will not be able to pay back.


Typically, if our decision model decided that we should not provide person A a loan, that would be the end of it. However, this is quite short-sighted. What if there are a million different people who are in a similar situation to that of A, would it still be a wise idea to not give person A a loan? Or should we instead lend A a loan, and then see if they can pay it back, since if A can pay back the loan, that would mean there's also a good chance the other million of people who we would once deny a loan, can also pay back.

This is what we try to demonstrate/prototype in this very brief model. I've made a very simple model (could have used nearal network or something far more suitable, but wanted to make something that was not a black-box in order to make it more easier to desmonstrate my idea) that only accepts real numbers as inputs.


Assumptions:
1. We have used somewhat of a rank based linear model. The features that are the most important will be taken into account far more. In addition, we have assumed a linear relationship betwen each feature. This is DEFINTELY not true in the real world, but the reason why we decided to do this was to ensure our model doesn't look like a black box, making it easier to demonstrate our idea
2. Haven't taken inflation into account when providing a loan. In fact, we haven't many costs into account when providing someone a loan. We should also take into account the cost of our employees in business to make it worth while and other economic/business factors
3. We also assume that all of the data of our clients can be transformed to real values. Some values such as job description may instead be discrete values and cannot be converted to real values. Granted there do exists serveral methods of transforming such discrete values into real values, but our model still requires continuous values nonetheless.
4. There are several methods of calculating the value in gain in information of giving someone a loan. We only have a look at 2 such possible methods. There are many others, and some may work better than others.

I've coded this up in python 3, so you must have python installed on your system. I've gone out of my way to make sure I don't use any libaries, so no need to install any libraries on your system. This demo project is made to be played around with. Have a go at tinkering with the hyper parameters, and tuning any of the parameters within the code. I've tried to make the code as simple as possible, and the model used as simple as possible for this purpose. 