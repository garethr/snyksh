# Snyk Shell

Snyk Shell provides a convenient shell interface to the Snyk API. You can
use any valid Python expression as well as make calls to the Snyk API using
the pre-configured Snyk API client. When you load the the shell it will
pre-load a list of your organizations and projects so you have some data to explore.

## Installation

Snyk Shell is available from PyPi. Use your prefered Python dependency management tool to install:

```
pip install snyksh
```

Snyk Shell is also available as a Docker image.

```
docker pull garethr/snyksh
```

## Configuration

In order to access the Snyk API you need to provide your API token. This is done using
an environment variable called `SNYK_TOKEN`:

```
export SNYK_TOKEN=<your-token-goes-here>
snyksh
```

```
docker run --rm -it -e SNYK_TOKEN=<your-token> garethr/snyksh
```

## Usage

With Snyk Shell running you can interact with data in Snyk. This includes your projects as
well as vulnerability data more generally.

Here's a few examples.

```ipython
Welcome to Snyk Shell

The following objects and methods are currently available:
  client - An instance of the Snyk client, which can be used to make requests to the API
  organizations - A prepopulated list of the Snyk organizations you are a member of
  projects - A prepopulated list of all of your Snyk projects
  pprint() - A pretty printer for objects returns by the API


In [1]: organizations
Out[1]: [Organization(name='garethr', id='<not-the-read-organization-id>', group=None)]

In [2]: pprint(organizations)
[
    snyk.models.Organization(
        name='garethr',
        id='<not-the-real-organization-id>'
    )
]

In [3]: results = client.organizations.first().test_python("django", "2.0.0")

In [4]: len(results.issues.vulnerabilities)
Out[4]: 6

In [5]: [x.identifiers["CVE"][0] for x in results.issues.vulnerabilities]
Out[5]:
['CVE-2019-6975',
 'CVE-2018-7536',
 'CVE-2018-7537',
 'CVE-2018-6188',
 'CVE-2018-14574',
 'CVE-2019-3498']
```

## The Snyk API client

Snyk Shell uses the Snyk Python API client `pysnyk`. If you want to build your own applications
which interact with the Snyk API, or you want to know all of the properties and methods avaiable
to you, see the client documentation and examples.


