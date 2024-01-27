<div align="center">
<h1 align="center">
<img src="" width="100" />
<br> Stock Analysis Terminal with Pairs Trading Algorithm</h1>
<h3>◦ Developed to interact with the ALPACA API with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat-square&logo=SciPy&logoColor=white" alt="SciPy" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy" />
</p>
<img src="https://img.shields.io/github/license/AidanAlr/Pairs-Trading-Algorithm?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/AidanAlr/Pairs-Trading-Algorithm?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/AidanAlr/Pairs-Trading-Algorithm?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/AidanAlr/Pairs-Trading-Algorithm?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running Pairs-Trading-Algorithm](#-running-Pairs-Trading-Algorithm)
- [🤝 Contributing](#-contributing)

---


## 📍 Overview
This command line interface (CLI) application, developed to interact with the Alpaca API (stock brokerage), allows users to manage and view positions, execute trades, run analyses, backtest strategies, and implement a pairs trading strategy. 

The code is organised in a modular format, with analysis and trading functions in separate directories. Executor files import functions and methods from these classes.

---

## 📦 Features

► Analysis

Conduct the analysis required to find a suitable pair for statistical arbitrage. Submit a CSV file of stock tickers and the program will download the stock data from the last year and check the correlation between all assets. If a pair has a sufficiently high correlation, it is placed through ADF test to check the stationarity of the time series and cointegration tests for the suitability of the pair. Once a suitable pair is chosen, we use a  60-day rolling regression on the asset prices allowing us to generate the hedge ratio; we then analyse the relative spread between assets. When the spread exceeds a certain boundary, we will buy one asset and short the other expecting the spread to retract.

You will be presented with the option to backtest the strategy as well.

► Backtest strategy

Dashboard that generates graphic representations of spread, zscored spread and strategy return.
Allows you to test different strategies by adjusting take profits and stop loss.

► Execute Pairs Trading Strategy

Once you have chosen a pair execute and manage a pairs trading strategy directly from your terminal.

► View current positions with profit and loss

Dashboard for viewing all important metrics about current positions.

► Manual Trade

Option to conduct a manual trade, market or limit order.

---


## 📂 Repository Structure

```sh
└── Pairs-trading-Algorithm/
    ├── utils/
    │   ├── my_timer.py
    │   ├── ProgressBar.py
    │   ├── formatting_and_logs.py
    ├── analysis/
    │   ├── DATES.py
    │   ├── errors.py
    │   ├── statistical_methods.py
    │   ├── stock_data.py
    │   └── visualisation.py
    ├── executors/
    │   ├── alpaca_executor.py
    │   ├── analysis_executor.py
    │   └── cli_controller.py
    ├── tests/
    │   ├── test_alpaca.py
    │   └── test_collect_metrics_for_pair.py
    ├── trading/
    │   └── alpaca_functions.py
    ├── requirements.txt
    └── to_do_list.txt

```


---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                               | Summary       |
| ---                                                                                                | ---           |
| [requirements.txt](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/requirements.txt) | ► Requirements needed to run program, use "pip install -r requirements.txt" |

</details>

<details closed><summary>Analysis</summary>

| File                                                                                                                  | Summary       |
| ---                                                                                                                   | ---           |
| [Visualisation.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Analysis/Visualisation.py)           | ► Functions to visualise important metrics |
| [StockData.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Analysis/StockData.py)                   | ► StockData class and methods |
| [Dates.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Analysis/Dates.py)                           | ► Enum for dates |
| [StatisticalMethods.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Analysis/StatisticalMethods.py) | ► Functions performing statisticaly analysis on StockData |

</details>

<details closed><summary>Tests</summary>

| File                                                                                                 | Summary       |
| ---                                                                                                  | ---           |
| [test_alpaca.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Tests/test_alpaca.py) | ► Testing the Alpaca Functions |

</details>

<details closed><summary>Executors</summary>

| File                                                                                                                 | Summary       |
| ---                                                                                                                  | ---           |
| [AnalysisExecutor.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Executors/AnalysisExecutor.py)   | ► Executor for analysis |
| [AlgorithmExecutor.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Executors/AlgorithmExecutor.py) | ► Executor for algorithm |

</details>

<details closed><summary>Aidanutils</summary>

| File                                                                                                      | Summary       |
| ---                                                                                                       | ---           |
| [MyTimer.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/AidanUtils/MyTimer.py)         | ► INSERT-TEXT |
| [ProgressBar.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/AidanUtils/ProgressBar.py) | ► INSERT-TEXT |

</details>

<details closed><summary>Trading</summary>

| File                                                                                                           | Summary       |
| ---                                                                                                            | ---           |
| [AlpacaFunctions.py](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/Trading/AlpacaFunctions.py) | ► INSERT-TEXT |

</details>

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the Pairs-Trading-Algorithm repository:
```sh
git clone https://github.com/AidanAlr/Pairs-Trading-Algorithm
```

2. Change to the project directory:
```sh
cd Pairs-trading-Algorithm
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running Program
1. Change to the Executors directory:
```sh
cd Pairs-trading-Algorithm/executors
```
```sh
python -m cli_controller
```


---


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/AidanAlr/Pairs-Trading-Algorithm/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Report Issues](https://github.com/AidanAlr/Pairs-Trading-Algorithm/issues)**: Submit bugs found or log feature requests for AIDANALR.



---

[**Return**](#Top)

---

