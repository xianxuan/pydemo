import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)  # 连接池
r = redis.Redis(connection_pool=pool)
r.set('name', 'junxi')
print(r['name'])
print(r.get('name'))
print(type(r.get('name')))
