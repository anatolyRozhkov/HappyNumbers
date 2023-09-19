LAUNCH TESTS

```
docker-compose up -d --build
docker exec -it app bash
pytest -sv --tb long --log-path 'artifacts/'
```