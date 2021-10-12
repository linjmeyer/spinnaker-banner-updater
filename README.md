# Spinnaker Banner Updater

A quick script for rotating banners on Spinnaker applications in bulk using Python

## Auth

Supports x509 auth

## Use

`python3 update-banner.py`

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