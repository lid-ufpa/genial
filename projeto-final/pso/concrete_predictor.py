import pickle
import numpy as np

class ConcreteStrengthPredictor:
    
    def __init__(self, model_path="concrete_rf.pkl", fixed_age=28.0):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        self.fixed_age = fixed_age
        self.feature_order = [
            "cement",
            "blastFurnaceSlag",
            "flyAsh",
            "water",
            "superplasticizer",
            "coarseAggregate",
            "fineAggregate",
            "age"
        ]

    def predict(
            self, cement, blastFurnaceSlag, flyAsh, water,
            superplasticizer, coarseAggregate, fineAggregate
            ):
        x = np.array([[
            cement,
            blastFurnaceSlag,
            flyAsh,
            water,
            superplasticizer,
            coarseAggregate,
            fineAggregate,
            self.fixed_age
        ]])

        return self.model.predict(x)[0]
