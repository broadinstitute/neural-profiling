user = michaelbornholdt
project = deep_profiler
tag = test_030

.DEFAULT_GOAL: build
build:
        docker build -t $(user)/$(project):$(tag) .
        docker login -u $(user)
        docker push $(user)/$(project):$(tag)
        echo "Your new docker registry is ready at: $(user)/$(project):$(tag)"

# --no-cache

