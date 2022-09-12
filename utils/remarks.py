def remarks(pm25):
    PM25=pm25
    if PM25 <= 50 :
        Remarks = "Good"
        return Remarks
    elif PM25 <=100:
        Remarks = "Satisfactory"
        return Remarks
    elif PM25 <=200:
        Remarks = "Moderate"
        return Remarks
    elif PM25 <=300:
        Remarks = "Poor"
        return Remarks
    elif PM25 <=400:
        Remarks = "Very Poor"
        return Remarks
    else:
        Remarks = "Severe"
        return Remarks