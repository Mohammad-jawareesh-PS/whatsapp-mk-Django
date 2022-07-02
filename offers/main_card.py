# Direct Payment End Point

# Import required libraries (make sure it is installed!)
from pickle import FALSE
import requests
import json
import sys

# -----------------------------Define Functions
def payment_now(price="Unknown", 
                Number="Unknown",
                ExpiryMonth="Unknown",
                ExpiryYear="Unknown",
                SecurityCode="Unknown",
                CardHolderName="Unknown",
                CallBackUrl="Unknown",
                ErrorUrl="Unknown",
                test_card=True):

    if test_card:
        Number = 5453010000095489
        ExpiryMonth = 12
        ExpiryYear = 28
        SecurityCode = 212
        CardHolderName = 'Abderrazzak Ai'
        CallBackUrl = 'http://www.example.com'
        ErrorUrl = 'http://www.example.com'


    def check_data(key, response_data):
        if key in response_data.keys() and response_data[key] is not None:
            return True
        else:
            return False

    # Error Handle Function
    def handle_response(response):
        if response.text == "":  # In case of empty response
            raise Exception("API key is not correct")

        response_data = response.json()
        response_keys = response_data.keys()

        if "IsSuccess" in response_keys and response_data["IsSuccess"] is True:
            return  # Successful
        elif check_data("ValidationErrors", response_data):
            error = []
            for i in range(len(response.json()["ValidationErrors"])):
                v_error = [response_data["ValidationErrors"][i].get(key) for key in ["Name", "Error"]]
                error.append(v_error)
        elif check_data("ErrorMessage", response_data):
            error = response_data["ErrorMessage"]
        elif check_data("Message", response_data):
            error = response_data["Message"]
        elif check_data("ErrorMessage", response_data["Data"]):
            error = response_data["Data"]["ErrorMessage"]
        else:
            error = "An Error has occurred. API response: " + response.text
        raise Exception(error)

    # Call API Function
    def call_api(api_url, api_key, request_data, request_type="POST"):
        request_data = json.dumps(request_data)
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_key}
        response = requests.request(request_type, api_url, data=request_data, headers=headers)
        handle_response(response)
        return response

    # Initiate Payment endpoint Function
    def initiate_payment(initiatepay_request):
        api_url = base_url + "/v2/InitiatePayment"
        initiatepay_response = call_api(api_url, api_key, initiatepay_request).json()
        payment_methods = initiatepay_response["Data"]["PaymentMethods"]
        # Initiate Payment output if successful
        print("Payment Methods: ", payment_methods)
        return payment_methods

    # Execute Payment endpoint Function
    def execute_payment(executepay_request):
        api_url = base_url + "/v2/ExecutePayment"
        executepay_response = call_api(api_url, api_key, executepay_request).json()
        invoice_id = executepay_response["Data"]["InvoiceId"]
        invoice_url = executepay_response["Data"]["PaymentURL"]
        # Execute Payment output if successful
        print("InvoiceId: ", invoice_id,
            "\nInvoiceURL: ", invoice_url)
        return invoice_id, invoice_url

    # Direct Payment endpoint Function
    # The payment link from execute payment is used as the API for direct payment
    def direct_payment(directpay_request, invoice_url):
        directpay_response = call_api(invoice_url, api_key, directpay_request).json()
        directpay_status = directpay_response["Data"]
        # Direct Payment output if successful
        print("Direct Payment Status: ", directpay_status)
        return directpay_status

    if test_card:
        # Test Environment
        base_url = "https://apitest.myfatoorah.com"
        api_key = "rLtt6JWvbUHDDhsZnfpAhpYk4dxYDQkbcPTyGaKp2TYqQgG7FGZ5Th_WD53Oq8Ebz6A53njUoo1w3pjU1D4vs_ZMqFiz_j0urb_BH9Oq9VZoKFoJEDAbRZepGcQanImyYrry7Kt6MnMdgfG5jn4HngWoRdKduNNyP4kzcp3mRv7x00ahkm9LAK7ZRieg7k1PDAnBIOG3EyVSJ5kK4WLMvYr7sCwHbHcu4A5WwelxYK0GMJy37bNAarSJDFQsJ2ZvJjvMDmfWwDVFEVe_5tOomfVNt6bOg9mexbGjMrnHBnKnZR1vQbBtQieDlQepzTZMuQrSuKn-t5XZM7V6fCW7oP-uXGX-sMOajeX65JOf6XVpk29DP6ro8WTAflCDANC193yof8-f5_EYY-3hXhJj7RBXmizDpneEQDSaSz5sFk0sV5qPcARJ9zGG73vuGFyenjPPmtDtXtpx35A-BVcOSBYVIWe9kndG3nclfefjKEuZ3m4jL9Gg1h2JBvmXSMYiZtp9MR5I6pvbvylU_PP5xJFSjVTIz7IQSjcVGO41npnwIxRXNRxFOdIUHn0tjQ-7LwvEcTXyPsHXcMD8WtgBh-wxR8aKX7WPSsT1O8d8reb2aR7K3rkV3K82K_0OgawImEpwSvp9MNKynEAJQS6ZHe_J_l77652xwPNxMRTMASk1ZsJL"
    else :
        # Live Environment
        base_url = "https://api.myfatoorah.com"
        api_key = "jSataQU9B4PkW2qQRZH3nG6ymtkKrQO_dWWfYfamhNDObkYJpQ76IPJj_GSS4vcYyRIsV9TMLGYrZPXsVXVcd8PIWHdePHM-GGzFw-ZziEbGk7UFpqveDRTbXgwvL91OLx1qAzcPLQaSTSjcIBBsJG2IF9yr2iy1H9CxRZBfjkgWXRrNhXpwt7RI-EF6y4VpRTQHw0fXKnXm4ITaqhPvnufjvzUhbv8b4NzPHKufyvIFh-0bQIO6eAnwu0SYd6CdilrVdOklCWjXKYrcxDVUNrrwa3RSyAVdHvlk32U1uVyiysdxaxlHI9EWNA64oBtrg9hBCZ3irqgPF_AYmi-mxdA4xTWJv_1baabwz6hta5a_Z2ZznyvjoY4YV6YHCRfrtEWd0pWNJ5Z_dU1nEkLLTMlHwJxPErfDMex1mOl0UTI079hutr3hO3NSpy5GoIJI3zdCzEJ3d_W-bMBrkdE9W9SsrFhHrR7-33dP2WZ0Db_lvg_0C2PWaLF_l5_advAYju0xJA7lg8o6DISZ_gi9CpSbTOL3YQ-Hgy0mogNSzIlsJht8m9B4iFDo1MYR6wWz-kpMhSKuXHl2ORaSZrkp6DZOGC-Vh93uLb_BGwhJvX92pHq6Q1hhZ1qDBffETMQL7RAY67xxFm8GNgiv2NFd06_NfK3OsS3-qkHr9OCBajuAsmegY1aHilKGheuz1dP-TeoLXo_6KOt60FVwBpp0IDCNp4cLhq9-tXOltz-6wqDNxvBD"

    # Initaite Payment request data
    initiatepay_request = {
                        "InvoiceAmount": price,
                        "CurrencyIso": "USD"
                        # "CurrencyIso": "KWD"
                        }

    try:
        # Getting the value of payment Method Id
        payment_method = initiate_payment(initiatepay_request)

        # Creating a simplified list for payment methods
        payment_method_list = []
        for item in range(len(payment_method)):
            if payment_method[item]["IsDirectPayment"] == True:
                y = [payment_method[item].get(key) for key in ["PaymentMethodEn", "PaymentMethodId"]]
                payment_method_list.append(y)
        print(payment_method_list)


        # Get the payment method key.
        while True:
            # payment_method_id = input("Kindly enter the number equivalent to the required payment method: ")
            payment_method_id = payment_method_list[0][1]
            try:
                if int(payment_method_id) in [el[1] for el in payment_method_list]:
                    break
                else:
                    print("Kindly enter a correct payment method id")
            except:
                print("The input must be a number")

        # Based on the initiate payment response, we select the value of reference number to choose payment method

        # Execute Payment Request
        executepay_request = {
                            "paymentMethodId" : payment_method_id,
                            "InvoiceValue"    : price,
                            "CallBackUrl"     : CallBackUrl,
                            "ErrorUrl"        : ErrorUrl,
                        # Fill optional data
                            #"CustomerName"       : "fname lname",
                            "DisplayCurrencyIso" : "USD",
                            #"DisplayCurrencyIso" : "KWD",
                            #"MobileCountryCode"  : "+965",
                            #"CustomerMobile"     : "1234567890",
                            #"CustomerEmail"      : "email@example.com",
                            #"Language"           : "en", #or "ar"
                            #"CustomerReference"  : "orderId",
                            #"CustomerCivilId"    : "CivilId",
                            #"UserDefinedField"   : "This could be string, number, or array",
                            #"ExpiryDate"         : "", #The Invoice expires after 3 days by default. Use "Y-m-d\TH:i:s" format in the "Asia/Kuwait" time zone.
                            #"SourceInfo"         : "Pure PHP", #For example: (Laravel/Yii API Ver2.0 integration)
                            #"CustomerAddress"    : "customerAddress",
                            #"InvoiceItems"       : "invoiceItems",
                        }

        # Execute payment t get Invoice Id and Invoice URL
        invoice_id, invoice_url = execute_payment(executepay_request)

        # Required Data for direct Payment
        directpay_request = {
                                "PaymentType": "card",
                                "Bypass3DS": False,
                                "SaveToken": "false",
                                "Token": "string",
                                "Card": {
                                    "Number": Number,
                                    "ExpiryMonth": ExpiryMonth,
                                    "ExpiryYear": ExpiryYear,
                                    "SecurityCode": SecurityCode,
                                    "CardHolderName": CardHolderName,
                                }
                        }

        direct_payment(directpay_request, invoice_url)
        return True
    except:
        ex_type, ex_value, ex_traceback = sys.exc_info()
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" % ex_value)
