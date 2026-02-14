IT User Onboarding & Offboarding Automation (Python)

🎯 Project Goal:
Simulate enterprise IT workflows for provisioning, managing, and deactivating user accounts with security, role-based access control (RBAC), and audit logging. This project mirrors real-world identity lifecycle management in organizations.

🚀 Features

User Onboarding & Offboarding

Create new employee accounts with secure, auto-generated passwords

Assign roles and permissions from roles.json

Disable accounts during offboarding

Role-Based Access Control (RBAC)

Define roles and permissions in roles.json

Automatic permission assignment

Security & Compliance

Passwords hashed with SHA-256

Enforce security policies

Audit logging in audit.log for compliance

Simulation of Enterprise IT Systems

Component	Real-World Equivalent
users.json	Active Directory / Okta / Google Workspace
roles.json	RBAC policy definitions
audit.log	SIEM / Compliance logging
Password generator	Security policy enforcement
Role assignment	IAM group provisioning
Offboarding function	Access revocation & deprovisioning
📁 Project Structure
it-automation/
│
├── main.py           # Menu-driven CLI for onboarding/offboarding
├── onboarding.py     # Handles user onboarding
├── offboarding.py    # Handles user offboarding
├── security.py       # Password generator, hashing, logging
├── users.json        # Simulated directory of employees
├── roles.json        # Role definitions and permissions
├── audit.log         # Logs all actions for audit/compliance
└── README.md         # Project documentation

🧩 How It Works

Onboarding a user

User provides name and role

System validates role from roles.json

Generates secure password and hashes it

Stores account in users.json

Logs action in audit.log

Offboarding a user

User provides name

Account status changed to disabled

Logs action in audit.log

💡 Enhancements You Can Add

Role validation & automatic group permission assignment

Account expiration & MFA enforcement

Export audit logs in CSV format

Unit testing with pytest

Dockerize the app for reproducibility

Cloud IAM simulation (mock AWS IAM / Terraform)

AI-powered features: role classification, anomaly detection, log summarization

🖥 How to Run

Clone the repository:

git clone https://github.com/yourusername/it-automation.git
cd it-automation


Run the main script:

python main.py


Follow the menu to onboard/offboard users. Temporary passwords will be displayed for new accounts.
