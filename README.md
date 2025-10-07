Below is the structure of the Project -> with the description

ML-SYNCHRONOUS -> Flow.py
ML-SYNCHRONOUS -> Train.py -> Trains a Random Forest on a toy dataset (or custom data), saves the model and metrics to the specified output directory, and prints accuracy.  
ML-SYNCHRONOUS -> ml-flow-k8s-deployment.yml ->Defines a Kubernetes job deployment for running the local_async_ml_flow Prefect flow with resource limits and container image settings.
ML-SYNCHRONOUS -> deploy_k8s.py -> Deploys the local_async_ml_flow Prefect flow to Kubernetes using the specified Docker image, work pool, and tags.
ML-SYNCHRONOUS -> deploy_flow.py  -> Deploys the local_async_ml_flow Prefect flow to a specific work queue on Kubernetes using the given Docker image and tags.
ML-SYNCHRONOUS -> create_deployment.py -> Creates and applies a Kubernetes deployment for the local_async_ml_flow Prefect flow with specified resource limits and Docker image.
ML-SYNCHRONOUS -> Steps.docx -> Runs and orchestrates parallel ML training experiments using Prefect, Docker, and Kubernetes — enabling scalable, asynchronous model training with automatic artifact tracking.
ML-SYNCHRONOUS -> Dockerfile -> Builds a lightweight Python 3.13 image with Prefect 3.x and project dependencies for running ML flows on Kubernetes.  


