# Calculadora de Consumo de Energia

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-repositorio-181717?logo=github&logoColor=white)](https://github.com/)
[![Energia](https://img.shields.io/badge/Energia-consumo%20el%C3%A9trico-F5A623)](#)

## Objetivo

Este sistema calcula o consumo mensal estimado de um aparelho elétrico a partir do nome, da potência em watts e do tempo médio de uso diário.

O resultado mostra o consumo em kWh por mês e uma estimativa de custo baseada no valor fixo de R$ 0,75 por kWh.

## Tecnologia

- Linguagem: Python 3
- Execução: terminal ou prompt de comando
- Unidade de consumo: kWh/mês

## Fórmula

```text
consumoMensal = (potencia * horasDia * 30) / 1000
```

O custo estimado é calculado assim:

```text
custoEstimado = consumoMensal * 0,75
```

## Como executar

1. Abra um terminal na pasta `projetos/consumo-energia`.
2. Execute:

```bash
python app.py
```

3. Informe o aparelho, a potência em watts e as horas de uso diário.