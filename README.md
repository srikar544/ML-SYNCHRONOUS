Below is the structure of the Project:

ML-SYNCHRONOUS -> Flow.py -> Runs multiple ML training experiments asynchronously with Prefect, executing train.py for different hyperparameters and saving outputs to /app/artifacts.
ML-SYNCHRONOUS -> Train.py
ML-SYNCHRONOUS -> ml-flow-k8s-deployment.yml
ML-SYNCHRONOUS -> deploy_k8s.py
ML-SYNCHRONOUS -> deploy_flow.py
ML-SYNCHRONOUS -> create_deployment.py
ML-SYNCHRONOUS -> Steps.docx
ML-SYNCHRONOUS -> Dockerfile
