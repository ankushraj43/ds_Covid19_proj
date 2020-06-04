# Impact of Corona Virus(Covid - 19) in India: Project Overview 
***
* Coronavirus or COVID-19 needs no introduction. It has already been declared as a pandemic by WHO and in past couple of weeks it’s impact has been disasterous from both health perspective and an economic one. 
* As of now, most of us are staying and working from home to avoid the spread of corona virus. I decided to utilize the surplus time to write a Python Script that pulls the latest Statewise data of COVID-19 cases from the official website of Ministry of Health and Family Welfare, Government of India and turning it into insightful visualizations using popular Python packages.


## Code and Resources Used 
***
**Python Version:** 3.7  
**Packages:** pandas, numpy, matplotlib, beautifulsoup, requests, GeoPandas, PrettyTable and seaborn  


## Web Scraping and Parsing
***
* Made the web scraper using the request library and scraped the data given on the website. 
* Fetching and parsing out the data using Beautifulsoup library, further removing the rows having the 'nan' values and the rows which were not useful.
* Also, converted the object data type or string data type features to integer type.
* Saving the data in csv file format and used this tabulated data to make visualizations using Seaborn/Matplotlib libraries.

## EDA
***
Having a look at the distributions of the data and the value counts for the various variables on the dataframe. I made the following visuals which will be much easier to understand the impact of this pandemic:

* Plotting horizontal barplot to show the statewise total confirmed cases -
***
![alt text](https://github.com/ankushraj43/ds_Covid19_proj/blob/master/bar_chart.png "Statewise confirmed cases on a bar chart")

* Donut Chart — Nationwide total Confirmed, Recovered and Deceased cases -
***
![alt text](https://github.com/ankushraj43/ds_Covid19_proj/blob/master/donut_chart.png "Distribution of cases on a donut chart")

* Chloropleth map of the total Confirmed Cases -
***
![alt text](https://github.com/ankushraj43/ds_Covid19_proj/blob/master/map.png "Cases on the Indian Map")

|Total confirmed cases|Active|Recovered|Deaths|
|---------|---------|----------|------|
|207615|101497|100303|5815|

# Updated till 3rd June, 2020.
