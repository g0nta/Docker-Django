#!/bin/bash
service mysql start
mysql -uroot -e "CREATE USER [koukou]@ IDENTIFIED BY 'password'"
mysqladmin -u root password 'rootpass'