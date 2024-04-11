# MAC_Guardian

The "MAC Address Protection" program, MAC_Guardian, provides a robust mechanism to ensure that a specific project or program is executed only on designated computers with predetermined MAC addresses. This enhances security and control over the distribution of the project by restricting its execution to authorized systems.

## Description

The script comprises two classes: `Mac_Guardian` and `Authentic`.

- `Mac_Guardian`: This class retrieves MAC addresses of network interfaces, hashes them using SHA-256, and stores the hashed value into a file named `db`.
- `Authentic`: This class reads the stored hashed MAC address from the `db` file, retrieves MAC addresses of network interfaces again, and checks if any of them match the stored value.

## Requirements

- Python 3.x
- `netifaces` library

## Usage

1. Clone the repository.
2. **MAC Address Registration**: Run the following command to register the MAC address:

    ```sh
    python main.py
    ```

    Follow the on-screen instructions to select a MAC address, which will be hashed and stored in the `db` file.

3. **Select Interface**: The output of `main.py` will display available network interfaces and their MAC addresses. Select the appropriate interface and note the corresponding index.

4. **Output of `main.py`**: This step generates the `db` file containing the hashed MAC address.

5. **Copy `db` File**: Copy the `db` file to your preferred location. The execution of `main.py` is no longer needed for MAC authentication.

6. **MAC Authentication**: Call the `Authentic` constructor in your code, ensuring that the `db` file is in the same location as your code.

    ```python
    authenticator = Authentic()
    ```

By following these steps, you can ensure that your project or program is executed only on authorized systems with designated MAC addresses, thereby enhancing security and control over its distribution.
