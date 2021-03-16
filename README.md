# py0x0
An easy-to-use command-line interface for 0x0 "Null Pointer" pastebin services written in Python3.

## Installation (Release)
  1. Download from https://www.antonmcclure.com/py0x0/, and extract the downloaded .zip or .tar.gz file.
  2. Go to directory `cd py0x0`
  3. Copy `config.py.example` to `config.py`
  4. Open `config.py` with your preferred text editor and set the `server` value
  5. Install requirements with `python3 pip install --user -r requirements.txt`
  6. Run `./py0x0.py`

## Usage
Run `py0x0.py`

Select menu options 1-3 for 0x0 features, or 4-6 for informational materials.

Remote files may specify protocol, such as `https://`, `http://`, `ftp://`. Example: `https://www.antonmcclure.com`. If one isn't included, https will automatically be used.

## Plans

  - Simplify install process
  - Make it possible to set config from within the program

## Contributing
Contributions via pull requests and issues via either [GitHub](https://github.com/AntonMcClure/py0x0), or git emails to <anton@antonmcclure.com> are welcomed! If your suggestion is a major change, please create an issue and describe your changes in detail before making them.

**Git emails are preferred over pull requests.** To learn how to send a git email, please see <https://git-send-email.io/>.

If your contribution is a security issue, please email me at <anton@antonmcclure.com> with a detailed description of the issue. **DO NOT DISCLOSE UNPATCHED SECURITY RISKS PUBLICLY**.

## Copyright & License
    Copyright (C) 2019-2021, Anton McClure <anton@antonmcclure.com>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
