# Realistic Login Timing Lab

A controlled Flask laboratory that behaves like a normal website login.

Important:
- Use only for your own authorized testing.
- `LAB_PASSWORD` is a lab secret, never a real account password.
- The login response intentionally contains no `elapsed_ms`, debug field, or timing information.
- The server has a deliberately vulnerable character-by-character comparison so timing behavior can be studied in a controlled environment.

## Deploy on Render

Create a GitHub repository, upload these files, then create a Render Web Service.

Environment variables:
- `LAB_USERNAME` = `labuser`
- `LAB_PASSWORD` = choose a lab-only password
- `LAB_DELAY` = `0.030`

Build:
`pip install -r requirements.txt`

Start:
`gunicorn app:app`

The public-facing login is `/`.
The form submits normally to `/login`.
`/health` is only a basic service health endpoint.
