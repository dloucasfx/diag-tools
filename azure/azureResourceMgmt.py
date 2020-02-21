import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient


def print_item(group):
    """Print a ResourceGroup instance."""
    print("\tName: {}".format(group.name))
    print("\tId: {}".format(group.id))
    print("\tLocation: {}".format(group.location))
    print("\tTags: {}".format(group.tags))
    print_properties(group.properties)


def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n\n")


def get_env(name):
    if name in os.environ:
        return os.environ[name]
    print("Environment variable {} is not set, make sure to set it first".format(name))
    exit()


if __name__ == "__main__":
    subscription_id = get_env('AZURE_SUBSCRIPTION_ID')

    credentials = ServicePrincipalCredentials(
        client_id=get_env('AZURE_CLIENT_ID'),
        secret=get_env('AZURE_CLIENT_SECRET'),
        tenant=get_env('AZURE_TENANT_ID')
    )

    client = ResourceManagementClient(credentials, subscription_id)
    for item in client.resource_groups.list():
        print_item(item)
