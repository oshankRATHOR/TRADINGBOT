"""Logging configuration for the trading bot."""

import logging
import sys
from datetime import datetime


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """Configure logging with console and file handlers.
    
    Args:
        level: Logging level (default: INFO).
        
    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger("trading_bot")
    logger.setLevel(level)

    # Prevent adding duplicate handlers if the logger is already configured
    if logger.handlers:
        return logger

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_format = logging.Formatter(
        "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # File handler
    log_filename = "trading_bot.log"
    try:
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(level)
        file_format = logging.Formatter(
            "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    except Exception as e:
        logger.warning(f"Could not create file handler: {e}")

    return logger
