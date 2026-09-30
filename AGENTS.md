This repository is a disposable executor-control verification fixture.

Rules:

- Only perform the explicitly requested task.
- Do not access secrets or credentials.
- Do not install dependencies unless explicitly instructed.
- Do not modify files unless explicitly allowed.
- Do not create or publish branches, commits, or pull requests unless explicitly instructed.
- Do not interact with external services unless explicitly instructed.
- Stop when the requested task is complete.

Verification command:

python3 -m unittest discover -s tests -v
