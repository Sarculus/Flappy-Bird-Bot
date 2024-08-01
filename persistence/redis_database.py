import redis
r = redis.Redis(
  host='redis-17414.c327.europe-west1-2.gce.redns.redis-cloud.com',
  port=17414,
  password='TZgxGtwgJost678XJpsSKdndjYFBQltA',
  decode_responses=True)

# get and set key-value pairs
# r.set('foo', 'bar')
# print(r.get('foo'))

# r.set('mykey', '["1", "31-07-2024", "34"]')
# print(r.get('1'))
# r.set('2', '["2", "31-07-2024", "26"]')
# print(r.get('2'))
# [["1", "31-07-2024", "34"], ["2", "31-07-2024", "26"]]

# get and set dictionaries
# r.mset({'go': 'flow', 'hello': 'world'})
# r.mget(['go', 'hello'])

# get and set dictionaries as a whole
# r.hset('user-session:123', mapping={
#     'name': 'John',
#     "surname": 'Smith',
#     "company": 'Redis',
#     "age": 29
# })
# r.hgetall('user-session:123')

# r.hset('score:1', mapping={
#     'number': '1',
#     "date": '31-07-2024',
#     "score": '34'
# })
# print(r.hgetall('score:1'))
