<h1 align="center"><b>English language</b></h1>
<h1>Calculator using the PyQt5 library</h1>
<p>PyQt5 is a set of Python libraries for creating a graphical interface based on the Qt5 platform from Digia.</p>
<p>To run, you need to install the PyQt5 and sys library.</p>
<h1>Realization</h1>
<ol>
  <li>Creating a Calculator class and methods for it</li>
  <li>We create a vertical (main) axis using the Qhboxlayout() function and already bind the horizontal alignment axes to it using the addLayout() function.</li>
  <li>Linking widgets (1, 2, ..., 0, +, -, *, /, ., C) to the axes using the addWidget() function.</li>
  <li>We create events responsible for reactions to button clicks using the connect() function, to which we pass the lambda function.</li>
  <li>Creating the _button(self, param) method responsible for entering numbers into the text input line.</li>
  <li>Creating the _operation(self, op) method, which is responsible for processing the pressing of the mathematical operation button.</li>
  <li>Creating the _result(self) method, which is responsible for processing clicking on the result button. In the same method, we process the error of dividing a number by 0.</li>
</ol>

<h1 align="center"><b>Русский язык</b></h1>
<h1>Калькулятор с использованием библиотеки PyQt5</h1>
<p>PyQt5 - это набор Python библиотек для создания графического интерфейса на базе платформы Qt5 от компании Digia.</p>
<p>Для запуска необходимо установить библиотеку PyQt5 и sys.</p>
<h1>Реализация</h1>
<ol>
  <li>Создаем класс Calculator и методы для него</li>
  <li>Создаем вертикальную (главную) ось с помощью функции QBBoxLayout() и уже к ней привязываем горизонтальные оси выравнивания с помощью функции addLayout().</li>
  <li>Привязываем виджеты (1, 2, ..., 0, +, -, *, /, ., С) к осям с помощью функции addWidget().</li>
  <li>Создаем события, отвечающие за реакции на нажатия по кнопкам с помощью функции connect(), в которую передаем lambda-функцию.</li>
  <li>Создаем метод _button(self, param), отвечающий за ввод цифр в линию ввода текста.</li>
  <li>Создаем метод _operation(self, op), отвечающий за обработку нажатия на кнопку математической операции.</li>
  <li>Создаем метод _result(self), отвечающий за обработку нажатия на кнопку результата. В этом же методе обрабатываем ошибку деления числа на 0.</li>
