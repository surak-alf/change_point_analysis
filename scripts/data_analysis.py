import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

def plot_price_distribution(data):
    """Plots the distribution of prices using a histogram and KDE."""
    plt.figure(figsize=(8, 6))
    sns.histplot(data['Price'], kde=True)
    plt.title('Distribution of Price')
    plt.xlabel('Price')  # Add x-axis label for clarity
    plt.ylabel('Frequency') # Add y-axis label for clarity
    plt.show()

def plot_price_boxplot(data):
    """Plots a box plot of prices."""
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=data['Price'])
    plt.title('Box Plot of Price')
    plt.ylabel('Price') # Add y-axis label for clarity
    plt.show()

def plot_historical_prices(data):
    """Plots the historical prices over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Price'], label='Brent Oil Price')
    plt.title('Historical Brent Oil Prices (1987-2022)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD per barrel)')
    plt.legend()
    plt.grid()
    plt.show()
def analyze_and_plot_prices(data):
    """Combines all price analysis and plotting functions."""
    plot_price_distribution(data)
    plot_price_boxplot(data)
    plot_historical_prices(data)

def resample_to_monthly(data):
    """Resamples the data to monthly frequency and calculates the mean price."""
    return data.resample('M', on='Date')['Price'].mean()

def calculate_rolling_mean(data, window=365):
    """Calculates the rolling mean of the price."""
    return data['Price'].rolling(window=window, center=True).mean()

def decompose_time_series(data, period=365, model='additive'):
    """Performs time series decomposition."""
    return seasonal_decompose(data['Price'], model=model, period=period)

def plot_time_series_components(data, monthly_data, rolling_mean, decomposition, window):
    """Plots the time series components."""
    plt.figure(figsize=(15, 10))

    plt.subplot(4, 1, 1)
    plt.plot(data['Date'], data['Price'], label='Original Data')
    plt.legend()
    plt.title('Original Data')

    plt.subplot(4, 1, 2)
    plt.plot(monthly_data.index, monthly_data.values, label='Monthly Average')
    plt.legend()
    plt.title('Monthly Average')

    plt.subplot(4, 1, 3)
    plt.plot(data['Date'], rolling_mean, label=f'{window}-Day Rolling Mean')  # Corrected line
    plt.legend()
    plt.title(f'{window}-Day Rolling Mean')  # Corrected line

    plt.subplot(4, 1, 4)
    decomposition.plot()
    plt.tight_layout()
    plt.show()

def analyze_and_plot_time_series(data, window=365, period=365, model='additive'):
    """Combines time series analysis and plotting."""
    monthly_data = resample_to_monthly(data)
    rolling_mean = calculate_rolling_mean(data, window)
    decomposition = decompose_time_series(data, period, model)
    plot_time_series_components(data, monthly_data, rolling_mean, decomposition, window)  # Corrected line

