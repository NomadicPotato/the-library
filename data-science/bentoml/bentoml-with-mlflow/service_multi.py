import bentoml
import numpy as np
import numpy.typing as npt
from bentoml.models import BentoModel

from common import MyInputParams, my_image
# Demo that shows running multiple parallel models or endpoints. Useful for ensamble models

@bentoml.service(
    image=my_image,
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)
class IrisClassifier:
    # had to modify because example called for versions I did not create at the time
    bento_model_1 = BentoModel("iris:latest") 
    bento_model_2 = BentoModel("iris:latest")

    def __init__(self):
        self.model_1 = bentoml.mlflow.load_model(self.bento_model_1)
        self.model_2 = bentoml.mlflow.load_model(self.bento_model_2)

    @bentoml.api(route="/v1/predict", input_spec=MyInputParams)
    def predict_1(
        self,
        input_data,
        client_id,
    ) -> np.ndarray:
        rv = self.model_1.predict(input_data)
        return np.asarray(rv)

    @bentoml.api(route="/v2/predict", input_spec=MyInputParams)
    def predict_2(
        self,
        input_data,
        client_id,
    ) -> np.ndarray:
        rv = self.model_2.predict(input_data)
        return np.asarray(rv)
    
    # Combine predictions
    @bentoml.api(input_spec=MyInputParams)
    def predict_combined(
        self,
        input_data,
        client_id,
    ) -> np.ndarray:
        rv_a = self.model_1.predict(input_data)
        rv_b = self.model_2.predict(input_data)
        return np.asarray([rv_a, rv_b])