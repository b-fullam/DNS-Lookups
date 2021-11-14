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
# opening and reading the file containing a list of domain names
    with open(input("\nEnter file name and/or path: ")) as fcontent:
        fstring = fcontent.readlines()
    
    # declaring the regex pattern to grab the most complete parts of the domain entries from a list to reduce errors
    pattern = re.compile(r'(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?')

    lst=[]
    
    # extracting the domains
    for line in fstring:
        lst.append(pattern.search(line)[0])

    print(" ")
    print(lst)
    print(" ")

    # iterate through the array of domains
    # with the dnsLookup function
    for i in lst:
        dnsLookup(i)

    

# Prompt user for input type of a single domain or import a list of domains
single_or_multiple_domains = int(input("Enter '1' for single entry or '2' to import a list of domain names: \n"))

# Conditional statement to handle user input for a single domain
# or call the function to handle the imported list of domains
if single_or_multiple_domains == 1:
    dnsLookup(input("\nEnter Domain: "))
else: 
    dnsLookupList()