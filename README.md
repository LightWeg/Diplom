# Diplom
Работа с базой данных

Задание 1

Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

    SELECT c.login, COUNT(o.id) 
        FROM "Orders" AS o 
    INNER JOIN  "Couriers" AS c ON o."courierId" = c.id 
        WHERE o."inDelivery" = true 
    GROUP by c.login;
    
<img width="580" height="90" alt="изображение" src="https://github.com/user-attachments/assets/155cd7fa-f125-4f5c-872e-0218b1bf0059" />



Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:

Если поле finished == true, то вывести статус 2.

Если поле canсelled == true, то вывести статус -1.

Если поле inDelivery == true, то вывести статус 1.

Для остальных случаев вывести 0.

    SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
        END AS status
        FROM "Orders";
![2задание sql](https://github.com/user-attachments/assets/1121ffa0-79aa-40c2-be21-6c8c79313718)

Автоматизация теста к API
Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:

    Клиент создает заказ.
    Проверяется, что по треку заказа можно получить данные о заказе.
![автотест](https://github.com/user-attachments/assets/11991f5f-fa34-4c1b-ae75-31f951821a9c)
