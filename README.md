# Итоговый проект на курсе Skillfactory

## Проект "Доска объявлений"

Необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений.
Пользователи ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации.
После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент.
Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём.
Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям,
удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление).
Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.
Также предусмотреть возможность отправлять пользователям новостные рассылки. 
___

Проект реализован с использованием фреймворка **Django**

___

Регистрация пользователя реализована с помощью стандартного механизма регистрации **Django**
Пользователь вводит Username, e-mail и пароль, после регистрации приходит письмо с одноразовым кодом на почту для завершения регистрации.

```
accounts/signup/
```

 ***Список всех объявлений по адресу:***
 
```
announcements/
```
Объявления на этой странице доступны всем пользователям.

 ***Просмотр информации отдельного объявления по адресу:***
 
```
announcements/{id}/
```

 ***Создание объявления по адресу:***
 
```
announcements/create/
```
Создание объявления доступно только зарегистрированным пользователям.
При создании объявления всем пользователям на почту приходит письмо с ссылкой на новое объявление.

 ***Редактирование объявления по адресу:***
 
```
announcements/{id}/update/
```
Редактирование объявления доступно только автору.

***Список объявлений из определенной категории по адресу:***
 
```
announcements/category/{id}/
```
Отображаются объявления с фильтрацией по категории

***Список объявлений, созданных пользователем по адресу:***
 
```
announcements/own/
```
Отображаются объявления с фильтрацией по id пользователя
______
***Список откликов на объявления пользователя по адресу:***
 
```
announcements/responds_list/
```
Отображаются отклики на объявления с фильтрацией по id пользователя. Страница доступна только зарегистрированным пользователям.
При отправке отклика, пользователю, создавшему объявление, приходит письмо на почту с ссылкой на отклик.
Пользователь может принять или отклонить отклик. В случае принятия, пользователю, оставившему отклик также приходит письмо с уведомлением.
______

Добавление различного контента в объявление реализовано с помощью пакета **CKEditor**.
