# Lightning Articles
Final project for ECE 382V Blockchain and Smart Contracts

Our website allows users to post articles, and for readers to pay Sat's to read those articles. We are using LN Bits to setup a paywall. To setup our website we used a Python packaged know an as Django and SQL Lite to store our data. Data including articles and user information.

## How to setup & use demo
01. Install Python 3
02. Download the repo
03. Change directory to `bc-fall22/nyt`
04. `python3 manage.py runserver`
05. Go to local host `localhost:8000`
06. Click on `publish`
07. Then you'll be prompted to sign-up, create an account
08. Click on `publish` again
09. Create an artcile
10. The article will be behind a paywall. You can open cash app to pay for the Ligtning invoice in the QR code.
11. Refresh page and you should see article.

## Helpful Links
01. Django [https://docs.djangoproject.com/en/4.1/]
02. LN Bits [https://legend.lnbits.co/]

## Other

Run
```
python3 manage.py runserver
```

LN Bits Paywall:

https://legend.lnbits.com/paywall/?usr=14ad60b5f0eb40cca1e63d1660db57f9
