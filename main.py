import numpy as np
import pandas as pd



def load_and_preview(file_path):
    df = pd.read_csv(file_path)


    return df


def preprocess(df):
    print("Before cleaning:", df.shape)
    df = df.dropna()  # For Missing Values
    df["Velocity_VDY"] = pd.to_numeric(df["Velocity_VDY"], errors='coerce') # For wrong data type
    df["Acceleration"] = pd.to_numeric(df["Acceleration"], errors='coerce')
    df = df.sort_values("MTS_TIME")
    print("After cleaning:", df.shape)

    return df
def add_features(df):
    df["Velocity_Change"] = df["Velocity_VDY"].diff().fillna(0)
    df["Acceleration_Change"] = df["Acceleration"].diff().fillna(0)

    return df

def detect_faults(df):
    faults = []

    # ---------- HIGH SPEED ----------
    in_fault = False
    start_time = None

    for i in range(len(df)):
        velocity = df["Velocity_VDY"].iloc[i]
        time = df["MTS_TIME"].iloc[i]

        if velocity > 120 and not in_fault:
            in_fault = True
            start_time = time

        elif velocity <= 120 and in_fault:
            end_time = df["MTS_TIME"].iloc[i - 1]
            faults.append(("High Speed", start_time, end_time))
            in_fault = False

    if in_fault:
        faults.append(("High Speed", start_time, df["MTS_TIME"].iloc[-1]))


    # ---------- ACCELERATION SPIKE ----------
    in_fault = False
    start_time = None

    for i in range(len(df)):
        acc_change = df["Acceleration_Change"].iloc[i]
        time = df["MTS_TIME"].iloc[i]

        if acc_change > 2 and not in_fault:
            in_fault = True
            start_time = time

        elif acc_change <= 2 and in_fault:
            end_time = df["MTS_TIME"].iloc[i - 1]
            faults.append(("Acceleration Spike", start_time, end_time))
            in_fault = False

    if in_fault:
        faults.append(("Acceleration Spike", start_time, df["MTS_TIME"].iloc[-1]))


    # ---------- SUDDEN SPEED DROP ----------
    in_fault = False
    start_time = None

    for i in range(len(df)):
        vel_change = df["Velocity_Change"].iloc[i]
        time = df["MTS_TIME"].iloc[i]

        if vel_change < -50 and not in_fault:
            in_fault = True
            start_time = time

        elif vel_change >= -50 and in_fault:
            end_time = df["MTS_TIME"].iloc[i - 1]
            faults.append(("Sudden Speed Drop", start_time, end_time))
            in_fault = False

    if in_fault:
        faults.append(("Sudden Speed Drop", start_time, df["MTS_TIME"].iloc[-1]))

    return faults

def save_output(faults):
    output_df = pd.DataFrame(faults, columns=["FaultName", "StartTime", "EndTime"])
    output_df.to_excel("output.xlsx", index=False)


df = load_and_preview("C:\\Users\\tanvi\\Downloads\\sensor_data_500\\sensor_data_500.csv")
df = preprocess(df)
df = add_features(df)
faults = detect_faults(df)


df.to_csv("processed_data.csv", index=False)

save_output(faults)

#print(df.head())