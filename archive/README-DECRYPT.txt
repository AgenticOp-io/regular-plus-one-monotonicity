Encrypted archive of Cursor agent chats for regular-plus-one-monotonicity.
Created: 2026-09-22T19:32:25.4714225-06:00

Decrypt:
  openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -in chat-archive.tar.gz.enc -out chat-archive.tar.gz
  tar -xzf chat-archive.tar.gz
