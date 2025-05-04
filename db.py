from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = 'mysql+pymysql://root:password@192.168.32.1:3306/BlogApp'

engine = create_engine(URL_DATABASE)

SessionLocale = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# To give access from MYSQL to connect between MYSQL WINDOWS and Code on WSL

# U need to paste this code in WSL to find the ip from conetion : ip route show | grep -i default | awk '{ print $3}'

# Then U need to enter in MYSQL and create a user root and grant access refering to that ip like : CREATE USER 'root'@'192.168.42.5' IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.42.5' WITH GRANT OPTION;
# FLUSH PRIVILEGES;
