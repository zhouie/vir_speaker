[![GitHub issues](https://img.shields.io/github/issues/zhouie/vir_speaker.svg)](https://github.com/zhouie/vir_speaker/issues)
[![GitHub forks](https://img.shields.io/github/forks/zhouie/vir_speaker.svg)](https://github.com/zhouie/vir_speaker/network)
[![GitHub stars](https://img.shields.io/github/stars/zhouie/vir_speaker.svg)](https://github.com/zhouie/vir_speaker/stargazers)
[![GitHub license](https://img.shields.io/github/license/zhouie/vir_speaker.svg)](https://github.com/zhouie/vir_speaker/blob/master/LICENSE)

## vir_speaker
A  small routine (compiled by Python) for exercise about English phrases in the field of computer.

## Guide post

[【Python学习实践】 speech智能语音模块](https://zhouie.cn/posts/201807271)

## Request
1. **python2.\* / python3.\***
2. **pywin32**
3. **speech**

## pywin32
[https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/)，根据 **Python版本（2.\*/3.\*）**和 **CPU位数（32位/64位**）下载相应版本安装

![](http://p7n85i5tr.bkt.clouddn.com/zhouie/img/speech/2.png)

比如，像我这种情况，就需要安装 `pywin32-221.win-amd64-py3.7.exe`

![](http://p7n85i5tr.bkt.clouddn.com/zhouie/img/speech/3.png)

## speech
`pip install speech`

对于Python3用户，安装完speech模块后，需要去修改 **speech.py**文件，该文件路径在`..\Python37\Lib\site-packages`下

1. line59 修改`import thread`，改成`import threading`；
2. line157 修改`print prompt`，改成`print(prompt)`；
3. 对最后的函数`_ensure_event_thread`修改如下：

```
class T(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
            pass
        
def _ensure_event_thread():
    """
    Make sure the eventthread is running, which checks the handlerqueue
    for new eventhandlers to create, and runs the message pump.
    """
    global _eventthread
    if not _eventthread:
        def loop():
            while _eventthread:
                pythoncom.PumpWaitingMessages()
                if _handlerqueue:
                    (context,listener,callback) = _handlerqueue.pop()
                    # Just creating a _ListenerCallback object makes events
                    # fire till listener loses reference to its grammar object
                    _ListenerCallback(context, listener, callback)
                time.sleep(.5)
        _eventthread = T()
        _eventthread.start()
```

## 效果展示

<iframe frameborder="0" width="100%" height="520" src="https://v.qq.com/iframe/player.html?vid=o0737zviriw&tiny=0&auto=0" allowfullscreen>
