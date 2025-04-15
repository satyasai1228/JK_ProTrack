from django.http import JsonResponse
from django.views import View
from bson.json_util import dumps, loads  
import ProTrack_API.settings as sts


class Reportdata(View):
    def get(self, request):
        try:
            start_date = "2024-04-01 00:00:00"
            end_date = "2025-04-09 23:59:59"

            date_filter = {
                "$gte": start_date,
                "$lte": end_date
            }

            query = {
                "createdOn": date_filter,
                "batchStatus": "Completed", 
            }

            snquery = {
                "createdOn": date_filter,
                "status": "Completed",
            }

            snAG = {
                "createdOn": date_filter,
                "status": "Completed",
                "rId": 68862725
            }

            AG_projection = {
                "_id": 0,
                "material": 1,
                "batchNumber": 1,
                "materialCode": 1,
                "psn": 1,
                "uom": 1,
                "numerator": 1,
                "csn": 1,
                "status": 1,  
            }

            BatchDetails = loads(dumps(sts.dbcursor.BatchDetails.find(query, {"_id": 0})))

            return JsonResponse({
                "code": 200,
                "status": "success",
                "message": "Data retrieved successfully",
                "data": BatchDetails
            })

        except Exception as e:
            return JsonResponse({
                "code": 500,
                "status": "error",
                "message": f"Server error: {str(e)}"
            })
