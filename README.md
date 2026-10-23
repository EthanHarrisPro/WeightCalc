##### What + Why

This application allows the user to input their average Resting and Active Calories, Calorie intake and Weight and outputs the expected weight loss or gain from this. I chose this project because I'm active in the fitness community and thought I could make a application that would save me from manually working out these calculations. This way I can input my burnt calories from my Apple Health and the calories I've consumed from MyFitnessPal and get the expected weight change.





###### No external dependencies
py weightcalc.py in terminal to run main.
py -m unittest test.py to run unittest


##### How it works

* Gets the user to input calories and weight
* Combines average Active and Resting kcal
* Gets total kcal burnt
* 1lb = 3500kcal so divides the difference in burnt calories and calories consumed by 3500 to get lb change
* 1kg = \~2.2lb so divides by that number to get kg
* works out bodyfat percentage using weight change and bodyweight
* outputs the loss or gain of weight



##### Improvements



With more time you could add a database to keep track of progress 





