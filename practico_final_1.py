# Paso 1: Definir el valor actual del Euro y Dólar con respecto al Peso Mexicano
tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

# Paso 2: Solicitar al usuario el tipo de conversión
tipo_conversion = input("Ingresa la moneda origen para la conversión (EUR/USD): ").strip().upper()

# Paso 3: Solicitar al usuario el monto a convertir
try:
    monto_a_convertir = float(input("Ingresa el monto a convertir: "))

    # Paso 4 y 5: Realizar la conversión y mostrar el resultado
    if tipo_conversion == "EUR":
        resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
        print(f"El resultado de la conversión de EUR a MXN es: {resultado:.2f}")
    elif tipo_conversion == "USD":
        resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
        print(f"El resultado de la conversión de USD a MXN es: {resultado:.2f}")
    else:
        print("No está disponible este tipo de conversión actualmente.")

except ValueError:
    print("Por favor, ingresa un número válido para el monto.")
