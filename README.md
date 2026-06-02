# 📈 Binance Futures Testnet Trading Bot CLI

A robust, user-friendly command-line interface (CLI) application for placing trades on the **Binance Futures Testnet**. Built using Python, `python-binance`, Typer, and Rich, this bot ensures inputs are thoroughly validated and output is beautifully styled in your terminal.

---

## 🚀 Features

- **Testnet Exclusive:** Safely test your trading strategies without risking real capital. The client is strictly configured for the Binance Futures Testnet.
- **Strict Validation:** Built-in safeguards check symbol formatting, positive quantities/prices, and exact matches for sides/order types.
- **Rich Console Output:** Pre-execution summaries and post-execution results (or errors) are displayed in readable, styled terminal panels.
- **Robust Error Handling:** Intercepts API and request exceptions, presenting clear messages instead of raw, confusing stack traces.
- **Detailed Logging:** Automatically logs all activity to `trading_bot.log` and the console with exact timestamps.

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.8 or higher.
- A Binance Testnet account with generated API keys.

### 2. Create a Virtual Environment
It is highly recommended to isolate your project dependencies using a virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Ensure you install the necessary packages. (If you don't have a `requirements.txt` yet, make sure you install `typer`, `rich`, `python-binance`, and `python-dotenv`).

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
1. Rename or copy your `.env.template` file to `.env` in the root directory.
2. Open `.env` and fill in your Binance Testnet API credentials:
   ```dotenv
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_api_secret_here
   ```

---

## 💻 Usage Examples

The CLI provides a single command `trade` to execute your orders.

### Place a MARKET Order
For a market order, you must provide the symbol, side, order type, and quantity.

```bash
python cli.py trade BTCUSDT BUY MARKET 0.001
```

### Place a LIMIT Order
For a limit order, append the `--price` flag.

```bash
python cli.py trade BTCUSDT SELL LIMIT 0.001 --price 65000.50
```

---

## 📝 Assumptions Made During Development

- **Safety First:** The bot is strictly hardcoded to use the Binance Futures Testnet URL (`https://testnet.binancefuture.com`). Mainnet execution is intentionally disabled to prevent accidental live trades.
- **Time in Force:** All LIMIT orders currently default to `GTC` (Good 'Til Canceled) within `orders.py`.
- **Environment Management:** It is assumed the user understands not to commit their `.env` file to version control.
- **API Wrappers:** The `python-binance` library is used as the underlying client instead of the official Binance Connector to provide a solid balance of stability and ease of use.