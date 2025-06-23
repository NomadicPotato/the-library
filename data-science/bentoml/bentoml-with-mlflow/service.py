import bentoml
import numpy as np

from bentoml.models import BentoModel

# Define the runtime environment for your Bento
#PythonImage is deprecated. use Image instead
demo_image = bentoml.images.Image(python_version="3.11") \
    .python_packages("mlflow", "scikit-learn")

target_names = ['setosa', 'versicolor', 'virginica']

@bentoml.service(
    # image=demo_image,
    resources={"cpu": "1"},
    traffic={"timeout": 10},
)
class IrisClassifier:
    # Declare the model as a class attribute
    bento_model = BentoModel("iris:latest")

    def __init__(self):
        self.model = bentoml.mlflow.load_model(self.bento_model)

    # Define an API endpoint
    @bentoml.api
    def predict(self, input_data: np.ndarray) -> list[str]: #expects np.ndarray
        preds = self.model.predict(input_data)
        return [target_names[i] for i in preds]