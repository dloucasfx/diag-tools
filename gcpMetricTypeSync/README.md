# GCP sync metric type
This docker image compares and syncs the GCP metric kind to SFX metric type.

## Build
Run the below to build the image
```
docker build -t <repo/name:tag> .
```
## Run
Run the below command after replacing <xxxxx> with the actual value
```
docker run -it -v <path_to_GCP_KEY_FILE.JSON>:/keyfile.json --env SFX_TOKEN=<token_to_access_SFX_API> --env ORG_ID=<ORG_ID> --env PROJECT_NAME=<GCP_Project_Name> <repo/name:tag>
```
