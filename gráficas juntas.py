import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
h = 6.626e-34  # Constante de Planck (J*s)
c = 3e8        # Velocidad de la luz (m/s)
k_B = 1.381e-23 # Constante de Boltzmann (J/K)

# Definir la función de la Ley de Planck
def planck_law(wavelength, temperature):
    numerator = 2 * h * c**2
    denominator = (wavelength**5) * (np.exp((h * c) / (wavelength * k_B * temperature)) - 1)
    return numerator / denominator

# Definir la función de la Ley de Rayleigh-Jeans
def rayleigh_jeans_law(wavelength, temperature):
    return (2 * c * k_B * temperature) / (wavelength**4)

# Definir los parámetros para el cálculo
temperature = 3000  # Temperatura de estrellas
wavelengths = np.linspace(1e-9, 3e-5, 1000)  # Longitudes de onda en metros (de 1 nm a 30000 nm)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Gráfico de la Ley de Planck
intensity_planck = planck_law(wavelengths, temperature)
ax.plot(wavelengths * 1e9, intensity_planck, label=f'Planck T = {temperature} K')

# Gráfico de la Ley de Rayleigh-Jeans
intensity_rayleigh = rayleigh_jeans_law(wavelengths, temperature)
ax.plot(wavelengths * 1e9, intensity_rayleigh, label=f'Rayleigh-Jeans T = {temperature} K', linestyle='dashed')

# Ajustar los límites de los ejes para mejorar la visibilidad
ax.set_xlim([0, 30000])
ax.set_ylim([0, np.max(intensity_planck) * 1.1])  # Ajustar el límite superior del eje y

ax.set_title('Radiación de Cuerpo Negro de Estrellas')
ax.set_xlabel('Longitud de Onda (nm)')
ax.set_ylabel('Intensidad Espectral (W/m^2/nm)')
ax.legend()
ax.grid(True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
