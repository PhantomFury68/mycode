import requests
import xml.etree.ElementTree as Xet
import pandas as pd


url = "http://tmstest.chmccorp.cchmc.org/tmswebservices/AssetWS.asmx"
payload = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.frsoft.com/webservices">  
                <soapenv:Header/>
                <soapenv:Body>
                    <web:Load>
                        <web:header>
                            <web:Server>mcfrsqldevnew</web:Server>
                            <web:Database>cmmsTEST</web:Database>
                            <web:UserName>system</web:UserName>
                            <web:Password>manager</web:Password>
                            <web:HostName>mcfrsqldevnew</web:HostName>
                            <web:OpenObjectId>?</web:OpenObjectId>
                            <web:UseSSOAuthentication>false</web:UseSSOAuthentication>
                        </web:header>
                        <web:assetNumber>KN166725</web:assetNumber>
                    </web:Load>
                </soapenv:Body>
            </soapenv:Envelope>"""

headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

cols = ["AssetNumber", "Description", "ManufacturerName", "ModelNumber", "SerialNumber", "StatusCode", "SiteName"]

#  Initialize the rows variable.  This will hold the values we want to pass to the dataframe.
rows = []

def main():
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:  # status code 200 indicates a successful URL query
        xmlparse = Xet.fromstring(response.text)
        ns = {'web': 'http://www.frsoft.com/webservices'}
        assetnumber = xmlparse.find(".//web:AssetNumber", ns).text
        description = xmlparse.find(".//web:Description", ns).text
        mfr = xmlparse.find(".//web:ManufacturerName", ns).text
        model = xmlparse.find(".//web:ModelNumber", ns).text
        serial = xmlparse.find(".//web:SerialNumber", ns).text
        statuscode = xmlparse.find(".//web:StatusCode", ns).text
        sitename = xmlparse.find(".//web:SiteName", ns).text

        rows.append({
        #    "AssetNumber": assetnumber,
        #    "Description": description,
        #    "ManufacturerName": mfr,
        #    "ModelNumber": model,
        #    "SerialNumber": serial,
        #    "StatusCode": statuscode,
        #    "SiteName": sitename

        #   Use values out of the cols list for the heading names
            cols[0]: assetnumber,
            cols[1]: description,
            cols[2]: mfr,
            cols[3]: model,
            cols[4]: serial,
            cols[5]: statuscode,
            cols[6]: sitename
        })

        #   With the AssetWS.asmx api, only 1 result will ever be returned because it 
        #   is designed to query 1 asset and return its tags and data.
        #   We then assign the header and results to a dataframe object and then print it
        df = pd.DataFrame(rows, columns=cols)
        print(df)
    else:
        print(f"Request failed with status code {response.status_code}")

main()
