CREATE TABLE Category (
    id INT IDENTITY,
    label  VARCHAR(255) NOT NULL, 
    CONSTRAINT PK_Category_Id PRIMARY KEY (id)
)
INSERT INTO Category VALUES 
('Thriller'), ('Humour'), ('Science Fiction'), 
('Horror'), ('Fantasy'), ('Mystery'), ('Classic'), 
('Adventure')

CREATE TABLE Student (
    id INT IDENTITY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    CONSTRAINT PK_Student_Id PRIMARY KEY (id)
)
INSERT INTO Student VALUES 
    ('Emma', 'Johnson', 'emma.j@example.com'),
    ('Liam', 'Smith', 'liam.s@example.com'),
    ('Olivia', 'Williams', 'olivia.w@example.com'),
    ('Noah', 'Brown', 'noah.b@example.com'),
    ('Ava', 'Taylor', 'ava.t@example.com'),
    ('William', 'Jones', 'william.j@example.com'),
    ('Sophia', 'Davis', 'sophia.d@example.com'),
    ('James', 'Miller', 'james.m@example.com'),
    ('Isabella', 'Wilson', 'isabella.w@example.com'),
    ('Benjamin', 'Anderson', 'benjamin.a@example.com'),
    ('Mia', 'Thomas', 'mia.t@example.com'),
    ('Elijah', 'Jackson', 'elijah.j@example.com'),
    ('Charlotte', 'White', 'charlotte.w@example.com'),
    ('Henry', 'Harris', 'henry.h@example.com'),
    ('Amelia', 'Martin', 'amelia.m@example.com')

CREATE TABLE Book (
    id INT IDENTITY,
    category_id INT,
	title VARCHAR(255) NOT NULL, 
    author VARCHAR(255) NOT NULL,
    published_at DATE,
    CONSTRAINT PK_Book_Id PRIMARY KEY (id),
    CONSTRAINT FK_Category_Id FOREIGN KEY (category_id) REFERENCES Category(id)
)

INSERT INTO Book VALUES 
  (5, 'The Lord of the Rings', 'JRR Tolkien', '1954-07-29'),
  (8, 'The Lost World', 'Sir Arthur Conan Doyle', '1912-12-12'),
  (6, 'The Da Vinci Code', 'Dan Brown', '2003-03-18'),
  (5, 'Harry Potter and the Chamber of Secrets', 'JK Rowling', '1998-07-02'),
  (8, 'The Little Prince', 'Antoine de Saint-Exupéry', '1943-04-06'),
  (1, 'Gone Girl', 'Gillian Flynn', '2012-05-24'),
  (4, 'It', 'Stephen King', '1986-09-15'),
  (3, '1984', 'George Orwell', '1949-06-08'),
  (7, 'Moby Dick', 'Herman Melville', '1851-10-18'),
  (7, 'Frankenstein', 'Mary Shelley', '1818-01-01'),
  (8, 'The Three Musketeers', 'Alexandre Dumas', '1844-03-14'),
  (7, 'Madame Bovary','Gustave Flaubert', '1856-12-15'),
  (4, 'The Exorcist', 'William Peter Blatty', '1971-05-19'),
  (3, 'Foundation', 'Isaac Asimov', '1951-02-28'),
  (3, 'Dune', 'Frank Herbert', '1965-08-05')

CREATE TABLE StudentBookLoanHistory (
    id INT IDENTITY,
    student_id INT,
    book_id INT,
    borrowed_date DATE,
    returned_date DATE,
    CONSTRAINT PK_StudentBookLoanHistory_Id PRIMARY KEY (id),
    CONSTRAINT FK_Student_Id FOREIGN KEY (student_id) REFERENCES Student(id),
    CONSTRAINT FK_Book_Id FOREIGN KEY (book_id) REFERENCES Book(id)
)

