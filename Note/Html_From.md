# Html Form

from: https://www.codingfactory.net/11576

- What Form dose

  1. "Form" is a TAG to transfer data to a server

- How to do?

  ```
  <form method="xxx" action="yyy">
  ...
  </form>
  ```

  method: the way to transfer data. put "get" or "post"
  action: the adress transfer data.

  1. Using GET method

  ```
  <html>
  ...
  <body>
    <form method="get" action="from-action.php">
      <p><label>Input Color : <input type="text" name="color"></label></p>
      <p><input type="submit" value="Submit"></p>
    </form>
  </body>
  </html>
  ```

  When you use get the data will be url as queries

  2. Using POST method

  ```
  <html>
  ...
  <body>
    <form method="post" action="from-action.php">
      <p><label>Input Color : <input type="text" name="color"></label></p>
      <p><input type="submit" value="Submit"></p>
    </form>
  </body>
  </html>
  ```
