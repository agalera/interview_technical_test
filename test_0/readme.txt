# build
docker build --no-cache -t test_0:1.0.0 .

# save
docker save -o /home/docker_images/test_0.docker test_0:1.0.0

# load
docker load -i /home/docker_images/docker_images/test_0.docker

# run
docker run --net devnet --ip 172.18.0.2 -dt gcr.io/mest-editor/test_0:1.0.0