from azure.mgmt.resource import ResourceManagementClient
import sys
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

# 1. Authentication
subscription_id = "Your-Subscription-ID"
creds = DefaultAzureCredential()

# 2. These are your the tools in Azure
compute_client = ComputeManagementClient(creds, subscription_id)
network_client = NetworkManagementClient(creds, subscription_id)
resource_client = ResourceManagementClient(creds, subscription_id)


def find_orphaned_disks():
    print("--- Searching for Unattached Disks ---")
    # Gets all disks in the subscription
    for disk in compute_client.disks.list():
        if disk.managed_by is None:
            print(
                f"ORPHAN FOUND: {disk.name} in {disk.location}")


def find_orphaned_ips():
    print("\n--- Searching for Unattached Public IPs ---")
    for rg in resource_client.resource_groups.list():
        ips = network_client.public_ip_addresses.list(rg.name)
        for ip in ips:
            # If the IP isn't linked to a Network Interface, it's an orphan
            if ip.ip_configuration is None:
                print(
                    f"ORPHAN FOUND: {ip.name} in {rg.name} - {ip.ip_address}")


# 3. EXECUTION
if __name__ == "__main__":
    find_orphaned_disks()
    find_orphaned_ips()
