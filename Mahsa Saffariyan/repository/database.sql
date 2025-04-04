CREATE DATABASE appointment_system;

--

CREATE TABLE appointment_system.customers
(
    customer_id   INT PRIMARY KEY AUTO_INCREMENT,
    first_name    VARCHAR(50),
    family_name   VARCHAR(50),
    gender        ENUM('Male', 'Female'),
    phone         VARCHAR(15) UNIQUE,
    birth_date    DATE
);

--

CREATE TABLE appointment_system.timings
(
    schedule_id   INT PRIMARY KEY AUTO_INCREMENT,
    date          DATE NOT NULL,
    start_time    TIME NOT NULL,
    end_time      TIME NOT NULL,
    status        ENUM('available', 'booked') NOT NULL,
    doctor_name   VARCHAR(100) NOT NULL
);

--

CREATE TABLE appointment_system.visits
(
    visit_id      INT PRIMARY KEY AUTO_INCREMENT,
    reason        VARCHAR(255),
    fee           DECIMAL(10, 2) DEFAULT 0,
    visit_status  ENUM('Pending', 'Completed', 'Cancelled') NOT NULL,

    customer_id   INT,
    FOREIGN KEY (customer_id) REFERENCES appointment_system.customers(customer_id),

    schedule_id   INT,
    FOREIGN KEY (schedule_id) REFERENCES appointment_system.timings(schedule_id)
);

--

CREATE VIEW VISIT_REPORT AS
SELECT * FROM visits
JOIN customers ON customers.customer_id = visits.customer_id
JOIN timings ON timings.schedule_id = visits.schedule_id;
