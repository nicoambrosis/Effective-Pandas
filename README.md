<p align="center">
  <img src="https://github.com/nicoambrosis/Effective-Pandas/blob/main/Banners%20GitHub.jpg">
</p>

---

Este repositorio contiene material de estudio relacionado a la librería PANDAS de Python realizado a partir de tutoriales, clases y libros de [Mat Harrison](https://twitter.com/__mharrison__).

the [`glorious_function`](https://github.com/nicoambrosis/Effective-Pandas/blob/main/tweak_autos.ipynb)
```python
def tweak_autos(autos):
    
    cols =['city08', 'comb08', 'highway08', 'cylinders', 'displ', 'drive', 'eng_dscr', 'fuelCost08', 'make', 'model',
       'trany', 'range', 'createdOn', 'year']
 
    return(autos
     [cols]
     .assign(cylinders = autos.cylinders.fillna(0).astype('int8'),
             displ = autos.displ.fillna(0).astype('float16'),
             drive = autos.drive.fillna('Other').astype('category'),      # completamos los NaN con 'Other'
             automatic = autos.trany.str.contains('Auto'),                # True si es Auto False si no
             speeds = autos.trany.str.extract(r'(\d)+').fillna('20').astype('int8'), # le damos un valor cualquiera a los NaN
             createdOn = pd.to_datetime(autos.createdOn.replace({' EDT': '-04:00', ' EST' : '-05:00'}, regex = True)),
             ffs = autos.eng_dscr.str.contains('FFS')
            )
     .astype({'highway08':'int8', 'city08':'int16', 'comb08':'int16',
              'fuelCost08':'int16', 'range':'int16', 'year':'int16', 'make':'category'})
     .drop(columns = ['trany', 'eng_dscr'])                                # Eliminamos esta columna 
    )

```
---
[`background_gradient()`](https://github.com/nicoambrosis/Effective-Pandas/blob/main/background_gradient.ipynb)
```python
(autos2
 .corr()
 .style
 .background_gradient(cmap = 'RdBu', vmin = -1, vmax = 1)
 .set_sticky(axis = 'index')
)
```
