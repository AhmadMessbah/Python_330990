create database patient_db;

--

create table patient_db.persons
(
    p_id         int primary key auto_increment,
    name       varchar(30),
    family     varchar(30),
    birth_date date,
    username   varchar(30),
    password   varchar(20)
);

--
