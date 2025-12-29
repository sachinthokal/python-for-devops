import json
import argparse

class LogLookUp:

    def __init__(self, filename):

        self.filename = filename
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "UNKNOWN": 0}

    def read_file(self):
        with open(self.filename,"r") as f:
            return f.readlines()
        
    def log_lookup(self, lines):
        """
        Analyzer to count the error patterns & Counts
        """
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
            else:
                self.counts["UNKNOWN"] += 1

        return self.counts
    

    def log_level_filter(self,level):
        data = []
        file_log = self.read_file() 
        for line in file_log:
            if level in line :
                data.append(line)
        
        return data



    def save_to_file(self,result,output_file):
        try:
            if output_file == None:
                output_file = "output.json"
            with open(output_file, "w+") as f:
                json.dump(result, f, indent=4)
            return True 
        except:
            print("Error Occured while writting data to file")
            return False

def main():
    """
    Main Function as a single entrypoint to the program
    """
    # create object of argparse
    parser = argparse.ArgumentParser(description="User info script") # take CLI inputs by --flags

    # define flags 
    parser.add_argument("--file", required=True, help="Logs file name to read logs")
    parser.add_argument("--out",  help="Result output file name")
    parser.add_argument("--level", help="Result output file name")

    args = parser.parse_args()

    # print(f"File : {args.file}")
    # print(f"Output : {args.out}")
    # print(f"level : {args.level}")

    analyzer = LogLookUp(args.file) # Object of the class
    lines = analyzer.read_file() # Class method call --> Logs read from file

    if not lines:
        print("No logs to analyze.")

    result = analyzer.log_lookup(lines) # Class method call --> Logs analysis function
    
    print("\nLog Analysis Summary:\n")
    for level, count in result.items():
        print(f"{level}: {count}")

    if args.level:
        level_filtered_data = analyzer.log_level_filter(args.level)    
        print(f"\nFilltered logs by {args.level} : {level_filtered_data}\n")
        final_result = result,level_filtered_data
        analyzer.save_to_file(final_result,args.out)


if __name__ == "__main__":
    main()