import csv
import argparse


def parse_logs(example):
    counts = {"INFO":0, "ERROR":0, "WARNING":0}
    with open(example, 'r') as f:
        lines =  f.readlines()
        for line in lines:
            cleaned = line.strip().split(" ", 2) #cleans data of date+time
            line = cleaned [2]
            if line.startswith("INFO"):
                counts["INFO"] += 1
            elif line.startswith("ERROR"):
                counts["ERROR"] += 1
            elif line.startswith("WARNING"):
                counts["WARNING"] += 1
            else:
                raise Exception("Unaccounted log output")
    return counts

def save_counts(counts, results):
    with open(results, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Count"])
        for k,v in counts.items():
            writer.writerow([k,v])

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument('output_file')
    args = parser.parse_args()

    counts = parse_logs(args.input_file)
    print("Results:", counts)
    save_counts(counts, args.output_file)
    print("results saved to {args.output_file}")

#to run in terminal follow format -> python project.py file.log file.csv
