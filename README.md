# fips-example

## Deployment

From within the root of this repository, run the following commands to deploy the application to OpenShift:

```bash
oc new-project fips-example
oc new-app --name=fips-example .
oc expose svc/fips-example
```
