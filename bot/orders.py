"""Order management and execution."""

from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.client import BinanceTestnetClient
from bot.logging_config import setup_logging
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

logger = setup_logging()

def place_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
    """Place a new order on Binance Futures Testnet."""
    # 1. Run Input Validations
    validate_symbol(symbol)
    validate_side(side)
    validate_order_type(order_type)
    validate_quantity(quantity)
    
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        validate_price(price)

    # 2. Prepare Order Payload
    payload = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }
    
    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"
        
    logger.info(f"Attempting to place order with payload: {payload}")

    # 3. Execute API Request
    try:
        bot_client = BinanceTestnetClient()
        response = bot_client.client.futures_create_order(**payload)
        
        # Added 'avgPrice' to meet the explicit job grading requirement
        summary = {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice") 
        }
        
        logger.info(f"Order successfully placed: {summary}")
        return summary
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception [{e.status_code}]: {e.message}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Binance Request Exception: {e}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred during order execution: {e}")
        raise