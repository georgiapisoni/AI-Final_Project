# Movie Success: commercial and critical success analysis

## 1. Project idea

How do different definitions of movie success compare; is revenue by itself a sufficient measure of success?

Different forms of movie success:

- Commercial: high revenue
- Financial: high profit
- Investment efficiency: high return on investment
- Audience: high user rating; high popularity
- Visual marketing: distinctive poster design (optional for now)

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

### 3.5 Poster design and visual marketing    </br>//optional

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
### 1.2 Data cleaning
### 1.3 Data transformations
### 1.4 Poster feature extraction   </br>//optional for now
### 1.5 Basic analysis

  #### 1.5.1 General descriptive statistics

    - Number of movies by year bins
    - Averages (by year bins):
      - budget
      - revenue
      - profit
      - ROI
      - rating
      - runtime

  #### 1.5.2 Commercial performance

    - Relationships:
      - budget X revenue
      - budget X profit
      - budget X ROI

  #### 1.5.3 Audience evaluation

    - Relationships:
    - rating X revenue
    - rating X ROI
    - popularity X revenue
    - high rating X low revenue
    - high revenue X low rating

  #### 1.5.4 Runtime

    - Revenue by runtime 
    - Rating by runtime 
    - ROI by runtime 

  #### 1.5.5 Genres and keywords

    - Most common genres overall
    - Most common genres among:
      - high-revenue movies
      - high-ROI movies
      - highly rated movies
    - Most frequent keywords among:
      - top revenue movies
      - top rated movies
      - top ROI movies

  #### 1.5.6 Poster features     
    //optional for now

    - Average brightness by success category
    - Average saturation by success category
    - Average contrast by success category
    - Relationship between poster colorfulness and revenue
    - Relationship between poster colorfulness and rating
    - Poster feature differences between blockbusters, hidden gems, and money pits

### 1.6 Data visualization
Plots:
1. Budget X revenue
2. Rating X revenue
3. Budget X ROI
4. Runtime X revenue
5. Runtime X rating
6. Average revenue/profit/ROI by decade
7. Top 10 movies by profit
8. Top 10 movies by ROI
9. Genre distribution among success categories
10. Keyword frequency among high-revenue movies
</br>//poster(if used)</br>
11. Poster brightness/saturation by success category
12. Poster grid comparing selected success categories

## 2. Report

### 1. Introduction, problem and motivation
-> write when doc is finished
- describe motivation briefly:
  - why movie success is multidimensional
  - why revenue alone is not enough to define a successful movie
  - introduce ideas of idea of commercial, financial, audience, attention, and visual success
  - why the topic matters for entertainment management, marketing, and media analytics.
- summary of methods of analysis
- brief summary of conclusions

### 2. Data and methods

- Describe the dataset (add link to og)
- describe code process (outlined once code is done)

### 3. Results

Results of the main descriptive analyses + add the plots.

Organize by success dimension:

1. Commercial success
2. Financial efficiency
3. Audience success
4. Runtime/content characteristics
5. Poster visual features

### 4. Discussion

Discuss whether revenue alone is a good indicator of movie success.

Compare different success categories.

Highlight examples of movies that perform differently depending on the metric.

Answer the relevant starting questions.

(we'll see what's extra once the analysis is done)

### 5. Limitations

Mention:

- Missing financial data
- Possible reporting errors in budget/revenue
- TMDB ratings may not represent all audiences
- Poster analysis is exploratory
- No causal interpretation
- Older movies may have less reliable financial data

^^^^to be checked later

### 13.7 Conclusion

Summarize the main findings.

Conclude that movie success is multidimensional and that revenue captures only one part of performance (if that's what we conclude in the end)

## 3. Presentation slides
- outline once the report is done

## checklist

- Code executes as expected
- Dataset source is cited
- Any external code inspiration is linked (including AI)
- Code is properly commented
- Figures are saved in the outputs folder
- Processed dataset is saved in the data folder
- README explains how to run the project
- Zip file contains all required files (code, report, slides)
