# Currency-Conversion-Webservice

This project consists of the development of a webservice that provides an endpoint for the conversion between different currencies.

La versión de python usada en este proyecto es `Python 3.7`.


## How to run services

In order to launch the project we must first create a `settings-variables.env` file that contains the environment variables that the webservice needs to work. This file must be located in the `root folder` of the project. The necessary variables are the following:

* `OER_APP_ID`: OpenExchangeRates App Id.
* `REDIS_HOST`: Host where the redis service is running.
* `REDIS_PORT`: Port where the redis service is running.
* `SERVER_PORT`(not required): This is the port where the webservice will run. note that if you change this variable you will have to open the webservice service port in the `docker-compose.yml` file.

An example of this file that works with the docker-compose would be the following:

```
SERVER_PORT=8080
REDIS_HOST=redis
REDIS_PORT=6379
OER_APP_ID=<OpenExchangeRates_App_Id>
```

Once we have the configuration variables we can launch the services described in the file `docker-compose.yml` launching in the terminal the following command from the root folder of the project:

```
$ docker-compose up
```

We will now be able to access the Swagger documentation page located at the following address:
```
http://<host>:<port>/api/doc
```

We'll find something like this:

![alt text](assets/swagger_screen_shoot.png "Swagger documentation page")


## How to run tests

If we want to launch the unittests we must install the dependencies file `requeriments_dev.txt` launching in the console the following command from proyect root folder (it is recommended to use a virtual environment):

```
$ pip install -r requeriments/requeriments_dev.txt
```

Once installed the necessary libraries, from the same folder we launch the tests with the following command:

```
$ pytest
```

Obtaining a result similar to the following:

![alt text](assets/unittest_result_screenshoot.png "Unnitests result")
