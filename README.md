# Онлайн-магазин мебели (Python/Django)
### Описание проекта:
**1) Стурктура состоит из следующих приложений:**
* authapp (Приложение для работы с пользователями: регистрация, авторизация, обновление);
* basketapp (Приложение для работы с корзиной: добавление товара в корзину, удаление, редактирование). В данном приложении также используется AJAX для редактирования корзины;
* mainapp (Приложения для работы с товарами и категориями, создан контекстный процессор для категорий товаров);
* adminapp (Собственная админка - поддерживает CRUD для пользователей, категорий и товаров. Все контроллеры реализованы через CBV. Также в данном приложении созданы mixins для дополнения базового функционала CBV. На страницах добавлена пагинация.)

**2) Frontend проекта:**
В данном проекте используется bootstrap и собственные стили. Во всех шаблонах динамика - backend получает даныне из БД (в своем проекте использую SQLite).

**3) Дополнительный функционал:**
* Реализация отправки электронной почты. Активация пользователя по e-mail.
* Авторизация пользователя через социальную сеть "ВКонтаке".
