# pyol
A simple python outlook script to schedule mails.
> Windows OS & outlook needed.

<p float="left">
  <img src="https://github.com/j3ygithub/pyol/blob/master/docs/images/screenshot1.png?" width="50%">
</p>

## Installation

Windows:

```
python -m venv C:\Users\jimmy_lin\envs\pyol
C:\Users\jimmy_lin\envs\pyol\Scripts\activate
git clone https://github.com/j3ygithub/pyol C:\Users\jimmy_lin\repos\pyol
pip install -r C:\Users\jimmy_lin\repos\pyol\requirements.txt
```

## Configure

Easily configure a mail job:

main.py
```
'''
...
def mail_job():
    """
    Customize your mail job here.
    Here comes an exmaple.
    Note that when you use this on a windows PC, 
    the format of attachments should be a list containing r-string like
    [r'path1', r'path2'].
    """
    send_mail(
        subject='hello',
        body='hello world',
        to='b00502013@gmail.com',
        cc='b00502013@gmail.com',
        attachments=[
            r'C:\Users\jimmy_lin\repos\pyol\pyol\testexcel.xlsx',
            r'C:\Users\jimmy_lin\repos\pyol\pyol\testword.docx',
        ]
    )
...
'''
```

Run it:

```
python C:\Users\jimmy_lin\repos\pyol\pyol\main.py
```

## Meta

Jimmy Lin <b00502013@gmail.com>

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/j3ygithub/](https://github.com/j3ygithub/)

## Contributing

1. Fork it (<https://github.com/j3ygithub/rj3y/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request




