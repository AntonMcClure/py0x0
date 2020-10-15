#!/usr/bin/env python3
#   Copyright (C) 2019-2020, Anton McClure <anton@antonmcclure.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
    print("Version 2.1.0")
    print("Copyright (C) 2019-2020, Anton McClure <anton@antonmcclure.com>.")
    choice = input("""
    1: HTTP Post Local File
    2: HTTP Post Remote File
    3: Shorten URL
    4: View py0x0 License Info
    5: What's New in This Version
    6: Check for Updates
    7: Exit

    Select an option [1-9]: """)
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
        cmdCheckUpdates()
    elif choice == "7":
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
    if txtRemoteFile.find("http://" or "https://"):
        txtRemoteFile = "https://"+txtRemoteFile
    else:
        txtRemoteFile = txtRemoteFile
    r = requests.post("https://"+config.server,data=dict(url=txtRemoteFile))
    if r.status_code != 200:
        print(f"ERROR: Server returned response code {r.status_code}")
        cmdPause()
        main()
    print(r.text)
    cmdPause()
    main()

def cmdShortenUrl():
    clear()
    print("=========================================================================")
    print("    py0x0 | Shorten URL")
    print("=========================================================================")
    txtLongUrl = str(input("Enter full url to shorten: "))
    if txtLongUrl.find("http://" or "https://"):
        txtLongUrl = "https://"+txtLongUrl
    else:
        txtLongUrl = txtLongUrl
    r = requests.post("https://"+config.server,data=dict(shorten=txtLongUrl))
    if r.status_code != 200:
        print(f"ERROR: Server returned response code {r.status_code}")
        cmdPause()
        main()
    print(r.text)
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

def cmdCheckUpdates():
    clear()
    print("=========================================================================")
    print("    py0x0 | Check for Updates")
    print("=========================================================================")

    cmdPause()
    main()

main()
