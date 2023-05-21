import tornado.websocket
import tornado.web
import tornado.ioloop

clients = set()



class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket connection opened")
        clients.add(self)
        print(clients)


    def on_message(self, message):        
        for client in clients:    
            if self != client:        
                client.write_message(message)

    def on_close(self):
        print("WebSocket connection closed")



app = tornado.web.Application([
    (r"/websocket", MyWebSocketHandler),
])

app.listen(8888)
tornado.ioloop.IOLoop.current().start()