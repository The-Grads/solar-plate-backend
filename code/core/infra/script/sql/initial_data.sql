INSERT INTO public.users
("name", email, "password", id, created_at)
VALUES('User Test', 'test@test.com', '$2b$12$M48uE/l9UdUkA5wsTG1ma.PejP.dLnFmsIOUMNUR/whdBmumkYmya', '70201000-3fa7-4b62-b514-217142fb392a', now());

INSERT INTO public.company
("name", id, created_at)
VALUES('Company Test', '2b7211c7-59d2-4029-a725-906caab00272', now());