INSERT INTO StudentBookLoanHistory VALUES 
  (15, 15, '2023-01-05', '2023-01-28'),
  (14, 10, '2023-01-05', '2023-01-19'),
  (13, 11, '2023-01-05', '2023-01-30'),
  (12, 13, '2023-01-06', '2023-02-02'),
  (1, 3, '2023-01-06', '2023-01-14'),
  (2, 9, '2023-01-06', '2023-02-12'),
  (3, 1, '2023-01-06', '2023-02-09'),
  (4, 4, '2023-01-06', '2023-02-20'),
  (5, 8, '2023-01-06', '2023-01-11'),
  (11, 5, '2023-01-06', '2023-01-23'),
  (10, 12, '2023-01-06', '2023-02-11'),
  (9, 14, '2023-01-06', '2023-02-12'),
  (8, 2, '2023-01-06', '2023-02-07'),
  (6, 7, '2023-01-07', '2023-02-27'),
  (7, 6, '2023-01-07', '2023-01-15'),
  (1, 6, '2023-03-06', '2023-03-19'),
  (2, 7, '2023-03-06', '2023-03-20'),
  (3, 9, '2023-03-06', '2023-03-21'),
  (4, 11, '2023-03-06', '2023-03-31'),
  (5, 13, '2023-03-06', '2023-03-29'),
  (6, 2, '2023-03-06', '2023-04-05'),
  (7, 1, '2023-03-06', '2023-03-16'),
  (8, 8, '2023-03-06', '2023-03-27'),
  (9, 12, '2023-03-06', '2023-04-01'),
  (10, 14, '2023-03-06', '2023-03-22'),
  (11, 1, '2023-03-06', '2023-04-08'),
  (12, 5, '2023-03-06', '2023-04-03'),
  (13, 10, '2023-03-06', '2023-04-07'),
  (14, 15, '2023-03-06', '2023-03-24'),
  (15, 4, '2023-03-06', '2023-03-18'),
  (1, 1, '2023-04-01', '2023-04-21'),
  (2, 2, '2023-04-02', '2023-04-22'),
  (3, 3, '2023-04-03', '2023-04-23'),
  (4, 4, '2023-04-04', '2023-04-24'),
  (5, 5, '2023-04-05', '2023-04-25'),
  (6, 6, '2023-04-06', '2023-04-26'),
  (7, 7, '2023-04-07', '2023-04-27'),
  (8, 15, '2023-04-08', '2023-04-28'),
  (9, 9, '2023-04-09', '2023-04-29'),
  (10, 10, '2023-04-10', '2023-04-30'),
  (11, 11, '2023-04-11', '2023-05-01'),
  (12, 12, '2023-04-01', '2023-05-02'),
  (13, 13, '2023-04-02', '2023-05-03'),
  (14, 8, '2023-04-03', '2023-05-04'),
  (15, 14, '2023-04-04', '2023-05-05'),
  (1, 12, '2023-06-03', '2023-06-30'),
  (2, 11, '2023-06-04', '2023-07-01'),
  (3, 10, '2023-06-05', '2023-07-02'),
  (4, 9, '2023-06-06', '2023-07-03'),
  (1, 11, '2023-08-09', '2023-08-31'),
  (1, 2, '2023-09-12', '2023-09-30'),
  (7, 3, '2023-08-09', '2023-08-30'),
  (7, 9, '2023-09-09', '2023-09-25'),
  (7, 15, '2023-10-10', '2023-10-05'),
  (12, 11, '2023-08-09', '2023-08-17'),
  (9, 8, '2023-08-09', '2023-08-19')


/* Question 1: */
select b.title, b.author, b.published_at from Book b
where year(b.published_at) > 1950
order by b.published_at DESC

/* Question 2: */
select b.author as 'Liste des auteurs' from Book b
where b.title like '%the%'

/* Reponse alternative pour titre en plus dans la 2*/
select b.author as 'Liste des auteurs', b.title from Book b
where b.title like '%the%'

/* Question 3: */
select count(*) as 'nb publié en juin et décembre'  from Book b
where month(published_at) in (6,12)

/* Question 4: */
select b.title from StudentBookLoanHistory sblh
JOIN Book b on b.id= sblh.book_id
JOIN Student s on s.id= sblh.student_id
where s.id=4

/* Reponse alternative pour éviter un doublon dans la 4*/
select DISTINCT b.title from StudentBookLoanHistory sblh
JOIN Book b on b.id= sblh.book_id
JOIN Student s on s.id= sblh.student_id
where s.id=4


/* Question 5: */
select c.label as 'label', count(b.id) as 'nb de livres' from StudentBookLoanHistory sblh
JOIN Book b on b.id= sblh.book_id
JOIN Category c on c.id= b.category_id
group by c.label
having count(b.id) >= 3