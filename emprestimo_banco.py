housePrice = int(input("Valor da casa R$ "))
salary = int(input("Salário R$ "))
years = int(input("Anos a pagar: "))
months = years * 12
installment = housePrice / months
minimal = (salary / 100) * 30


print(f"O valor da casa dividido em {months} meses é de: {installment:.2f} por mes.")

if installment < minimal:
    print("Seu empréstimo foi aprovado.")
else:
    print(f"Seu empréstimo não foi aprovado, pois o valor das parcelas é maior que 30% do seu salário que é de {minimal}")
