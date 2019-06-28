# -*- coding: utf-8 -*-

import json
import dpath
import pandas


DISINFO_DIR = "/Volumes/Transcend/_disinfo_hackathon"

def get_json_content(json_filename):
    with open(json_filename, 'r') as f:
        content = json.load(f)
    return content


fr_report_data = get_json_content(DISINFO_DIR + "/facebook/reports/FR/2019-06-27/data.json")
totalSpend = dpath.util.get(fr_report_data, "lifetime_data/2019-06-27/payload/totalSpend")
# print("totalSpend", totalSpend)


def get_csv_content(csv_filename):
    content = pandas.read_csv(csv_filename)
    return content
    
facebookAdLibraryReport = DISINFO_DIR + "/facebook/reports/FR/2019-06-27/FacebookAdLibraryReport_2019-06-26_FR_yesterday/FacebookAdLibraryReport_2019-06-25_FR_yesterday_locations.csv"
fr_report = get_csv_content(facebookAdLibraryReport)  # DataFrame
columns = fr_report.columns.map(lambda x: x.replace(' ', '_'))
fr_report.columns = columns
# print("Locations", fr_report.Location_Name)

