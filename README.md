# Exploratory-Data-Analysis
Projects performing exploratory analysis on various datasets available in kaggle

1. Boston Housing Dataset: This dataset contains information collected by the U.S Census Service concerning housing in the area of Boston Mass.

![boston](https://github.com/Riwaj22/Exploratory-Data-Analysis/assets/99485058/2823b70c-3035-40f1-8bd3-f95e262d0e18)


2. Titanic Dataset: This dataset contains detailed explanantion of survived and unsurvived in titanic(the unsinkable ship)


![download](https://github.com/Riwaj22/Exploratory-Data-Analysis/assets/99485058/b42079cb-28d9-419b-ac11-bd827d74cce5)


3: Covid 19 dataset:
It contains preprocessed dataset where:
a.Countrywise data <br>
b. daywise data

4: Womens E commerce clothing reviews:  Women’s Clothing E-Commerce dataset revolving around the reviews written by customers. Its nine supportive features offer a great environment to parse out the text through its multiple dimensions

This dataset includes 23486 rows and 10 feature variables. Each row corresponds to a customer review, and includes the variables:

Clothing ID: Integer Categorical variable that refers to the specific piece being reviewed.<br>
Age: Positive Integer variable of the reviewers age. <br>
Title: String variable for the title of the review. <br>
Review Text: String variable for the review body. <br>
Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1 Worst, to 5 Best. <br>
Recommended IND: Binary variable stating where the customer recommends the product where 1 is recommended, 0 is not recommended. <br>
Positive Feedback Count: Positive Integer documenting the number of other customers who found this review positive. <br>
Division Name: Categorical name of the product high level division. <br>
Department Name: Categorical name of the product department name. <br>
Class Name: Categorical name of the product class name. <br>

Packages used: <br>
a. nltk <br>
b. plotly <br>
c. cufflinks <br>
d. missingno <br>

5: IPL dataset: All Indian Premier League Cricket matches between 2008 and 2022.

This is the ball by ball data of all the IPL cricket matches till season 13.The dataset contains 2 files: deliveries.csv and matches.csv.



matches.csv contains details related to the match such as location, contesting teams, umpires, results, etc. <br>
Match ID: A unique identifier for each match. <br>
Date: The date on which the match took place.<br>
Team 1: The name or identifier of the first team participating in the match.<br>
Team 2: The name or identifier of the second team participating in the match.<br>
Venue: The location or venue where the match was played.<br>
Umpire 1: The name or identifier of the first umpire officiating the match.<br>
Umpire 2: The name or identifier of the second umpire officiating the match.<br>
Result: The outcome or result of the match, such as "Team 1 won," "Team 2 won," or "Match tied."<br>
Winner: The name or identifier of the winning team.<br>
Win by runs: The margin of victory for the winning team, measured in runs.<br>
Win by wickets: The margin of victory for the winning team, measured in wickets.<br>
Player of the Match: The name or identifier of the player who was awarded the "Player of the Match" title.<br>

deliveries.csv is the ball-by-ball data of all the IPL matches including data of the batting team, batsman, bowler, non-striker, runs scored, etc.

Match ID: A unique identifier for each match. <br>
Inning: Indicates whether the delivery belongs to the first or second inning of the match. <br>
Batting Team: The name or identifier of the team that is currently batting. <br>
Bowling Team: The name or identifier of the team that is currently bowling. <br>
Over: The specific over number in which the delivery was bowled. <br>
Ball: The ball number within the over. <br>
Batsman: The name or identifier of the batsman facing the delivery. <br>
Non-Striker: The name or identifier of the non-striker at the time of the delivery. <br>
Bowler: The name or identifier of the bowler delivering the ball. <br>
Is Super Over: Indicates whether the delivery belongs to a super over, which is a tiebreaker in case of a draw. <br>
Wide Runs: The number of runs scored as extras due to a wide delivery. <br>
Bye Runs: The number of runs scored as extras due to a bye, where the batsman doesn't make contact with the ball. <br>
Leg Bye Runs: The number of runs scored as extras due to a leg bye, where the ball hits the batsman's body or gear. <br>
No Ball Runs: The number of runs scored as extras due to a no-ball, where the bowler oversteps the crease or delivers a illegal delivery. <br>
Penalty Runs: The number of runs awarded to the batting team as a penalty for the bowling team's misconduct. <br>
Batsman Runs: The number of runs scored by the batsman off the delivery. <br>
Extra Runs: The total number of runs scored as extras (Wide Runs + Bye Runs + Leg Bye Runs + No Ball Runs + Penalty Runs). <br>
Total Runs: The total runs scored off the delivery (Batsman Runs + Extra Runs).<br>
Player Dismissed: The name or identifier of the batsman who got dismissed on the delivery (if applicable).<br>
Dismissal Kind: The type of dismissal if the batsman got out on the delivery (e.g., caught, bowled, run out).<br>
Fielder: The name or identifier of the fielder involved in the dismissal (if applicable). <br>

6:Fifa World Cup Dataset: 
Contains 3 dataset namely Worldcupmatches, WorldCupPlayers and WorldCups

WorldCupMatches detailed explanation:

Year: The year in which the match took place. <br>
Datetime: The date and time of the match. <br>
Stage: The stage of the tournament in which the match was played (e.g., group stage, knockout stage).<br>
Stadium: The name of the stadium where the match was held.<br>
City: The city where the stadium is located.<br>
Home Team Name: The name of the home team.<br>
Home Team Goals: The number of goals scored by the home team in the match.<br>
Away Team Goals: The number of goals scored by the away team in the match.<br>
Away Team Name: The name of the away team.<br>
Win conditions: The conditions under which the winning team was determined (e.g., regular time, extra time, penalty shootout).<br>
Attendance: The number of spectators present at the match.<br>
Half-time Home Goals: The number of goals scored by the home team at half-time.<br>
Half-time Away Goals: The number of goals scored by the away team at half-time.<br>
Referee: The name of the referee officiating the match.<br>
Assistant 1: The name of the first assistant referee.<br>
Assistant 2: The name of the second assistant referee.<br>
RoundID: A unique identifier for the round of the tournament.<br>
MatchID: A unique identifier for the match.<br>
Home Team Initials: The three-letter initials of the home team.<br>
Away Team Initials: The three-letter initials of the away team.<br>



