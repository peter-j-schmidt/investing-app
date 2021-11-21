import os
import requests

from dotenv import load_dotenv

from flask import redirect, render_template, request, session
from functools import wraps


def index_info():
    
    load_dotenv

    try:
        fred_key = os.getenv('FRED_KEY')
        response = request.get("https://api.stlouisfed.org/fred/series?series_id=DJIA&api_key={fred_key}&file_type=json")
        response.raise_for_status()
    except request.RequestException:
        return None

    
    try:
        quote = response.json()
        return {
            "title": quote["title"],
            "id": quote["id"],
            "frequency": quote["frequency"]
        }
    except (KeyError, TypeError, ValueError):
        return None
        



def lookup(symbol):

    load_dotenv

    try:
        api_key = os.getenv('IEX_KEY')
        response = requests.get("https://sandbox-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")
        response.raise_for_status()
    except request.RequestException:
        return None


    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def news():

    load_dotenv

    try:
        api_key = os.getenv('IEX_KEY')
        response = request.get('https://sandbox-sse.iexapis.com/stable/news-stream?token={api_key}')
        response.raise_for_status()
    except response.RequestException:
        return None

    
    try:
        feed = response.json()
        return {
            "headline": feed["headline"],
            "related": feed["related"],
            "summary": feed["summary"]
        }
    except (KeyError, TypeError, ValueError):
        return None