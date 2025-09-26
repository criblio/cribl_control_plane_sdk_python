# cribl-control-plane Examples

This directory contains example scripts that demonstrate how to use the cribl_control_plane SDK.

## Prerequisites

- Python 3.9 or higher
- pip

## Setup

1. **Set up virtual environment:**
   ```bash
   python3 -m venv examples-env
   source examples-env/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure credentials in `.env`:**
   ```bash
   CLIENT_ID="your-client-id"
   CLIENT_SECRET="your-client-secret"
   WORKSPACE_NAME="your-workspace-name"
   ORG_ID="your-org-id"
   ```

3. **Run an example:**
   ```bash
   python example_worker_group_replication.py
   ```


## Configuration

Each example can be configured by either:
1. Using a `.env` file (recommended for examples that support both cloud and on-prem)
2. Editing the configuration variables directly in the example files (for simple examples)

### Environment Variables

For cloud deployments:
- `DEPLOYMENT_ENV=cloud` (or omit for cloud as default)
- `ORG_ID` - Your organization ID
- `CLIENT_ID` - Your OAuth2 client ID
- `CLIENT_SECRET` - Your OAuth2 client secret
- `WORKSPACE_NAME` - Your workspace name

For on-prem deployments:
- `DEPLOYMENT_ENV=onprem`
- `ONPREM_SERVER_URL` - Your on-prem server URL
- `ONPREM_USERNAME` - Your username
- `ONPREM_PASSWORD` - Your password
