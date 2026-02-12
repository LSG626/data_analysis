# AAPL Stock Price Predictor 📈

An experimental machine learning project attempting to predict Apple Inc. (AAPL) stock price movements using technical indicators and historical data.

## 🎯 Project Goal

Build a machine learning model that can predict:
- **Price Direction**: Whether the stock will go up or down (Classification)
- **Percentage Return**: The expected percentage change (Regression)

**Target Accuracy**: 80%+

## 📊 Current Performance

- Classification Accuracy: **51.42%** ❌
- Regression R²: **0.0111** ❌
- Regression MAE: **1.2260%**

**Status**: The model is currently performing at near-random levels. I need help improving it!

## 🆘 Known Issues & Bugs


I've identified several issues in my code, but I'm looking for the community's expertise on how to fix them:

### 1. **Ticker Symbol Typo**
```python
SYMBOL = "AAPLE"  # Line 4 - This is wrong!
```
Should be "AAPL" but there might be other naming inconsistencies.

### 2. **Exposed API Key**
```python
API_KEY = "Y1jjPqrJXeDs15L6RvIXAKbO9EWd5mwA"  # Visible in code
```
**Question**: What's the best practice for handling API keys in Python projects? Should I use `.env` files or another method?

### 3. **Suspicious Future Data**
The dividend API returns dates in **2030**, and my training data shows dates like **2025-11-04** onward. 
**Question**: Is this data leakage? How can I ensure I'm only using historical data that would have been available at prediction time?

### 4. **Target Variable Creation**
```python
df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
```
**Question**: Is using `shift(-1)` causing look-ahead bias? How should I properly create targets for time series prediction?

### 5. **Data Structure Issues**
Multiple DataFrame column naming problems throughout the code.
**Question**: What's the cleanest way to handle yfinance's multi-index columns?

### 6. **Train/Test Split**
```python
split_index = int(len(X) * 0.8)
```
**Question**: Should I be using a validation set? What's the best practice for time series data splitting?

### 7. **Limited Features**
Currently only using 7 basic technical indicators.
**Question**: What other features or indicators should I add to improve prediction accuracy?

### 8. **Model Configuration**
```python
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
```
**Question**: Are these good hyperparameters? Should I be using a different model entirely?

### 9. **No Feature Scaling**
I'm not scaling my features before training.
**Question**: Does this matter for Random Forest and Linear Regression? Should I normalize my data?

### 10. **Model Accuracy**
51.42% is basically random guessing.
**Question**: Is 80% accuracy even realistic for stock prediction, or should I adjust my expectations?

## 🤝 How You Can Help

I'm actively seeking collaborators and feedback! Here's what I need help with:

### Critical Questions:

1. **Is 80% accuracy realistic?** 
   - What accuracy do professional models achieve?
   - Should I be targeting a different metric?

2. **Which features actually matter?**
   - What technical indicators work best?
   - Should I include fundamental data?
   - What about sentiment analysis from news?

3. **What's the best model architecture?**
   - Should I stick with Random Forest?
   - Would LSTM or GRU work better for time series?
   - What about ensemble methods?

4. **How do I prevent data leakage?**
   - How can I verify my data is clean?
   - What validation strategy should I use?

5. **Which API should I use for real-time data?**
   - See API section below - which do you recommend?

### Areas Where I Need Expertise:

- 🔧 **Code Review**: Point out bugs and anti-patterns
- 📊 **Feature Engineering**: Suggest better indicators or data sources
- 🤖 **Model Selection**: Recommend better ML algorithms
- 📈 **Financial Domain Knowledge**: Help me understand what actually drives stock prices
- 🔬 **Validation Strategy**: Ensure I'm testing the model properly

## 💬 Discussion Topics

