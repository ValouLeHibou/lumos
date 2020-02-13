# lumos
ECV Hackathon Project


RUN docker mysql image 

`docker run --name=my_mysql -v /home/valentin/Documents/git/lumos:/var/lib/mysql --env="MYSQL_ROOT_PASSWORD=root" -p 3306:3306 -d mysql`

RUN docker phpmyadmin image :

`sudo docker run --name myadmin -d --link my_mysql:db -p 8080:80 phpmyadmin/phpmyadmin`

RUN bash inside the container :

`docker exec -it user_mysql_1 mysql -u root -p root`

Une fois à l'intérieur création d'un user (% => donne les droits partout) :

```
$ CREATE USER 'valentin'@'%' IDENTIFIED BY 'root';
$ CREATE DATABASE user
$ GRANT ALL PRIVILEGES ON test_db.* to 'valentin'@'%';
```


