import json
def log_analyzer(filename): 
    
    data = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
    }

    with open(filename,"r") as file:
        file_data=file.readlines()
        for log_line in file_data:
            if "error" in log_line.lower():
                data['ERROR'] += 1
            elif "warning" in log_line.lower():
                data['WARNING'] += 1
            elif "info" in log_line.lower():
                 data['INFO'] += 1
    return data

def save_to_file(data, output_file):
    try:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        return True 
    except:
        print("Error Occured while writting data to file")
        return False


if __name__ == "__main__":
    data = log_analyzer("app.log")
    print(data)
    save_to_file(data,"log_summary.json")