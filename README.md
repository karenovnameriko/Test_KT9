Написанные тесты

Регистрация нового пользователя (test_register_user).
Цель: Проверить возможность регистрации нового пользователя.
Данные: username=testuser, password=testpass, email=testuser@example.com, name=Test User.
Ожидаемый результат: HTTP 200, в ответе есть access_token.


Регистрация существующего пользователя (test_register_existing_user).
Цель: Проверить, что повторная регистрация того же пользователя вызывает ошибку.
Данные: те же, что и выше.
Ожидаемый результат: HTTP 400, сообщение "User already exists".

Логин с неверным паролем (test_login_wrong_password)
Цель: Проверить обработку ошибки при неверном пароле.
Данные: username=testuser, password=wrongpass.
Ожидаемый результат: HTTP 401, сообщение "Invalid credentials".

<img width="1040" height="224" alt="Screenshot 2025-12-19 at 4 33 17 AM" src="https://github.com/user-attachments/assets/70b3fc0f-3760-4f65-8568-f6af1cf174e5" />

