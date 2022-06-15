import redis

r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)

def hit(user):
    r.incr(user)

def get_hit(user):
    return (r.get(user))
