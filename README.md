# Overview

For this project, I watned to try my hand at some basic data analysis. I wanted to do this because I thiunk it would be useful for me to be familiar with
some basic data analysis skills, that I can hopefully build, upon, if needed, in the future. 

I went to ```kaggle.com``` and found a dataset about laptops that looked interesting enough. It has a ton of columns that cover different information
about the laptops, and it also has nearly 1000 entries, so the data is not super small. The last 2 digits of any price represent the cent values, but there is no commas to show that, so prices may appear larger than they actually are. 
This is where I downloaded it from:
[Brand Laptops Dataset](https://www.kaggle.com/datasets/bhavikjikadara/brand-laptops-dataset?resource=download)

Below is a brief video that goes over the program and dataset.

[Software Demo Video](https://youtu.be/Ii2GjiuMhzs)

# Data Analysis Results

1. What is the count of each processor brand in this dataset?
 * Intel: 705
 * AMD: 267
 * Apple: 15
 * Other: 4

2. What are the results for showing laptoops with a certain processor brand and below a certain price?
 * This depends on the processor brand that is chosen and the maximum price.
 * I used AMD and a price roof of 22000.
 * There are 4 latops that match these criteria.

3. What are the 5 most expensive (or cheap) laptops?
 * This depends on if you want to see the cheapest or the most expensive laptops.
* Cheapest:
   * iBall Exeleance CompBook (9800)
   * Ultimus Pro (11990)
   * Primebook (12990)
   * Jio JioBook (14701)
   * Ultimus Lite (14990)

* Most Expensive:
  * Dell Alienware X16 (454490)
  * Dell Alienware M18 R1 2023 (450990)
  * MSI CreatorPro Z16 HX (449990)
  * Apple MacBook Pro 16 2023 (399900)
  * Dell Alienware X16 R1 (388490)


# Development Environment

I used Microsoft Visual Studio Code to make this.

I used the ```Python``` prgoramming language with the ```Pandas``` library for data analysis,

# Useful Websites

Below are the 2 main sites I used for help in this project.
* [towardsdatascience.com](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)
* [pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min)

# Future Work

Below is a list of things that I think I could do better or change.
* Let the user choose what processor brands to use
* Let the user decide what price to use as well
* Fix the price column, so that it is formatted better (last 2 digits are the cents value, but it might not appear that way)