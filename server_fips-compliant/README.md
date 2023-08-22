# FIPS-Compliant Server

To run this server on OpenShift, simply follow the instructions below:

- Create a new project in OpenShift
- Go to the Developer Perspective
- Click on the project you just created
- Click on the "Add" button
- Click on "Import from Git"
- Enter the Git Repository URL: <https://github.com/HunterGerlach/fips-example>
- Click "Show Advanced Git Options"
- Enter the Context Dir: server_fips-compliant
- Create a new application by clicking "Application" -> "Create Application"
- Specify a name for the application: fips-client-server-example
- Specify a name for the service: fips-compliant-server
- Specify a target port: 8443
- Click "Show Advanced Routing, Build, Deployment Options"
- Specify TLS termination type: Passthrough
- Click "Create"
