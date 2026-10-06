# quotes-data-analysis-dashboard
Data analysis and visualization of 100 quotes using Python
Quotes Data Analysis and Visualization Dashboard

Project Overview

This project performs Data Analysis and Visualization on a dataset containing 100 quotes collected from different authors.

The project uses Python to clean, analyze, and visualize the quote data. An interactive HTML dashboard was also created to present the important findings in an easy-to-understand format.

Objectives

- Analyze the quotes dataset.
- Identify the most common authors.
- Calculate quote lengths.
- Find the average quote length by author.
- Identify the most common words.
- Analyze the distribution of quote lengths.
- Create meaningful visualizations.
- Build an interactive data analysis dashboard.

Dataset

The dataset contains two columns:

Column| Description
"Quote"| The text of the quote
"Author"| The author of the quote

Dataset Summary

- Total Quotes: 100
- Total Authors: 50
- Missing Values: 0
- Duplicate Rows: 0
- Average Quote Length: 122.27 characters
- Longest Quote: 1084 characters
- Shortest Quote: 34 characters

Technologies Used

- Python
- Pandas
- HTML
- CSS
- JavaScript
- Pydroid 3
- GitHub

Data Analysis

The following analysis was performed:

1. Author Analysis

Albert Einstein has the highest number of quotes in the dataset with 10 quotes, followed by:

1. Albert Einstein - 10
2. J.K. Rowling - 9
3. Marilyn Monroe - 7
4. Dr. Seuss - 6
5. Mark Twain - 6

2. Quote Length Analysis

The average quote length is 122.27 characters.

The longest quote contains 1084 characters, while the shortest quote contains 34 characters.

3. Average Quote Length by Author

The authors with the highest average quote length are:

1. Pablo Neruda - 319 characters
2. Bob Marley - 286.33 characters
3. J.D. Salinger - 241 characters
4. Marilyn Monroe - 240.86 characters
5. Elie Wiesel - 224 characters

4. Common Words

The most common words in the dataset include:

- you - 103
- the - 75
- to - 75
- is - 69
- a - 69
- it - 58
- i - 58
- of - 49
- and - 48
- not - 36

5. Meaningful Words

After removing common words, love was the most common meaningful word with 23 occurrences.

Other frequently occurring meaningful words include:

- can
- who
- will
- what
- one
- all
- never
- she
- life

Visualizations

The project includes the following visualizations:

- Top 10 Authors
- Average Quote Length by Author
- Top 10 Most Meaningful Words
- Quote Length Distribution
- Top 10 Most Common Words
- Top Authors by Average Quote Length
- Top 5 Authors Pie Chart

Dashboard

An HTML dashboard was created to present the main analysis results in one place.

Dashboard Features

- Dataset summary
- Total quotes
- Total authors
- Average quote length
- Most common author
- Most common meaningful word
- Author analysis
- Quote length analysis
- Word frequency analysis
- Interactive visualizations

EDA Insights

The main findings from the exploratory data analysis are:

1. The dataset contains 100 quotes from 50 authors.
2. There are no missing values.
3. There are no duplicate rows.
4. Albert Einstein has the highest number of quotes.
5. The average quote length is 122.27 characters.
6. The longest quote contains 1084 characters.
7. The shortest quote contains 34 characters.
8. Pablo Neruda has the highest average quote length.
9. "love" is the most common meaningful word.
10. Most quotes belong to the 51-100 character length group.

Project Files

Quotes-Data-Analysis/
│
├── scraped_data.csv
├── dashboard.py
├── quotes_dashboard.html
└── README.md

File Description

scraped_data.csv
Contains the original quotes and author information used for analysis.

dashboard.py
Python source code used to perform data analysis and generate the dashboard.

quotes_dashboard.html
HTML dashboard containing the final visualizations and analysis results.

README.md
Project documentation and summary.

How to Run the Project

Step 1: Install Python Libraries

Install Pandas if required:

pip install pandas

Step 2: Place the Dataset

Keep "scraped_data.csv" in the same folder as the Python program.

Step 3: Run the Python Program

Run:

python dashboard.py

The program will analyze the dataset and create the dashboard.

Step 4: Open the Dashboard

Open:

quotes_dashboard.html

in a web browser.

Conclusion

This project demonstrates the complete basic Data Analysis workflow, including dataset loading, data validation, exploratory data analysis, text analysis, statistical calculations, visualization, and dashboard creation.

The project helped identify patterns in quote authorship, quote length, and word usage while presenting the results through an easy-to-understand dashboard.

Future Improvements

- Add more quote datasets.
- Add more interactive filters.
- Add author-based search.
- Add additional charts.
- Deploy the dashboard online.
- Add automated data collection.
- Improve dashboard design and responsiveness.

Author

Anusha Veeranki

B.Tech - Computer Science and Engineering
Data Analytics Enthusiast
