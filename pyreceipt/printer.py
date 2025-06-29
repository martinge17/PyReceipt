from escpos.printer import File
from .api.model import Options, Item, List
from datetime import datetime
import logging

import tomllib

# Load configuration
try:
    file = open("printer.toml", "rb")
except Exception:
    logging.error("Can't open config file", exc_info=True)
    exit(1)
else:
    with file:
        config = tomllib.load(file)

# Path to the printer device
PRINTER_DEVICE = config["printer"]["device"]
DEFAULT_HEADER = config["strings"]["header"]
DEFAULT_FOOTER = config["strings"]["footer"]

# Get the current date
current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S%z")


def print_receipt(
    items: List[Item],
    options: Options,
    PRINTER_DEVICE=PRINTER_DEVICE,
):

    # Initialize the printer
    printer = File(PRINTER_DEVICE)

    header = options.header or DEFAULT_HEADER
    footer = options.footer or DEFAULT_FOOTER

    # Print receipt content
    try:
        if options.header_toggle:
            printer.set(
                align="center", bold=True, double_width=True, double_height=True
            )
            printer.textln(header)
            printer.ln()
            printer.set(
                align="center", bold=False, normal_textsize=True, double_width=False
            )
            printer.textln(f"{current_date}")  # Print the current date
            # printer.set(font=1)

        # Column header
        printer.set(align="left", bold=True)
        printer.textln(f"{'Producto':<33} {'Uds':>3} {'Precio/u':>10}")
        printer.textln("------------------------------------------------")

        # Print the items and prices dynamically from arrays
        printer.set(align="left", bold=False, smooth=True)
        total = 0
        for i in items:
            item_name = i.name
            qty = i.quantity
            price = i.price_per_unit
            line = f"{item_name:<33} {qty:>3}   {price:>6.2f}/u"
            printer.textln(line)

            total += price * qty

        printer.textln("------------------------------------------------")
        printer.set(
            align="right",
            normal_textsize=False,
            bold=True,
            double_height=True,
            double_width=True,
        )
        printer.textln(f"TOTAL: {total:7.2f}")
        # TODO: It seems there are problems when only footer is printed. So I unified header and footer
        if options.header_toggle:
            # Footer
            printer.set(
                align="center",
                bold=False,
                double_height=False,
                double_width=False,
                normal_textsize=True,
            )
            printer.ln()
            printer.textln(footer)

        printer.cut()  # Cut the paper
        print("Receipt printed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise Exception(e)
    finally:
        try:
            printer.close()
        except Exception as close_err:
            print(f"Failed to close printer: {close_err}")
