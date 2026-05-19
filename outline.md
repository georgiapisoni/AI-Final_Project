# Movie Success: commercial and critical success analysis

## 1. Project idea

How do different definitions of movie success compare; is revenue by itself a sufficient measure of success?
Different forms of movie success:

- Commercial: high revenue
- Financial: high profit
- Investment efficiency: high return on investment
- Audience: high user rating; high popularity
- Visual marketing: distinctive poster design     //optional for now

## 3. Sub-questions

### 3.1 Commercial and financial success

- Do higher-budget movies generate higher revenue?
- Which movies generate the highest profit?
- Which movies generate the highest return on investment?
- Are the most profitable movies also the most efficient investments?

### 3.2 Audience success

- Are high-revenue movies also highly rated?
- Are highly rated movies always commercially successful?
- Which movies are highly rated but commercially modest?
- Which movies are commercially successful but poorly rated?

### 3.3 Product characteristics

- Does runtime relate to revenue?
- Does runtime relate to rating?
- Do successful movies cluster around specific runtime ranges?
- Do successful movies differ across release periods?

### 3.4 Content patterns

- Which genres are most common among high-revenue movies?
- Which genres are most common among high-ROI movies?
- Which keywords appear more often among high-revenue or highly rated movies?
- Are some themes associated with commercial success but not with audience ratings?

### 3.5 Poster design and visual marketing    //optional

- Do high-revenue movies have different poster features from highly rated movies?
- Are poster brightness, contrast, and saturation associated with revenue, popularity, or rating?
- Do commercially successful movies have more visually intense posters?
- Are poster features different across genres or decades?

## 4. Dataset

The project uses the TMDB Movies Dataset 2023 from Kaggle.
https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies

## Project steps
## 1. Code
### 1.1 Data loading
- Load w/ pandas.
- Inspect number of rows and columns.
- Check column types.
- Check missing values.
- Identify which variables are useful
- Save a smaller working dataset

### 1.2 Data cleaning
- Keep only released movies.
- Convert release_date to datetime.
- Extract release_year and decade.
- Convert budget, revenue, runtime, vote_average, vote_count, and popularity to numeric format.
- Remove or flag movies with missing or invalid financial data.
- Treat budget = 0 and revenue = 0 as missing for financial analysis.
- Remove movies with runtime <= 0.
- Apply a minimum vote_count threshold for rating analysis.
- Remove extreme or unrealistic values if necessary.

### 1.3 Data transformations
calculate:
- profit = revenue - budget
- roi = profit / budget
- log_budget = log10(budget)
- log_revenue = log10(revenue)
- log_profit = log10(profit), only where profit > 0
var
- release_year
- decade
- runtime_group
- budget_group
- revenue_group
- rating_group
- success_category

