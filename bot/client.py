"""Binance Futures API Client."""

import os
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import setup_logging

logger = setup_logging()


class BinanceTestnetClient:
    """Wrapper for Binance Futures testnet client using python-binance."""

    def __init__(self):
        """Initialize Binance Futures testnet client."""
        load_dotenv()
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found. Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file.")

        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )

    def ping_server(self):
        """Verify connection to the server and log the result."""
        try:
            # Ping the Futures testnet server
            self.client.futures_ping()
            logger.info("Successfully connected to Binance Futures Testnet.")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Binance Futures Testnet: {e}")
            return False
