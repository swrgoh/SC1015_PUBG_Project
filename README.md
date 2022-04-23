# Mini-Project for SC1015 Introduction to Data Science and Artificial Intelligence
---
## Introduction
The gaming industry is a prime area for data exploration and extraction due to massive datasets and online characteristics. We can get great insight on the decision-making and logic that individual players experience and utilize when put in hypothetical and virtual scenarios like games.

![alt text](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/image_folder/PUBG.jpg "Source: https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/")

In this project, we provide over 13,000,000 player data inputs from the popular game PlayerUnknown's Battlegrounds. The relevant data presented was extracted from the website [pubg.op.gg](http://pubg.op.gg), a game tracker website that directly collects data from PlayerUnknown's Battleground's API. We proceed to explore and visualize this data, and further create predictive models to better understand more optimal styles of gameplay.





---
### This repository consists of 4 main folders
##  - [1) Data Scraping from website PUBG.OP.GG](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/1_Collect_Scrape_Data)
>Notebooks of Data Scraping utilizing Multiprocessing
>| Step | Brief Summary |
>| --- | ---|
>| 1A |[Collecting player list through a few initial "seeds", finding other players they play with and recusively adding to player list](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/1a_data_player_scrape.ipynb)<br>**Requires json & requests library**|
>|1B| [Using 50k discrete player names to recusrively search their match history, and returning data from all players within each match](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/1b_data_match_detail_scrape.ipynb)<br>**Requires json & requests library**|
>|2| [Helper script written in Python 3.0, utilizing **multiprocessing** & **chunking** to speed up data collection process](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/2_helper.py) <br>**Important helper fiile for multithreading and HTTP linking**|
#### <br>

##  - [2) Data Cleaning and Separation](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/2_Cleaning_Data)
>Notebooks of Cleaning up Scraped Data for Further Use
>| Step | Brief Summary |
>| --- | ---| 
>| 1 | [Combination of data chunks from scraping process & initial cleaning](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/2_Cleaning_Data/1_data_combination_initial_observation.ipynb) |
>|2A | [Comprehensive cleaning of General Data with analysis, further utilizing **Feature Scaling** to re-represent win conditions](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/2_Cleaning_Data/2a_comprehensive_data_cleaning_erangel_gen.ipynb)|
#### <br>

##  - [3) Data Visualization, Map Heatmap Visualization for Deaths](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/3_Map_%26_General_Visualization)
>Contains Notebooks of Using Data to Identify Dangerous Areas 
>| Step | Brief Summary |
>| ----------- | ----------- |
>| 1| [Dynamically generate heatmap with **User Input** to generate heat map of **Danger Areas**](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/1_heatmap_visualisation.ipynb) |
>| 2 | [Kills per Distance by weapon type](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/2_kill_distance_weapon_type.ipynb) |
>   ##### Example of Heatmap 
> [![Demo Doccou alpha](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/sniper.gif)](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/3_Map_%26_General_Visualization/1_heatmap_visualisation.ipynb)
#### <br>

##  - [4) Regression & Machine Learning](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/4_Models_and_Analysis)
> Using Matchdata to Determine Winning Probability and Determining Critical Factors for Winning
>| Step | Brief Summary |
>| --- | ---| 
>| 1A | [Gradient Boosting to Explore Possible Correlation For General Information Dataset](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/1a_gradient_boosting.ipynb) |
>|1B | [Linear Regression on General Information Dataset to Produce Reasoned Deductions](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/1b_linear_regression_model.ipynb)|
>|2 | [Random Forest Classification on Distance for Sniper Rifle Avoidiance Strategy](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/4_Models_and_Analysis/2_sniper_classification_tree.ipynb)|
#### <br>
---

