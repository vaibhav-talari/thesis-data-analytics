# Build
Build docker image
- `docker build -t data-analytics .`

# Run
Run docker image with volumes to access existing notebooks
- `docker run -p 8888:8888 -v $(pwd):/app/notebooks data-analytics`