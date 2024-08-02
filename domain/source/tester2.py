import ast
from datetime import date
import redis

score = 12
date_dmy = f"{date.today().day}-{date.today().month}-{date.today().year}"
r = redis.Redis(
    host='redis-17414.c327.europe-west1-2.gce.redns.redis-cloud.com',
    port=17414,
    password='TZgxGtwgJost678XJpsSKdndjYFBQltA',
    decode_responses=True)
r.incr('idcounter')
name = f"{r.get("idcounter")} {date_dmy}"
r.zadd('highscorestest2', {name: score})




sorted_list = r.zrange('highscorestest2', 0, 9, desc=True, withscores=True)
print(sorted_list)
# r.incr('idcounter')
# r.set(f'{r.get("idcounter")}', highscore)

return_list = []
# print(sorted_list[0][1])
# print(sorted_list[1][1])
# print(sorted_list[0][0])
# print(type(sorted_list[0][0]))
# stringto = sorted_list[0][0]
# a = stringto.split(" ")
# print(a[1])
# test2 = ast.literal_eval(sorted_list[0][0])
# print(test2)
for i in range(0, 10):
    score_part = sorted_list[i][1]
    date_part = sorted_list[0][0]
    date_part2 = date_part.split(" ")
    test2 = [date_part2[1], score_part]
    return_list.append(test2)
print(return_list)