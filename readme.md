# 📈 Stock Return Calculator

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org)
[![Yahoo Finance](https://img.shields.io/badge/Yahoo%20Finance-API-purple)](https://pypi.org/project/yfinance/)

A powerful Python tool for analyzing stock returns and performance metrics using real-time market data. Built with NumPy for efficient calculations and yfinance for reliable data fetching.

## ✨ Features

### 🎯 Core Analytics
- **📊 Historical Data Retrieval** - Fetches 1-year historical stock data
- **💰 Return Calculations** - Computes yearly returns including dividends
- **📈 Daily Performance** - Analyzes daily return patterns and trends
- **⚡ Volatility Analysis** - Measures price volatility and risk metrics
- **💎 Dividend Tracking** - Tracks total dividend payments

### 🛠️ Technical Capabilities
- **🌐 Global Market Support** - US stocks and Indian stocks (`.ns` suffix)
- **🔢 NumPy Integration** - Efficient numerical computations
- **🖥️ Interactive Interface** - User-friendly menu-driven experience
- **📋 Comprehensive Reports** - Detailed summary analytics

## 🚀 Quick Start

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/stock-return-calculator.git
   cd stock-return-calculator
   ```

2. **Install dependencies**
   ```bash
   pip install numpy yfinance
   ```

3. **Run the application**
   ```bash
   python stock_calculator.py
   ```

## 📖 Usage Guide

### Basic Usage

1. **Launch the program**
   ```bash
   python stock_calculator.py
   ```

2. **Enter stock ticker** (default: AAPL)
   - **US Stocks**: `AAPL`, `GOOGL`, `MSFT`, `TSLA`
   - **Indian Stocks**: `TATASTEEL.ns`, `RELIANCE.ns`, `INFY.ns`

3. **Navigate the interactive menu**

### Menu Options

| Option | Description | Output |
|--------|-------------|---------|
| 📈 **Yearly Return** | Total return including dividends | Percentage gain/loss |
| 📊 **Daily Returns** | Day-to-day price changes | Array of daily returns |
| 📉 **Average Daily Return** | Mean daily performance | Average percentage |
| 💰 **Total Dividends** | Dividend payments received | Total dividend amount |
| 🎯 **Max/Min Returns** | Best and worst single days | Highest/lowest daily returns |
| ⚡ **Volatility** | Price volatility measure | Standard deviation |
| 🔄 **Change Ticker** | Analyze different stock | Switch to new symbol |
| 📋 **Summary Report** | Complete analysis | All metrics combined |

## 🎓 Learning Objectives

This project demonstrates key programming and financial concepts:

### 🐍 Python Skills
- **Object-Oriented Programming** - Class design and implementation
- **Error Handling** - Robust exception management
- **API Integration** - Working with external data sources

### 🔢 NumPy Mastery
- **Array Operations** - Efficient data manipulation
- **Statistical Functions** - Mean, standard deviation, min/max
- **Mathematical Computations** - Financial calculations

### 💼 Finance Concepts
- **Return Analysis** - Understanding investment performance
- **Risk Assessment** - Volatility and drawdown analysis
- **Dividend Tracking** - Income component evaluation


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **yfinance** - Yahoo Finance API wrapper
- **NumPy** - Numerical computing library
- **Python Community** - Continuous inspiration and support

---

<div align="center">
  <strong>Built with ❤️ for the Python and Finance community</strong>
  <br>
  <sub>⭐ Star this repo if you found it helpful!</sub>
</div>