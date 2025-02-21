# Brent Oil Price Analysis and Interactive Dashboard

This project focuses on analyzing historical Brent oil prices to understand the impact of major events (e.g., political decisions, economic sanctions, OPEC policies) on price fluctuations. It includes advanced time series modeling, change point detection, and an interactive dashboard for visualizing results.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

The goal of this project is to:
- Analyze historical Brent oil prices (1987–2022) to detect significant change points.
- Correlate price changes with major global events (e.g., conflicts, economic sanctions, OPEC decisions).
- Build advanced time series models (e.g., ARIMA, GARCH, LSTM) to forecast oil prices.
- Develop an interactive dashboard to visualize trends, forecasts, and event impacts.

---

## Features

### Data Analysis
- **Change Point Detection**: Identify significant shifts in oil prices using statistical methods.
- **Time Series Modeling**: Use ARIMA, GARCH, and LSTM models to analyze and forecast prices.
- **Event Correlation**: Correlate price changes with major global events.

### Interactive Dashboard
- **Backend**: Flask API to serve data and model outputs.
- **Frontend**: React-based interface with interactive visualizations (e.g., line charts, event highlights).
- **Key Features**:
  - Filter data by date range.
  - Highlight specific events and their impact on prices.
  - Display model performance metrics (e.g., RMSE, MAE).
