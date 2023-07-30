INSERT INTO public.company
("name", id, created_at)
VALUES('Company Test', '2b7211c7-59d2-4029-a725-906caab00272', now());

INSERT INTO public.users
("name", email, "password", id, "company_id", created_at)
VALUES('User Test', 'test@test.com', '$2b$12$M48uE/l9UdUkA5wsTG1ma.PejP.dLnFmsIOUMNUR/whdBmumkYmya', '70201000-3fa7-4b62-b514-217142fb392a', '2b7211c7-59d2-4029-a725-906caab00272', now());

INSERT INTO public.solar_plate
("name", user_id, id, created_at)
VALUES('Plate 1', '70201000-3fa7-4b62-b514-217142fb392a', 'b616183e-584a-41fa-9355-9f8b57003275', now());

INSERT INTO public.power_data
(power_delivery, solar_plate_id, id, event_date, created_at)
VALUES(10.5, 'b616183e-584a-41fa-9355-9f8b57003275', '6b282041-2976-4efe-aaf1-7b144270a487', '2023-07-20T14:12:37.723919', now());

INSERT INTO public.power_data
(power_delivery, solar_plate_id, id, event_date, created_at)
VALUES(5, 'b616183e-584a-41fa-9355-9f8b57003275', '38578e2d-50af-4b19-97d8-e371023418f6', '2023-07-20T15:12:37.723919', now());

INSERT INTO public.power_data
(power_delivery, solar_plate_id, id, event_date, created_at)
VALUES(9, 'b616183e-584a-41fa-9355-9f8b57003275', '718febe3-dd22-4713-96c9-3872d53224aa', '2023-07-20T16:12:37.723919', now());