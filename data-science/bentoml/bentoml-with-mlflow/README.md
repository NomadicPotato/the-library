# BentoML
## General
SO it is pretty nice tool. The ability to combine it with mlflow is really convenient to pull models and will work well with the proposed workflow I had in mind for the team.
> Some of the guidance had to be updated since at this time many of the packages got new releases that broke some previous functionality.

The guide I am following is here:[Building ML Pipelines With MLFlow and BentoML](https://www.bentoml.com/blog/building-ml-pipelines-with-mlflow-and-bentoml)

## Getting started
In order to run this example I had to do the following commands:
* Create conda environment from the yaml file, or pip install the packages inside the yaml
* Start and MLFlow server: `$ mlflow server --host 127.0.0.1 --port 8080`
* This will start a mlflow server locally and any runs created will be stored into the mlruns folder and mlartifacts folder
* alternatively store data in a sqlite db by first `$ export MLFLOW_TRACKING_URI=sqlite:///mlruns.db`
and then run `$ mlflow ui --port 8080 --backend-store-uri sqlite:///mlruns.db`
* Artifacts will still be stored seperately
* Run the notebook to get first model in bentoml
* run the command `$ bentoml serve service.py:IrisClassifier` to test locally
* Run the command below to test locally
```
$ curl -X 'POST' \
  'http://localhost:3000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input_data": [[
    0.1, 0.2, 0.1, 0.1
  ]]
}'
```
* run `bentoml build` (Unfortunately this will only work with `service.py` in `./`, or a `bentofile.yml`, but this approach is deprecated)

