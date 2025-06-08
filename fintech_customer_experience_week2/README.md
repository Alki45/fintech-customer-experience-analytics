# 📊 Ethiopian Bank App Reviews Analysis

This project focuses on analyzing user reviews of three major Ethiopian bank mobile applications on the Google Play Store. It is structured into two main tasks:

- **Task 1**: Data Collection and Preprocessing  
- **Task 2**: Sentiment and Thematic Analysis (in progress)

---

## ✅ Task 1: Data Collection and Preprocessing

### 🎯 Objective

To scrape and clean user reviews from Google Play Store for three Ethiopian bank apps. The data will be used for downstream sentiment and theme analysis.

### 🏦 Target Bank Apps

- **Dashen Bank** (`com.dashen.dashensuperapp`)
- **Commercial Bank of Ethiopia** (`com.combanketh.mobilebanking`)
- **Bank of Abyssinia** (`com.boa.boaMobileBanking`)

### 🛠️ Tools and Libraries

- `google-play-scraper`: Extract Play Store review data.
- `pandas`: Data processing and cleanup.
- `datetime`: Date formatting.
- `csv`: File handling.
- `logging`: Log scraping activity.

### ⚙️ Process Steps

1. **Scraping**:
   - Collected 400+ reviews per bank.
   - Collected fields: `review`, `rating`, `date`, `bank`, `source`.

2. **Preprocessing**:
   - Removed duplicate entries.
   - Handled missing values.
   - Converted dates to `YYYY-MM-DD` format.
   - Merged and exported data to CSV format.

### 🧾 Output Structure

Cleaned reviews saved with the following columns:

| review | rating | date | bank | source |
|--------|--------|------|------|--------|

### 📁 Files in Which I have extracted and working in `task-1`

- `play_store_scraper.py` – Scrapes reviews using `google-play-scraper`.
- `preprocessing.py` – Cleans and formats review data.
- `Dashen_Bank_reviews_20250608_154622.csv`, `Commercial_Bank_of_Ethiopia_reviews_20250608_154621.csv`, `Bank_of_Abyssinia_reviews_20250608_154623.csv` – Raw scraped data.
- `cleaned_reviews.csv` – Final merged and cleaned dataset.

### ✅ KPIs Met

- ✅ 1,200+ reviews collected
- ✅ <5% missing data
- ✅ Normalized and cleaned CSV
- ✅ Code committed with clear structure and messages

---

## 🚧 Task 2: Sentiment and Thematic Analysis (In Progress)

### 🎯 Objective

To analyze user sentiment and extract common review themes to help banks understand satisfaction drivers and pain points.

### 📊 Analysis Components

#### 1. Sentiment Analysis

- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Alternative**: VADER (for quick benchmarking)
- **Labels**: `positive`, `neutral`, `negative`

#### 2. Thematic Analysis

- **Tools**: TF-IDF, spaCy
- **Themes**: Extracted keywords clustered into 3–5 categories per bank, such as:
  - `Login/Access Issues`
  - `Transaction Failures`
  - `User Interface`
  - `Support/Service Quality`
  - `Feature Requests`

#### 3. Pipeline Steps

- Text preprocessing (cleaning, tokenization)
- Sentiment scoring
- Keyword extraction
- Theme grouping

### 📁 Planned Files in `task-2/`

- `sentiment_analysis.py` – BERT or VADER-based sentiment analysis.
- `thematic_analysis.py` – TF-IDF + rule-based theme extraction.
- `sentiment_results.csv` – Reviews with sentiment labels and scores.
- `themes_by_bank.json` – Final thematic clusters per bank.

### 📝 Minimum Deliverables (WIP)

- 🔲 Sentiment for 400+ reviews
- 🔲 At least 2–3 themes per bank
- 🔲 Saved results with review, sentiment, and theme

