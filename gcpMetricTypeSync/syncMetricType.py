import json
import logging
import os
import requests

from google.cloud import monitoring_v3


def enable_debug():
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

# Get metric descriptor from GCP
def list_metric_descriptors(project_id, metric_pref):
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"
    filter_val = f"metric.type = starts_with(\"{metric_pref}\")"
    return client.list_metric_descriptors(name=project_name, filter_=filter_val)


def get_sfx_metric_type(metric):
    metric = metric.replace("/", "%5C%2F")
    parameters = 'limit=10000&organizationId={orgID}&query=(((sf_key:sf_metric+AND+sf_metric:{value}))+AND+sf_organizationID:{orgID})+AND+(sf_organizationID:{orgID})'.format(
        value=metric, orgID=org)
    response = requests.get(api_url_base+"/v1/metric", headers=headers, params=parameters)
    if len(response.json()["rs"]) == 1: 
        return response.json()["rs"][0]["sf_metricType"]
    else: 
        print("0 or more than 1 entry found for metric: {}".format(metric))
        return None


def update_sfx_metric_type(data_body, update_metric):
    update_url = api_url_base+"/v2/metric/"+update_metric.replace("/", "%2F")
    if read_only:
        print("UPDATE. URL: {} BODY: {}".format(update_url, data_body))
    else:
        response = requests.put(update_url, headers=headers, json=data_body)
        if response.status_code != 200:
            prin("Error Updating. URL: {} BODY: {}".format(update_url, data_body))

if __name__ == "__main__":
    #enable_debug()
    realm = "us0"
    if "SFX_TOKEN" in os.environ:
        api_token = os.getenv('SFX_TOKEN')
    else:
        print("SFX_TOKEN env variable is missing")
        exit(1)

    if "ORG_ID" in os.environ:
        org = os.getenv('ORG_ID')
    else:
        print("ORG_ID env variable is missing")
        exit(1)

    realm = os.getenv('SFX_REALM', 'us0')
    
    read_only = (os.getenv("READ_ONLY", "true") == 'true')

    metric_prefix = 'loadbalancing.googleapis.com'
    if "METRIC_PREFIX" in os.environ:
        metric_prefix = os.getenv('METRIC_PREFIX')
    else:
        print("METRIC_PREFIX is not defined, fetching the load balancer metrics: loadbalancing.googleapis.com")

    if "PROJECT_NAME" in os.environ:
        project = os.getenv("PROJECT_NAME")
    else:
        print("A PROJECT_NAME environment variable should be defined in order to get the contact GCP")
        exit(1)

    # GCP Kind -> SFX Type
    metrictypedict = {
            "DELTA" : "COUNTER",
            "GAUGE" : "GAUGE",
            "CUMULATIVE" : "CUMULATIVE COUNTER"
            }

    api_url_base = 'https://support-server.{value}.signalfx.com'.format(value=realm)
    headers = {'Content-Type': 'application/json', 'X-SF-TOKEN': api_token}

    gcp_metrics = list_metric_descriptors(project, metric_prefix)

    for gcp_metric in gcp_metrics:
        metric_name = gcp_metric.type.replace(metric_prefix+"/", "")
        sfx_metric_type = get_sfx_metric_type(metric_name)

        if sfx_metric_type is None:
            continue
        # reverse enum
        metric_type_name = next(name for name, value in vars(monitoring_v3.enums.MetricDescriptor.MetricKind).items() if value == gcp_metric.metric_kind)
        gcp_to_sfx_type = metrictypedict[metric_type_name]
        if len(gcp_to_sfx_type) > 1 and gcp_to_sfx_type != sfx_metric_type:
            print("update ---{}--- ---{}--- metric Name {}".format(gcp_to_sfx_type, sfx_metric_type, metric_name))
            data = {'name': metric_name , 'type': gcp_to_sfx_type}
            update_sfx_metric_type(data, metric_name)
