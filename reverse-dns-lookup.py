import subprocess
import re

def dnsLookup(arg):
    # use subprocess to call the host command in the os
    process = subprocess.Popen(['host', arg], 
                               stdout=subprocess.PIPE,
                               encoding='utf-8')
    data = process.communicate()
    print(data[0])


def dnsLookupList():
# opening and reading the file containing a list of IPs
    with open(input("\nEnter file name and/or path: ")) as fh:
        string = fh.readlines()

    # declaring the regex pattern to filter Private from Public IP addresses in a list
    pattern = re.compile(r'(^0\.)|(^10\.)|(^100\.6[4-9]\.)|(^100\.[7-9]\d\.)|(^100\.1[0-1]\d\.)|(^100\.12[0-7]\.)|(^127\.)|(^169\.254\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.0\.0\.)|(^192\.0\.2\.)|(^192\.88\.99\.)|(^192\.168\.)|(^198\.1[8-9]\.)|(^198\.51\.100\.)|(^203.0\.113\.)|(^22[4-9]\.)|(^23[0-9]\.)|(^24[0-9]\.)|(^25[0-5]\.)')

    Private_IPs =[]
    Public_IPs=[]

    # extracting the IP addresses
    for line in string:
        line = line.rstrip()
        result = pattern.search(line)
  
        if result:
            Private_IPs.append(line)
    
        else:
            Public_IPs.append(line)
    
    
    """
    Display the sorted Private and Public IP addresses found in the imported list for debugging purposes.

    print("Private IPs")
    print(Private_IPs)
    
    print("Public IPs")
    print(Public_IPs)

    """
    
    # declaring the regex pattern to further filter the list for valid Public IP addresses
    pattern2 =re.compile(r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')
    
    # initialized array values
    valid2 =[]
    invalid2=[]

    for i in Public_IPs:
        i = i.rstrip()
        result = pattern2.search(i)
        
        if result:
            valid2.append(i)
        else:
            invalid2.append(i)

    # displaying the sorted valid IP addresses prior to running the reverse dns lookup
    print("Valid Public IPs")
    print(valid2)
    print(" ")

    # Display invalid ip addresses for debugging
    #print("Invalid IPs")
    #print(invalid2)

    # iterate through the array of valid public ip addresses
    # with the dnsLookup function
    for i in valid2:
        dnsLookup(i)

    

# Prompt user for input type of a single IP or import a list of IP addresses
single_or_multiple_ips = int(input("Enter '1' for single entry or '2' to import a list of IP addresses: \n"))

# Conditional statement to handle user input for a single domain
# or call the function to handle the imported list of domains
if single_or_multiple_ips == 1:
    dnsLookup(input("\nEnter IP address: "))
else: 
    dnsLookupList()