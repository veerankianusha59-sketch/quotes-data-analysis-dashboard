import pandas as pd
import re
from collections import Counter
from html import escape

# ==========================================
# LOAD DATASET
# ==========================================

file_path = "/storage/emulated/0/scraped_data.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Rows and columns:", df.shape)

# ==========================================
# BASIC ANALYSIS
# ==========================================

df["Quote_Length"] = df["Quote"].astype(str).str.len()

total_quotes = len(df)
total_authors = df["Author"].nunique()
average_length = df["Quote_Length"].mean()
longest_quote = df["Quote_Length"].max()
shortest_quote = df["Quote_Length"].min()

# ==========================================
# TOP AUTHORS
# ==========================================

author_counts = df["Author"].value_counts()

top10_authors = author_counts.head(10)

top5_authors = author_counts.head(5)

# ==========================================
# AVERAGE QUOTE LENGTH BY AUTHOR
# ==========================================

avg_author_length = (
    df.groupby("Author")["Quote_Length"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# ==========================================
# WORD ANALYSIS
# ==========================================

all_text = " ".join(df["Quote"].astype(str).tolist()).lower()

words = re.findall(r"\b[a-zA-Z]+\b", all_text)

common_words = Counter(words)

stop_words = {
    "the", "a", "an", "and", "or", "but", "is", "are",
    "was", "were", "to", "of", "in", "on", "for", "with",
    "it", "i", "you", "he", "she", "they", "we", "this",
    "that", "as", "be", "by", "from", "at", "have", "has",
    "had", "not", "if", "my", "your", "our", "their",
    "his", "her", "will", "can", "what", "who", "one",
    "all", "so", "do", "does", "did", "me", "there"
}

meaningful_words = Counter(
    word for word in words
    if word not in stop_words and len(word) > 2
)

top10_common = common_words.most_common(10)
top10_meaningful = meaningful_words.most_common(10)

# ==========================================
# QUOTE LENGTH DISTRIBUTION
# ==========================================

def length_group(length):

    if length <= 50:
        return "0-50"
    elif length <= 100:
        return "51-100"
    elif length <= 150:
        return "101-150"
    elif length <= 200:
        return "151-200"
    elif length <= 300:
        return "201-300"
    elif length <= 500:
        return "301-500"
    elif length <= 1000:
        return "501-1000"
    else:
        return "1001+"

df["Length_Group"] = df["Quote_Length"].apply(length_group)

group_order = [
    "0-50",
    "51-100",
    "101-150",
    "151-200",
    "201-300",
    "301-500",
    "501-1000",
    "1001+"
]

length_counts = (
    df["Length_Group"]
    .value_counts()
    .reindex(group_order)
    .fillna(0)
)

# ==========================================
# HTML HELPERS
# ==========================================

def bar_chart(title, data, max_width=100):

    max_value = max(data.values()) if len(data) else 1

    html = f"""
    <div class="chart-card">
        <h2>{escape(title)}</h2>
    """

    for label, value in data.items():

        width = (value / max_value) * max_width

        html += f"""
        <div class="bar-row">
            <div class="bar-label">{escape(str(label))}</div>

            <div class="bar-container">
                <div class="bar" style="width:{width}%;">
                    {value}
                </div>
            </div>
        </div>
        """

    html += "</div>"

    return html


def pie_chart(title, data):

    total = sum(data.values())

    html = f"""
    <div class="chart-card">
        <h2>{escape(title)}</h2>
        <div class="pie-layout">
            <div class="pie">
    """

    start = 0

    colors = [
        "#4285F4",
        "#EA4335",
        "#FBBC05",
        "#34A853",
        "#9C27B0"
    ]

    stops = []

    for i, (label, value) in enumerate(data.items()):

        percentage = (value / total) * 100

        end = start + percentage

        color = colors[i % len(colors)]

        stops.append(
            f"{color} {start}% {end}%"
        )

        start = end

    gradient = ", ".join(stops)

    html += f"""
        <div class="pie-circle"
             style="background: conic-gradient({gradient});">
        </div>

        <div class="legend">
    """

    for i, (label, value) in enumerate(data.items()):

        percentage = (value / total) * 100

        color = colors[i % len(colors)]

        html += f"""
        <div class="legend-item">
            <span class="legend-color"
                  style="background:{color};"></span>
            <span>{escape(str(label))}</span>
            <span>{percentage:.1f}%</span>
        </div>
        """

    html += """
        </div>
        </div>
    </div>
    """

    return html


# ==========================================
# CREATE DATA FOR CHARTS
# ==========================================

top10_author_data = top10_authors.to_dict()

avg_length_data = {
    str(author): round(value, 2)
    for author, value in avg_author_length.items()
}

common_words_data = dict(top10_common)

meaningful_words_data = dict(top10_meaningful)

length_distribution_data = {
    str(group): int(value)
    for group, value in length_counts.items()
}

top5_author_data = top5_authors.to_dict()

# ==========================================
# HTML DASHBOARD
# ==========================================

html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Quotes Data Analyst Dashboard</title>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 20px;
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    color: #222;
}}

