# Azure Diag Tool
This docker image is used to diagnose customer's Azure metrics. It currently fetches the list of resource managements available for this particular credentials.

## Build
Run the below to build the image
```
docker build -t <repo/name:tag> .
```
## Run
Run the below command after replacing <xxxxx> with the actual value
```
docker run -it --env AZURE_CLIENT_ID=<client_ID or app_ID> --env AZURE_SUBSCRIPTION_ID=<sub_ID> --env AZURE_CLIENT_SECRET=<secret> --env AZURE_TENANT_ID=<tenant_id> <repo/name:tag>
```
