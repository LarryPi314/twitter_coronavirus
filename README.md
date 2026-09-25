# Coronavirus Twitter Analysis

This project analyzes geotagged tweets from all of 2020 to study how coronavirus-related hashtags were used across languages, countries, and time.

The dataset contains hundreds of millions of geotagged tweets. I processed the data using a MapReduce-style pipeline. Daily Twitter archives were mapped independently and in parallel, producing hashtag counts grouped by language and country. I then reduced those daily outputs into aggregate datasets and visualized the results with Python and Matplotlib.

The project demonstrates large-scale data processing, Unix process control, parallel computation, JSON processing, multilingual text analysis, and data visualization.

## Coronavirus by Language

![Coronavirus by language](plots/coronavirus_languages.png)

## Coronavirus by Country

![Coronavirus by country](plots/coronavirus_countries.png)

## Korean Coronavirus Hashtag by Language

![Korean coronavirus hashtag by language](plots/korean_coronavirus_languages.png)

## Korean Coronavirus Hashtag by Country

![Korean coronavirus hashtag by country](plots/korean_coronavirus_countries.png)

## Hashtag Usage Over Time

![Coronavirus hashtag timeline](plots/hashtag_timeline.png)

The time-series visualization shows how usage of selected coronavirus hashtags changed over the course of 2020.
