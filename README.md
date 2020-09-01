# pyol
A simple python outlook script to schedule mails.
> Windows OS & outlook needed.

<p float="left">
  <img src="https://github.com/j3ygithub/pyol/blob/master/docs/images/screenshot1.png?" width="70%">
</p>

## Installation

Windows:

```
python -m venv C:\Users\jimmy_lin\envs\pyol
C:\Users\jimmy_lin\envs\pyol\Scripts\activate
git clone https://github.com/j3ygithub/pyol C:\Users\jimmy_lin\repos\pyol
pip install -r C:\Users\jimmy_lin\repos\pyol\requirements.txt
```

## Configuration

pyol is easy to configure, like this:

```
[main.py]
...
def mail_job():
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
    
schedule.every(5).seconds.do(mail_job)
...
```
See pyol/main.py for more details.


## Run

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




