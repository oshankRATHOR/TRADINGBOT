import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from typing import Optional

from bot.orders import place_order

app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI")
console = Console()


@app.command()
def trade(
    symbol: str = typer.Argument(..., help="Trading pair (e.g., BTCUSDT)"),
    side: str = typer.Argument(..., help="'BUY' or 'SELL'"),
    order_type: str = typer.Argument(..., help="'MARKET' or 'LIMIT'"),
    quantity: float = typer.Argument(..., help="Order quantity"),
    price: Optional[float] = typer.Option(None, "--price", help="Price for LIMIT order")
):
    """
    Place a new order on the Binance Futures Testnet.
    """
    # Clean inputs to uppercase strings
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    # Create a pre-execution summary table
    table = Table(title="Order Request Summary", header_style="bold magenta")
    table.add_column("Parameter", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="bold white")

    table.add_row("Symbol", symbol)
    table.add_row("Side", side)
    table.add_row("Order Type", order_type)
    table.add_row("Quantity", str(quantity))
    if price is not None:
        table.add_row("Price", str(price))

    console.print(table)
    console.print("\n[bold yellow]Executing order...[/bold yellow]\n")

    try:
        # Call the actual order execution logic
        summary = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        # 1. Guard against a None or empty response
        if not summary:
            raise ValueError("No response received from the order execution module.")

        # 2. Styled success output if everything passed
        success_msg = (
            f"[bold green]Order Placed Successfully![/bold green]\n\n"
            f"Order ID: [white]{summary.get('orderId', 'N/A')}[/white]\n"
            f"Status: [white]{summary.get('status', 'NEW')}[/white]\n"
            f"Executed Qty: [white]{summary.get('executedQty', quantity)}[/white]\n"
            f"Avg Price: [white]{summary.get('avgPrice', 'N/A')}[/white]"
        )
        console.print(Panel(success_msg, title="Success", border_style="green"))
        
    except Exception as e:
        # Styled error output handling unhandled environment/network exceptions
        error_msg = f"[bold red]System Exception Encountered:[/bold red]\n{str(e)}"
        console.print(Panel(error_msg, title="Execution Error", border_style="red"))


if __name__ == "__main__":
    app()