
# Finance Nifty50 Most Volatile Days

This mini project aims to analyze historical Nifty 50 data and assess market volatility using Python. The primary focus of this project was to understand financial metrics such as daily returns, volatility, and Z-scores, which are crucial in assessing the behavior of financial markets.

## Project Overview

In this project, I worked with historical Nifty 50 stock data to calculate key metrics that measure market risk and volatility. The key steps of the analysis are as follows:

1. **Data Cleaning & Preprocessing**: Removed unwanted columns and prepared the dataset for analysis.
2. **Daily Returns Calculation**: Calculated daily percentage returns based on the 'Close' price.
3. **Volatility Calculation**: Computed the 20-day rolling volatility to measure short-term fluctuations in stock prices.
4. **Advanced Metrics - Moving Averages & Standard Deviation**: Used a 250-day rolling mean and standard deviation to measure long-term trends in volatility.
5. **Z-Score Calculation for Volatility**: Calculated the Z-score of 20-day volatility to assess market behavior relative to historical trends.
6. **Sorting & Filtering**: Filtered out missing data and sorted the Z-scores to identify the most volatile periods.

## Files

- **assignment_VOL_data.xlsx**: Raw input data used for the analysis.
- **NIFTY50_Zret_Compare.xlsx**: Output file showing volatility comparisons.
- **NIFTY50_Zret_Sorted.xlsx**: Final output showing the sorted results of volatility.

## Requirements

This project requires the following Python libraries:

- pandas
- openpyxl (for working with Excel files)

You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## How to Run

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/Ruturaj-Vasant/Finance_Nifty50_Most_Volatile_Days.git
   ```

2. Navigate to the project directory and install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the Python script to perform the analysis:

   ```python
   python Nifty50_Vol.py
   ```

## License

This project is open-source and available under the MIT License.
