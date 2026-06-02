"""Input validation utilities."""

def validate_symbol(symbol: str) -> bool:
    """Validate trading pair symbol format.
    
    Args:
        symbol: Trading pair (e.g., 'BTCUSDT').
        
    Returns:
        True if valid.
        
    Raises:
        ValueError: If invalid.
    """
    if not isinstance(symbol, str) or not symbol.isupper() or not symbol.isalnum():
        raise ValueError(f"Symbol must be an uppercase string, got: {symbol}")
    return True


def validate_quantity(quantity: float) -> bool:
    """Validate order quantity.
    
    Args:
        quantity: Order quantity.
        
    Returns:
        True if valid.
        
    Raises:
        ValueError: If invalid.
    """
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError(f"Quantity must be a positive float, got: {quantity}")
    return True


def validate_price(price: float) -> bool:
    """Validate price.
    
    Args:
        price: Price value.
        
    Returns:
        True if valid.
        
    Raises:
        ValueError: If invalid.
    """
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError(f"Price must be a positive float, got: {price}")
    return True


def validate_side(side: str) -> bool:
    """Validate order side.
    
    Args:
        side: Order side ('BUY' or 'SELL').
        
    Returns:
        True if valid.
        
    Raises:
        ValueError: If invalid.
    """
    if side not in ("BUY", "SELL"):
        raise ValueError(f"Side must be exactly 'BUY' or 'SELL', got: {side}")
    return True


def validate_order_type(order_type: str) -> bool:
    """Validate order type.
    
    Args:
        order_type: Order type ('MARKET' or 'LIMIT').
        
    Returns:
        True if valid.
        
    Raises:
        ValueError: If invalid.
    """
    if order_type not in ("MARKET", "LIMIT"):
        raise ValueError(f"Order type must be exactly 'MARKET' or 'LIMIT', got: {order_type}")
    return True
