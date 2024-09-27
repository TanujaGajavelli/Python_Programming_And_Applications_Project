from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    try:
        file=open(fileName,'r')
        try:
            patients_list=file.readlines()
            patient_detail = []
            for i in range(0,len(patients_list)):
                line= patients_list[i].strip().split(',')
                #if fields are not 8
                if len(line)!=8:
                    print(f"Invalid number of fields {len(line)} in line:{i+1}")
                try:
                    patientId=int(line[0])
                    date=line[1]         # date
                    temp=float(line[2])  # temperature
                    hr=int(line[3])      # heart rate
                    rr=int(line[4])      # respiratory rate
                    sbp=int(line[5])     # systolic blood pressure
                    dbp=int(line[6])     # diastolic blood pressure
                    spo2=int(line[7])    # oxygen saturation value

                    patient_detail=[date,temp,hr,rr,sbp,dbp,spo2]
                    # if temperature not in range of 35 to 42
                    if temp<35 or temp>42:
                        print(f"Invalid temperature value {temp} in line:{i+1}")
                    # if heart rate is not in range of 30 to 180
                    elif hr<30 or hr>180:
                        print(f"Invalid heart rate value {hr} in line: {i+1}")
                    # if respiratory rate is not in range 5 to 40
                    elif rr<5 or rr>40:
                        print(f"Invalid respiratory rate value {rr} in line: {i+1}")
                    # if the systolic blood pressure is not in range 70 to 200
                    elif sbp<70 or sbp>200:
                        print(f"Invalid systolic blood pressure value {sbp} in line:{i+1}")
                    # if the diastolic blood pressure is not in range 40 to 120
                    elif dbp<40 or dbp>120:
                        print(f"Invalid diastolic blood pressure value {dbp} in line:{i + 1}")
                    # if the oxygen saturation is not in range 70 to 100
                    elif spo2<70 or spo2>100:
                        print(f"Invalid oxygen saturation value {spo2} in line:{i+1}")
                    else:
                        if patientId in patients:
                            patients[patientId].append(patient_detail)
                        else:
                             patients[patientId]=[patient_detail]
                except ValueError:
                    print(f"Invalid data type in line:{i + 1}")
        #if file not read
        except:
            print("An unexpected error occurred while reading the file")
    except FileNotFoundError:
        print(f"The file {fileName} could not be found")
    file.close()
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    if patientId == 0:
        #to display data for all patients
        for id in patients:
            print(f"patientId: {id}")
            for visit in patients[id]:
                print(f"    Visit Date: {visit[0]}")
                print(f"     Temperature: {visit[1]} C")
                print(f"     Heart Rate: {visit[2]} bpm")
                print(f"     Respiratory Rate: {visit[3]} bpm")
                print(f"     Systolic Blood Pressure: {visit[4]} mmHg")
                print(f"     Diastolic Blood Pressure: {visit[5]} mmHg")
                print(f"     Oxygen Saturation: {visit[6]} %\n")
    elif patientId in patients:
        print(f"patientId: {patientId}")
        for visit in patients[patientId]:
            print(f"    Visit Date: {visit[0]}")
            print(f"     Temperature: {visit[1]} C")
            print(f"     Heart Rate: {visit[2]} bpm")
            print(f"     Respiratory Rate: {visit[3]} bpm")
            print(f"     Systolic Blood Pressure: {visit[4]} mmHg")
            print(f"     Diastolic Blood Pressure: {visit[5]} mmHg")
            print(f"     Oxygen Saturation: {visit[6]} %\n")
    # if patientId is not found
    else:
        print(f"Patient with Id {patientId} is not found")
