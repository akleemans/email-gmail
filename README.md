# email-gmail

Send an email with gmail.

As mentioned in the source, this will only work with a gmail address not using two-factor authentication and the activated option "less secure apps" which you can change here: https://www.google.com/settings/security/lesssecureapps

You could copy and modify the methods provided, or just simply use it like this:
```python
import gmail
gmail.send_email('from-email@gmail.com', 'password', 'to-email@gmail.com', 'Example subject', 'Example message')
```
  
