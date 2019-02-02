import nsq
import tornado.ioloop


# tornado==4.5.3

def pub_message():
    msg = "nihao"
    # 转为bytes数组
    writer.pub('test', msg.encode(encoding="utf-8"), finish_pub)


def finish_pub(conn, data):
    print(data)


writer = nsq.Writer(['127.0.0.1:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
