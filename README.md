# ProShield

## Overview

ProShield is a Python program designed to manage power settings and create custom power plans based on usage for Windows systems. With ProShield, users can list available power plans, create new power plans, activate a specific power plan, and delete unwanted power plans.

## Features

- **List Available Power Plans:** View all power plans currently available on your Windows system.
- **Create Custom Power Plans:** Duplicate existing power plans to create new ones based on your needs.
- **Activate Power Plans:** Switch between different power plans by activating them using their GUID.
- **Delete Power Plans:** Remove power plans that are no longer needed.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Ensure Python is installed on your system.
2. Clone this repository or download the `proshield.py` file.

## Usage

1. Open a command prompt or terminal.
2. Navigate to the directory containing `proshield.py`.
3. Run the script using Python:

   ```bash
   python proshield.py
   ```

4. Follow the prompts to manage power plans.

## Example

To create a new power plan:

```python
proshield.create_power_plan("My Custom Plan", proshield.power_plans[0]['guid'])
```

To activate a power plan:

```python
proshield.activate_power_plan(new_plan_guid)
```

To delete a power plan:

```python
proshield.delete_power_plan(new_plan_guid)
```

## Notes

- Ensure you have the necessary permissions to modify power plans on your system.
- This program is intended for use on Windows platforms only.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.