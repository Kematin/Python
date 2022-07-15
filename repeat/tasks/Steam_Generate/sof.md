<h1 style="text-align: center">Steam account generate</h1>

<h3>Для чего нужен проект?</h3>

Steam account generate - программа для автоматического создания аккаунтов стим для будущей
перепродажи. Для создания из инструментов используется только `Python`.

<h3>Этапы создания аккаунта стим</h3>
<ol>
    <li>Создание почты rambler</li>
    <li>Создание аккаунта steam</li>
    <li>Добавить никнейм, аватарку, подтвердить почту</li>
    <li>Покупка номера на сервисе 5sim (3р)</li>
    <li>Привязать аккаунт к sda и профилю стим, записать код восстановления sda</li>
    <li>Продажа аккаунта на сервисе: funpay/lolzsteam</li>
</ol>

После каждого этапа кроме `3` идет автоматическая `запись в файл`.


<h3>Библиотеки для проекта</h3>
<ul>
    <li>Datetime - время и дата создания аккаунта</li>
    <li>Csv - запись данных в файл</li>
    <li>Selenium - создание аккаунтов</li>
    <li>Time (sleep) - задержка перед повторениями</li>
</ul>

<h3>Сервисы для проекта</h3>
<ul>
    <li><a href="https://store.steampowered.com/">Steam</a></li>
    <li><a href="https://www.rambler.ru/">Rambler</a></li>
    <li><a href="https://5sim.net/">5Sim</a></li>
    <li><a href="https://lolz.guru/market">Lolz market</a></li>
    <li><a href="https://funpay.com/">Funpay</a></li>
</ul>


<h2 style="text-align: center">Примеры записи данных в файлы</h2>
<h4>Для txt файлов:</h4>
<p style="color: grey">P.S. звездочек при записе данных не будет.</p>

> Data/emails.txt
```txt
data: *time---day---month*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
email: *email*
email password: *password*
secret word: *word*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

> Data/logins.txt
```txt
data: *time---day---month*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
login: *login*
password: *password*
email: *email*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

> Data/phones.txt
```txt
data: *time---day---month*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
login: *login*
phone: *0123456789*
SDA recovery code: *R12345*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

<h4>Для csv файла:</h4>

> Data/data.csv

<table>
    <thead>
        <tr>
            <th>Data</th>
            <th>Login</th>
            <th>Password</th>
            <th>Email</th>
            <th>Email password</th>
            <th>Secret word</th>
            <th>Phone</th>
            <th>SDA</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>time--day--month</td>
            <td>*login*</td>
            <td>*password*</td>
            <td>*email*</td>
            <td>*email password*</td>
            <td>*email secret word*<td>
            <td>*0123456789*</td>
            <td>*R12345*</td>
        </tr>
    </tbody>
</table>
