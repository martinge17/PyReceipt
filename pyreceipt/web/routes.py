from flask import Blueprint, render_template, send_file
import json
from pyreceipt import app

web = Blueprint("web", __name__, template_folder="templates", static_folder="static")


@web.get("/")
def main():
    return render_template("index.html")


# Service Worker for PWA
@web.get("/sw.js")
def sw():
    return send_file("static/scripts/sw.js")
