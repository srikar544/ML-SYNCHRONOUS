# Flow.py
from prefect import flow, task
import subprocess

@task
def run_train_task(trial_id, n_estimators, max_depth):
    cmd = [
        "python", "train.py",
        "--trial_id", str(trial_id),
        "--n_estimators", str(n_estimators),
        "--max_depth", str(max_depth),
        "--output_dir", "/app/artifacts"
    ]
    subprocess.run(cmd, check=True)

@flow
def local_async_ml_flow():
    # Define multiple trials
    trials = [
        {"trial_id": "t1", "n_estimators": 100, "max_depth": 5},
        {"trial_id": "t2", "n_estimators": 200, "max_depth": 8},
        {"trial_id": "t3", "n_estimators": 150, "max_depth": 10},
    ]

    # Run tasks asynchronously
    for t in trials:
        run_train_task.submit(**t)  # submit() => async execution
