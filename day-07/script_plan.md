# Thinking Before Coding (DevOps Mindset)

## Example

```bash
import psutil


def system_health_check():
    cpu_threshold = int(input("\nEnter cpu threshold in % : "))
    disk_threshold = int(input("Enter disk threshold in % : "))
    memory_threshold = int(input("Enter memory threshold in % : "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage('/').percent
    current_memory = psutil.virtual_memory().percent

    print("\nSystem Health Check Report:")
    print("----------------------------")

    if current_cpu > cpu_threshold:
        print(f"CPU usage is above threshold: {current_cpu}%")
    else:
        print(f"CPU usage is within threshold: {current_cpu}%")

    if current_disk > disk_threshold:
        print(f"Disk usage is above threshold: {current_disk}%")
    else:
        print(f"Disk usage is within threshold: {current_disk}%")

    if current_memory > memory_threshold:
        print(f"Memory usage is above threshold: {current_memory}%")
    else:
        print(f"Memory usage is within threshold: {current_memory}%")
    
    print("-----------------------------\n")


system_health_check()

```

#### KEY POINTS :

  - What is the problem?

    ```
    User want to know the system health and he want to get alert once system cross threshold whatever he set.
    ```
  - What input does it need?
    
    ```
    User threshold value.
    ```
  - What output should it give?
    ```
    Script give system health & action once threshold over.
    ```
  - What steps are involved?

    ```
    - User will give threshold value as a input.
    - Script will take user threshold and compare with system health and perform action as a result.
    - Once action done user will get output as a script result.
    ```


