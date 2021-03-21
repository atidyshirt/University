## Terminal One

Run Mysql through an ssh port

```bash
ssh jpy19@linux.cosc.canterbury.ac.nz -L 3308:db2.csse.canterbury.ac.nz:3306 -N
```

## .env Example

This is an example .env for the above port forwarded `ssh` dbms route

```bash
HOST=localhost
PORT=1234
LOCALUSER=jpy19
PASSWORD=87433186
DATABASE=jpy19_s365_lab2
```

## Basic Javascript connection to db

```Javascript
const mysql = require("mysql2");
require("dotenv").config({ path: "../.env" });
const connection = mysql.createConnection({
  // pulled from .env
  host: process.env.HOST,
  port: process.env.PORT,
  user: process.env.LOCALUSER, // note don't use USER and it pulls from $USER (global var on mac)
  password: process.env.PASSWORD,
  database: process.env.DATABASE,
});
connection.connect((err) => {
  if (err) throw err;
  console.log("Connected!");
});

```