**Open Issues:**
- [How to achieve better accuracy?](#) - Share your ideas!
- [Best APIs for stock data?](#) - See section below
- [Is this approach fundamentally flawed?](#) - Be honest!

**I want to hear from you:**
- Have you built stock prediction models before?
- What worked and what didn't?
- What am I missing in my approach?

## 📡 API Recommendations Needed!

I'm currently using **yfinance** (free, no API key needed), but I'm open to other options. 

### APIs I'm Considering:

**Free Options:**
1. **Yahoo Finance (yfinance)** - Currently using
   - No API key needed
   - Good historical data
   - Rate limited

2. **Alpha Vantage** - Free tier available
   - 25 requests/day free
   - Real-time data
   - [Get API Key](https://www.alphavantage.co/support/#api-key)

3. **Finnhub** - Free tier available
   - 60 calls/minute
   - Includes news & sentiment
   - [Get API Key](https://finnhub.io/register)

4. **IEX Cloud** - Free tier available
   - Real-time data
   - [Get API Key](https://iexcloud.io/cloud-login#/register)

5. **Twelve Data** - Free tier available
   - 800 requests/day
   - [Get API Key](https://twelvedata.com/pricing)

**Paid Options:**
- Polygon.io (~$29/month)
- Quandl/Nasdaq Data Link
- Bloomberg Terminal (expensive!)

### ❓ Questions for You:

- **Which API do you recommend and why?**
- **Which gives the most reliable real-time data?**
- **Have you hit rate limits with any of these?**
- **Are there better alternatives I'm missing?**
- **Is free data sufficient for a learning project?**

**Please share your experience in the Issues or Discussions tab!**

## 🚀 Getting Started

Want to run the code and help improve it?

### Prerequisites
```bash
pip install yfinance pandas numpy scikit-learn ta matplotlib seaborn
```

### Running the Project
1. Clone this repository
2. Open the Jupyter notebook or Python script
3. Run the cells and observe the poor performance 😅
4. Submit a PR with your improvements!

## 🤔 Current Approach

**Data Source**: Yahoo Finance (via yfinance)  
**Timeframe**: 5 years of historical data  
**Features**: Close price, MA(80), MA(200), RSI, MACD, MACD Signal, MACD Diff  
**Models**: 
- RandomForestClassifier for direction prediction
- Linear Regression for return prediction

**The Problem**: This isn't working! Help me figure out why.

## 📚 What I'm Learning

This is a learning project where I'm trying to understand:
- Time series forecasting
- Machine learning for financial data
- Proper validation techniques
- Feature engineering for technical analysis

**I'm not claiming this works** - I'm sharing my attempt and asking for help to improve it!

## ⚠️ Disclaimer

**This is an educational project only.**
- These predictions should NOT be used for real trading
- I'm a learner, not a financial expert
- Stock markets are unpredictable
- You will lose money if you trade based on this
- Not financial advice - consult a professional

## 🙏 Contributing

**All contributions welcome!**

Ways you can help:
- 🐛 Report bugs in Issues
- 💡 Suggest improvements in Discussions
- 🔧 Submit PRs with fixes
- 📖 Improve documentation
- 💬 Share your experience with stock prediction
- 📊 Recommend better data sources

**Even if you just tell me "this approach won't work because..."** - that's valuable feedback!

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Submit a Pull Request with explanation

## 💭 Open Questions for the Community

1. **Is this approach salvageable or should I start over?**
2. **What accuracy is actually achievable in stock prediction?**
3. **Should I be predicting something different (volatility, trends, etc.)?**
4. **What features am I missing that could make a real difference?**
5. **Are there better datasets I should be using?**
6. **How do professional quant traders approach this problem?**

## 📬 Contact & Discussion

- **Issues**: For bug reports and specific problems
- **Discussions**: For general questions and ideas
- **Pull Requests**: For code contributions

**Let's learn together!** Even if you can't code, your insights on finance, data science, or trading would be valuable.

## 📝 License

MIT License - Feel free to use and modify

## 🙌 Acknowledgments

Thanks in advance to everyone who:
- Points out my mistakes
- Suggests improvements  
- Shares their knowledge
- Helps me learn

---

**⭐ Star this repo if you find it interesting (even as a cautionary tale of what not to do!)** 

**💬 Drop a comment with your thoughts - I genuinely want to learn from the community!**
