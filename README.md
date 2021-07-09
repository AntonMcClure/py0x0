# py0x0
An easy-to-use command-line interface for 0x0 "Null Pointer" pastebin services written in Python3.

**Note:** This tool is designed for UNIX/Linux. Windows users are strongly encouraged to use [ez0x0](https://antonmcclure.com/software/ez0x0/) instead. Ez0x0 is intended to provide an easier-to-use interface as compared to the command-line version.

## Installation (Release)
  1. Download from https://antonmcclure.com/software/py0x0/, and extract the downloaded .zip or .tar.gz file.
  2. Go to directory `cd py0x0`
  3. Copy `config.py.example` to `config.py`
  4. Open `config.py` with your preferred text editor and set the `server` value
  5. Install requirements with `python3 pip install --user -r requirements.txt`
  6. Run `./py0x0.py`

## Usage
Run `py0x0.py`

Select menu options 1-3 for 0x0 features, or 4-6 for informational materials.

Remote files may specify protocol, such as `https://`, `http://`, `ftp://`. Example: `https://antonmcclure.com`. If one isn't included, https will automatically be used.

## Plans

  - Simplify install process
  - Make it possible to set config from within the program

## Contributing
Contributions via pull requests and issues via it emails to <anton@antonmcclure.com> are welcomed! To learn how to send a git email, please see <https://git-send-email.io/>.

If your contribution is a security issue, please email me at <anton@antonmcclure.com> with a detailed description of the issue. **DO NOT DISCLOSE UNPATCHED SECURITY RISKS PUBLICLY**.

## Copyright & License

#### MIT License

Copyright (c) 2019-2021 Anton McClure &lt;<anton@antonmcclure.com>&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
