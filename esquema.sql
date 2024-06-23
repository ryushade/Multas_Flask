CREATE TABLE Vehiculos (
    Placa VARCHAR(10) PRIMARY KEY,
    Modelo VARCHAR(255),
    Serie VARCHAR(255)
);

CREATE TABLE Multas (
    Codigo VARCHAR(10) PRIMARY KEY,
    Descripcion TEXT,
    Gravedad VARCHAR(50),
    Precio DECIMAL,
    MedidaPreventiva TEXT
);

CREATE TABLE RegistroMultas (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Placa VARCHAR(10),
    CodigoMulta VARCHAR(10),
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Placa) REFERENCES Vehiculos(Placa),
    FOREIGN KEY (CodigoMulta) REFERENCES Multas(Codigo)
);
