Build for CPU: `docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g .`

Run for CPU: `docker run -it --rm --network=bridge -p 8000:8000 vllm-cpu-env`


