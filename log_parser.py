import csv
import argparse


def parse_logs(example, severity_filter):
    counts = {"INFO":0, "ERROR":0, "WARNING":0, "DEBUG":0}
    with open(example, 'r') as f:
        lines =  f.readlines()
        for line in lines:
            cleaned = line.strip().split(" ", 2) #cleans data of date+time
            if len(cleaned) < 3:
                continue 
            line = cleaned [2]
            line_upper = line.upper() #not all logs have capitalised severities 
            if severity_filter != "ALL" and not line_upper.startswith(severity_filter):
                continue
            if line_upper.startswith("INFO"):
                counts["INFO"] += 1
            elif line_upper.startswith("ERROR"):
                counts["ERROR"] += 1
            elif line_upper.startswith("WARNING"):
                counts["WARNING"] += 1
            elif line_upper.startswith("DEBUG"):
                counts["DEBUG"] += 1
            else:
                raise Exception("Unaccounted log output")
    
    if severity_filter != "ALL":
        counts = {severity_filter: counts[severity_filter]}
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
    parser.add_argument("--filter", choices=["ERROR", "WARNING", "INFO", "DEBUG"], 
                        default="ALL", help="Filter by log severity")
    args = parser.parse_args()

    counts = parse_logs(args.input_file, args.filter)
    print("Results:", counts)
    save_counts(counts, args.output_file)
    print(f"results saved to {args.output_file}")

#to run in terminal follow format -> python project.py file.log file.csv --filter SEVERITY
