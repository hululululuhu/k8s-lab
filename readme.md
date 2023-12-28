before run it, need install docker and minikube.

1. create mysql container
   ```bash
   ./deployment/deploy-mysql.sh
   ```
2. into slave
   ```bash
   kubectl exec -it <pod-name> -- mysql -uroot -p
   ```
   ```sql
   CHANGE MASTER TO
   MASTER_HOST='mysql-master',
   MASTER_USER='root',
   MASTER_PASSWORD='your-password',
   MASTER_LOG_FILE='mysql-bin.000003',
   MASTER_LOG_POS=4;
    ```
   ```sql
   start slave;
   ```
3. create application container
   ```bash
   ./deployment/deploy-app.sh
   ```
4. magic
   ```sql
   CREATE TABLE test.users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL,
       email VARCHAR(100) NOT NULL,
       birthdate DATE,
       is_active BOOLEAN DEFAULT TRUE
   );
   ```
   
   ```sql
   INSERT INTO test.users (username, email, birthdate, is_active)
   VALUES
       ('test1', 'test1@runoob.com', '1985-07-10', true),
       ('test2', 'test2@runoob.com', '1988-11-25', false),
       ('test3', 'test3@runoob.com', '1993-05-03', true);
   ```


echo "dckr_pat_K_QVoCbLkYecg8uYv-OGD_VcWYU" | docker login --username magiwu --password-stdin