runtime bins: (see w/ dataset later what's relevant)

- Under 80 minutes
- 80-100 minutes
- 100-120 minutes
- 120-150 minutes
- Over 150 minutes

year bins groups:

- Before 1980
- 1980s
- 1990s
- 2000s
- 2010s
- 2020s

success categories:       //necessary/relevant????

- Blockbuster: high budget and high revenue
- Surprise hit: low or medium budget and high ROI
- Money pit: high budget and low or negative ROI
- Hidden gem: high rating and low or moderate revenue
- Overhyped: high revenue and low rating
- Critical and commercial success: high rating and high revenue

### 1.4 Poster feature extraction   //optional for now

- Use poster_path to construct poster URLs.
- Download poster images for a selected sample
  - Select a manageable sample, such as:
    - Top 500 by revenue
    - Top 500 by rating, with vote_count threshold
    - Top 500 by ROI
    - Random sample of 500 movies

Poster features to calculate:
- brightness
- contrast
- saturation
- colorfulness
- dominant color
- warm/cool color tendency

Important limitation:   //thats why its optional for now

Poster analysis is exploratory. It should not be presented as proof that poster design causes revenue or ratings.

### 1.5 Basic analysis

  #### 1.5.1 Descriptive statistics
  
  Calculate:

  - Number of movies by decade
  - Average budget by decade
  - Average revenue by decade
  - Average profit by decade
  - Average ROI by decade
  - Average rating by decade
  - Average runtime by decade

### 9.2 Commercial performance

Analyze:

- Relationship 
- budget X revenue
- budget X profit
- budget X ROI
- Top 10
  - revenue
  - profit
  - ROI

### 9.3 Audience evaluation

Analyze:

- Relationship between rating and revenue
- Relationship between rating and ROI
- Relationship between popularity and revenue
- Movies with high rating but low revenue
- Movies with high revenue but low rating

### 9.4 Runtime

Analyze:

- Revenue by runtime group
- Rating by runtime group
- ROI by runtime group

### 9.5 Genres and keywords

Analyze:

- Most common genres overall
- Most common genres among high-revenue movies
- Most common genres among high-ROI movies
- Most common genres among highly rated movies
- Most frequent keywords among top revenue movies
- Most frequent keywords among top rated movies
- Most frequent keywords among top ROI moviesf

### 9.6 Poster features

Analyze:

- Average brightness by success category
- Average saturation by success category
- Average contrast by success category
- Relationship between poster colorfulness and revenue
- Relationship between poster colorfulness and rating
- Poster feature differences between blockbusters, hidden gems, and money pits

## 10. Data visualization

Required plots:

1. Budget vs revenue
2. Rating vs revenue
3. Budget vs ROI
4. Runtime vs revenue
5. Runtime vs rating
6. Average revenue/profit/ROI by decade
7. Top 10 movies by profit
8. Top 10 movies by ROI
9. Genre distribution among success categories
10. Keyword frequency among high-revenue movies
11. Poster brightness/saturation by success category
12. Poster grid comparing selected success categories

Recommended plot types:

- Scatter plots
- Bar charts
- Boxplots
- Line charts
- Heatmaps
- Poster image grids

## 11. Interpretation strategy

The project should avoid claiming that one variable causes success.

Instead, the interpretation should use language such as:

- "is associated with"
- "is more common among"
- "appears more frequently in"
- "differs across"
- "suggests a pattern"

The project should not claim:

- budget causes revenue
- poster colors cause success
- keywords cause high ratings
- runtime determines quality

## 12. Expected findings

Possible expected findings:

- Budget is likely strongly associated with revenue but less clearly associated with ROI.
- High-revenue movies are not always the highest-rated movies.
- High-rated movies are not always commercially successful.
- Some low-budget movies may have very high ROI.
- Popularity may be more closely related to revenue than rating.
- Runtime may show weak or moderate associations with rating and revenue.
- Poster visual features may differ across success categories, but probably will not strongly explain success alone.

## 13. Report structure

### 13.1 Introduction

Explain why movie success is multidimensional.

Discuss why revenue alone is not enough to define a successful movie.

Introduce the idea of commercial, financial, audience, attention, and visual success.

### 13.2 Problem and motivation

Explain why the topic matters for entertainment management, marketing, and media analytics.

### 13.3 Data and methods

Describe the dataset, selected variables, cleaning process, transformations, and poster feature extraction.

### 13.4 Results

Present the main descriptive analyses and visualizations.

Organize results by success dimension:

1. Commercial success
2. Financial efficiency
3. Audience success
4. Runtime/content characteristics
5. Poster visual features

### 13.5 Discussion

Discuss whether revenue alone is a good indicator of movie success.

Compare different success categories.

Highlight examples of movies that perform differently depending on the metric.

### 13.6 Limitations

Mention:

- Missing financial data
- Possible reporting errors in budget/revenue
- TMDB ratings may not represent all audiences
- Poster analysis is exploratory
- No causal interpretation
- Older movies may have less reliable financial data

### 13.7 Conclusion

Summarize the main findings.

Conclude that movie success is multidimensional and that revenue captures only one part of performance.

## 14. Slides structure

Suggested slide deck:

1. Title and group members
2. Motivation: why movie success is not just revenue
3. Dataset and variables
4. Data cleaning and transformations
5. Success indicators: revenue, profit, ROI, rating, popularity, poster features
6. Budget vs revenue
7. Rating vs revenue
8. Profit and ROI rankings
9. Runtime, genres, and keywords
10. Poster visual analysis
11. Key findings
12. Limitations and conclusion

## 16. Reproducibility checklist

Before submission:

- Code runs from top to bottom.
- File paths are relative, not absolute.
- Dataset source is cited.
- Any external code inspiration is linked.
- Code is commented.
- Figures are saved automatically.
- Processed dataset is saved.
- README explains how to run the project.
- PDF report is exported.
- Slides are exported.
- Zip file contains all required files.