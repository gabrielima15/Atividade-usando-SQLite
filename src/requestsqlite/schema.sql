CREATE TABLE IF NOT EXISTS tb_instituicao_ensino (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    no_entidade TEXT NOT NULL,
    co_entidade INTEGER NOT NULL,
    no_uf TEXT NOT NULL,
    sg_uf TEXT NOT NULL,
    co_uf INTEGER NOT NULL,
    no_municipio TEXT NOT NULL,
    co_municipio INTEGER NOT NULL,
    nu_ano_censo INTEGER NOT NULL,
    qt_mat_bas INTEGER DEFAULT 0,
    qt_mat_inf INTEGER DEFAULT 0,
    qt_mat_fund INTEGER DEFAULT 0,
    qt_mat_med INTEGER DEFAULT 0,
    qt_mat_prof INTEGER DEFAULT 0,
    qt_mat_eja INTEGER DEFAULT 0,
    qt_mat_esp INTEGER DEFAULT 0,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tb_usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);