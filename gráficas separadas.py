import numpy as np
import matplotlib.pyplot as plt

#constantes físicas
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
temperatures = [3000]  #(temperatura de estrellas)
wavelengths = np.linspace(1e-7, 3e-6, 1000)  # Longitudes de onda en metros (de 1 nm a 3000 nm)

# Crear el gráfico
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Gráfico de la Ley de Planck
for T in temperatures:
    intensity_planck = planck_law(wavelengths, T)
    ax1.plot(wavelengths, intensity_planck, label=f'T = {T} K')

ax1.set_title('Radiación de Cuerpo Negro de Estrellas según la Ley de Planck')
ax1.set_xlabel('Longitud de Onda (nm)')
ax1.set_ylabel('Intensidad Espectral (W/m^2/nm)')
ax1.legend()
ax1.grid(True)
#ax1.set_yscale('log')  # Escala logarítmica para la intensidad

# Gráfico de la Ley de Rayleigh-Jeans
for T in temperatures:
    intensity_rayleigh = rayleigh_jeans_law(wavelengths, T)
    ax2.plot(wavelengths, intensity_rayleigh, label=f'T = {T} K')

ax2.set_title('Radiación de Cuerpo Negro de Estrellas según la Ley de Rayleigh-Jeans')
ax2.set_xlabel('Longitud de Onda (nm)')
ax2.set_ylabel('Intensidad Espectral (W/m^2/nm)')
ax2.legend()
ax2.grid(True)
#ax2.set_yscale('log')  # Escala logarítmica para la intensidad

# Mostrar el gráfico
plt.tight_layout()
plt.show()