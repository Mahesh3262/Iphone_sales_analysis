# let’s import the necessary Python libraries and the dataset to get started with the task of iPhone sales analysis.
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:\\apple_products.csv")
print(data.head())


# let’s have a quick look at whether this dataset contains any null values or not.
print(data.isnull().sum())

#let’s have a look at the descriptive statistics of the data.
print(data.describe())

# I will create a new dataframe by storing all the data about the top 10 highest-rated iPhones in India on Flipkart.
highest_rated = data.sort_values(by=["Star Rating"],
                                 ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])


# let’s have a look at the number of ratings of the highest-rated iPhones on Flipkart.
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label,
                y = counts,
            title="Number of Ratings of Highest Rated iPhones")
figure.show()


# let’s have a look at the number of reviews of the highest-rated iPhones on Flipkart.
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label,
                y = counts,
            title="Number of Reviews of Highest Rated iPhones")
figure.show()


# Now let’s have a look at the relationship between the sale price of iPhones and their ratings on Flipkart.
figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Sale Price", size="Discount Percentage",
                    trendline="ols",
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()


# let’s have a look at the relationship between the discount percentage on iPhones on Flipkart and the number of ratings
figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price",
                    trendline="ols",
                    title="Relationship between Discount Percentage and Number of Ratings of iPhones")
figure.show()


# By Analysing the given iphone sales data the takeaways are:
    #APPLE iPhone 8 Plus (Gold, 64 GB) was the most appreciated iPhone in India.
    #iPhones with lower sale prices are sold more in India.
    #iPhones with high discounts are sold more in India.
