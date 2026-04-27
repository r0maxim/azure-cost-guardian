# Azure Cost Guardian
*Automated Infrastructure Governance for Azure*

## The Business Problem
In cloud management, orphaned resources (unattached disks/IPs) are a silent budget killer. This script provides real-time auditing to identify waste that Azure Advisor might miss due to latency.

## Features
- **Disk Audit:** Finds Managed Disks not attached to any VM.
- **Network Audit:** Finds Public IPs not associated with any interface.
- **Secure Auth:** Uses `DefaultAzureCredential` for professional-grade security.
