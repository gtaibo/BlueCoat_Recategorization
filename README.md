
Blue Coat Site Review Checker (CLI)

Description-

"The purpose of Site Review is to allow Blue Coat customers to check the current categorization of WebPulse URL ratings and report sites that they believe are incorrectly categorized."

https://sitereview.bluecoat.com/sitereview.jsp



Python script allows users to query the current categorization of a site via CLI. After querying Site Review, it provides the user with an option to Re-Categorize the site. 

Usage-
Siterecat.py takes one argument and submits the query to get current categorization. It also provides the option to recategorize by providing a menu of options available. Just enter the number corresponding to most appropriate category.

Important: Update line 130 with your e-mail address if you would like to receive a notification from Blue Coat. 

example: 

Siterecat.py malicious.com
*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
Blue Coat Site Review
*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=

Domain:http://malicious.com

Category:Suspicious

Would you like to re-categorize it? (y/n)
y

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
        
Choose a number from 1 to 12: 
1

 Submitting as Dynamic DNS Host
Your categorization has been submitted

Python Requirements

argparse
bs4
json
requests
sys
