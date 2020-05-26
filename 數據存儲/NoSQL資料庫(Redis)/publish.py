from redis import Redis

cache = Redis(host='127.0.0.1', port=6379, password='851230')
# 向email頻道發送消息
cache.publish('email', 'hihihi')
