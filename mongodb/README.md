# MongoDB Connection Test
This docker image is used to test customer's connection to MongoDB using the specific version
of pymongo the smart agent uses. 

You can run the script directly, without docker, as long as you have the pymongo package installed
(example: run it in the same place where the agent is running)

## Build
Run the below to build the image
```
docker build -t <repo/name:tag> .
```
## Run
`--net host` is only needed if you mongodb is installed on the same docker host and you are trying
to access it through localhost

```
docker run -it --net host <repo/name:tag>
```
