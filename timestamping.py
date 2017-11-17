import time
import numpy as np

def main():
    name = input("Experiment Name: ")
    data = []
    while True:
        obs = input("Observation: ").replace(","," ")
        current_time = time.time()
        data.append([current_time,obs])
        if (obs.upper() == "EXIT"):
            break
    again = input("New Experiment? (y/n):")
    if again.upper() == "Y":
        main()
    np.savetxt("%s.csv"%name,data,fmt="%s", delimiter=",")

if __name__ == "__main__":
    main()