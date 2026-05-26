# Syncing Files From Training Server

For larger training runs, we typically would use a dedicated remote training server to run.

This short document notes down a way to easily synchronize training checkpoints from the server down to local workspace.

To do this, we will use this VSCode extension:

{% embed url="<https://github.com/Natizyskunk/vscode-sftp>" %}

After download, create a `sftp.json` configuration under the `.vscode/` directory and add these configurations:

```json
{
    "name": "Your Remote Training Server",
    "host": "server.ip.address",
    "port": 22,
    "protocol": "sftp",
    "context": "./logs",
    "remotePath": "/PATH/TO/THE/WORKSPACE/logs",
    "username": "YOUR-USERNAME",
    "ignore": [],
    "uploadOnSave": false,
    "useTempFile": false,
    "openSsh": false,
    "privateKeyPath": "~/.ssh/id_ed25519"
}

```

\
Now, you can run "> SFTP: Sync Remote -> Local" command to fetch all the training logs and checkpoints.


---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://berkeley-humanoid-lite.gitbook.io/docs/in-depth-contents/syncing-files-from-training-server.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
