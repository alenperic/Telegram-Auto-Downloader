# Telegram-Auto-Downloader

## Description
This Python script automates the downloading of new data (files, images, videos, etc.) posted to a specific Telegram group. It uses the Telethon library to interact with Telegram's API. Additionally, it sends a notification via Pushover API whenever a file is downloaded.

## Features
- Monitors a specified Telegram group for new files.
- Downloads new files to a predefined location.
- Sends a Pushover notification upon successful download.

## Installation

Before running the script, install the required packages:

```bash
pip install telethon requests
```

## Configuration

1. **Telegram API Credentials**: Obtain your `api_id` and `api_hash` from [Telegram's developer portal](https://my.telegram.org).

2. **Pushover Credentials**: Obtain your `pushover_user_key` and `pushover_api_token` from [Pushover's website](https://pushover.net).

3. **Download Location**: Specify the path where you want the downloaded files to be saved in the script.

## Usage

Update the script with your credentials and desired download location. Run the script using:

```bash
python TeleMonitor.py
```

## Important Notes

- Ensure you have the necessary permissions to access and download content from the Telegram group.
- Respect user privacy and comply with Telegram's terms of service.
- Using the script to download copyrighted or sensitive content without permission may violate legal and ethical standards.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under [MIT License](LICENSE).

## Contact

For any queries or assistance, feel free to open an issue in this repository.

---

**Disclaimer**: This script is for educational purposes only. The author is not responsible for any misuse or violation of Telegram's terms of service.
```

### Instructions for Use:
- Replace placeholders (like `python TeleMonitor.py`) with actual details relevant to your project.
- Ensure that the licensing information (`MIT License` in this case) matches your project's license.
- Add or remove sections as necessary for your project's scope and features.
