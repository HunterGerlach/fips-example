# FIPS Non-Compliant Server

To run this server on OpenShift, simply follow the instructions below:

- Create a new project in OpenShift
- Go to the Developer Perspective
- Click on the project you just created
- Click on the "Add" button
- Click on "Import from Git"
- Enter the Git Repository URL: <https://github.com/HunterGerlach/fips-example>
- Click "Show Advanced Git Options"
- Enter the Context Dir: server_fips-non-compliant
- Create a new application by clicking "Application" -> "Create Application"
- Specify a name for the application: fips-client-server-example
- Specify a name for the service: fips-non-compliant-server
- Specify a target port: 8443
- Click "Show Advanced Routing, Build, Deployment Options"
- Specify TLS termination type: Passthrough
- Click "Create"

If the browser/client you're using to connect does not have a matching cipher suite listed in `app.py`, you may need to select a different cipher suite that is available on your system but incompatible with FIPS. To find out which cipher suites your client supports, you can use the following command:

```bash
openssl ciphers -s -tls1_2 'ALL:eNULL'
```
