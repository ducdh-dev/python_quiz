"""
Input:
s: "We expect the %f%% growth this week"
Expected Output:
"We expect the {}% growth this week"

Input:
s: "%d%d%%-growth in products is expected quite soon"
Expected Output:
"{}{}%-growth in products is expected quite soon"

Input:
s: "Much %%s we have here!"
Expected Output:
"Much %s we have here!"
"""
import re


def new_style_formatting(s):
    return '%'.join(re.sub('%\w', '{}', part) for part in s.split('%%'))
