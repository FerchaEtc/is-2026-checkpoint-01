CREATE TABLE IF NOT EXISTS members (
    id        SERIAL PRIMARY KEY,
    nombre    VARCHAR(100) NOT NULL,
    apellido  VARCHAR(100) NOT NULL,
    legajo    VARCHAR(20)  NOT NULL UNIQUE,
    feature   VARCHAR(100) NOT NULL,
    servicio  VARCHAR(100) NOT NULL,
    estado    VARCHAR(20)  NOT NULL DEFAULT 'unknown'
);

-- El campo estado es un placeholde, el backend lo sobreescribe en ejecución.

INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) VALUES
    ('Fermin', 'Etchanchu Paoltroni', '30446', 'Feature 01 — Coordinación e Infraestructura', 'compose / repo',  'unknown'),
    ('Bautista', 'Flores', '32223', 'Feature 02 — Frontend', 'frontend :8080', 'unknown'),
    ('Nahuel', 'Iroz', '27019', 'Feature 03 — Backend', 'backend :5000', 'unknown'),
    ('Fermin', 'Etchanchu Paoltroni', '30446', 'Feature 04 — Base de datos', 'db (interno)', 'unknown'),
    ('Bautista', 'Flores', '32223', 'Feature 05 — Panel Portainer', 'portainer :9000', 'unknown'),
    ('Nahuel', 'Iroz', '27019', 'Feature 06 — Panel pgAdmin', 'pgadmin :5050', 'unknown');
