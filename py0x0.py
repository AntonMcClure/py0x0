#!/usr/bin/env python3
#
# py0x0.py
#
# Copyright (c) 2019-2021 Anton McClure <anton@antonmcclure.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import config
import sys
import os
import requests

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print("=========================================================================")
    print("                    -=[ py0x0 -- The Null Pointer ]=-")
    print("=========================================================================")
    print("Version 2.1.1")
    print("Copyright (C) 2019-2021, Anton McClure <anton@antonmcclure.com>.")
    choice = input("""
    1: HTTP Post Local File
    2: HTTP Post Remote File
    3: Shorten URL
    4: View py0x0 License Info
    5: What's New in This Version
    6: Exit

    Select an option [1-6]: """)
    if choice == "1":
        cmdPostLocalFile()
    elif choice == "2":
        cmdPostRemoteFile()
    elif choice == "3":
        cmdShortenUrl()
    elif choice == "4":
        cmdShowLicense()
    elif choice == "5":
        cmdWhatsNew()
    elif choice == "6":
        sys.exit()
    else:
        print()
        print("Invalid selection.")
        cmdPause()
        main()

def cmdPause():
    print()
    input("Press Enter to continue...")

def cmdPostLocalFile():
    clear()
    print("=========================================================================")
    print("    py0x0 | HTTP Post Local File")
    print("=========================================================================")
    txtLocalFile = str(input("Enter full local file path: "))
    with open(txtLocalFile) as localFile:
        r = requests.post("https://"+config.server,files=dict(file=localFile))
        if r.status_code != 200:
            print(f"ERROR: Server returned response code {r.status_code}")
            cmdPause()
            main()
        print(r.text)
    cmdPause()
    main()

def cmdPostRemoteFile():
    clear()
    print("=========================================================================")
    print("    py0x0 | HTTP Post Remote File")
    print("=========================================================================")
    txtRemoteFile = str(input("Enter full remote file url: "))
    if "http://" in txtRemoteFile:
        str.replce("http://", "https://")
    if "https://" not in txtRemoteFile:
        txtRemoteFile = 'https://' + txtRemoteFile
    if "https://" in txtRemoteFile:
        txtRemoteFile = txtRemoteFile
    try:
        rRemote = requests.get(txtRemoteFile)
    except requests.exceptions.ConnectionError:
        print('Cannot connect to site. (Connection error)')
    except requests.exceptions.HTTPError:
        print('Cannot connect to site. (HTTP error)')
    else:
        rpRemote = requests.post("https://" + config.server,data=dict(url=txtRemoteFile))
        if rpRemote.status_code != 200:
            print(f'\nERROR: Server returned response code: {rpRemote.status_code}\n{rpRemote.text}')
        if rpRemote.status_code == 200:
            print(f'\n{rpRemote.text}')
    cmdPause()
    main()

def cmdShortenUrl():
    clear()
    print("=========================================================================")
    print("    py0x0 | Shorten URL")
    print("=========================================================================")
    txtLongUrl = str(input("Enter full url to shorten: "))
    if "http://" in txtLongUrl:
        str.replce("http://", "https://")
    if "https://" not in txtLongUrl:
        txtLongUrl = 'https://' + txtLongUrl
    if "https://" in txtLongUrl:
        txtLongUrl = txtLongUrl
    try:
        rShorten = requests.get(txtLongUrl)
    except requests.exceptions.ConnectionError:
        print('Cannot connect to site. (Connection error)')
    except requests.exceptions.HTTPError:
        print('Cannot connect to site. (HTTP error)')
    else:
        rpShorten = requests.post("https://" + config.server,data=dict(shorten=txtLongUrl))
        if rpShorten.status_code != 200:
            print(f'\nERROR: Server returned response code: {rpShorten.status_code}\n{rpShorten.text}')
        if rpShorten.status_code == 200:
            print(f'\n{rpShorten.text}')
    cmdPause()
    main()

def cmdShowLicense():
    clear()
    print("=========================================================================")
    print("    py0x0 | py0x0 Software License")
    print("=========================================================================")
    print('Copyright (C) 2019, Anton McClure <anton@antonmcclure.com>')
    print()
    print('Licensed under the Apache License, Version 2.0 (the "License");')
    print('you may not use this file except in compliance with the License.')
    print('You may obtain a copy of the License at')
    print()
    print('    http://www.apache.org/licenses/LICENSE-2.0')
    print()
    print('Unless required by applicable law or agreed to in writing, software')
    print('distributed under the License is distributed on an "AS IS" BASIS,')
    print('WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.')
    print('See the License for the specific language governing permissions and')
    print('limitations under the License.')

    cmdPause()
    main()

def cmdWhatsNew():
    clear()
    print("=========================================================================")
    print("    py0x0 | What's New in This Version")
    print("=========================================================================")
    fileWhatsNew = open("WhatsNew.txt", "r")
    print(fileWhatsNew.read())
    fileWhatsNew.close()

    cmdPause()
    main()

main()
