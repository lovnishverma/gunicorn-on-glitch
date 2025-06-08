**Gunicorn for a more production-like environment**

# Flask + Gunicorn App on Glitch

This is a simple Flask application that uses the Python `datetime` module and runs with Gunicorn for production-grade serving. It is designed to run smoothly on [Glitch.com](https://glitch.com).

---

## Features

- Minimal Flask app with basic routes.
- Returns current UTC time as JSON.
- Accepts POST requests to add days to current date.
- Runs with Gunicorn for better concurrency and robustness.
- Configured to run on Glitch platform without additional start scripts.

---

## Project Structure

```

.
├── server.py          # Flask application source code
├── requirements.txt   # Python dependencies
├── glitch.json        # Glitch platform configuration file
├── README.md          # This file

```

---

## server.py

- Contains Flask app.
- Binds to `0.0.0.0` and reads the port from the `PORT` environment variable (required by Glitch).
- Supports routes:
  - `/` — simple text response.
  - `/time` — returns current UTC time in ISO 8601 format.
  - `/add_days` — POST endpoint to add days to current date and return the result.

---

## requirements.txt

```

Flask==2.3.2
gunicorn==20.1.0

````

---

## glitch.json

This file instructs Glitch how to install dependencies and start your app:

```json
{
  "install": "pip3 install --user -r requirements.txt",
  "start": "gunicorn server:app --bind 0.0.0.0:$PORT",
  "watch": {
    "ignore": [
      "\\.pyc$"
    ],
    "install": {
      "include": [
        "^requirements\\.txt$"
      ]
    },
    "restart": {
      "include": [
        "\\.py$",
        "^start\\.sh"
      ]
    },
    "throttle": 1000
  }
}
````

---

## How to Run Locally

1. Install dependencies:

```bash
pip3 install -r requirements.txt
```

2. Run the app using Gunicorn:

```bash
gunicorn server:app --bind 0.0.0.0:3000
```

3. Visit `http://localhost:3000/` in your browser.

---

## How to Run on Glitch

1. Upload all files to your Glitch project.
2. Glitch will automatically install dependencies using `pip3` and run Gunicorn with the provided command.
3. Your app will be available at `https://your-project-name.glitch.me`.

---

## Example Requests

* **GET /**
  Returns a simple greeting text:

  ```
  hello gunicorn on glitch!
  ```

* **GET /time**
  Returns current UTC time:

  ```json
  {
    "current_utc_time": "2025-06-08T07:50:30.123456Z"
  }
  ```

* **POST /add\_days**
  Request:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"days": 5}' https://your-project-name.glitch.me/add_days
  ```

  Response:

  ```json
  {
    "future_date": "2025-06-13T07:50:30.123456Z",
    "days_added": 5
  }
  ```

---

## Gunicorn Logs Explanation

Your logs might look like this:

```
[2025-06-08 07:50:30 +0000] [1946] [INFO] Worker exiting (pid: 1946)
[2025-06-08 07:50:30 +0000] [1935] [INFO] Handling signal: term
[2025-06-08 07:50:30 +0000] [1935] [ERROR] Worker (pid:1946) was sent SIGTERM!
[2025-06-08 07:50:30 +0000] [1935] [INFO] Shutting down: Master
[2025-06-08 07:50:30 +0000] [1992] [INFO] Starting gunicorn 23.0.0
[2025-06-08 07:50:30 +0000] [1992] [INFO] Listening at: http://0.0.0.0:3000 (1992)
[2025-06-08 07:50:30 +0000] [1992] [INFO] Using worker: sync
[2025-06-08 07:50:30 +0000] [2003] [INFO] Booting worker with pid: 2003
```

* These indicate Gunicorn gracefully shutting down old workers and starting new ones.
* This is normal behavior during deployment or restarts.
* No error unless followed by crashes or inability to bind to the port.

---

## Troubleshooting

* Ensure your app binds to `0.0.0.0` and listens on the `PORT` environment variable.
* Check `requirements.txt` for necessary dependencies.
* Confirm `glitch.json` has the correct `start` command.
* Use Glitch logs to identify errors (`Logs` tab in your project).

---

## License

MIT License © Lovnish Verma

