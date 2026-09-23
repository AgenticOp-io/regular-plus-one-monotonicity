# Chat archive

`chat-history.md` is the research conversation for this repository (Quanta graph sandwich through the Chernoff-chain notes), restored from the encrypted transcript. Tool calls are omitted.

`chat-archive.tar.gz.enc` is the original AES-256-CBC (PBKDF2, 200000 iterations) archive of the Cursor agent transcript.

## Decrypt

```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 \
  -in chat-archive.tar.gz.enc -out chat-archive.tar.gz
tar -xzf chat-archive.tar.gz
```

Password is not stored in this repository.
