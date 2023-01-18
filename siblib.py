from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

key = "xxxx"
mail = "xxxx"

def sendMail(recipientMail, recipientName, subject, content):

    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = key

    # create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    senderSmtp = sib_api_v3_sdk.SendSmtpEmailSender(name="SendinBlue Server ",email=mail)
    sendTo = sib_api_v3_sdk.SendSmtpEmailTo(email=recipientMail,name=recipientName)
    arrTo = [sendTo] #Adding `to` in a list
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(sender=senderSmtp,to=arrTo,html_content=content,subject=subject)

    try:
        # Send a transactional email
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)%