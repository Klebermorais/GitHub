def ler_numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("Digite um valor numerico maior ou igual a zero.")


def main():
    nome_aparelho = input("Nome do aparelho: ").strip()
    potencia = ler_numero_positivo("Potencia do aparelho (W): ")
    horas_dia = ler_numero_positivo("Tempo medio de uso diario (horas): ")

    consumo_mensal = (potencia * horas_dia * 30) / 1000
    custo_por_kwh = 0.75
    custo_estimado = consumo_mensal * custo_por_kwh

    print("\nResultado:")
    print(f"- Aparelho: {nome_aparelho}")
    print(f"- Consumo estimado: {consumo_mensal:.2f} kWh/mes")
    print(f"- Custo estimado: R$ {custo_estimado:.2f} por mes")


if __name__ == "__main__":
    main()