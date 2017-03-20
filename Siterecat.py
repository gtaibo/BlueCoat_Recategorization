from argparse import ArgumentParser
import json
import requests
import sys
import cookielib


class SiteReview(object):
    def __init__(self):
        self.baseurl = "http://sitereview.bluecoat.com/rest/categorization"
        self.useragent = {"User-Agent": "Mozilla/5.0"}

    def sitereview(self, url):
        payload = {"url": url}
        
        try:
            self.req = requests.post(
                                    self.baseurl,
                                    headers=self.useragent,
                                    data=payload
                                    )
        except requests.ConnectionError:
            sys.exit("[-] ConnectionError: " \
                     "A connection error occurred")

        return json.loads(self.req.content)

    def check_response(self, response):

        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} returned".format(req.status_code))

        elif "error" in response:
            sys.exit(response["error"])

        else:
            self.url = response["url"]
            self.category = response["categorization"].split('>')[1].split('<')[0]
            self.trackid = response["curtrackingid"]

      

def main(url):
    s = SiteReview()
    response = s.sitereview(url)
    s.check_response(response)
    border = "*=" * (len("BlueCoat Site Review") + 2)

    print "\n{0}\n{1}\n{0}\n".format(border, "Blue Coat Site Review")
    print ("Domain:") +s.url + ("\n")
    print ("Category:") +s.category +("\n")
    

    bccat = ['Dynamic DNS Host','Hacking','Malicious Outbound Data/Botnets','Malicious Sources/Malnets','Mixed Content/Potentially Adult','Peer-to-Peer (P2P)','Phishing','Pornography','Potentially Unwanted Software','Proxy Avoidance','Remote Access Tools','Spam','Suspicious']
    
    recategorize=raw_input("Would you like to re-categorize it? (y/n)\n")
    if recategorize == "n":
            print("\nNow Exiting...")
            raise SystemExit


    if recategorize == "y" or "Y":
          
        print(""" 

        Menu
        ------------------
        1.Dynamic DNS Host
        2.Hacking
        3.Malicious Outbound Data/Botnets
        4.Malicious Sources/Malnets
        5.Mixed Content/Potentially Adult
        6.Peer-to-Peer (P2P)
        7.Phishing
        8.Pornography
        9.Potentially Unwanted Software
        10.Proxy Avoidance
        11.Remote Access Tools
        12.Suspicious
        """)
        ans=raw_input("Choose a number from 1 to 12: \n")

        

    
    if ans=="1":
        print("\n Submitting as Dynamic DNS Host")
        submitted_ans= "103"     
             
    elif ans=="2":
            print("\n Submitting as Hacking")
            submitted_ans= "17"
             
    elif ans=="3":
            print("\n Submitting as Malicious Outbound Data/Botnets")
            submitted_ans= "44"
             
    elif ans=="4":
            print("\n Submitting as Malicious Sources/Malnets") 
            submitted_ans= "43"

    elif ans=="5":
            print("\n Submitting as Mixed Content/Potentially Adult")
            submitted_ans= "50"
    elif ans=="6":
            print("\n Submitting as Peer-to-Peer (P2P)")
            submitted_ans= "83"
    elif ans=="7":
            print("\n Submitting as Phishing")
            submitted_ans= "18"
    elif ans=="8":
            print("\n Submitting as Pornography")
            submitted_ans= "3"
    elif ans=="9":
            print("\n Submitting as Potentially Unwanted Software")
            submitted_ans= "102"
    elif ans=="10":
            print("\n Submitting as Proxy Avoidance")
            submitted_ans= "86"
    elif ans=="11":
            print("\n Submitting as Remote Access Tools")
            submitted_ans= "57"
    elif ans=="12":
            print("\n Submitting as Suspicious")
            submitted_ans= "92"

    else:
            print("\n Not Valid Choice! Now Exiting...")
            raise SystemExit



              
    email = "your-email@yahoo.com"
    trackid =  s.trackid
    jssid = s.req.headers["set-cookie"]
    
    url = "http://sitereview.bluecoat.com/rest/submitCategorization"
    origin = "http://sitereview.bluecoat.com"
    headers= {'Cookie':jssid, 'Accept':'application/json, text/javascript','User-Agent': 'Mozilla/5.0','X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://sitereview.bluecoat.com/sitereview.jsp'}
    data= {'referrer':'bluecoatsg', 'suggestedcat':submitted_ans ,'suggestedcat2':submitted_ans ,'emailCheckBox':'on','email': email , 'emailcc':'','comments':'', 'overwrite':'no','trackid':trackid }
    r = requests.post(url, data, headers=headers)

    if r.status_code == 200:
        print("Your categorization has been submitted")        


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("url", help="Submit domain/URL to Blue Coat's Site Review")
    args = p.parse_args()

    main(args.url)

else:
    pass
