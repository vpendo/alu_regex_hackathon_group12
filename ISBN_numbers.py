import re

# Test string
test_string = """ISBN Numbers:
ISBN 0307459914
ISBN 978-0-307-45991-4 
ISBN 978-1-4516-1100-0
ISBN 978-0-385-33388-5
ISBN 978-0-262-13474-6
ISBN 978-0-14-313082-2"""

# Regex pattern to match ISBN numbers
ISBN_pattern = re.compile(r'ISBN \d{3}-\d-\d{3}-\d{5}-\d')

# Test to see if pattern matches them correctly
if len(ISBN_pattern.findall(test_string)) != 0:
    print(f"Matches: {ISBN_pattern.findall(test_string)}")
else:
    print(f"{test_string} has no matches")