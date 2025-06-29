from flask import Blueprint, request
from .model import Item, Options, General
from pyreceipt.printer import print_receipt

api = Blueprint("api", __name__, url_prefix="/api")


# Print ticket from JSON data
@api.post("/print")
def print_ticket():
    # Process entry data
    try:
        raw_data = request.get_json()
        data = General.parse_obj(raw_data)
        print_receipt(data.items, data.options)
    except Exception as e:
        return {"error": str(e)}
    return {"message": "Success!"}
