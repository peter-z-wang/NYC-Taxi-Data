# CSCI 4502 - Data Mining Project - Spring 2018 | NYC Taxi Data
## Project: Catching a Ride in the Big Apple

### Group Members: Spencer Milbrandt, Rasheeq Jahan, and Peter Wang

### Project Description:
   This project was aimed to discover information that would be able to be applied to the underlying problem of
   predicting the best pick-up and drop-off locations as well as what the best time in the day to catch a ride 
   in New York City. In addition, this project strives to identify useful attribute correlations that can be 
   used to solve these problems such as identifying any correlation between distance traveled and fare amount to
   determine whether or not prices dictate the average distance traveled and thus dictate the most common pick-up
   and drop-off locations. Along with discovering the best pick-up and drop-off locations, this project looks at
   different datasets throughout the year of the NYC Limousine and Commission website to analyze whether or not
   certain weather or seasons of the year change the fare amount based on distance traveled. Overall, this project
   has created a base to be built upon to discover more information and apply it to solving various problems not
   only within NYC but other cities throughout the world that have a relatively thriving taxi service or similar
   transportation service.

### Questions to be Answered and the Corresponding Knowledge Gained:
  * What are the best neighborhoods to get a taxi?
    Manhatten Midtown Center/East
    Upper East Side North/South
    Madison Square West
    Times Square
    Union Square
  * In what neighborhoods is it more viable to take a different transportation service?
    In areas of low pickup frequency it is suggested to find a different means for transportation. This is due to the high frequency neighborhood areas having
    taxis as their main mode of transportation. As such, taxi drivers tend to not go to areas with low pickup and dropoff frequency.
  * Do fare amounts really change based on trip distances?
    Correlation shows that fare amounts don't change based on distance traveled and that the linear regression model fits the distance traveled vs fare amount
    data. Regardless of distance, fare amounts generally stay at a fixed rate. If distance is strongly correlated to fare amounts, this may be influenced by 
    trips during peak periods that would increase fares during short trips.
  * What affects the frequency of the pickup and dropoff locations?
    Generally, wealthy residential areas and business sectors within NYC will carry the most frequent taxi users while low income areas tend to not take a taxi.
    Since areas in NYC are compact, the trip distance tends to be short (0-3 mi). 

#### Application of Knowledge:
   The best areas to get a taxi in NYC include Manhattan Midtown, Times Square, Madison Square, Upper East Side, and Union Square.
   These areas mostly consist of wealthy individuals and business centers which create a stable and consistent fare rate regardless
   of distance traveled. Typically, an individual would be able to get a taxi consistently during the hours of 5-7 PM with some frequency
   of pickups in the late morning between 8-11 AM. 

### Video Demonstration Link:
  * 

### Final Project Paper Link:
  * 

#### Tools Used: iPythonNotebook, WEKA, SQL, Python Scripts, JSON