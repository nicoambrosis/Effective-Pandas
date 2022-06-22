#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

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

