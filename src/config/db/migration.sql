SELECT table_name FROM user_tables;

select * from AREA;
select * from CULTURA;
select * from PLANTIO;
select * from IRRIGACAO;
select * from FEEDBACK;

DROP TABLE FEEDBACK;
DROP TABLE IRRIGACAO;
DROP TABLE PLANTIO;
DROP TABLE CULTURA;
DROP TABLE AREA;

CREATE TABLE area (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    localizacao VARCHAR2(200) NOT NULL,
    hectar NUMBER(10,2)
);

INSERT INTO area (nome, localizacao, hectar) VALUES ('Fazenda São João', 'Zona Rural - MG', 25.50);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Sítio Verde Vale', 'Interior de SP', 12.30);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Chácara Bela Vista', 'Sul de GO', 8.00);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Fazenda Sol Nascente', 'Norte de MT', 32.75);
INSERT INTO area (nome, localizacao, hectar) VALUES ('Sítio Santa Clara', 'Oeste da BA', 15.10);

CREATE TABLE cultura (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    consumo_hidrico_diario_l_m2 NUMBER(6,2)
);

INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Milho', 5.20);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Soja', 4.80);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Cana-de-açúcar', 6.50);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Feijão', 3.90);
INSERT INTO cultura (nome, consumo_hidrico_diario_l_m2) VALUES ('Algodão', 5.75);

CREATE TABLE plantio (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR2(100) NOT NULL,
    observacao VARCHAR2(100) NOT NULL,
    area_id NUMBER NOT NULL,
    cultura_id NUMBER NOT NULL,
    data_plantio DATE NOT NULL,
    CONSTRAINT fk_area_id FOREIGN KEY (area_id) REFERENCES area(id) ON DELETE CASCADE,
    CONSTRAINT fk_cultura_id FOREIGN KEY (cultura_id) REFERENCES cultura(id) ON DELETE CASCADE
);

INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 1', 'Início da safra', 1, 1, DATE '2024-11-01');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 2', 'Boa germinação', 2, 2, DATE '2024-11-05');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 3', 'Chuva leve', 3, 3, DATE '2024-11-10');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 4', 'Aplicado fertilizante', 4, 4, DATE '2024-11-12');
INSERT INTO plantio (nome, observacao, area_id, cultura_id, data_plantio) VALUES ('Plantio 5', 'Replantio parcial', 5, 5, DATE '2024-11-15');

CREATE TABLE irrigacao (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    plantio_id NUMBER NOT NULL,
    data_irrigacao DATE NOT NULL,
    volume_agua_l NUMBER(10,2),
    CONSTRAINT fk_plantio_id FOREIGN KEY (plantio_id) REFERENCES plantio(id) ON DELETE CASCADE
);

INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (1, DATE '2024-11-02', 1250000);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (1, DATE '2024-11-03', 1500000);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (2, DATE '2024-11-06', 509400);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (3, DATE '2024-11-11', 533000);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (4, DATE '2024-11-13', 1375000);
INSERT INTO irrigacao (plantio_id, data_irrigacao, volume_agua_l) VALUES (5, DATE '2024-11-16', 1176000);

CREATE TABLE feedback (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cultura_id NUMBER NOT NULL,
    message_feedback VARCHAR2(400) NOT NULL,
    tips VARCHAR2(400) NOT NULL,
    percent NUMBER NOT NULL,
    CONSTRAINT fk_feedback_cultura_id FOREIGN KEY (cultura_id) REFERENCES cultura(id) ON DELETE CASCADE
);

INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Irrigação no ponto ideal.', 'Continue monitorando as condições do solo e clima.', 0.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Leve déficit hídrico (-4.5%).', 'Aumente um pouco o volume irrigado nos próximos dias.', -4.5);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Déficit moderado detectado (-9.3%).', 'Revise o cronograma de irrigação semanal.', -9.3);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Irrigação abaixo do necessário (-14.7%).', 'Aplique reforço imediato para evitar estresse hídrico.', -14.7);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Crítico: Irrigação muito baixa (-22.1%).', 'Risco à produção. Urgente rever manejo hídrico.', -22.1);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Leve excesso de irrigação (+3.8%).', 'Reduza discretamente o tempo de irrigação.', 3.8);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Excesso moderado detectado (+8.5%).', 'Ajuste o sistema de irrigação para evitar desperdício.', 8.5);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Volume irrigado acima do ideal (+13.4%).', 'Monitore a drenagem e a umidade do solo.', 13.4);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (1, 'Crítico: Excesso elevado de água (+19.9%).', 'Reduza imediatamente a frequência de irrigação.', 19.9);

INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Irrigação dentro dos parâmetros ideais.', 'Continue com a gestão atual de irrigação.', 0.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Leve falta de irrigação (-3.9%).', 'Ajuste levemente o volume aplicado por ciclo.', -3.9);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Déficit hídrico moderado (-8.6%).', 'Considere irrigar com maior frequência.', -8.6);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Baixa irrigação detectada (-13.2%).', 'Avalie a distribuição da água na área.', -13.2);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Crítico: irrigação deficiente (-20.4%).', 'Aumente a irrigação e revise o manejo.', -20.4);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Leve excesso detectado (+4.1%).', 'Reduza o tempo de irrigação em dias úmidos.', 4.1);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Excesso moderado de água (+9.2%).', 'Monitore sinais de saturação no solo.', 9.2);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Irrigação acima do necessário (+12.7%).', 'Faça ajustes finos nos bicos de irrigação.', 12.7);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (2, 'Crítico: Excesso de irrigação (+18.6%).', 'Evite encharcamento e revise o cronograma.', 18.6);

INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Volume irrigado ideal.', 'Continue observando os padrões climáticos locais.', 0.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Pequeno déficit de água (-4.7%).', 'Reforce a irrigação nos próximos ciclos.', -4.7);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Déficit moderado (-10.1%).', 'Verifique o funcionamento dos aspersores.', -10.1);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Volume abaixo do esperado (-15.0%).', 'Adicione irrigação suplementar em horários críticos.', -15.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Crítico: déficit de irrigação (-21.8%).', 'Urgente reforço hídrico na lavoura.', -21.8);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Leve excesso de irrigação detectado (+3.5%).', 'Ajuste os horários de irrigação automática.', 3.5);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Excesso moderado registrado (+8.0%).', 'Evite aplicar em dias consecutivos.', 8.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Volume superior ao necessário (+14.5%).', 'Reduza o tempo de irrigação por setor.', 14.5);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (3, 'Alerta: excesso elevado de irrigação (+20.3%).', 'Pode causar lixiviação de nutrientes. Corrigir urgente.', 20.3);

INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Irrigação equilibrada.', 'Manter práticas de irrigação atuais.', 0.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Leve deficiência hídrica (-3.6%).', 'Ajuste leve no manejo pode corrigir.', -3.6);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Déficit considerável de água (-8.9%).', 'Reforce a irrigação em dias secos.', -8.9);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Baixa irrigação crítica (-14.1%).', 'Verificar pressão no sistema e uniformidade.', -14.1);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Grave: irrigação insuficiente (-19.5%).', 'Aumentar frequência urgentemente.', -19.5);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Pequeno excesso de irrigação (+2.9%).', 'Reduza o volume nos dias de menor evaporação.', 2.9);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Excesso moderado identificado (+6.8%).', 'Monitore sinais de encharcamento.', 6.8);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Volume acima do ideal (+11.9%).', 'Ajuste a rotação dos setores de irrigação.', 11.9);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (4, 'Excesso grave de água aplicado (+17.4%).', 'Rever o plano de irrigação da área.', 17.4);

INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Irrigação adequada registrada.', 'Continue seguindo o planejamento atual.', 0.0);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Leve escassez de água (-4.1%).', 'Ajustar volume aplicado nos dias mais secos.', -4.1);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Déficit médio identificado (-10.4%).', 'Verificar consumo diário e redistribuir irrigação.', -10.4);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Volume abaixo do mínimo recomendado (-13.9%).', 'Rever capacidade de irrigação do setor.', -13.9);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Crítico: irrigação insuficiente (-18.2%).', 'Pode comprometer o florescimento. Reagir rapidamente.', -18.2);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Pequeno excesso de irrigação detectado (+3.2%).', 'Ajuste de bicos ou tempo pode resolver.', 3.2);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Irrigação levemente acima (+7.6%).', 'Reduza intervalos em dias chuvosos.', 7.6);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Excesso significativo de água (+12.2%).', 'Cheque drenagem e compactação do solo.', 12.2);
INSERT INTO feedback (cultura_id, message_feedback, tips, percent) VALUES (5, 'Grave: excesso de irrigação (+19.0%).', 'Interromper irrigação por alguns dias pode ser necessário.', 19.0);
