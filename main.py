"""
Welcome to the Hash Application! 
"""

import hashlib
from appJar import gui

SUPPORTED_HASH = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA256": hashlib.sha256,
    "SHA384": hashlib.sha384,
    "SHA512": hashlib.sha512,
}

def hash_generator(algorithm, text):
    """
    Generates a hash for the given byte-encoded text using the specified algorithm.

    >>> hash_generator("SHA256", b"hello")
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    """
    if algorithm in SUPPORTED_HASH:
        return SUPPORTED_HASH.get(algorithm)(text).hexdigest()
    raise ValueError(f"Unsupported hash algorithm: {algorithm}")


def action_handler(btn):
    "Handles actions for hash generation and clearing based on the button input."
    action_type, action_key = btn.split("-")
    if action_type == "Submit":
        text = app.getEntry(f"Hash-{action_key}").encode()
        app.setEntry(action_key,  str(hash_generator(action_key, text)))
    if action_type == "Clear":
        app.clearEntry(f"Hash-{action_key}")
        app.setEntry(action_key,"")


app = gui("Hash App")

app.startTabbedFrame("TabbedFrame")

for key in SUPPORTED_HASH.keys():
    app.startTab(key)
    app.label(f"Hash-{key}", f"Hash-{key}")
    app.entry(f"Hash-{key}", focus=True)
    app.buttons([f"Submit-{key}", f"Clear-{key}"], action_handler, colspan=4)
    app.entry(key, "", sticky="ew",state="readonly")
    app.stopTab()

app.startTab("Help")
app.addMessage("help", """📌 Welcome to the Hash Application!

💡 Need help? Here's how to reach me:
👤 Created by: Ziad Hany
📧 Email: ziadhany2016@gmail.com
🌐 GitHub: https://github.com/ziadhany/Hash/issues

Thank you for using Hash Application! 🚀
""")
app.setMessageFg("help","red")
app.stopTab()

app.stopTabbedFrame()

for key in SUPPORTED_HASH.keys():
    app.setButton(f"Submit-{key}", "Submit")
    app.setButton(f"Clear-{key}", "Clear")

if __name__ == "__main__":
    app.go()
