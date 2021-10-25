# Spinnaker Banner Updater

Some quick scripts for disabling triggers and adding banners to Spinnaker applications and pipelines.

## Auth

Supports x509 auth

## Use

`python3 update-banner.py` or `python3 disable-triggers.py`

## Config

Create a file named `config.py` in the root like this:

```python
filter = "keyword-or-app-name"
host="https://spinnaker-gate-address.com"
verify="/path/to/certs/bundle_ca.pem"
cert="/path/to/certs/auth.pem"
banners = [
    {
        "backgroundColor": "var(--color-warning-light)", 
        "text": "Hello i am new banner!"
        "textColor": "var(--color-text-primary)", 
        "enabled": True
    } 
]
```