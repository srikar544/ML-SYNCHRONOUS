Below is the structure of the Project -> with the description

ML-SYNCHRONOUS → Flow.py → Defines Prefect async flow that runs multiple ML training trials in parallel.  
ML-SYNCHRONOUS → Train.py → Trains a Random Forest model, saves metrics and model artifacts.  
ML-SYNCHRONOUS → ml-flow-k8s-deployment.yml → Defines Kubernetes job deployment for running the Prefect flow with resource limits and image settings.  
ML-SYNCHRONOUS → deploy_k8s.py → Deploys the Prefect flow to Kubernetes using a specified Docker image, work pool, and tags.  
ML-SYNCHRONOUS → deploy_flow.py → Registers and deploys the Prefect flow to a specific Kubernetes work queue.  
ML-SYNCHRONOUS → create_deployment.py → Builds and applies a Kubernetes deployment for the Prefect flow with defined resources.  
ML-SYNCHRONOUS → Steps.docx → Describes setup steps, execution flow, and Prefect–Kubernetes orchestration.  
ML-SYNCHRONOUS → Dockerfile → Builds a Python 3.13 Prefect 3.x image for running ML flows on Kubernetes.  

## 📁 ML-SYNCHRONOUS Project Structure

ML-SYNCHRONOUS
│
├── Flow.py
│ └── Defines Prefect flow (local_async_ml_flow) → orchestrates multiple async ML trials (t1, t2, t3)
│
├── Train.py
│ └── Called by Flow.py → trains RandomForest models and saves model + metrics JSONs to /artifacts
│
├── ml-flow-k8s-deployment.yml
│ └── YAML config for Prefect flow as Kubernetes Job → defines image, namespace, CPU/memory limits
│
├── deploy_k8s.py
│ └── Deploys Prefect flow to Kubernetes → uses Docker image + work pool, creates deployment definition
│
├── deploy_flow.py
│ └── Registers Prefect flow to Kubernetes work queue → schedules async runs via Prefect agent
│
├── create_deployment.py
│ └── Builds and applies KubernetesJob deployment → sets resource requests and container image
│
├── Steps.docx
│ └── Documentation → explains setup, installation, flow execution, and architecture
│
└── Dockerfile
└── Builds Python 3.13 image with Prefect 3.x + project dependencies → used by Kubernetes pods


---

### ⚙️ Execution Flow Summary
Flow.py → Train.py → artifacts  
Dockerfile → builds image  
ml-flow-k8s-deployment.yml → defines K8s job  
deploy_flow.py / deploy_k8s.py / create_deployment.py → deploy Prefect flow  
Kubernetes → runs pods → Prefect orchestrates async training → artifacts/logs collected  
---
