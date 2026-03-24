IMAGE_NAME=rohitutekar123/student-api:latest
CONTAINER_NAME=student-api-container
PORT=5000

run:
	docker run -d -p $(PORT):5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

restart: stop run

logs:
	docker logs -f $(CONTAINER_NAME)
