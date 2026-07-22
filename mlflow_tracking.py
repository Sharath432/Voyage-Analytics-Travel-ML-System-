import joblib
import mlflow
import mlflow.sklearn

# Set experiment name
mlflow.set_experiment("Voyage Flight Price Prediction")

with mlflow.start_run(run_name="RandomForest_Best_Model"):

    # Load trained model
    model = joblib.load("models/best_rf_model.pkl")

    # Log model parameters
    mlflow.log_param("Algorithm", "Random Forest")
    mlflow.log_param("n_estimators", 50)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("min_samples_split", 5)
    mlflow.log_param("max_features", 27)
    mlflow.log_param("random_state", 42)

    # Log evaluation metrics
    mlflow.log_metric("MSE", 0.43459)
    mlflow.log_metric("RMSE", 0.659235)
    mlflow.log_metric("MAE", 0.044337)
    mlflow.log_metric("R2", 0.999997)
    mlflow.log_metric("Adjusted_R2", 0.999997)

    # Save model to MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="RandomForest_Model"
    )

print(" Random Forest model logged successfully!")+