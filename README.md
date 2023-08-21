# fips-example

This repository contains examples highlighting the differences between FIPS and non-FIPS enabled containers.

Both applications are exactly the same (simple Python Flask applications), except for the inclusion of the FIPS non-compliant `md5` package in the fips-non-compliant application.

## Deployment

To run the applications simply navigate to any FIPS enabled OpenShift cluster and switch to the Developer perspective. From there, click on the `+Add` button and select `Git Repository` from the list of options. Enter the following URL into the `Git Repo URL`. Next specify the context directory as `fips-non-compliant` or `fips-compliant` depending on which application you would like to deploy. Finally, click on the `Create` button to deploy the application.

Compare the applications side by side to see the differences between FIPS and non-FIPS enabled containers.
