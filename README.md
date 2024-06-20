# Malicious IP List

> This is a CSV list of malicious IPs that have performed
> unsolicited scans against production applications.

<a href="https://www.abuseipdb.com/user/155510" title="AbuseIPDB is an IP address blacklist for webmasters and sysadmins to report IP addresses engaging in abusive behavior on their networks">
	<img src="https://www.abuseipdb.com/contributor/155510.svg" alt="AbuseIPDB Contributor Badge" style="width: 401px; background-color: white;">
</a>

## Installation

### Clone the repo, create venv and install requirements

```bash
git clone https://github.com/ashleykleynhans/ipset.git
cd ipset
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Configure API AbuseIPDB API key and your timezone

1. Copy the `.env.example file to .env`
```bash
cp .env.example .env
```
2. Edit the .env file and configure your
   [AbuseIPDB API Key](https://www.abuseipdb.com/account/api)
   and timezone.
3. Save the file.

## Create IP Set JSON

```bash
python3 create_ip_set_json.py
```

This will output JSON in the following format:

```json
[
    "64.176.194.36/32",
    "104.234.204.32/32",
    "104.207.139.139/32",
    "54.206.45.15/32",
    "138.199.18.131/32",
    "20.127.152.198/32"
]
```

## Check an IP in AbuseIPDB

> [!NOTE]
> Obviously change the IP address below to the IP address
> that you actually want to check.

```bash
python3 check_abuse_ipdb.py --ip-address 64.176.194.36
```

## Report a malicious IP to AbuseIPDB

> [!NOTE]
> This is just an example, you should obviously change the IP
> address to the one that you actually want to report.  You
> can get a list of category ids [here](https://www.abuseipdb.com/categories),
> and set the reason to the reason why you are reporting the
> malicious IP.

```bash
python3 report_to_abuse_ipdb.py \
    --ip-address 64.176.194.36 \
    --categories 19,21 \
    --reason "Malicious Behaviour/Probing for vulnerabilities/Brute force attempts"
```

## Community and Contributing

Pull requests and issues on [GitHub](https://github.com/ashleykleynhans/ipset)
are welcome. Bug fixes and new features are encouraged.

## Appreciate my work?

<a href="https://www.buymeacoffee.com/ashleyk" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
