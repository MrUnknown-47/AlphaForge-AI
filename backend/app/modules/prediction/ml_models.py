import logging
import numpy as np

logger = logging.getLogger(__name__)

# Try importing ML libraries
try:
    import xgboost as xgb
    HAS_XGB = True
except Exception as e:
    HAS_XGB = False
    logger.warning(f"xgboost could not be loaded: {e}. Falling back to sklearn.")

try:
    import lightgbm as lgb
    HAS_LGBM = True
except Exception as e:
    HAS_LGBM = False
    logger.warning(f"lightgbm could not be loaded: {e}. Falling back to sklearn.")

try:
    from sklearn.ensemble import RandomForestRegressor
    HAS_SKLEARN = True
except Exception as e:
    HAS_SKLEARN = False
    logger.warning(f"sklearn could not be loaded: {e}.")

try:
    import torch
    import torch.nn as nn
    HAS_TORCH = True
except Exception as e:
    HAS_TORCH = False
    logger.warning(f"torch could not be loaded: {e}. Falling back to sklearn MLP.")


# --- Base Est Estimator Abstraction ---
class BaseEstimator:
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.zeros(len(X))


# --- Concrete Estimators ---
class XGBoostModel(BaseEstimator):
    def __init__(self, **kwargs) -> None:
        self.params = kwargs or {"n_estimators": 100, "max_depth": 5, "learning_rate": 0.05}
        self.model = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        if HAS_XGB:
            self.model = xgb.XGBRegressor(**self.params)
            self.model.fit(X, y)
        elif HAS_SKLEARN:
            from sklearn.ensemble import GradientBoostingRegressor
            logger.warning("xgboost not installed. Falling back to sklearn GradientBoostingRegressor.")
            self.model = GradientBoostingRegressor(n_estimators=self.params.get("n_estimators", 100), max_depth=self.params.get("max_depth", 5))
            self.model.fit(X, y)
        else:
            logger.error("No compatible regressor libraries found on environment.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.model:
            return self.model.predict(X)
        return np.zeros(len(X))



# PyTorch LSTM time-series classifier
if HAS_TORCH:
    class PyTorchLSTM(nn.Module):
        def __init__(self, input_dim: int, hidden_dim: int, num_layers: int = 1) -> None:
            super(PyTorchLSTM, self).__init__()
            self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
            self.linear = nn.Linear(hidden_dim, 1)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            # Input: (batch, seq, features)
            out, _ = self.lstm(x)
            # Pick last sequence step output
            out = out[:, -1, :]
            return self.linear(out)

class LSTMModel(BaseEstimator):
    def __init__(self, **kwargs) -> None:
        self.hidden_dim = kwargs.get("hidden_dim", 32)
        self.epochs = kwargs.get("epochs", 5)
        self.model = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        if HAS_TORCH:
            # Reshape X to fit sequence dims (batch, seq_len=1, features)
            X_seq = torch.tensor(X[:, np.newaxis, :], dtype=torch.float32)
            y_tensor = torch.tensor(y[:, np.newaxis], dtype=torch.float32)
            
            input_dim = X.shape[1]
            self.model = PyTorchLSTM(input_dim, self.hidden_dim)
            optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)
            criterion = nn.MSELoss()
            
            self.model.train()
            for epoch in range(self.epochs):
                optimizer.zero_grad()
                outputs = self.model(X_seq)
                loss = criterion(outputs, y_tensor)
                loss.backward()
                optimizer.step()
        elif HAS_SKLEARN:
            from sklearn.neural_network import MLPRegressor
            logger.warning("torch not installed. Falling back to sklearn Multi-Layer Perceptron (MLP) for LSTM.")
            self.model = MLPRegressor(hidden_layer_sizes=(self.hidden_dim, self.hidden_dim), max_iter=self.epochs*10)
            self.model.fit(X, y)
        else:
            logger.error("No Neural Network libraries found on environment.")

    def predict(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X)
        if self.model:
            if HAS_TORCH and isinstance(self.model, nn.Module):
                self.model.eval()
                with torch.no_grad():
                    X_seq = torch.tensor(X[:, np.newaxis, :], dtype=torch.float32)
                    preds = self.model(X_seq).numpy()
                    return preds.squeeze()
            else:
                return self.model.predict(X)
        return np.zeros(len(X))


class Scaler:
    def __init__(self) -> None:
        self.mean = None
        self.std = None

    def fit(self, X: np.ndarray) -> None:
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)
        # Prevent zero division
        self.std = np.where(self.std == 0, 1e-8, self.std)

    def transform(self, X: np.ndarray) -> np.ndarray:
        return (X - self.mean) / self.std

