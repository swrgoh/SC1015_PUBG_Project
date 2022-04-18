# Mini-Project for SC1015 Introduction to Data Science and Artificial Intelligence
---
## Introduction
The gaming industry is a prime area for data exploration and extraction due to massive datasets and online characteristics. We can get great insight on the decision-making and logic that individual players experience and utilize when put in hypothetical and virtual scenarios like games.

![alt text](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/image_folder/PUBG.jpg "Source: https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/")

In this project, we provide over 13,000,000 player data inputs from the popular game PlayerUnknown's Battlegrounds. The relevant data presented was extracted from the website [pubg.op.gg](http://pubg.op.gg), a game tracker website that directly collects data from PlayerUnknown's Battleground's API. We proceed to explore and visualize this data, and further create predictive models (INSERT WHAT TYPE OF MODEL HERE @FRASER).



---
### This repository consists of 4 main folders
###  - [Data Scraping from website PUBG.OP.GG](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/1_Collect_Scrape_Data)
>Notebooks of Data Scraping utilizing Multiprocessing
>| Step | Brief Summary |
>| --- | ---|
>| 1A |[Collecting player list through a few initial "seeds", finding other players they play with and recusively adding to player list](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/1a_data_player_scrape.ipynb)|
>|1B| [Using 50k discrete player names to recusrively search their match history, and returning data from all players within each match](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/1b_data_match_detail_scrape.ipynb)|
>|2| [Helper script written in Python 3.0, utilizing **multiprocessing** & **chunking** to speed up data collection process](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/1_Collect_Scrape_Data/2_helper.py) |
#### 
###  - [Data Cleaning and Separation](https://github.com/Gyanroh/SC1015_PUBG_Project/tree/main/2_Cleaning_Data)
>Notebooks of Cleaning up Scraped Data for Further Use
>| Step | Brief Summary |
>| --- | ---| 
>| 1 | [Combination of data chunks from scraping process & initial cleaning](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/2_Cleaning_Data/1_data_combination_initial_observation.ipynb) |
>|2A | [Comprehensive cleaning of General Data with analysis, further utilizing **Feature Scaling** to re-represent win conditions](https://github.com/Gyanroh/SC1015_PUBG_Project/blob/main/2_Cleaning_Data/2a_comprehensive_data_cleaning_erangel_gen.ipynb)|
#### 

###  - [Data Visualization Heatmap for Deaths](https://github.com/yeotzunkai/CS1015MiniProject-DataScience_Python/blob/main/DSAI%20Project/Model/Price_Predictor.ipynb)
     Contains Notebooks of Using Data to Identify Dangerous Areas 
#### 

###  - [Regression & Machine Learning](https://github.com/yeotzunkai/CS1015MiniProject-DataScience_Python/tree/main/DSAI%20Project/Dataset)
     Using Matchdata to Determine Winning Probability and Determining Critical Factors for Winning
---
| Folder | ==Brief Description== |
| ----------- | ----------- |
| test| trial |
| Paragraph | Text |
