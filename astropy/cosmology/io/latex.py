import astropy
from astropy.cosmology.io.table import to_table
import astropy.cosmology.units as cu
import astropy.units as u
from astropy.cosmology.connect import readwrite_registry
from astropy.cosmology.core import Cosmology
from astropy.table import QTable
from astropy.units import def_unit
from astropy.io.ascii import write

def write_latex(cosmology, file, *, overwrite=False, cls=QTable, format=None, cosmology_in_meta=True, **kwargs):
    
    # cur_table is a Qtble
    cur_table = to_table(cosmology, cls=cls, cosmology_in_meta=cosmology_in_meta)

    for name in cosmology.__parameters__:
        if name == "H0":
            param = getattr(cosmology.__class__, name)
            new_name = param.get_format_name("$H_0 \rm{[Mpc]}$")
            cur_table.rename_column(name, new_name)
            kwargs["format"] = "ascii.latex"
            cur_table.write(file, overwrite=overwrite, **kwargs)


# Register
readwrite_registry.register_writer("latex.py", Cosmology, write_latex)
