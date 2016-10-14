[![Build Status](https://travis-ci.org/oceanhouse21/instant-lawyer.svg?branch=master)](https://travis-ci.org/oceanhouse21/instant-lawyer)
# instant-lawyer

This is a simple REST web service providing API to send whatsapp messages

It is based on the great **Yowsup** library provided by tgalal [https://github.com/tgalal/yowsup].

##APIs
<br>
These are the provided APIs:

####/iluser/u_uid [GET]
```
Retrieve information related to a instant-lawyer user
--------------------------------------------------

example:

curl -u inderpal74:12345678 http://46.101.213.142/iluser/891e51de206c4597be2e16f6869c32dc

returns:

{
  "api_version": "0.2.2",
  "u_created_at": "Wed, 30 Apr 2014 08:11:10 GMT",
  "u_email": "inderpal6785@gmail.com",
  "u_name": "inderpal6785",
  "u_uid": "891e51de206c4597be2e16f6869c32dc",
  "wu_avail_mex_day": 100,
  "wu_cc": "39",
  "wu_max_mex_day": 100,
  "wu_passwd": "A/qgXnDiss+0kb1pqOFc07mKJrt=",
  "wu_phone_number": "1234567890"
}
```

<br>
####/iluser [POST]

```
Register a instant-lawyer user
---------------------------
Note this is the only API which does not require BASIC authentication. Please don't abuse it

example:

curl -H "Content-type: application/json" -X POST  -d '{"u_name": "inderpal6785", "u_passwd": "12345678","u_email": "inderpal6785@gmail.com","wu_cc": "39","wu_phone_number": "1234567890","wu_passwd": "A/qgXnDiss+0kb1pqOFc07mKJrt="}'  http://46.101.213.142/iluser

returns:

{
  "username": "inderpal6785",
  "uuid": "891e51de206c4597be2e16f6869c32dc"
}

Please note that wu_passwd can be empty if you first need to register a phone to Whatsapp service.
```

<br>
####/iluser/u_uid [PUT]
```
Update a instant lawyer user
---------------------------

example:

curl -u inderpal6785:12345678 -H "Content-type: application/json" -X PUT -d '{"u_passwd": "12345678","u_email": "inderpal6785@gmail.com","wu_cc": "39","wu_phone_number": "0987654321","wu_passwd": "khfkwhfioweffhenckjwsdcihj="}'  http://46.101.213.142/iluser/891e51de206c4597be2e16f6869c32dc

returns:

{
  "api_version": "0.2.2",
  "u_created_at": "Wed, 30 Apr 2014 08:11:10 GMT",
  "u_email": "inderpal6785@gmail.com",
  "u_name": "inderpal6785",
  "u_uid": "891e51de206c4597be2e16f6869c32dc",
  "wu_avail_mex_day": 100,
  "wu_cc": "39",
  "wu_max_mex_day": 100,
  "wu_passwd": "khfkwhfioweffhenckjwsdcihj=",
  "wu_phone_number": "0987654321"
}
```

<br>
####/iluser/u_uid [DELETE]
```
Delete a instant lawyer user
---------------------------

example:

curl -u inderpal6785:12345678 -X DELETE http://46.101.213.142/iluser/891e51de206c4597be2e16f6869c32dc

returns:

{
  "891e51de206c4597be2e16f6869c32dc": "deleted"
}
```

<br>
####/requestcode [GET]
```
Request a Whatsapp SMS code
---------------------------

example:

curl  -u inderpal6785:12345678 http://46.101.213.142/requestcode/891e51de206c4597be2e16f6869c32dc

returns:

{
  "result": "status: ok\nkind: free\npw: aN7owet4z5WMSTFK+mOFi+Pq4tU=\nprice: \u20ac 0,89\nprice_expiration: 1401905090\ncurrency: EUR\ncost: 0.89\nlogin: 393316835779\ntype: existing\nexpiration: 1427206874"
}

Please note that this will instruct Whatsapp server to send a SMS message to the registered phone number which is useful for true registration.

```

<br>
####/registercode [POST]
```
Register the Whatsapp user (phone numner) by providing the SMS code
-------------------------------------------------------------------

example:

curl  -u inderpal6785:12345678 -H "Content-type: application/json" -X POST  -d '{"u_uid": "891e51de206c4597be2e16f6869c32dc", "sms_code": "857-401"}' http://46.101.213.142/registercode

returns:

{
  "result": "status: ok\nkind: free\npw: u6kgSp2cwDmw0z1kewB9iG1C+fM=\nprice: \u20ac 0,89\nprice_expiration: 1401892268\ncurrency: EUR\ncost: 0.89\nexpiration: 1427206874\nlogin: 390123456789\ntype: existing"
}

This call also return the Whatsapp password (u6kgSp2cwDmw0z1kewB9iG1C+fM=) which should be part of the iluser object (update)
```

<br>
####/ilmex [POST]
```
Send a Whatsapp message to a given number
-----------------------------------------

example:

curl  -u inderpal6785:12345678 -H "Content-type: application/json"   -X POST  -d '{"u_uid": "891e51de206c4597be2e16f6869c32dc", "dst_phone": "3901234987654","body_mex": "this is a test message"}' http://46.101.213.142/ilmex

returns:

{
  "mex_status": "sent",
  "remaining_mex_for_today": 97
}
```
