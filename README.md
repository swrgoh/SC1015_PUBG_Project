# Mini-Project for SC1015 Introduction to Data Science and Artificial Intelligence
---
## Introduction
The gaming industry is a prime area for data exploration and extraction due to massive datasets and online characteristics. We can get great insight into the decision-making and logic that individual players experience and utilize when put in hypothetical and virtual scenarios like games.

![alt text](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/image_folder/PUBG.jpg "Source: https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/")

This project provides over 13,000,000 player data inputs from the popular game PlayerUnknown's Battlegrounds. The relevant data presented was extracted from the website [pubg.op.gg](http://pubg.op.gg), a game tracker website that directly collects data from PlayerUnknown's Battleground's API. We proceed to explore and visualize this data and further create predictive models to better understand more optimal styles of gameplay.

 ![PUBG TEAM](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/image_folder/PUBG%20Team%20demo.gif)

---
<br />
<br />
<br />
<br />
<br />

# Motivation
Our group is tired of always loosing our PUBG games, as we spend too much time studying and do not have much free time to practice shooting, driving ect. in game.<br>
We want to use Data Science and Machine Learning to win more games.<br>
#### Main issues that cause us to loose our games & questions derived from them:
>| In-Game issues that our team faced | Problem Definition / Question we develop|
>| --- | --- |
>| We always enter highly contested areas that cause us to die | **A) Are there specific areas players should avoid?** |
>| Our group keeps on getting instantly killed by high-powered sniper rifles | **B) Are there specific ways to avoid or reduce chances of getting sniped?** |
>| We don't know what is the best strategy to survive | **C) What are the factors that help a player win more?** |


---
<br />
<br />
<br />
<br />
<br />

# This repository consists of 4 main folders
>##   [1) Data Scraping from website PUBG.OP.GG](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/1_Collect_Scrape_Data)
>Notebooks of Data Scraping utilizing Multiprocessing
>| Step | Brief Summary |
>| --- | ---|
>| 1A |[Collecting player list through a few initial "seeds", finding other players they play with and recusively adding to player list](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/1a_data_player_scrape.ipynb)<br>**Requires json & requests library**|
>|1B| [Using 50k discrete player names to recusrively search their match history, and returning data from all players within each match](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/1b_data_match_detail_scrape.ipynb)<br>**Requires json & requests library**|
>|2| [Helper script written in Python 3.0, utilizing **multiprocessing** & **chunking** to speed up data collection process](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/2_helper.py) <br>**Important helper fiile for multithreading and HTTP linking**|
>#### <br>
>
>##   [2) Data Cleaning and Separation](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/2_Cleaning_Data)
>Notebooks of Cleaning up Scraped Data for Further Use
>| Step | Brief Summary |
>| --- | ---| 
>| 1 | [Combination of data chunks from scraping process & initial cleaning](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/2_Cleaning_Data/1_data_combination_initial_observation.ipynb) <br>**Requires OS & Glob library**|
>|2A | [Comprehensive cleaning of **General Data component** with analysis, further utilizing **Feature Scaling** to re-represent win conditions](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/2_Cleaning_Data/2_comprehensive_data_cleaning_erangel_gen.ipynb)<br> Also removes anomalous data generated from cheaters using third-party tools to gain unfair advantage|
>#### <br>
>
>##   [3) Data Visualization, Map Heatmap Visualization for Deaths](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/3_Map_%26_General_Visualization)
>Contains Notebooks of Using Data to Identify Dangerous Areas 
>| Step | Brief Summary |
>| ----------- | ----------- |
>| 1| [Dynamically generate heatmap with **User Input** to generate heat map of **Danger Areas**](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/1_heatmap_visualisation.ipynb) <br> **Requires ipywidgets, re, HTML & PIL libraries**|
>| 2 | [Kills per Distance by weapon type](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/2_kill_distance_weapon_type.ipynb) |
>   #### Example of Heatmap 
> [![Demo Doccou alpha](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/sniper.gif)](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/1_heatmap_visualisation.ipynb)
> #### Chart Statistic
> ![alt text](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/image_folder/death-distance-weap-chart.png)
>#### <br>
>
>##   [4) Regression & Machine Learning](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/4_Models_and_Analysis)
> Using Matchdata to Determine Winning Probability and Determining Critical Factors for Winning
>| Step | Brief Summary |
>| --- | ---| 
>| 1A | [Gradient Boosting to Explore Possible Correlation For General Information Dataset](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/1a_gradient_boosting.ipynb)<br> **Resulting Correlation Score at 0.7866** |
>| 1B | [K-Nearest Neighbour Analysis to select Predictor Feature For Linear Regression](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/1b_K-Nearest_neighbour.ipynb)<br> **Resulting R2 value at 0.8835** |
>| 1C | [eXtreme Gradient Boosting, check if possible for direct gradient regression](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/1c_eXtreme_Grad_Boost.ipynb)<br> **Resulting R2 value at 0.7777** |
>|2 | [Linear Regression on General Information Dataset to Produce Reasoned Deductions](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/2_linear_regression_model.ipynb)<br> **Conclusions Below**|
>|3 | [Random Forest Classification on Distance for Sniper Rifle Avoidance Strategy](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/3_sniper_forest_classification_tree.ipynb)<br>**Conclusions Below**|
>### Conclusions of Linear Regression
>We set up the model to have 7 predictors. We can utilize their coefficients to determining how much impact one value will have on a player's winning chances
>| Predictor | Coefficient | Unit|  Observation and Thoughts |
>| --- | --- | --- | --- |
>|`game_size `         |**0.0289%** | per player|  With a smaller pool of players, it makes sense that a player will have higher chances of winning  <br>~|
>|`player_survive_time`| **0.038%** |per second| Every minute, a player's chances of winning increases by **2.28%!**<br>~|
>|`player_dmg `        |**0.0013%** |per 1 damage dealt| A single bullet from a AK-47 deals 47 damage. Hitting 30 bullets increases winning chance by **1.833%**<br>~|
>|`player_dbno   `     | **-15%**| per knockdown| Every knockdown reduces a players winning chance by a significant margin <br> ~  |
>|`player_dist_walk`   | **0.002%** |per meter walked |   Every **km** a player walks, his chance of winning increases by **2%**<br>~|
>|`player_dist_ride`   |  **0.005%**| per distance driven | Every **km** a player drives, his chance of winning increases by **5%**! <br>This is much better than walking |
>|`player_kills `      |**8.103%**| per kill| Wow! In PUBG, there are many strategies players use. <br>One strategy is avoiding fights, and the other is actively hunting people to kill.<br>This data reveals that it is extremely worthwhile to go for kills, as one single kill increases your chance of winning by **8%**|
>### Conclusions of Random Forest
>#### 4-Deep Tree Structure
>High Caliber Sniper Rifles are instant-kill for headshot type damage. This results in the **most dangerous** item in the game.<br>
>After **39.818m**, neighbouring gini coefficient is at **0.499**. This means there is a 49.9% / 50.1% chance that the player may be killed by a sniper rifle.
At this distance, if you do not have proper armour, protection or methods to deal with snipers, **Strictly keep inside buildings!**
---
### Contributors
🤖 [Ryan Goh / Gyanroh](https://github.com/Gyanroh) - Data Scraping, Multithreading, Data Preparation, Predictive Modeling, Distance Visualization<br>
🤖 [Kai / SlothKai](https://github.com/SlothKai) - Heatmap Visualization, User-interface implimentation, Histogram Preparation<br>
🤖 [Fraser / FCWX](https://github.com/Fcwx) - HTTP implimentation, Basic Visualization, Slides and Video Editing<br>


#### <br>
---

