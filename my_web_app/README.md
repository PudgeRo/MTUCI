<h1 align="center"><b>English language</b></h1>
<h1>Login and registration on the website using the database</h1>
To work, you need to install the necessary dependencies from the file req.txt to the virtual environment with the command "pip3 install -r req.txt " (without buckets) for Windows.
<h2>File system</h2>
<li>app.py - the main file to start</li>
<li>req.txt - a text file with the necessary modules for operation</li>
<li>templates -> registartion.html - file with page data for registration in the database</li>
<li>templates -> login.html - the file with the page data for logging into the created account</li>
<li>templates -> account.html - a file with the data of the page that is displayed after entering the desired login and password</li>
<h2>Database</h2>
<p>Name: service_db.</p>
The database consists of three columns: user name, user login, user password.
<h2>Realization</h2>
<ol>
  <li>In the file "app.py " connecting to the database "service_db".</li>
  <li>In the login() function, select the fields with the login and password from the table to access the page (account.html) with exception handling when entering an incorrect username or password.</li>
  <li>In the registration() function, we fill in the "service_db" database by entering a new username, username and password. We handle exceptions when either a username, login, or password is not entered, or when the password is shorter than four characters. After successful registration, we display a message about successful registration ("You have successfully registered") and redirect you to the login and password entry page (login.html).</li>
</ol> 

<h1 align="center"><b>Русский язык</b></h1>
<h1>Логин и регистрация на сайте с использованием базы данных</h1>
Для работы необходимо установить нужные зависимости из файла req.txt в виртуальную среду командой "pip3 install -r req.txt" (без ковычек) для Windows.
<h2>Файловая система</h2>
<li>app.py - основной файл для старта</li>
<li>req.txt - текстовый файл с необходимыми модулями для работы</li>
<li>templates -> registartion.html - файл с данными страницы для регистрации в базе данных</li>
<li>templates -> login.html - файл с данными страницы для захода в созданный аккаунт</li>
<li>templates -> account.html - файл с данными страницы, которая отображается после введение нужного логина и пароля</li>
<h2>База данных</h2>
<p>Название: service_db.</p>
База данных состоит из трех столбцов: имени пользователя, логина пользователя, пароля пользователя.
<h2>Реализация</h2>
<ol>
  <li>В файле "app.py" подключаемся к базе данных "service_db".</li>
  <li>В функции login() выбираем из таблицы поля с логином и паролем для захода на страницу (account.html) с обработкой исключений при вводе неверного логина или пароля.</li>
  <li>В функции registation() заполняем базу данных "service_db" путем ввода нового имени пользователя, логина и пароля. Обрабатываем искючения, когда не введено либо имя      пользователя, либо логин, либо пароль или когда пароль короче чем четыре символа. После успешной регистрации выводим на экран сообщение о успешной регистрации ("You have successfully registered") и перенаправляем на страницу ввода логина и пароля (login.html).</li>
</ol> 
