
import requests
import json

url =  "https://returnxdigital.leadbyte.co.uk/api/submit.php?returnjson=yes&campid=FUNERAL-COVER&sid=24845&testmode=yes&email=test@test.com&firstname=Test&lastname=Test&phone1=0613394600&optinurl=http://url.com&optindate=INSERTVALUEyes&grossmonthlyincome=11&acceptterms=true&offer_id=2719"

response = requests.post(url = url)
content = str(response.content);
content = content.replace("b'", '')
content= content.rstrip("\'")
res = json.loads(content)
print(res.get("code"))
print(response.content)