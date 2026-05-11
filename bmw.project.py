#BMW vs porsche sales analysis 
#created by MOHAMMED MUBASHIR AHMED 
#tools used : python, pandas , matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# load datasets
# load datasets
bmw = pd.read_csv("scripts/cleaned_bmw_data.csv")
porsche = pd.read_csv("scripts/cleaned_porsche_data.csv")
print(porsche.columns)

# show first rows
print(bmw.head())
print(porsche.head())

# plot both closing prices
plt.plot(bmw["Close"], label="BMW")
plt.plot(porsche["close"], label="Porsche")

# chart title and labels
plt.title("BMW vs Porsche Stock Closing Price")
plt.xlabel("Days")
plt.ylabel("Closing Price")

# legend and grid
plt.legend()
plt.grid(True)
plt.savefig("bmw_porsche_sales.png")

# show graph
plt.show()

# show graph
plt.show()

# Check missing values
print(bmw.isnull().sum())

print("----------------")

print(porsche.isnull().sum())
# Average closing price
print("BMW Average Close Price:", bmw["Close"].mean())

print("Porsche Average Close Price:", porsche["close"].mean())
# Moving Average for BMW
bmw["Moving_Avg"] = bmw["Close"].rolling(30).mean()

# Plot moving average
plt.figure(figsize=(10,5))

plt.plot(bmw["Close"], label="BMW Close Price")
plt.plot(bmw["Moving_Avg"], label="30 Day Moving Average")

plt.title("BMW Moving Average Analysis")
plt.xlabel("Days")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.show()
# Save cleaned BMW data
bmw.to_csv("cleaned_bmw_data.csv", index=False)

# Save cleaned Porsche data
porsche.to_csv("cleaned_porsche_data.csv", index=False)

print("Cleaned files saved successfully!")
# Highest BMW closing price
print("Highest BMW Close Price:", bmw["Close"].max())

# Lowest BMW closing price
print("Lowest BMW Close Price:", bmw["Close"].min())

# Highest Porsche closing price
print("Highest Porsche Close Price:", porsche["close"].max())

# Lowest Porsche closing price
print("Lowest Porsche Close Price:", porsche["close"].min())
# Correlation between BMW Open and Close prices
correlation = bmw["Open"].corr(bmw["Close"])

print("Correlation between BMW Open and Close:", correlation)
# Histogram of BMW Closing Prices
plt.figure(figsize=(10,5))

plt.hist(bmw["Close"], bins=30)

plt.title("Distribution of BMW Closing Prices")
plt.xlabel("Closing Price")
plt.ylabel("Frequency")

plt.grid(True)

plt.show()
plt.figure(figsize=(10,5))

plt.hist(bmw["Close"], bins=30)

plt.title("Distribution of BMW Closing Prices")
plt.xlabel("Closing Price")
plt.ylabel("Frequency")

plt.savefig("bmw_histogram.png")

plt.show()
plt.figure(figsize=(10,5))

plt.hist(porsche["close"], bins=30)

plt.title("Distribution of Porsche Closing Prices")
plt.xlabel("Closing Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig("porsche_histogram.png")

plt.show()
# Correlation Analysis
correlation = bmw["Close"].corr(porsche["close"])

print("Correlation between BMW and Porsche closing prices:")
print(correlation)
# BMW vs Porsche Closing Price Comparison

plt.figure(figsize=(12,6))

plt.plot(bmw["Close"], label="BMW Close Price")
plt.plot(porsche["close"], label="Porsche Close Price")

plt.title("BMW vs Porsche Stock Price Comparison")
plt.xlabel("Days")
plt.ylabel("Price")

plt.legend()
plt.grid(True)
plt.savefig("bmw_porsche_sales.png")

plt.show()

# Take equal length
min_length = min(len(bmw), len(porsche))

comparison_df = pd.DataFrame({
    "BMW": bmw["Close"][:min_length].values,
    "Porsche": porsche["close"][:min_length].values
})

# Heatmap
plt.figure(figsize=(6,4))
corr = comparison_df.corr()

try:
    import seaborn as sns
    sns.heatmap(corr, annot=True, cmap="coolwarm")
except ImportError:
    plt.imshow(corr, cmap="coolwarm", aspect="auto")
    plt.colorbar()
    ticks = range(len(corr.columns))
    plt.xticks(ticks, corr.columns)
    plt.yticks(ticks, corr.columns)
    for i in ticks:
        for j in ticks:
            plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", color="white" if abs(corr.iloc[i,j]) > 0.5 else "black")

plt.title("BMW vs Porsche Correlation Heatmap")

plt.savefig("correlation_heatmap.png")

plt.show()

# Daily Returns Analysis

bmw["Daily_Return"] = bmw["Close"].pct_change()

porsche["Daily_Return"] = porsche["close"].pct_change()

# Plot daily returns
plt.figure(figsize=(12,6))

plt.plot(bmw["Daily_Return"], label="BMW Daily Return")
plt.plot(porsche["Daily_Return"], label="Porsche Daily Return")

plt.title("BMW vs Porsche Daily Returns")
plt.xlabel("Days")
plt.ylabel("Daily Return")

plt.legend()
plt.grid(True)
plt.savefig("daily_returns.png")

plt.show()





