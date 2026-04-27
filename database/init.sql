CREATE TABLE IF NOT EXISTS members (
    id        SERIAL PRIMARY KEY,
    nombre    VARCHAR(100) NOT NULL,
    apellido  VARCHAR(100) NOT NULL,
    legajo    VARCHAR(20)  NOT NULL,
    feature   VARCHAR(100) NOT NULL,
    servicio  VARCHAR(100) NOT NULL,
    estado    VARCHAR(20)  DEFAULT NULL
);

INSERT INTO members (nombre, apellido, legajo, feature, servicio) VALUES
    ('Fermin', 'Etchanchu Paoltroni', '30446', 'Feature 01 — Coordinación e Infraestructura', 'compose / repo'),
    ('Bautista', 'Flores', '32223', 'Feature 02 — Frontend', 'frontend:8080'),
    ('Nahuel', 'Iroz', '27019', 'Feature 03 — Backend', 'backend:5000'),
    ('Fermin', 'Etchanchu Paoltroni', '30446', 'Feature 04 — Base de datos', 'db'),
    ('Bautista', 'Flores', '32223', 'Feature 05 — Panel Portainer', 'portainer:9000');
