from Flow import local_async_ml_flow
from prefect.deployments import Deployment
from prefect.infrastructure.kubernetes import KubernetesJob

# Define Kubernetes infrastructure
k8s_job = KubernetesJob(
    image="9177746770/ml-prefect-flow:latest",
    namespace="prefect",
    cpu_request="500m",
    memory_request="1Gi",
    cpu_limit="1",
    memory_limit="2Gi",
)

# Build and apply deployment
deployment = Deployment.build_from_flow(
    flow=local_async_ml_flow,
    name="ml-flow-k8s",
    infrastructure=k8s_job
)

if __name__ == "__main__":
    deployment.apply()
