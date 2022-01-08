import json
from datetime import datetime
from dateutil import tz
import csv
import os

KILOUNITS = 1000


def convertLocal(utcDateTime):
    """
    Coverts UTC format to local time (sydney/Australia)
    :param utcDateTime: UTC time
    :return: local time
    """
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Australia/Sydney')
    try:
        utc = datetime.strptime(utcDateTime, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        return
    utc = utc.replace(tzinfo=from_zone)
    return str(utc.astimezone(to_zone))


def dateExtractUTC(utcDateTime):
    """
    Extracts Date from UTC time format
    :param utcDateTime: UTC date and time
    :return: extracted UTC date
    """
    try:
        dateT = datetime.strptime(utcDateTime, '%Y-%m-%dT%H:%M:%S.%fZ')
        return str(dateT.date())
    except ValueError:
        return


def dateExtractLocal(localDateTime):
    """
    Extracts Date from local time format
    :param localDateTime: Local date and Time
    :return: extracted local date
    """

    try:
        dateT = datetime.strptime(localDateTime[:18], '%Y-%m-%d %H:%M:%S')
        return str(dateT.date())
    except ValueError:
        return


def analytics(waterReadings):
    """
    Calculates the total consumption of water per day, also calls time conversion and date extraction functions
    internally
    :param waterReadings: json file
    :return: key value pair that has date and usage in liters
    """

    trackDate = {}
    for dateTimeUTC in waterReadings['values']:
        if dateExtractUTC(dateTimeUTC) is not None:
            dateTLocal = convertLocal(dateTimeUTC)
            dateLocal = dateExtractLocal(dateTLocal)
            if dateLocal not in trackDate and waterReadings['values'][dateTimeUTC][0] is not None:
                trackDate[dateLocal] = waterReadings['values'][dateTimeUTC][0]['min']
            elif dateLocal in trackDate and waterReadings['values'][dateTimeUTC][0] is not None:
                trackDate[dateLocal] += waterReadings['values'][dateTimeUTC][0]['min']

    return trackDate


def literTokLiter(liter):
    """
    Converts liters to kilo liters
    :param liter: water units in liters
    :return: water units in kilo liters
    """
    return liter/KILOUNITS


def writeToCsv(json_file, outFileName):
    """
    Writes the calculation to a csv file, calls the analytics method internally.
    :param outFileName: output file name
    :param json_file: json file(readings)
    :return: True if file is created
    """
    with open(outFileName, 'w') as f:
        columns = ['Date', 'Usage(kL)']
        csv_writer = csv.DictWriter(f, fieldnames=columns)
        csv_writer.writeheader()
        for key in analytics(json_file).keys():
            f.write("%s, %s\n" % (key, literTokLiter(analytics(json_file)[key])))
        if os.path.exists('./Output/consumption.csv'):
            return True


if __name__ == '__main__':

    with open('data/readings.json') as file:
        water_file = json.load(file)
    writeToCsv(water_file, './Output/consumption.csv')


