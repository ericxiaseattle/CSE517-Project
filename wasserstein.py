import pandas as pd
from scipy.stats import wasserstein_distance
import sys
import os

def main():
    if len(sys.argv) < 2:
        usage()
        return
    path = sys.argv[1]
    
    df = pd.read_csv(path + "/all.csv")
    all_pred = df["pred"].to_numpy()

    for f in os.listdir(path):
        if f != "all.csv":
            df = pd.read_csv(path + "/" + f)
            dec_pred = df["pred"].to_numpy()
            print(f"{f} {wasserstein_distance(all_pred, dec_pred)}") 
    

def usage():
    print(f"Usage: python {sys.argv[0]} path/to/input/directory/")

if __name__ == "__main__":
    main()