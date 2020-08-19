'''
Created on 2016年2月16日

@author: 15051125
'''
import websocket
import time
import struct
import json
import threading
import logging
from suning.messagePush import message

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='messagePush.log',
                filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
 
class WebSocketClient():
    """Base for web socket clients.
    """
    ws = websocket.WebSocket()
    def __init__(self,uri,appKey,appSecret,groupName):
        self.uri=uri
        self.appKey=appKey
        self.appSecret=appSecret
        self.groupName=groupName
        self.mess=message.Message()
        
    def ping(self):
        def run():
            while True:
                try:
                    if self.ws.connected:
                        self.ws.ping()
                except:
                    pass
                time.sleep(30)
        t1 = threading.Thread(target=run,args=())
        t1.setDaemon(True)
        t1.start()
        
    def auth(self):        
        _b_auth = bytes(self.authMessage(), encoding = "utf8")
        _bi_auth = struct.pack('%ds'%len(_b_auth),_b_auth)
        frame = websocket.ABNF.create_frame(_bi_auth, websocket.ABNF.OPCODE_BINARY)
        if self.ws.connected:
            self.ws.send_frame(frame)
            
    def connect(self):
        def conn():
            while True:
                if not (self.ws.connected):
                    try:
                        logging.info("disconnected... will try to reconnect in 5 sec...")
                        self.ws.connect(self.uri)
                        self.auth()
                    except:
                        pass
                time.sleep(5)
        try:
            self.ws.connect(self.uri)
            self.auth()
        except:
            pass
        t2 = threading.Thread(target=conn,args=())
        t2.setDaemon(True)
        t2.start()
        self.ping()
        
    def onMessage(self):
        while True:
            try:
                if self.ws.connected:                    
                    fre = self.ws.recv_frame()
                    if fre.opcode == websocket.ABNF.OPCODE_PONG:
                        self.mess.setMessageId("pong")
                        logging.info("client recived pong")
                    elif fre.opcode == websocket.ABNF.OPCODE_CLOSE:
                        print("closed")
                    elif fre.opcode == websocket.ABNF.OPCODE_BINARY:      
                        _bi_re = fre.data
                        _b_re, = struct.unpack('%ds'%len(_bi_re),_bi_re)
                        re = str(_b_re, encoding = "utf-8")
                        _j_re = json.loads(re)
                        msg = _j_re['msg']
                        msgType = _j_re['messageType']
                        if msgType == "AUTHACK":
                            if msg == "OK":
                                logging.info("client handshake success!")
                            else:
                                raise RuntimeError("auth error:"+msg)
                        elif msgType == "FROM":
                            self.mess.setAppId(_j_re['appId'])
                            self.mess.setAppKey(_j_re['appKey'])
                            self.mess.setCreateTime(_j_re['createTime'])
                            self.mess.setMessageId(_j_re['messageId'])
                            self.mess.setMessageType(_j_re['messageType'])
                            self.mess.setMsg(_j_re['msg'])
                            self.mess.setRecevieTime(_j_re['recevieTime'])
                            self.mess.setSendTime(_j_re['sendTime'])
                            self.mess.setSource(_j_re['source'])
                            self.mess.setTopic(_j_re['topic'])
                            self.mess.setUser(_j_re['user'])
                            _j_send = _j_re
                            _j_send['appId']=None
                            _j_send['createTime']=None
                            _j_send['recevieTime']=None
                            _j_send['sendTime']=None
                            _j_send['source']=None
                            _j_send['msg']=None
                            _j_send['messageType']="ACK"
                            _str_send = json.dumps(_j_send)
                            _b_send = bytes(_str_send, encoding = "utf8")
                            _bi_send= struct.pack('%ds'%len(_b_send),_b_send)
                            frame = websocket.ABNF.create_frame(_bi_send, websocket.ABNF.OPCODE_BINARY)
                            self.ws.send_frame(frame)
                            return self.mess                          
                    else:
                        logging.info("client wrong")
                else:
                    time.sleep(10)
            except RuntimeError as err:
                raise RuntimeError(err)
            except:
                self.ws.close()
                time.sleep(10)

                    
    def authMessage(self):
        return "{\"appKey\":\"" + self.appKey + "\",\"appSecret\":\"" + self.appSecret + "\",\"groupName\":\"" + self.groupName + "\"}"