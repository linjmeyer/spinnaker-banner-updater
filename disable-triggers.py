import gate
import config

pipeline_response = gate.gate_request("/pipelineConfigs")
pipeline_response.raise_for_status()
pipelines = pipeline_response.json()

pipelines_filtered = []

for pipeline in pipelines:
    if not config.filter or config.filter in pipeline["application"]:
        pipelines_filtered.append(pipeline)
        print("Considering pipeline " + pipeline["name"] + " in application " + pipeline['application'])


print("Updating triggers.....")

for pipeline in pipelines_filtered:
    if ('triggers' in pipeline):
        for trigger in pipeline['triggers']:
            trigger['enabled'] = False
            print("Disabled trigger " + trigger['type'] + " for " + pipeline['name'] + " in application " + pipeline['application'])
            gate.update_pipeline(pipeline)
