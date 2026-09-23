# Encrypted chat archive

`chat-archive.tar.gz.enc` is an AES-256-CBC (PBKDF2, 200000 iterations) archive of Cursor agent transcripts for this project.

## Decrypt

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 \
  -in chat-archive.tar.gz.enc -out chat-archive.tar.gz
tar -xzf chat-archive.tar.gz
```

Password is not stored in this repository.
