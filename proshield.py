import os
import subprocess

class ProShield:
    def __init__(self):
        self.power_plans = self.get_power_plans()

    def get_power_plans(self):
        """Retrieve the list of available power plans."""
        try:
            output = subprocess.check_output(['powercfg', '-list'], shell=True).decode()
            return self.parse_power_plans(output)
        except subprocess.CalledProcessError as e:
            print(f"Error fetching power plans: {e.output}")
            return []

    def parse_power_plans(self, output):
        """Parse the output of powercfg -list to get power plan names and GUIDs."""
        plans = []
        for line in output.splitlines():
            if "GUID" in line:
                parts = line.split(':')
                plan_info = parts[1].strip().split('  ')
                guid = plan_info[0].strip()
                name = plan_info[1].strip()
                plans.append({'name': name, 'guid': guid})
        return plans

    def create_power_plan(self, name, based_on_guid):
        """Create a new power plan based on an existing one."""
        try:
            result = subprocess.run(['powercfg', '-duplicatescheme', based_on_guid, name], check=True, stdout=subprocess.PIPE)
            new_guid = result.stdout.decode().strip()
            print(f"Created a new power plan '{name}' with GUID {new_guid}")
            return new_guid
        except subprocess.CalledProcessError as e:
            print(f"Error creating power plan: {e}")
            return None

    def activate_power_plan(self, guid):
        """Activate a power plan using its GUID."""
        try:
            subprocess.run(['powercfg', '-setactive', guid], check=True)
            print(f"Activated power plan with GUID {guid}")
        except subprocess.CalledProcessError as e:
            print(f"Error activating power plan: {e}")

    def delete_power_plan(self, guid):
        """Delete a power plan using its GUID."""
        try:
            subprocess.run(['powercfg', '-delete', guid], check=True)
            print(f"Deleted power plan with GUID {guid}")
        except subprocess.CalledProcessError as e:
            print(f"Error deleting power plan: {e}")

    def display_power_plans(self):
        """Display all available power plans."""
        print("Available Power Plans:")
        for plan in self.power_plans:
            print(f"Name: {plan['name']}, GUID: {plan['guid']}")

if __name__ == "__main__":
    proshield = ProShield()
    proshield.display_power_plans()

    # Example usage:
    # new_plan_guid = proshield.create_power_plan("My Custom Plan", proshield.power_plans[0]['guid'])
    # proshield.activate_power_plan(new_plan_guid)
    # proshield.delete_power_plan(new_plan_guid)