def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    if type(patients)==dict:   #to check if patients is dictionary or not
        try:
            patientId1=int(patientId)
            if patientId1==0:
                total_temp,total_hr,total_rr,total_sbp,total_dbp,total_spo2=0,0,0,0,0,0
                count=0   #to count all visits for all the patients
                for id in patients:
                    for visit in patients[id]:
                        total_temp+=visit[1]
                        total_hr+=visit[2]
                        total_rr+=visit[3]
                        total_sbp+=visit[4]
                        total_dbp+=visit[5]
                        total_spo2+=visit[6]
                        count+=1
                print("Vital Signs for All Patients:")
                print(f"    Average Temperature: {total_temp/count :.2f} C")
                print(f"    Average heart rate: {total_hr/count :.2f} bpm")
                print(f"    Average respiratory rate: {total_rr/count :.2f} bpm")
                print(f"    Average systolic blood pressure: {total_sbp/count :.2f} mmHg")
                print(f"    Average diastolic blood pressure: {total_dbp/count :.2f} mmHg")
                print(f"    Average oxygen saturation: {total_spo2/count :.2f} %\n")
            elif patientId1 in patients:
                total_temp,total_hr,total_rr,total_sbp,total_dbp,total_spo2=0,0,0,0,0,0
                count=0   #to count all visits for the patient
                for visit in patients[int(patientId1)]:
                    total_temp+=visit[1]
                    total_hr+=visit[2]
                    total_rr+=visit[3]
                    total_sbp+=visit[4]
                    total_dbp+=visit[5]
                    total_spo2+=visit[6]
                    count+=1
                print(f"Vital Signs for Patient {patientId1}:")
                print(f"    Average Temperature: {total_temp/count :.2f} C")
                print(f"    Average heart rate: {total_hr/count :.2f} bpm")
                print(f"    Average respiratory rate: {total_rr/count :.2f} bpm")
                print(f"    Average systolic blood pressure: {total_sbp/count :.2f} mmHg")
                print(f"    Average diastolic blood pressure: {total_dbp/count :.2f} mmHg")
                print(f"    Average oxygen saturation: {total_spo2/count :.2f} %\n")
            else:    #if there is no patient with the given id
                print(f"No data found for patient with Id: {patientId1}")
        except ValueError:  #if patientId is not an integer
            print("Error: 'patientId' should be an integer.")
    else:       #if patients is not a dictionary
        print("Error: 'patients' should be a dictionary")

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    file=open(fileName,'a')
    try:
        yyyy,mm,dd=date.split('-')
        year=int(yyyy)
        month=int(mm)
        day=int(dd)
        #to check for valid date
        if (day<1 or day>31) or (month<1 or month>12) or year<1900:
            print("Invalid date. Please enter a valid date.")
        #to check temperature
        elif temp<35.0 or temp>42.0:
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius")
        #to check heart rate
        elif hr<30 or hr>180:
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm")
        #to check respiratory rate
        elif rr<5 or rr>40:
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm")
        #to check systolic blood pressure
        elif sbp<70 or sbp>200:
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg")
        #to check diastolic blood pressure
        elif dbp<40 or dbp>120:
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg")
        #to check oxygen saturation
        elif spo2<70 or spo2>100:
            print("Invalid oxygen saturation.Please enter an oxygen saturation between 70 and 100%")
        else:
            #adding the data
            try:
                patient_detail=[date,temp,hr,rr,sbp,dbp,spo2]
                patient=str(patientId)+','+','.join(str(patient_detail[i]) for i in range(0,7))
                file.write('\n'+patient)
                print(f"Visit saved for patient # {patientId}")
                if patientId in patients:
                    patients[patientId].append(patient_detail)
                else:
                    patients[patientId] = [patient_detail]
                file.close()
            except:
                print("An unexpected error occurred while adding new data")
    except:
        print("Invalid date format. Please enter date in the format ‘yyyy-mm-dd’")
def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    if year==None:
        year=0
    if month==None:
        month=0
    if patients!={}:     #to check if patients is empty or not
        if year>=0 and 0<=month<=12:   #to check for valid year and month
            if year==0 and month==0:   #to get all visits
                for patientId in patients:
                    for visit in patients[patientId]:
                        visits.append((patientId, visit))
            elif year!=0 and month==0:  #to get all visits done in the year
                for patientId in patients:
                    for visit in patients[patientId]:
                        date = visit[0]  # visit date of patient
                        yyyy, mm, dd = date.split('-')
                        visit_year = int(yyyy)
                        if visit_year == year:
                            visits.append((patientId, visit))
            # to get all the visits in the year and month
            else:
                for patientId in patients:
                    for visit in patients[patientId]:
                        date=visit[0]   #visit date of patient
                        yyyy,mm,dd=date.split('-')
                        visit_year=int(yyyy)
                        visit_month=int(mm)
                        if visit_year==year and visit_month==month:
                            visits.append((patientId,visit))
    #if patients is empty or date is invalid it returns an empty list
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    for patientId in patients:
        for visit in patients[patientId]:
            hr = visit[2]   # heart rate
            sbp = visit[4]  # systolic blood pressure
            dbp = visit[5]  # diastolic blood pressure
            spo2 = visit[6] # oxygen saturation value
            #to check for abnormal vital signs
            if hr> 100 or hr< 60 or sbp> 140 or dbp> 90 or spo2< 90:
                followup_patients.append(patientId)
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    file=open(filename,"w")
    if patientId in patients:
        for id in patients:
            #while id is not equal to patientId the data is added in the file
            if id!=patientId:
                for visit in patients[id]:
                    #string to add in the text file
                    patient_detail=str(id)+','+','.join(str(visit[i]) for i in range(0,7))+'\n'
                    file.write(patient_detail)
        #the visit details of the required patient is deleted from dictionary
        patients.pop(patientId)
        print(f"Data for patient {patientId} has been deleted")
    #if patientId is not in text file
    else:
        print(f"No data found for patient with ID {patientId}")
    file.close()



###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()