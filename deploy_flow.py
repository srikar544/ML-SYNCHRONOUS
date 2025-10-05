from Flow import local_async_ml_flow

local_async_ml_flow.deploy(
    name="ml-flow-k8s",
    image="9177746770/ml-prefect-flow:latest",
    work_queue_name="process-queue",
    tags=["k8s"]
)

print("Deployment created successfully!")
