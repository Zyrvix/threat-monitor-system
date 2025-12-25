USER_ROLES = (
    ('admin', 'Admin'),
    ('analyst', 'Analyst'),
)

EVENT_TYPES = (
    ('intrusion', 'Intrusion'),
    ('malware', 'Malware'),
    ('anomaly', 'Anomaly'),
    ('bruteforce', 'Brute Force Attack'),
    ('ddos', 'DDoS Attack'),
    ('phishing', 'Phishing Attempt'),
    ('ransomware', 'Ransomware'),
    ('data_exfiltration', 'Data Exfiltration'),
    ('unauthorized_access', 'Unauthorized Access'),
    ('privilege_escalation', 'Privilege Escalation'),
    ('policy_violation', 'Policy Violation'),
    ('suspicious_login', 'Suspicious Login'),
    ('command_execution', 'Malicious Command Execution'),
    ('file_integrity', 'File Integrity Violation'),
    ('network_scan', 'Network Scanning'),
    ('bot_activity', 'Bot Activity'),
    ('configuration_change', 'Unauthorized Configuration Change'),
    ('vulnerability_detected', 'Vulnerability Detected'),
    ('login_fail', 'Login Failure'),
    ('sql_injection', 'SQL Injection Attempt'),
    ('file_mod', 'Sensitive File Modification'),
    ('system_scan', 'Vulnerability Scan'),
)

SEVERITY_LEVELS = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('critical', 'Critical'),
)

ALERT_STATUS = (
    ('open', 'Open'),
    ('acknowledged', 'Acknowledged'),
    ('resolved', 'Resolved'),
)

ACTIVITY_ACTIONS = (
    ('login', 'User Login'),
    ('logout', 'User Logout'),
    ('alert_assigned', 'Alert Assigned'),
    ('alert_resolved', 'Alert Resolved'),
    ('alert_acknowledged', 'Alert Acknowledged'),
    ('user_registered', 'User Registered'),
    ('profile_update', 'Profile Updated'),
)

ACTIVITY_MODULES = (
    ('accounts', 'Accounts & Auth'),
    ('alerts', 'Alert Management'),
    ('events', 'Event Monitoring'),
    ('system', 'System Configuration'),
)
