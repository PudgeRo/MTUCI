
<h1 align="center"><b>Русский язык</b></h1>
<h1 align="center">UI (User Interface) с базой данных (расписание)</h1>

Приложение умеет показывать, изменять, удалять расписание.

<h1>Начало работы</h1>
<p>Для старта необходимо создать виртуальную среду и установить в нее необходимые библиотеки: psycopg2, PyQt5.</p>
<p>Запуск происходит через консоль путем ввода команды "py main.py" (без ковычек), находясь в нужной дериктории в виртуальной среде.</p>
<h1>База данных</h1>
<p>База данных должна находится локально на вашем компьютере</p>
<p>База данных должна состоять из базы данных timetable и схемы timetable, в которой должны быть таблицы timetable, teacher, subject</p>
<p>Таблица timetable состоит из:</p>
<li>id</li>
<li>day</li>
<li>subject</li>
<li>room_numb</li>
<li>start_time</li>
<p>Таблица teacher состоит из:</p>
<li>id</li>
<li>full_name</li>
<li>subject</li>
<p>Таблица subject состоит из:</p>
<li>name</li>
<h1>Структура</h1>
<p>Функция week() определяет четность недели (1 - нечетная, 0 - четная).</p>
<p>В функции _update_table() используется цифра 2 для обозначение обоих недель одновременно. </p>
<p>В функции _connect_to_db() подключаемся к уже созданной базе данных.</p>

<h1 align="center"><b>English language</b></h1>
<h1 align="center">UI (User Interface) with database (schedule)</h1>

The application is able to show, change, delete the schedule.

<h1>Getting started</h1>
<p>To start, you need to create a virtual environment and install the necessary libraries into it: psycopg2, PyQt5.</p>
<p>The launch takes place via the console by entering the command "py main.py " (without quotes), being in the right directory in a virtual environment.</p>
<h1>Database</h1>
<p>The database must be located locally on your computer</p>
<p>The database should consist of a timetable database and a timetable schema, which should contain the tables timetable, teacher, subject</p>
<p>The timetable table consists of:</p>
<li>id</li>
<li>day</li>
<li>subject</li>
<li>room_numb</li>
<li>start_time</li>
<p>The teacher table consists of:</p>
<li>id</li>
<li>full_name</li>
<li>subject</li>
<p>The subject table consists of:</p>
<li>name</li>
<h1>Structure</h1>
<p>The week() function determines the parity of the week (1 - odd, 0 - even).</p>
<p>The _update_table() function uses the digit 2 to indicate both weeks at the same time.</p>
<p>In the _connect_to_db() function, we connect to an already created database.</p>
