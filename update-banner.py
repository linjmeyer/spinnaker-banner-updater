import gate
import config

applications_response = gate.gate_request("/applications/")
applications_response.raise_for_status()
applications = applications_response.json()

apps_filtered = []

for app in applications:
    if not config.filter or config.filter in app["name"]:
        apps_filtered.append(app)
        print("Considering application " + app["name"])


print("Updating banners.....")

for app in apps_filtered:
    gate.update_banners(app["name"], config.banners)
    print("Created update banner task for app: " + app["name"])
