# Gecko_sport_academic_project
This repository contains files for the group project for the exam Big Data within the Master BIBDA - Unimib



***Intro to the project***

The project aim was trying to retrieve data from 4 sport store websites for the Running and trying to cluster items in technical, ecological, eccentric and social classes.
After clustering these items, a Python GUI using was created to interact with users and assign them the same cluster of the items scraped. In this way an user can have all in one place a dynamic list to shop, close to his/her interests and coming from multiple sources.

***Folders and file***
1. Ingestion: in this folder there are Colabs used for each website to scrape date with ***Selenium***
2. Machine_learning_for_technical_cluster_and_Twitter_social: in this folder there are colabs used for Machine Learning in ***DataBricks*** to assign technical Cluster to items using TF-IDF and Naive Bayes algorithms and another Colab used to catch sentiment on Twitter by counting # and @ of brands from 01/01/2020 to 31/07/2020 in order to assign social cluster;
3. Fact_table_DQ_SQL_GUI_Tkinter: in this folder there are:
  1. DB_unificato_v1.sql : factual table stored as sqlite DB used as DB for tkinter GUI
  2. Project_v2.py: python code to create tkinter GUI
  3. Here you can donwload and unzip the images in the same project folder in order to let the GUI work: https://drive.google.com/file/d/1NR3kKIuCagmA3f9fUNR2GyJY1JkXfsJL/view
4. Here the link for Tableau Visualization of the products: https://public.tableau.com/profile/giulia1439#!/vizhome/sportviewok/Dashboard5
 
 
 ***Tips***
 To let the tkinter GUI working rembember to change the path where images are saved in the code and be sure you have the PIL library installed
 
