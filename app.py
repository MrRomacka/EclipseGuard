import requests
import sqlite3 #Приоритетнее использование PostgreSQL
from flask import Flask, request
import base64

d = {'click': 'On', 'double_click': 'Off', 'long_press': 'Sleep Mode'}

def changeStatus(device, action):
    global cur
    global d
    cur.execute(f'UPDATE owner SET status = {d[action]} where device = {device}')

def notifyChange(device, action):
    pass
    #Здесь могла быть функция с уведомлением владельца
    #об изменении статуса сигнализации, но её пока нет ¯\_(ツ)_/¯

def decrypting(device):
    pass
    #Декриптинг, чтобы не было взломов сигнализации без кнопки.

app = Flask(__name__)

@app.route('/MTSButton')
def FL():
    global d
    js = request.args.get('data')
    js = base64.b64decode(js)
    print(type(js))
    decrypting()
    telemetry = js['telemetry']
    firstButton = telemetry['firstButton']
    status = firstButton['status']
    if js[deviceName] not in cur.execute('SELECT device FROM owner'):
        cur.execute(f'INSERT INTO owner (device, owner, status) VALUES ({js[serialNumber]}, {js[iccid]}, {status}')
    else:
        changeStatus(js[serialNumber], status)
    notifyChange()
    return 'Hi, Mark'

@app.route('/Signalling') #Страница для датчика двери
def signal():
    pass
    #decrypting() - получение номера владельца через decrypting, чтобы не было специальных взломов.
    #Включение в систему датчика двери, который посылает запрос при открытии двери.
    #Если Статус Off, то ничего не делает,
    #On - посылает уведомление на телефон владельца, если не отреагировал спустя минуту-две - вызов ЧОП,
    #Sleep - моментальный вызов ЧОП и уведомление владельцу.

@app.route('/')
def outDB():
        db_connection = sqlite3.connect('db/ecliptic.db')
        cur = db_connection.cursor()
        res = cur.execute('SELECT * FROM owner').fetchall()
        res = ' '.join(map(str, res))
        db_connection.close()
        return res


db_connection = sqlite3.connect('db/ecliptic.db')
cur = db_connection.cursor()

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
