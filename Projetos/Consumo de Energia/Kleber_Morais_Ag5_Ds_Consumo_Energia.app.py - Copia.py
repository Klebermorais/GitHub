
aparelho = input('Digite o nome do aparelho. ')
print ('Aparelho:',aparelho,)

potencia = float(input ('Digite a potência do aparelho em Watts.'))

horasDia = float(input ('Digite o tempo médio de uso diário em horas.'))

consumoMensal = (potencia * horasDia * 30) / 1000
custoEstimado = (consumoMensal * 0.75) 

print ('Aparelho:',aparelho,)
print(f'Consumo Estimado: {consumoMensal:.2f} kWh/mês')
print(f'Custo Estimado: R$ {custoEstimado:.2f}')




       



       
