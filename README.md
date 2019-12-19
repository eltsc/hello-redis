# hello-redis

to new build:
oc start-build flask-redis

to create imagestream:
oc create imagestream flask-redis

to create a service:
oc expose dc redis-py --type=ClusterIP --name=redis-py

to create a route:
oc expose service redis-py --name=web --port=8080