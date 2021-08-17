# Customer-Service-Support

## Backend part
Backend part is created with Django Framework version 2.2.6 and Python version 3.8.<br/><br/>
All packages are installed with pipenv packaging tool.<br/>
#### Packages:<br/>
- pipenv install django==2.2.6 
- pipenv install djangorestframework==3.10.3
- pipenv install django-cors-headers==3.1.1
- pipenv install coreapi==2.3.3
- pipenv install django-rest-swagger==2.2.0

### Admin page 
- http://127.0.0.1:8000/admin/ <br/>
On this page youcan navigate to customer service support administration. <br/>
1. Admin can add, change, delete or update data.
2. Data can be sorted by the date/time they got submitted as well as the preferred time from the customer.
3. Admin can comment and archive data. It is possible to see all data, archived or non-archived data. <br/> <br/>
![ScreenShot](https://github.com/uroscvetkovic/Customer-Service-Support/blob/docs-images/images/Admin.jpg) <br/>
```
If needed:
Username -> user
Password -> password
```

### Swagger-docs
- http://127.0.0.1:8000/swagger-docs/ <br/>
On this page can be seen all APIs endpoints. <br/>
All CRUD operations are implemented. <br/> <br/>
![ScreenShot](https://github.com/uroscvetkovic/Customer-Service-Support/blob/docs-images/images/swagger-docs.jpg)

## Frontend part

Frontend part is created with React js.

#### Dependencies:<br/>
- npm install axios
- npm install node-sass
- npm install react-datepicker --save

### Customer Service Support Form
![ScreenShot](https://github.com/uroscvetkovic/Customer-Service-Support/blob/docs-images/images/Form%20UI.jpg) <br/>
### Date time 
![ScreenShot](https://github.com/uroscvetkovic/Customer-Service-Support/blob/docs-images/images/Calendar%20UI.jpg) <br/>
All days are time limited from 8:00 to 20:00 (Saturday from  8:00 to 13:00 ). Client can not choose sunday.
### Feedback modal
![ScreenShot](https://github.com/uroscvetkovic/Customer-Service-Support/blob/docs-images/images/Success%20Modal.jpg) <br/>