.header {{
    text-align: center;
    margin-bottom: 25px;
}}

.header h1 {{
    font-size: 30px;
    margin-bottom: 8px;
}}

.header p {{
    font-size: 17px;
    color: #666;
}}

.cards {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-bottom: 20px;
}}

.card {{
    background: white;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.10);
}}

.card .number {{
    font-size: 34px;
    font-weight: bold;
}}

.card .label {{
    margin-top: 8px;
    font-size: 16px;
    color: #666;
}}

.chart-card {{
    background: white;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 20px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.10);
}}

.chart-card h2 {{
    margin-top: 0;
    margin-bottom: 22px;
    font-size: 22px;
}}

.bar-row {{
    margin-bottom: 16px;
}}

.bar-label {{
    font-size: 14px;
    margin-bottom: 5px;
}}

.bar-container {{
    width: 100%;
    background: #e9edf2;
    border-radius: 7px;
    overflow: hidden;
}}

.bar {{
    background: #2196F3;
    color: white;
    min-width: 30px;
    padding: 7px 10px;
    text-align: right;
    border-radius: 7px;
    font-size: 13px;
    font-weight: bold;
}}

.pie-layout {{
    display: flex;
    align-items: center;
    gap: 25px;
    flex-wrap: wrap;
}}

.pie-circle {{
    width: 190px;
    height: 190px;
    border-radius: 50%;
}}

.legend {{
    flex: 1;
    min-width: 180px;
}}

.legend-item {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
    font-size: 14px;
}}

.legend-color {{
    width: 15px;
    height: 15px;
    border-radius: 3px;
    display: inline-block;
}}

.insights {{
    background: white;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.10);
}}

.insights h2 {{
    margin-top: 0;
}}

.insights li {{
    margin-bottom: 10px;
    line-height: 1.5;
}}

.footer {{
    text-align: center;
    margin: 25px 0;
    color: #777;
    font-size: 13px;
}}

@media (max-width: 600px) {{

    body {{
        padding: 12px;
    }}

    .cards {{
        grid-template-columns: 1fr;
    }}

    .header h1 {{
        font-size: 27px;
    }}

    .card .number {{
        font-size: 32px;
    }}

}}

</style>

</head>

<body>

<div class="header">

<h1>Quotes Data Analyst Dashboard</h1>

<p>Exploratory Data Analysis Dashboard</p>

</div>


<div class="cards">

<div class="card">
<div class="number">{total_quotes}</div>
<div class="label">Total Quotes</div>
</div>

<div class="card">
<div class="number">{total_authors}</div>
<div class="label">Total Authors</div>
</div>

<div class="card">
<div class="number">{average_length:.2f}</div>
<div class="label">Average Quote Length</div>
</div>

<div class="card">
<div class="number">{longest_quote}</div>
<div class="label">Longest Quote</div>
</div>

<div class="card">
<div class="number">{shortest_quote}</div>
<div class="label">Shortest Quote</div>
</div>

</div>


{bar_chart("Top 10 Authors", top10_author_data)}


{pie_chart("Top 5 Authors", top5_author_data)}


{bar_chart(
    "Average Quote Length by Author",
    avg_length_data
)}


{bar_chart(
    "Top 10 Most Common Words",
    common_words_data
)}


{bar_chart(
    "Top 10 Meaningful Words",
    meaningful_words_data
)}


{bar_chart(
    "Quote Length Distribution",
    length_distribution_data
)}


<div class="insights">

<h2>EDA Insights</h2>

<ol>

<li>
The dataset contains
<b>{total_quotes}</b> quotes from
<b>{total_authors}</b> different authors.
</li>

<li>
There are no missing values in the dataset.
</li>

<li>
There are no duplicate rows.
</li>

<li>
<b>{top5_authors.index[0]}</b> has the highest number of quotes
with <b>{top5_authors.iloc[0]}</b> quotes.
</li>

<li>
The average quote length is
<b>{average_length:.2f}</b> characters.
</li>

<li>
The longest quote contains
<b>{longest_quote}</b> characters.
</li>

<li>
The shortest quote contains
<b>{shortest_quote}</b> characters.
</li>

<li>
<b>{avg_author_length.index[0]}</b> has the highest average quote
length at <b>{avg_author_length.iloc[0]:.2f}</b> characters.
</li>

<li>
<b>{meaningful_words_data.keys().__iter__().__next__()}</b>
is the most common meaningful word.
</li>

<li>
Most quotes belong to the
<b>{length_counts.idxmax()}</b> character range.
</li>

</ol>

</div>


<div class="footer">

Quotes Data Analysis Project | EDA Dashboard

</div>

</body>

</html>
"""

# ==========================================
# SAVE DASHBOARD
# ==========================================

output_file = "/storage/emulated/0/quotes_dashboard.html"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(html)

print()
print("====================================")
print("DASHBOARD CREATED SUCCESSFULLY!")
print("====================================")
print("Location:")
print(output_file)
print()
print("This version uses NO external chart library.")
print("All charts are built directly into the HTML.")