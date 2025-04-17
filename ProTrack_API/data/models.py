# data/models.py
from datetime import datetime

def get_report_query(start_date_str, end_date_str, psn):
   
    return {
        "createdOn": {
            "$gte": start_date_str,
            "$lte": end_date_str
        },
        "psn": psn
    }
