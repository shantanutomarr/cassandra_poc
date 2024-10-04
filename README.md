# Prerequisites
- Install the latest version of Java 8 or Java 11, either the Oracle Java Standard Edition 8 / Oracle Java Standard Edition 11 (Long Term Support) or OpenJDK 8 / OpenJDK 11. To verify that you have the correct version of java installed, type `java -version`.
- For using `cqlsh`, the latest version of *Python 3.6+* or *Python 2.7 (support deprecated)*. To verify that you have the correct version of Python installed, type `python --version`.

# Install the Debian packages
- Add the repository for version cassandra {41_version} (41x):
  
  ```
  echo "deb [signed-by=/etc/apt/keyrings/apache-cassandra.asc] https://debian.cassandra.apache.org 41x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
  ```

- Add the Apache Cassandra repository keys to the list of trusted keys on the server:
  
  ```
  curl -o /etc/apt/keyrings/apache-cassandra.asc https://downloads.apache.org/cassandra/KEYS
  ```

  ```
  sudo apt-get update
  ```

- Install Cassandra with APT:

  ```
  sudo apt-get install cassandra
  ```

- Start Cassandra service:
  
  ```
  sudo systemctl start cassandra
  ```

  ```
  sudo systemctl enable cassandra
  ```

- Check the status of Cassandra:

  ```
  sudo nodetool status
  ```

# Install the Python packages

- Install Python and pip

  ```
  sudo apt install python3 python3-pip python3-venv -y
  ```

- Create Virtual Environemnt:

  ```
  python3 -m venv path/to/env/folder
  source path/to/env/folder/bin/activate
  ```
  
- Install requirements:
  
  ```
  pip install -r requirements.txt
  ```

# Steps needed to configure new project

- Start a new Django project

  ```
  django-admin startproject myproject
  cd myproject
  ```

- Create a new app

  ```
  python manage.py startapp myapp
  ```

- Modify `myproject/settings.py` to configure Cassandra as the database:

  ```py
  # settings.py
  
  DATABASES = {
      'default': {
          'ENGINE': 'django_cassandra_engine',
          'NAME': 'mykeyspace',  # Replace with your keyspace
          'HOST': '127.0.0.1',
          'OPTIONS': {
              'replication': {
                  'strategy_class': 'SimpleStrategy',
                  'replication_factor': 1
              },
              'connection': {
                  'consistency': 1,
                  'retry_connect': True,
                  'lazy_connect': True
              }
          }
      }
  }

  # Add 'myapp' to INSTALLED_APPS
  INSTALLED_APPS = [
      # Other installed apps
      'django_cassandra_engine',
      'myapp',
  ]
  ```

- Create the Cassandra Keyspace:

  ```
  sudo cqlsh
  ```
  ```
  CREATE KEYSPACE mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
  ```

- Performing Migrations:
  
  Since Cassandra doesn’t have Django migrations, you don’t need to run the usual migration commands.Run the following command instead:

  ```
  python manage.py sync_cassandra
  ```

  
