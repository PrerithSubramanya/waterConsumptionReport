import json
from datetime import datetime
from dateutil import tz
import collections
import csv

json_f = open('readings.json')
water_file = json.load(json_f)


def convertLocal(value):
    """
    Coverts UTC formate to local time (sydney/Australia)
    :param value: UTC time
    :return: local time
    """
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Australia/Sydney')
    try:
        utc = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        return
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


def dateExtractUTC(date_time):
    """
    Extracts Date from UTC time format
    :param date_time: UTC time
    :return: extracted date
    """
    try:
        dateT = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        return dateT.date()
    except ValueError:
        return


def dateExtractLocal(date_time):
    """
    Extracts Date from local time format
    :param date_time: Local Time
    :return: extracted local date
    """

    try:
        dateT = datetime.strptime(date_time[:18], '%Y-%m-%d %H:%M:%S')
        return dateT.date()
    except ValueError:
        return


def analytics(readings):
    """
    Calculates the total consumption of water per day, also calls time conversion and date extraction functions internally
    :param readings: json file
    :return: key value pair that has date and usage in liters
    """

    trackDate = collections.defaultdict()
    for dateT in readings['values']:
        if dateExtractUTC(dateT) is not None:
            dateTLocal = convertLocal(dateT)
            date = dateExtractLocal(str(dateTLocal))
            if str(date) not in trackDate:
                trackDate[str(date)] = readings['values'][dateT][0]['min']
            else:
                trackDate[str(date)] += readings['values'][dateT][0]['min']

    return trackDate


def writeToCsv(file):
    """
    Writes the calculation to a csv file, calls the analytics method internally.
    :param file:
    :return:
    """
    with open('./consumption.csv', 'w') as f:
        columns = ['Date', 'Usage(kL)']
        csv_writer = csv.DictWriter(f, fieldnames=columns)
        csv_writer.writeheader()
        for key in analytics(file).keys():
            f.write("%s, %s\n" % (key, analytics(file)[key] / 1000))



