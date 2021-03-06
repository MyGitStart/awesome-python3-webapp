import www.orm,asyncio
from www.models import User,Blog,Comment

def test(loop):
    yield from www.orm.create_pool(loop=loop,user='root',password='password',db='awesome')
    u=User(name='test3',email='test4@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()