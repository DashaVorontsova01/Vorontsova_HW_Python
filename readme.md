# Тестирование процесса покупки в интернет-магазине

Проект автоматизированного тестирования для проверки полного цикла покупки на сайте демо-магазина SauceDemo.

## Структура проекта

```
project/
├── pages/                    # Классы Page Object
│   ├── __init__.py
│   ├── login_page.py        # Страница авторизации
│   ├── inventory_page.py    # Страница товаров
│   ├── cart_page.py         # Страница корзины
│   └── checkout_page.py     # Страница оформления заказа
├── tests/                   # Тестовые файлы
│   └── test_shop_purchase.py
├── requirements.txt         # Зависимости проекта
├── README.md               # Документация
└── allure-results/         # Результаты Allure (создается при запуске)
```

## Предварительные требования

1. **Python 3.8+**
2. **Браузер Firefox** (установлен по умолчанию)
3. **Geckodriver** (автоматически управляется Selenium)

## Установка зависимостей

```bash
# Установка всех необходимых пакетов
pip install -r requirements.txt

# Или установка вручную
pip install selenium==4.15.0
pip install allure-pytest==2.13.2
pip install pytest==7.4.3
```

## Запуск тестов

### 1. Запуск тестов с генерацией Allure отчетов

```bash
# Запуск теста с сохранением результатов для Allure
python -m pytest tests/test_shop_purchase.py -v --alluredir=allure-results
```

### 2. Параллельный запуск тестов (если будет несколько тестов)

```bash
# Запуск с использованием нескольких ядер процессора
python -m pytest tests/ -v --alluredir=allure-results -n 2
```

### 3. Запуск конкретного теста

```bash
# Запуск только одного тестового метода
python -m pytest tests/test_shop_purchase.py::TestShopPurchase::test_shop_purchase_total -v --alluredir=allure-results
```

## Просмотр отчетов Allure

### Способ 1: Генерация статического отчета

```bash
# Установите Allure командной строки (требуется Java 8+)
# Инструкция по установке: https://docs.qameta.io/allure/

# Генерация HTML отчета
allure generate allure-results -o allure-report --clean

# Открытие отчета в браузере
allure open allure-report
```

### Способ 2: Запуск сервера Allure

```bash
# Запуск сервера Allure для просмотра отчетов
allure serve allure-results
```

### Способ 3: Просмотр без установки Allure CLI

Если Allure CLI не установлен, можно использовать Python сервер:

```bash
# Установите дополнительный пакет
pip install allure-python-commons

# Запуск тестов с немедленным открытием отчета
python -m pytest tests/test_shop_purchase.py -v --alluredir=allure-results --allure-link-pattern=issue:https://example.com/issue/{}
```

## Структура отчета Allure

Отчет Allure содержит:
- **Dashboard**: Общая статистика выполнения тестов
- **Behaviors**: Группировка тестов по функциональности
- **Graphs**: Графики и диаграммы выполнения
- **Timeline**: Временная шкала выполнения тестов
- **Suites**: Дерево тестовых наборов

## Тестовые данные

- **URL**: https://www.saucedemo.com/
- **Пользователь**: standard_user
- **Пароль**: secret_sauce
- **Ожидаемая сумма**: $58.29

## Ключевые особенности проекта

1. **Page Object Pattern**: Каждая страница инкапсулирована в отдельный класс
2. **Allure Integration**: Подробные отчеты с шагами и скриншотами
3. **Типизация**: Полная аннотация типов для всех методов
4. **Следование PEP8**: Код соответствует стандартам Python
5. **Логирование**: Детальное логирование всех действий

## Расширение проекта

### Добавление новых тестов

1. Создайте новый метод в классе `TestShopPurchase`
2. Используйте декораторы Allure для разметки
3. Добавьте соответствующие методы в Page Object классы при необходимости

### Добавление скриншотов

```python
import allure
from selenium.webdriver.common.by import By

@allure.step("Сделать скриншот")
def take_screenshot(driver, name="screenshot"):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
```

## Устранение неполадок

### Проблема: Не находится элемент на странице
**Решение**: Увеличьте время неявного ожидания в `setUp()` методе

### Проблема: Allure отчет не генерируется
**Решение**: Убедитесь, что директория `allure-results` создается после запуска тестов

### Проблема: Ошибка с Geckodriver
**Решение**: Убедитесь, что Firefox установлен и актуальная версия Selenium

## Контакты

Для вопросов и предложений по проекту обращайтесь к команде разработки.

---
*Проект создан для демонстрации лучших практик автоматизации тестирования*