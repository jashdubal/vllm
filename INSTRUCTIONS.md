Build for CPU: `docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g .`

Run for CPU: `docker run -it --rm --network=bridge -p 8000:8000 vllm-cpu-env`

### 1) CPU Execution
**Building the Image:**
```
DOCKER_BUILDKIT=1 docker build -f Dockerfile.cpu -t vllm-cpu-env \
--build-arg MAX_JOBS=<num_jobs> \
--shm-size=4g .
```

**Explanation:**

- `-f Dockerfile.cpu`: Specifies the Dockerfile for CPU execution.
- `-t vllm-cpu-env`: Tags the image as `vllm-cpu-env`.
- `--build-arg MAX_JOBS=<num_jobs>`: (Optional) Sets the maximum number of parallel jobs during the build, impacting build speed. Replace `<num_jobs>` with the desired number.
- `--shm-size=4g`: Sets the shared memory size to 4GB. Adjust this if needed based on your model and system resources.

**Running the Container:**

```
docker run -it \
--rm \
--network=host \
--cpuset-cpus=<cpu_id_list> \
--cpuset-mems=<memory_node> \
vllm-cpu-env \
vllm serve \
--model <model_name> \
<engine_args...>
```

**Explanation:**

- `-it`: Runs the container in interactive mode.
- `--rm`: Removes the container after it exits.
- `--network=host`: Uses the host's network stack.
- `--cpuset-cpus=<cpu_id_list>`: (Optional) Specifies the CPU cores to use. Replace `<cpu_id_list>` with a comma-separated list or a range (e.g., `0-3`, `0,2,4`).
- `--cpuset-mems=<memory_node>`: (Optional) Assigns a specific memory node. Replace `<memory_node>` with the node ID.
- `vllm-cpu-env`: The name of the built CPU image.
- `vllm serve`: Starts the vLLM server.
- `--model <model_name>`: Specifies the Hugging Face model to use.
- `<engine_args...>`: Include any desired engine arguments for customizing the server (see the "Settings and Configurations" section in the previous response).

**CPU-Specific Environment Variables:**

You can set these environment variables inside the Docker container to further configure vLLM for CPU execution:

- `VLLM_CPU_KVCACHE_SPACE=<cache_size_gb>`: Sets the CPU key-value cache size in GB. The default is 4GB.
- `VLLM_CPU_OMP_THREADS_BIND=<cpu_core_binding>`: Defines the CPU core binding for OpenMP threads (e.g., `0-31`, `0,1,2`, `0-31,33`). Separate core ranges for different ranks using '|'.

### 2) GPU Execution

**Building the Image:**

```
DOCKER_BUILDKIT=1 docker build . --target vllm-openai --tag vllm/vllm-openai \
--build-arg max_jobs=<num_jobs> \
--build-arg nvcc_threads=<num_threads> \
--build-arg torch_cuda_arch_list=<gpu_arch_list>
```

**Explanation:**

- Refer to the "Building the Docker Image" section in the previous response for explanations of common arguments.
    
- `--build-arg torch_cuda_arch_list=<gpu_arch_list>`: (Optional) Optimizes the build for specific GPU architectures by specifying a list of supported architectures (e.g., `"8.0"` for Ampere, `"9.0"` for Hopper). Leaving this argument empty will make vLLM build for the detected GPU type of the machine.
    

**Running the Container:**

```
docker run --runtime nvidia --gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
-p 8000:8000 \
--env "HUGGING_FACE_HUB_TOKEN=<secret>" \
--ipc=host \
vllm/vllm-openai \
vllm serve \
--model <model_name> \
<engine_args...>
```

**Explanation:**

- Refer to the "Running the Docker Container" section in the previous response for explanations of common arguments.
- `--ipc=host`: Shares the host's shared memory with the container. This is important for efficient tensor parallel inference.

## [Command line arguments](https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html#command-line-arguments-for-the-server "Permalink to this heading") for the server 
