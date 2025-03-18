import re
import os

log_pattern = r"Failed password for invalid user (\S+) from (\S+)"

def analyze_logs(log_file):

    """
    Function to analyze logs for suspicious activities such as failed login attempts.

    """

    suspicious_activity = []

    if not os.path.exists(log_file):
        print("Log file does not exist.")
        return []

    with open(log_file, 'r') as file:
        logs = file.readlines()

    for line in logs:
        match = re.search(log_pattern, line)
        if match:
            user = match.group(1)
            ip = match.group(2)
            suspicious_activity.append(f"Suspicious login attempt: User '{user}' from IP {ip}")
    
    return suspicious_activity

# Example usage
if __name__ == "__main__":
    suspicious_activities = analyze_logs("/var/log/auth.log")  # Update path to a real log file
    for activity in suspicious_activities:
        print(activity)
