# train.py
import argparse
import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run_train(params, output_dir="/tmp/artifacts"):
    # Generate toy dataset OR read file path from params["data_path"]
    X, y = make_classification(n_samples=2000, n_features=20, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(
        n_estimators=int(params.get("n_estimators", 100)),
        max_depth=None if params.get("max_depth") is None else int(params.get("max_depth")),
        random_state=42,
        n_jobs=1
    )
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)

    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, f"model_{params.get('trial_id', 't')}.joblib")
    joblib.dump(clf, model_path)

    metric_path = os.path.join(output_dir, f"metrics_{params.get('trial_id', 't')}.json")
    with open(metric_path, "w") as f:
        json.dump({"accuracy": acc, "params": params, "model_path": model_path}, f)

    print(f"TRAIN DONE: trial={params.get('trial_id')} acc={acc:.4f} model={model_path}")
    return {"accuracy": acc, "model_path": model_path, "metrics_path": metric_path}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trial_id", default="t0")
    parser.add_argument("--n_estimators", default="100")
    parser.add_argument("--max_depth", default="")
    parser.add_argument("--output_dir", default="/tmp/artifacts")
    args = parser.parse_args()
    params = vars(args)
    # normalize empty string -> None
    if params["max_depth"] == "": params["max_depth"] = None
    print("Running training with", params)
    res = run_train(params, output_dir=params["output_dir"])
    print(res)
