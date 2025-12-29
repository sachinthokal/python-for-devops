import json
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

    
    def save_to_file(self,result,output_file):
        try:
            with open(output_file, "w") as f:
                json.dump(result, f, indent=4)
            return True 
        except:
            print("Error Occured while writting data to file")
            return False

def main():
    """
    Main Function as a single entrypoint to the program
    """
    analyzer = LogLookUp("app.log") # Object of the class
    lines = analyzer.read_file() # Class method call --> Logs read from file

    if not lines:
        print("No logs to analyze.")

    result = analyzer.log_lookup(lines) # Class method call --> Logs analysis function
    
    print("Log Analysis Summary:\n")
    for level, count in result.items():
        print(f"{level}: {count}")

    response = analyzer.save_to_file(result,"output.json")

    if response == True:
        print("\nResult stored successfully in file !! \n")
    else:
        print("Result not stored")


if __name__ == "__main__":
    main()

