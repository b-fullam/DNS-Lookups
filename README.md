# DNS-Lookups
Python scripts to perform both DNS and Reverse DNS lookups from either a single entry or from a list.


## Getting Started

For more information about each script, check out my article on "[Security automation with Python — DNS and Reverse DNS lookups](https://www.brettfullam.com/security-automation-with-python-dns-and-reverse-dns-lookups/)." 

1. Download the scripts or use git to clone the repository

2. Install dependencies.  Both scripts were created using Python3, and the only dependency you'll need to install is the "module re" to add support for regular expressions.

3. I also included 2 text files for testing each of the dns lookup scripts.  One for domains, test-domains.txt, which has domains with intentional formatting errors to test the regex pattern included in the dns lookup script.  One for IP addresses, test-ips.txt, which includes a mix of public and private IP addresses, as well as a handful of improperly formatted IP addresses to test the regex patterns included in the reverse dns lookup script.

