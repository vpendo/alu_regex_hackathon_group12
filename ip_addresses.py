import re

# Test string
test_string = """IP Addresses:
256.2.134.282
192.168.1.100
10.0.0.1
8.8.8.8
172.16.0.1
255.255.255.256"""

# Regex pattern to match IP
ip_pattern = re.compile(r'((?:(?:[01]\d{2}|2[0-4]\d|25[0-5]|\d{1,2})\.){3}(?:[01]\d{2}|2[0-4]\d|25[0-5]|\d{1,2}(?=\D|$)))')

# Test to see if pattern matches them correctly
if len(ip_pattern.findall(test_string)) != 0:
    print(f"Matches: {ip_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")