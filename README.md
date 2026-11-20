# Netflix Movie and TV Show Clustering and Recommendation System

A Machine Learning-based project that uses **K-Means Clustering** and similarity-based recommendations to group Netflix Movies and TV Shows and recommend similar titles.

## Project Overview

The goal of this project is to analyze Netflix Movies and TV Shows, identify similar content using unsupervised machine learning, and build a recommendation system that suggests titles based on a user's selected movie or TV show.

The project uses the Netflix Titles dataset and applies data preprocessing, feature engineering, clustering, and similarity-based recommendation techniques.

## Dataset

The project uses the Netflix Titles dataset (`netflix_titles.csv`).

**Dataset information:**
- Total records: 8,807
- Movies: 6,131
- TV Shows: 2,676
- Total columns: 12

**Main dataset features:**
- `show_id`
- `type`
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in`
- `description`

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Current Implementation

### 1. Data Loading and Cleaning
- Loaded the Netflix dataset using Pandas.
- Checked the dataset shape and missing values.
- Replaced missing values in selected text columns with `"Unknown"`.
- Checked duplicate show IDs.
- Analyzed the distribution of Movies and TV Shows.

### 2. Feature Engineering

**Duration Features**
- Extracted numerical values from duration strings.
- Handled missing duration values using the median duration of the corresponding content type.

**Rating Features**
- Grouped original Netflix rating categories into:
  - Kids
  - Teens
  - Adults
  - Other
- Converted rating groups into numerical dummy variables.

**Genre Features**
- Split multiple genres into individual labels.
- Used `MultiLabelBinarizer` to convert genres into binary features.
- Selected the top 15 most frequent genres.

**Content Type Feature**
- Converted the content type into a binary feature:
  - Movie = 1
  - TV Show = 0

### 3. Feature Matrix

Combined the following features into a single feature table:

- Numerical duration
- Content type
- Rating dummy variables
- Top 15 genre features

This feature matrix will be used for machine learning.

## Project Workflow

1. Dataset loading
2. Data cleaning
3. Feature engineering
4. Feature scaling
5. K-Means clustering
6. Cluster evaluation and analysis
7. Similarity calculation
8. Movie and TV Show recommendations
9. Backend development
10. Frontend development

## Planned Features

- Group Netflix Movies and TV Shows using K-Means clustering.
- Search for a movie or TV show by title.
- Identify the cluster of the selected title.
- Calculate similarity between titles.
- Rank similar titles from closest to least similar.
- Display personalized content recommendations.
- Build an interactive frontend for exploring recommendations.

## Expected Output

When a user searches for a Netflix title, the system will:

1. Find the selected title in the dataset.
2. Identify its cluster.
3. Find similar titles from the same cluster.
4. Rank recommendations based on similarity.
5. Display recommended Movies and TV Shows.

## Project Status

**Currently Completed:**
- Dataset loading
- Missing value handling
- Duration feature extraction
- Rating feature grouping
- Genre encoding
- Feature matrix creation

**Upcoming:**
- Feature scaling
- K-Means clustering
- Cluster evaluation
- Similarity-based recommendation
- Backend and frontend integration

## Author

Asmi Pandey