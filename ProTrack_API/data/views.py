from django.http import JsonResponse
from django.views import View
from bson.json_util import dumps, loads
import ProTrack_API.settings as sts
from data import models as dat 

class Reportdata(View):
   def get(self, request):
    try:
        start_date = "2025-01-01 00:00:00"
        end_date = "2025-04-15 23:59:59"
        psn = 25663974097630

        query = dat.get_report_query(start_date, end_date, psn)

        sn_agg_data = loads(dumps(sts.dbcursor.SNAggregation.find(query, {"_id": 0})))

        psn_list = [doc["psn"] for doc in sn_agg_data if "psn" in doc]
        print(sn_agg_data,"sn_agg_datasn_agg_datasn_agg_data")
        
        serial_details =  loads(dumps(sts.dbcursor.SerialNumbers.find({"sn": {"$in": psn_list}}, {"_id": 0})))
        print(serial_details,"serial_detailsserial_detailsserial_details")

        rid_list = [int(doc["rId"]) for doc in serial_details if "rId" in doc]


        batch_details =  loads(dumps(
        sts.dbcursor.BatchDetails.find(
        { "recordId": { "$in": rid_list } },
        { "_id": 0,
         "recordId":0,
         "batchType":0,"gtin": 0,
            "gtin1": 0,
            "gtin2": 0,
            "gtin3": 0,
            "gtin4": 0,
            "gtin5": 0,
            "gtinQuantity": 0,
            "gtin1Quantity": 0,
            "gtin2Quantity": 0,
            "gtin3Quantity": 0,
            "gtin4Quantity": 0,
            "gtin5Quantity": 0,
            "reinitiateQuantity": 0,
            "lineIP": 0,
            "level1": 0,
            "level2": 0,
            "level3": 0,
            "level4": 0,
            "level5": 0,
            "reason": 0,
            "shippingId": 0,
            "createdBy": 0,
             "parent": 0, 
            "oecdRefNo":0,
            "toLocation":0,
            "plantCode":0,
            "level":0,
            "gs1gcp":0,
            "ssccgcp":0,
            "packingLevel":0,
            "snType":0,
            "isSync":0,  }  
            )
        ))

        return JsonResponse({
            "code": 200,
            "status": "success",
            "message": "BatchDetails retrieved successfully",
            "SHP":sn_agg_data,
            "data": batch_details,
        })

    except Exception as e:
        return JsonResponse({
            "code": 500,
            "status": "error",
            "message": f"Server error: {str(e)}"
        })
