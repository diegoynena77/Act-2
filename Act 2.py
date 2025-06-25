class Persona:
    #Una clase es como un "molde" o un "plano" para crear objetos. En este caso, el molde es para crear objetos de tipo "Persona"
    def __init__(self, nombre, edad, peso, estatura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso  # en kilogramos
        self.estatura = estatura  # en metros
    #Este es el constructor de la clase. Se ejecuta automáticamente cada vez que creas un nuevo objeto Persona.
    #self es una referencia al objeto que se está creando
    #nombre, edad, peso, estatura son los parámetros que debes pasar cuando creas una persona, Dentro de este método, se asignan esos valores a atributos del objeto
    def calcular_imc(self):
        imc = self.peso / (self.estatura ** 2)
        return round(imc, 2)
    #def calcular_imc(self), metodo para calcular el indice de masa corporal.
    #def mostrar_info(self):muestra la informacion d ela consola
    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Estatura: {self.estatura} m")
        print(f"IMC: {self.calcular_imc()}")

        imc = self.calcular_imc()
        if imc < 18.5:
            print("→ Bajo peso")
        elif 18.5 <= imc < 25:
            print("→ Peso normal")
        elif 25 <= imc < 30:
            print("→ Sobrepeso")
        else:
            print("→ Obesidad")

    #Mostrar un resumen de la información de todas las personas registradas.
def main():
    print("👤 Registro de personas e IMC")
    personas = []

    while True:
        nombre = input("\nNombre: ")
        edad = int(input("Edad: "))
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))

        persona = Persona(nombre, edad, peso, estatura)
        personas.append(persona)

        otra = input("¿Registrar otra persona? (s/n): ").lower()
        if otra != 's':
            break

    print("\n📋 Resultados:")
    for p in personas:
        p.mostrar_info()


if __name__ == "__main__":
    main()