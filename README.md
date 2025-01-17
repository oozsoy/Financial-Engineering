## Financial-Engineering

This repo provide several introductory tutorials on important concepts related to Financial Time-series analysis and Algorithmic Trading. There are tutorials for 7 seperate sections available, each comes with a python notebook: 

1. Fundamentals of Financial Time Series: Stock returns, distribution of stock returns (mean, std, skewness, kurtosis), t-distribution, statistical testing of return distributions, covariance and correlation, alpha and beta, volatility clustering, mixture of Gaussians 
2. Time Series basics
3. Modern Portfolio Theory (MPT) and Capital Asset Pricing Model (CAPM)
4. Intro to Algorithmic Trading: Trend following strategy and simple Machine Learning based strategies using Linear Regression, Logistic Regression and Random Forest Classifiers. 
5. Reinforcement Learning for Algorithmic Trading: Q-learning, Trend Following Strategy with RL approach (without learning), Algorithmic trading with Q-learning. 
6. Statistical Factor Models & PCA
7. Regime Detection and Sequence Modelling with Hidden Markov Models 

In addition to the tutorials, there are two scripts that can be used to download and append financial data for tickers of interest: 
- `get_data.py` : get financial data from yfinance 
- `append_stocks.py`: to stack different tickers within a time range specified and save it as a `.csv` 