CRUD with Python using Django and MySQL

This project aims to implement a simple system for managing personal records, such as clients, friends, or any other group of individuals who may benefit from this database. Using Django for the web application and MySQL as the database, the system allows users to perform full CRUD operations: Create, Read, Update, and Delete records.

Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/amandazve/pythonCRUD.git

2. Navigate to the project directory:
cd pythonCRUD

3. Install the dependencies:
pip install -r requirements.txt

4. Create migrations 
python manage.py makemigrations
python manage.py migrate

5. After installation, run the project:
python manage.py runserver 


Features
Add people: The system allows users to create records with First Name, Last Name, and Contact Details.

Read: Users can view the information of the people stored in the database.

Update: Users can edit the existing records easily.

Delete: Records can be removed as needed.


Technologies Used
Python: Most of the project was developed in Python, a language I've been specializing in due to its dynamic nature, reusable code, widespread usage, and an active community that I enjoy following.

HTML: For this project, HTML was used to structure and organize the content. I appreciate how straightforward it is to work with—it’s the backbone of web development. Its simplicity, combined with the ability to create well-organized and semantic layouts, makes it a great foundation for any web project. Plus, it's universally supported, making it easy to integrate with other technologies and ensuring broad compatibility. I also had the help of the Bootstrap framework website, which made styling and responsive design a lot quicker and more efficient.

Javascript: I implemented an interactive functionality with the user, requesting a double confirmation for data deletion. I believe it’s crucial to ensure the user has a second chance to review their action when it comes to removing data from the database, minimizing the risk of unintended deletions.

Django: A Python web framework that makes web development faster and more efficient. One thing that impressed me about Django is its relatively simple and interesting infrastructure. It makes handling backend tasks like routing, database management, and templating seamless and straightforward. The migrations and Django ORM simplify data manipulation and allow you to avoid writing SQL manually in many cases.

MySQL: A widely-used open-source relational database system, chosen for its performance, cross-platform compatibility, and broad support across multiple programming languages. I selected MySQL not only because of its popularity but also due to my interest in learning more about it. While I didn't directly use SQL queries (thanks to Django ORM), I found it valuable to see how the database operates and integrates seamlessly into the project.

What I Learned
Throughout the development of this project, I gained practical experience integrating Django with a MySQL database. Setting up the database in Django was easier than I expected, and using the Django ORM made interacting with the database feel natural and less error-prone.
Another key takeaway was how Django simplifies the creation of admin interfaces. By using just a few commands, I was able to implement a graphical interface to manage the data stored in the database, which saved a lot of time.

On the MySQL side, I gained a good understanding of how to work with relational databases in a production environment, which complements the skills I developed using Django. Even though I didn’t dive deep into SQL, I gained an appreciation for MySQL’s role in powering web applications.
Overall, this project helped solidify my understanding of database management and web frameworks, and it provided hands-on experience with two powerful tools for building web applications.



