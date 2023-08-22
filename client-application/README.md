# Client Application to Test Server FIPS Compliance

To run this server on OpenShift, simply follow the instructions below:

- Create a new project in OpenShift
- Go to the Developer Perspective
- Click on the project you just created
- Click on the "Add" button
- Click on "Import from Git"
- Enter the Git Repository URL: <https://github.com/HunterGerlach/fips-example>
- Click "Show Advanced Git Options"
- Enter the Context Dir: client-application
- Create a new application by clicking "Application" -> "Create Application" (if necessary)
- Specify a name for the application: fips-client-server-example
- Specify a name for the service: client-application
- Specify a target port: 8443
- Click "Show Advanced Routing, Build, Deployment Options"
- Specify TLS termination type: Edge
- Click "Create"

Go to the Deployment tab and click on the "client-application" deployment. Click on the "Environment" tab and add the following environment variables:

```yaml
- name: SERVER_URL
  value: https://{SERVER_URL for either fips-compliant-server or fips-non-compliant-server}
```
