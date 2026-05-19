from scipy.io import loadmat
import pandas as pd
import numpy as np

'''

NOTE : This function converts our mat file from simulink to the
proper format of DataFrame required for the use of this project.

Points to be remembered is that :
- Frequency of supply is taken to be 50 Hz
- Sampling time is taken to be 50 micro second
- Due to this for RMS calculation, window = 400

'''

def convert_mat_to_dataframe(file_name):
    data = loadmat(file_name)

    Vabc = data["Vabc"]
    Iabc = data["Iabc"]
    t = data["t"]

    df = pd.DataFrame()
    df["Time"] = pd.DataFrame(t)
    df[["Va","Vb","Vc"]] = pd.DataFrame(Vabc)
    df[["Ia","Ib","Ic"]] = pd.DataFrame(Iabc)

    df["In"] = df["Ia"] + df["Ib"] + df["Ic"]

    phases = ["Va","Vb","Vc","Ia","Ib","Ic"]

    for phase in phases:
        df[f"{phase}_rms"] = np.sqrt((df[phase]**2).rolling(window = 400,
                                    center = True).mean())
    df["In_rms"] = np.sqrt((df["In"]**2).rolling(window = 400,
                                    center = True).mean())
    df = df.bfill().ffill()

    return df



