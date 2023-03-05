
 
# HHW_27 Django 

## Установка
Создать виртуальное окружение.
Установить зависимости

```sh
poetry update
```
Выполнить миграции.
```sh
./manage.py makemigrations
./manage.py migrate 
```

Загрузить тестовые данные в базу
```sh
 python ./manage.py loaddata data/categories.json
 python ./manage.py loaddata data/ads.json

```

Запустить сервер
```sh
./manage.py runserver  
```


### Шаг 1

Установите Django.

Создайте app `ads` и в нем вьюшку для обращения к корневому домену  `/`.

Верните из вьюшки:

```python
200 {"status": "ok"}
```

### Шаг 2

Вам предоставлена [база данных в CSV](https://github.com/skypro-008/lesson27_project_source).

Используя хитрость и смекалку, перегоните ее в JSON.

### Шаг 3

Создайте модели на основе предоставленных вам данных. 

- Подсказка
    
     Это объявления и категории.
    

Накатите миграции.

Используя модели, наполните базу данных из предоставленной вам CSV.

### Шаг 4

Реализуйте для `/cat` метод GET.
Реализуйте для `/ad` метод GET.

```json
Request
GET /cat/

Response
200
[
	{
		"id": 1,
		"name": "Автотовары"
	},
	...
]

Request
GET /ad/

Response
200
[
	{
		"id": 1,
		"name": "Толстовка",
		"author": "Мария",
		"price": 500,
	},
	...
] 

```

Реализуйте для `/cat/:id` метод GET.
Реализуйте для `/ad/:id` метод GET.

```json
Request
GET /cat/1/

Response
200
{
	"id": 1,
	"name": "Автотовары"
}

404

Request
GET /ad/1/

Response
200
{
	"id": 1,
	"name": "Толстовка",
	"author": "Мария",
	"price": 500,
	"description": "Продаю новую кофту на рост 110 см, по всем вопросам пишите", 
	"address": "Москва, ул. Борисовские Пруды, 16к2",
	"is_published": true
}

404

```

### Шаг 5

Реализуйте для `/cat` метод POST.
Реализуйте для `/ad` метод POST.

```json
Request
POST /cat/
{
	"name": "Кухня"
}

Response
200
{
	"id": 2,
	"name": "Кухня"
}

Request
POST /ad/
{
	"name": "Гель для душа",
	"author": "Настя",
	"price": 0,
	"description": "Отдам даром, не подошел", 
	"address": "Москва, метро Коломенская",
	"is_published": false
}

Response
200
{
	"id": 2,
	"name": "Гель для душа",
	"author": "Настя",
	"price": 0,
	"description": "Отдам даром, не подошел", 
	"address": "Москва, метро Коломенская",
	"is_published": false
}
```

**Критерии выполнения:**

- [ ]  Корневой роут отдает верные данные.
- [ ]  В моделях есть все поля из CSV.
- [ ]  Для view на корневой роут используется подход FBV.
- [ ]  Для всех остальных view используется подход CBV и GenericView.
- [ ]  Типы данных в JSON отдаются корректно.
- [ ]  Методы POST работают.
- [ ]  Возврат ошибки 404 происходит через встроенные возможности DetailView.