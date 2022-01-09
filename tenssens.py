# Import Modules
import os
import json
import ipapi
import banner
import hashlib
import requests
import panelList
import builtwith
import robotsList
from time import sleep
from colorama import Fore
from getpass import getpass


# 1. Whois
def whoisInformation():
    try:
        websiteURL = input("(Whois) Enter Website Link : ")
        url = websiteURL
        result = requests.get(f"http://api.hackertarget.com/whois/?q={url}").text
        print(result)
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 2. MD5 Hash Cracker
def md5Cracker():
    try:
        flag = 0
        getHashedPassword = input("(MD5 Cracker) Enter hashed password : ")
        getWordlist = input("Enter password wordlist : ")
        getWordlist = open(wordlist, "r")

        for word in getWordlist:
            enc_wrd = word.encode("utf-8")
            digest = hashlib.md5(enc_wrd.strip()).hexdigest()

            if digest == getHashedPassword:
                print("Password found!!")
                print(f"Password is: {word} ")
                flag = 1
                break
        if flag == 0:
            print("Password is not in the list.")
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 3. Subdomain finder
def getSubDomains():
    try:
        getDomain = input("(Subdomain Finder) Enter Domain name : ")
        filepath = input("Enter a file name to save (txt Format) : ")

        url = f"https://api.securitytrails.com/v1/domain/ {getDomain} /subdomains"
        querystring = {"children_only": "true"}
        headers = {"accept": "application/json", "apikey": "APIKEY"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        resultJson = json.loads(response.text)
        subDomains = [i + "." + getDomain for i in resultJson["subdomains"]]
        f = open(filepath, "w+")
        for i in subDomains:
            f.write(i + "\n")
        f.close()
        return subDomains
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 4. website builtwith information
def siteBuiltWith():
    try:
        target = input("(BuiltWith) Enter Domain URL : : ")
        if not "https://" in target or not "http://" in target:
            target = f"http://{target}"
        information = builtwith.parse(target)
        for name in information:
            value = ""
            for val in information[str(name)]:
                name = name.replace("-", " ")
                name = name.title()
                value = value + str(val)
            print(f"{name} : {value}")
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 5. DNS Lockup
def websiteDNSlockup():
    try:
        getDomainName = input("(DNS Lockup) Enter Domain URL : ")
        result = requests.get(
            "http://api.hackertarget.com/dnslookup/?q=" + getDomainName
        ).text
        print(result)
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 6. Admin Panel Finder
def adminPanelFinder():
    try:
        url = input("(Admin Panel Finder) Enter Website URL : ")
        if "http" in url:
            url = url + "/"
        elif "https" in url:
            url = url + "/"
        else:
            url = "http://" + url + "/"
        for i in panelList.pathList:
            r = requests.get(url + i)
            if r.status_code == 200:
                print(f"{url} {i} Found.")
            else:
                print(f"{url} {i} Not Found.")
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 7. HTTP Header
def httpHeader():
    try:
        getSiteDomain = input("(HTTP Header) Enter The Website URL : ")
        result = requests.get(
            "https://api.hackertarget.com/httpheaders/?q=" + getSiteDomain
        ).text
        print(result)
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 8. IP Location
def ipLocationFinder():
    try:
        getIpAddress = input("(IP Location) Enter IP Address : ")
        source = ipapi.location(ip=getIpAddress, key=None, field=None)
        try:
            print("Your information : ")
            print(" ip = " + source["ip"])
            print(" city = " + source["city"])
            print(" region = " + source["region"])
            print(" id country = " + source["country"])
            print(" country = " + source["country_name"])
            print(" Calling Code = " + source["country_calling_code"])
            print(" Languages = " + source["languages"])
            print(" org = " + source["org"])
        except:
            print("Please Enter Valid IP Address.")
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 9. Port Scanning
def portScanning():
    try:
        getIpOrDomainName = input("(Port Scanner.) Enter IP or Domain name : ")
        result = requests.get(
            "https://api.hackertarget.com/nmap/?q=" + getIpOrDomainName
        ).text
        print(result)
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


# 10. Get Robots txt File
def robotstxt():
    try:
        getDomain = input("(Robots txt) Plase Enter WebSite Address : ")
        if "http" in getDomain:
            pass
        elif "http" != getDomain:
            websiteURL = "http://" + getDomain
        for i in robotsList.pathList2:
            reqs = requests.get(websiteURL)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(websiteURL)
            else:
                print(websiteURL)
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


banner.toolBanner()

# Login
credentials = ["username", "password"]
username = input(Fore.GREEN + "Enter Login Username : ")
password = getpass("Enter Login Password : ")
if username == credentials[0] and password == credentials[1]:
    print("\nLogin Successull.")
    print("\nPlease Wait, Loading.")
    sleep(0.3)
    os.system("clear")
    print("\nPlease Wait, Loading..")
    sleep(0.3)
    os.system("clear")
    print("\nPlease Wait, Loading...")
    sleep(0.3)
    os.system("clear")
    print("\nPlease Wait, Loading....")
    sleep(0.3)
    os.system("clear")
    print("\nPlease Wait, Loading.....")
    sleep(1.5)
    os.system("clear")

    # All Tools
    print(
        """

                ALl Tools (Select a Number)
 ------------------------------------------------------
   01. Whois            : Get Website Whois Information.
   02. MD5 Cracker      : MD5 Hash Cracker.
   03. Subdomain finder : Find Subdomain of any website.
   04. Site BuiltWith   : Find CMS of and All Technology.
   05. DNS Lockup       : Get Information About DNS.
   06. Admin Finder     : Find Admin Panel of Website.
   07. HTTP Header      : Get HTTP Header Information.
   08. IP Location      : Find Location From IP Address.
   09. Port Scan        : Network Port Scanner.
   10. Robots.txt       : Get Robots txt File of any website.
    
    """
    )

    try:
        tools = input("Select a Number : ")
        if "1" == tools or "01" == tools:
            whoisInformation()
        elif "2" == tools or "02" == tools:
            md5Cracker()
        elif "3" == tools or "03" == tools:
            getSubDomains()
        elif "4" == tools or "04" == tools:
            siteBuiltWith()
        elif "5" == tools or "05" == tools:
            websiteDNSlockup()
        elif "6" == tools or "06" == tools:
            adminPanelFinder()
        elif "7" == tools or "07" == tools:
            httpHeader()
        elif "8" == tools or "08" == tools:
            ipLocationFinder()
        elif "9" == tools or "09" == tools:
            portScanning()
        elif "10" == tools:
            robotstxt()
        else:
            print("Enter Valid Number.")
    except Exception as err:
        print(f"An Error Occurred : {err}, Try Again.")


else:
    print("Wrong Login Information. Please try Again.")
    exit()
