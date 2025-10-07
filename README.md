Below is the structure of the Project -> with the description

1)ML-SYNCHRONOUS -> Flow.py
2)ML-SYNCHRONOUS -> Train.py -> Trains a Random Forest on a toy dataset (or custom data), saves the model and metrics to the specified output directory, and prints accuracy.  
3)ML-SYNCHRONOUS -> ml-flow-k8s-deployment.yml ->Defines a Kubernetes job deployment for running the local_async_ml_flow Prefect flow with resource limits and container image settings.
4)ML-SYNCHRONOUS -> deploy_k8s.py -> Deploys the local_async_ml_flow Prefect flow to Kubernetes using the specified Docker image, work pool, and tags.
5)ML-SYNCHRONOUS -> deploy_flow.py  -> Deploys the local_async_ml_flow Prefect flow to a specific work queue on Kubernetes using the given Docker image and tags.
6)ML-SYNCHRONOUS -> create_deployment.py -> Creates and applies a Kubernetes deployment for the local_async_ml_flow Prefect flow with specified resource limits and Docker image.
7)ML-SYNCHRONOUS -> Steps.docx -> Runs and orchestrates parallel ML training experiments using Prefect, Docker, and Kubernetes — enabling scalable, asynchronous model training with automatic artifact tracking.
8)ML-SYNCHRONOUS -> Dockerfile -> Builds a lightweight Python 3.13 image with Prefect 3.x and project dependencies for running ML flows on Kubernetes. 

ML-SYNCHRONOUS
│
├── Flow.py
│     └── Defines Prefect flow (local_async_ml_flow)
│         → orchestrates multiple async ML trials (t1, t2, t3)
│
├── Train.py
│     └── Called by Flow.py
│         → trains RandomForest models, saves model + metrics JSONs to /artifacts
│
├── ml-flow-k8s-deployment.yml
│     └── YAML configuration for running Prefect flow as a Kubernetes Job
│         → defines image, namespace, CPU/memory limits, and labels
│
├── deploy_k8s.py
│     └── Deploys Prefect flow to Kubernetes
│         → uses Docker image + work pool, creates deployment definition
│
├── deploy_flow.py
│     └── Registers Prefect flow to a specific Kubernetes work queue
│         → schedules async runs via Prefect agent
│
├── create_deployment.py
│     └── Programmatically builds and applies a KubernetesJob deployment
│         → sets resource requests and container image
│
├── Steps.docx
│     └── Documentation
│         → explains setup, installation, flow execution, and architecture
│
└── Dockerfile
      └── Builds Python 3.13 image with Prefect 3.x + project dependencies
          → base image used by Kubernetes pods to run ML flows

**Execution Flow Summary**

Flow.py defines the Prefect flow → runs 3 async training trials.
Each trial calls Train.py → trains a Random Forest, saves model_*.joblib and metrics_*.json in /artifacts.
Dockerfile containerizes the code with Prefect installed.
ml-flow-k8s-deployment.yml describes how this flow runs on Kubernetes.
deploy_flow.py / deploy_k8s.py / create_deployment.py deploy the Prefect flow to K8s (via Prefect agent).
Kubernetes runs pods for each task → Prefect orchestrates them asynchronously.
Artifacts and logs are collected centrally → verified using Steps.docx instructions.

