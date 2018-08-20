# import the library

import hashlib
from appJar import gui
def MD5(text):
    return str(hashlib.md5(text).hexdigest())
def SHA512(text):
    return str(hashlib.sha512(text).hexdigest())
def SHA256(text):
    return str(hashlib.sha256(text).hexdigest())
def SHA1(text):
    return str(hashlib.sha1(text).hexdigest())


def Hash_MD5(btn):
    if btn == "Submit":
        text = app.getEntry("Hash-MD5")
        app.setEntry("MD5",MD5(text))
    if btn =="Clear":
        app.clearEntry("Hash-MD5")
        app.setEntry("MD5","")
def Hash_SHA512(btn):
    if btn == "Submit ":
        text = app.getEntry("Hash-SHA512")
        app.setEntry("SHA512",SHA512(text))
    if btn =="Clear ":
        app.clearEntry("Hash-SHA512")
        app.setEntry("SHA512","")
def Hash_SHA256(btn):
    if btn == " Submit":
        text = app.getEntry("Hash-SHA256")
        app.setEntry("SHA256",SHA512(text))
    if btn == " Clear":
        app.clearEntry("Hash-SHA256")
        app.setEntry("SHA256","")
def Hash_SHA1(btn):
    if btn == " Submit ":
        text = app.getEntry("Hash-SHA1")
        app.setEntry("SHA1",SHA1(text))
    if btn == " Clear ":
        app.clearEntry("Hash-SHA1")
        app.setEntry("SHA1","")



app = gui("Hash")

app.startTabbedFrame("TabbedFrame")
app.startTab("MD5")
app.label("Hash-MD5", "Hash-MD5")
app.entry("Hash-MD5", focus=True)
app.buttons(["Submit", "Clear"], Hash_MD5, colspan=4)
app.entry("MD5", "MD5", sticky="ew",state="readonly")
app.stopTab()

app.startTab("SHA1")
app.label("Hash-SHA1", "Hash-SHA1")
app.entry("Hash-SHA1", focus=True)
app.buttons([" Submit ", " Clear "], Hash_SHA1, colspan=4)
app.entry("SHA1", "SHA1", sticky="ew",state="readonly")
app.stopTab()

app.startTab("SHA256")
app.label("Hash-SHA256", "Hash-SHA256")
app.entry("Hash-SHA256", focus=True)
app.buttons([" Submit", " Clear"], Hash_SHA256, colspan=4)
app.entry("SHA256", "SHA256", sticky="ew",state="readonly")
app.stopTab()

app.startTab("SHA512")
app.label("Hash-SHA512", "Hash-SHA512")
app.entry("Hash-SHA512", focus=True)
app.buttons(["Submit ", "Clear "], Hash_SHA512, colspan=4)
app.entry("SHA512", "SHA512", sticky="ew",state="readonly")
app.stopTab()

app.startTab("Help")
app.addMessage("help", """Made by ziad hany \nemail:- ziadhany2016@gmail.com \n Github:- https://github.com/ziadhany   
""")
app.setMessageFg("help","red")
app.stopTab()

app.stopTabbedFrame()

app.go()