from api import API
import ast
import json
from webob.response import Response
import os
import africastalkingwrapper

# from africastalkingwrapper.tasks import send_message

username = os.getenv('USERNAME')   
api_key = os.getenv('API_KEY')

# Initialize Creds
africastalkingwrapper.initialize(username, api_key)

print(africastalkingwrapper.initialize(username, api_key))
# Initialize Wrapper
sms = africastalkingwrapper.SMS


# sms = africastalkingwrapper.tasks



app = API()


@app.route("/api/send_sms/")
class SendSmsHandler:
    def post(self,req, resp):
        """Send message endpoint"""
        _decoded = req.body.decode('utf-8')
        req_data = json.loads(_decoded)
        try:
            msg = req_data["msg"]
            phone_number_list= req_data["phoneNumber"]
            phone_vals = [str(i) for i in phone_number_list]
            
            resp.json = sms.send(msg,phone_vals)
            return resp.json

        except Exception as e:
            return f"A problem occured! {e}"



# @app.route("/api/send_premium/")
# def post(self,request, response=None):
#     """Send premium message endpoint"""
#     try:
#         print(request)
#         _decoded = request.body.decode('utf-8')
#         req_data = json.loads(_decoded)
#         msg = req_data["msg"]
#         short_code = req_data["short_code"]
#         recipients = req_data["receipients"]
#         resp = sms.send_premium(msg,recipients)
   
#         return resp.json
#     except Exception as e:
#         print(e)



    # @app.route("/api/fetch_subscriptions(/")
    # def fetch_subscriptions(self,req, resp):
    #     """
    #     :param request: {"msg":"Hello Wprld", "phone_number":["0722212132","0738161159"]}
    #     :param response:
    #     :return:

    #     short_code: Premium short code mapped to your account. REQUIRED
    #     keyword: Premium keyword under the above short code and is also mapped to your account. REQUIRED
    #     phone_number: PhoneNumber to be subscribed REQUIRED
    #     checkout_token: Token used to validate the subscription request REQUIRED. See token service
    #     """
    #     # response = sms.send(req["msg"],req["phone_number"])
    #     response = sms.send("Hello Message!", ["+254722212132"])
    #     print(response)
    #     # x = req.body.decode('utf-8')
    #     # f = json.dumps(x)
    #     # print(x)
    #     # resp.text =print

    # @app.route("/api/create_subscription/")
    # def create_subscription(self,req, resp):
    #     """
    #     :param request: {"msg":"Hello Wprld", "phone_number":["0722212132","0738161159"]}
    #     :param response:
    #     :return:

    #     short_code: Premium short code mapped to your account. REQUIRED
    #     keyword: Premium keyword under the above short code and mapped to your account. REQUIRED
    #     last_received_id: ID of the subscription you believe to be your last. Defaults to 0
    #     """
    #     # response = sms.send(req["msg"],req["phone_number"])
    #     response = sms.send("Hello Message!", ["+254722212132"])
    #     print(response)
    #     # x = req.body.decode('utf-8')
    #     # f = json.dumps(x)
    #     # print(x)
    #     # resp.text =print


    # @app.route("/api/delete_subscription/")
    # def delete_subscription(self,req, resp):
    #     """
    #     :param request: {"msg":"Hello World", "phone_number":["0722212132","0738161159"]}
    #     :param response:
    #     :return:

    #     short_code: Premium short code mapped to your account. REQUIRED
    #     keyword: Premium keyword under the above short code and is also mapped to your account. REQUIRED
    #     phone_number: PhoneNumber to be subscribed REQUIRED
    #     """
    #     # response = sms.send(req["msg"],req["phone_number"])
    #     response = sms.send("Hello Message!", ["+254722212132"])
    #     print(response)
    #     # x = req.body.decode('utf-8')
    #     # f = json.dumps(x)
    #     # print(x)
    #     # resp.text =print
