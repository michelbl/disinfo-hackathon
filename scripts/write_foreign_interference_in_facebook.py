# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import dpath
import json

from collections import Counter
from read_facebook_report import get_json_content


JSON = "../international_facebook_advertising.json"
content = get_json_content(JSON)

# 'disclaimer': disclaimer,
# 'page_name': page_name,
# 'page_id': page_id,
# 'advertiser': advertiser,
# 'advertiser_kind': 'disclaimer' if has_disclaimer else 'page',
# 'countries': set(),
# 'spent': Counter(),
# 'spent_euro': Counter(),
# 'ads': Counter()

spent_per_country = Counter()
foreign_interference_per_country = Counter()
proportion_per_country = Counter()

for record in content.values():
    # advertisement for more than one country ~ "foreign interference"
    foreign_interference = len(record['countries']) > 1
    for country, amount in record['spent_euro'].items():
        spent_per_country[country] += amount
        if foreign_interference:
            foreign_interference_per_country[country] += amount

print("spent_per_country", spent_per_country)
print("foreign_interference_per_country", foreign_interference_per_country)      
        
for country, spent in spent_per_country.items():
    proportion_per_country[country] = round(100 * foreign_interference_per_country[country] / spent, 2)   

print("proportion_per_country", proportion_per_country)

with open("foreign_interference_facebook.json", 'w') as f:
    json.dump(proportion_per_country, f)
