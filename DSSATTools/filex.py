"""
New management module
"""
from datetime import date
from .base.partypes import (
    DateType, MethodType, NumberType, Record, TabularRecord, DescriptionType,
    TableType
)
    
class Planting(Record):
    '''
    Class to define a single planting event
    '''
    prefix = "p"
    dtypes = {
        "pdate": DateType, "edate": DateType, "ppop": NumberType, 
        "ppoe": NumberType, "plme": MethodType, "plds": MethodType, 
        "plrs": NumberType, "plrd": NumberType, "pldp": NumberType, 
        "plwt": NumberType, "page": NumberType, "penv": NumberType, 
        "plph": NumberType, "sprl": NumberType, "plname": DescriptionType
    }
    pars_fmt = {
        "pdate": "%y%j", "edate": "%y%j", "ppop": ">5.1f", "plrs": ">5.0f", 
        "ppoe": ">5.1f", "plds": ">5", "plrd": ">5.0f", "plme": ">5", 
        "pldp": ">5.0f", "plwt": ">5.1f", "page": ">5.0f", "penv": ">5.1f", 
        "plph": ">5.0f", "sprl": ">5.0f", "plname": ">25"
    }
    # Typehints must be in order following DSSAT column order
    def __init__(self, pdate:date, ppop:float, plrs:float, 
                 ppoe:float=None, plds:str="R", plrd:float=0, plme:str="S", 
                 pldp:float=5, plwt:float=None, page:float=None, penv:float=None, 
                 plph:float=None, sprl:float=0, edate:date=None, plname:str=None):
        """
        Initializes a Planting instance.

        Arguments
        ----------
        pdate: datetime
            Planting date
        edate: datetime
            Emergence day
        ppop: float
            Plant population at seeding, m-2
        plrs: float
            Row spacing, cm
        plds: str
            Planting distribution, row R, broadcast B, hill H
        ppoe: float, optional
            Plant population at emergence, m-2. Equal to ppop if not set.
        plrd: float, optional
            Row direction, degrees from N
        plme: str, optional
            Planting method. Direct dry seed is default.
        pldp: float, optional
            Planting depth, cm
        plwt: float, optional. It is mandatory for Potato crop
            Planting material dry weight, kg ha-1
        page: float, optional. Mandatory when plme is Transplanting.
            Transplant age, days
        penv: float, optional.
            Transplant environment, oC
        plph: float, optional.
            Plants per hill (if appropriate)
        sprl: float, optional
            Initial sprout lenght, cm
        plname: str, optional
            Planting treatment name
        """
        super().__init__()
        kwargs = {
            "pdate": pdate, "edate": edate, "ppop": ppop, "ppoe": ppoe, 
            "plme": plme, "plds": plds, "plrs": plrs, "plrd": plrd, "pldp": pldp,
            "plwt": plwt, "page": page, "penv": penv, "plph": plph, "sprl": sprl, 
            "plname": plname
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)


class Cultivars(Record):
    prefix = "c"
    dtypes = {
        "cr": MethodType, "ingeno": DescriptionType, "cname": DescriptionType
    }
    pars_fmt = {
        "cr": ">2", "ingeno": ">6", "cname": "<16"
    }
    def __init__(self, cr:str, ingeno:str, cname:str=None):
        """
        Initializes a Cultivar instance.

        Arguments
        ----------
        cr: str
            Crop code
        ingeno: str
            Cultivar code
        cname: str
            Cultivar name
        """
        super().__init__()
        kwargs = {
            'cr': cr, 'ingeno': ingeno, 'cname': cname, 
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)


class Harvest(Record):
    prefix = "h"
    dtypes = {
        "hdate": DateType, "hstg": MethodType, "hcom": MethodType,
        "hsize": MethodType, "hpc": NumberType, "hbpc": NumberType, 
        "hname": DescriptionType
    }
    pars_fmt = {
        "hdate": "%y%j", "hstg": ">5", "hcom": ">5", "hsize": ">5", 
        "hpc": ">5.1f", "hbpc": ">5.1f", "hname": "<25"
    }
    def __init__(self, hdate:date, hstg:str=None, hcom:str=None, hsize:str=None,
                hpc:float=None, hbpc:float=None, hname:str=None):
        """
        Initializes a Harvest instance.

        Arguments
        ----------
        hdate: datetime
            Harvest date
        hstg: str 
            Specified growth stage for harvesting.
        hcom: str
            Harvest component: C (Canopy), L (Leaves), or H (Harvest product)
        hsize: str
            Harvest size category: A (All), S (Small - less than 1/3 full size),
            M (Medium - from 1/3 to 2/3 full size), L (Large - greater than 2/3 full size)
        hpc: float
            Harvest percentage, %
        hbpc: float
            Byproduct takeoff, %. This is especially applicable when, in addition
            to the grains, the straw is also harvested
        """
        super().__init__()
        kwargs = {
            "hdate": hdate, "hstg": hstg, "hcom": hcom, "hsize": hsize, 
            "hpc": hpc, "hbpc": hbpc, "hname": hname
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)


class InitialConditionsLayer(Record):
    prefix = "c"
    dtypes = {
        "icbl": NumberType, "sh2o": NumberType, "snh4": NumberType, 
        "sno3": NumberType
    }
    pars_fmt = {
        "icbl": ">4.0f", "sh2o": ">4.0f", "snh4": ">4.0f", "sno3": ">4.0f"
    }
    table_index = "icbl" # Index when buliding table
    def __init__(self, icbl:float, sh2o:float, snh4:float=None, 
                 sno3:float=None):
        """
        Initializes a initial conditions for layer instance.

        Arguments
        ----------
        icbl: float
            Depth of base layer, cm
        sh2o: float
            Volumetric water content, cm3 cm-3
        snh4: float
            Ammonioum (NH4), g[N] Mg-1[Soil]
        sno3: float
            Nitrate (NO3), g[N] Mg-1[Soil]
        """
        super().__init__()
        kwargs = {"icbl": icbl, "sh2o": sh2o, "snh4": snh4, "sno3": sno3}
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        return

class InitialConditions(TabularRecord):
    prefix = "c"
    dtypes = {
        "pcr": MethodType, "icdat": DateType, "icrt": NumberType, 
        "icnd": NumberType, "icrn": NumberType, "icre": NumberType,
        "icwd": NumberType, "icres": NumberType, "icren": NumberType,
        "icrep": NumberType, "icrip": NumberType, "icrid": NumberType,
        "icname": DescriptionType
    }
    pars_fmt = {
        "pcr": ">5", "icdat": ">5", "icrt": ">5.0f", "icnd": ">5.0f", 
        "icrn": ">5.0f", "icre": ">5.0f", "icwd": ">5.0f", "icres": ">5.0f", 
        "icren": ">5.0f", "icrep": ">5.0f", "icrip": ">5.0f", "icrid": ">5.0f",
        "icname": "<25"
    }
    table_dtype = InitialConditionsLayer
    def __init__(self, pcr:str, icdat:date=None, icrt:float=None, 
                 icnd:float=None, icrn:float=None, icre:float=None, 
                 icwd:float=None, icres:float=None, icren:float=None,
                 icrep:float=None, icrip:float=None, icrid:float=None,
                 icname:str=None, table:list[InitialConditionsLayer]=None):
        """
        Initializes a Initial conditions instance.

        Arguments
        ----------
        pcr: str
            Previous crop code
        icdat: date
            Initial conditions measurement date
        icrt: float
            Root weight, kg/ha
        icnd: float
            Nodule weight, kg/ha
        icrn: float
            Rhizobia number (0-1)
        icre: float
            Rhizobia effectivity (0-1)
        icwd: float
            Water table depth, cm
        icres: float
            Crop residue, kg/ha
        icren: float
            Residue N, %
        icrep: float
            Residue P, %
        icrip: float
            Residue incorporation, %
        icrid: float
            Residue incorporation depth, cm
        icname: str
            Initial conditions name
        table: list of InitialConditionsLayer
            List of initial conditions defined for the soil layer
        """
        super().__init__()
        kwargs = {
            "pcr": pcr, "icdat": icdat, "icrt": icrt, "icnd": icnd, 
            "icrn": icrn, "icre": icre, "icwd": icwd, "icres": icres, 
            "icren": icren, "icrep": icrep, "icrip": icrip, "icrid": icrid,
            "icname": icname
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        self.table = table
        return


class FertilizerEvent(Record):
    prefix = "f"
    dtypes = {
        "fdate": DateType, "fmcd": MethodType, "facd": MethodType, 
        "fdep": NumberType, "famn": NumberType, "famp": NumberType,
        "famk": NumberType, "famc": NumberType, "famo": NumberType,
        "focd": MethodType, "fername": DescriptionType
    }
    pars_fmt = {
        "fdate": "%y%j", "fmcd": ">5", "facd": ">5", "fdep": ">5.0f", 
        "famn": ">5.1f", "famp": ">5.1f", "famk": ">5.1f", "famc": ">5.1f",
        "famo": ">5.1f", "focd": ">5", "fername": "<16"
    }
    table_index = "fdate" # Index when buliding table
    def __init__(self, fdate:date, fmcd:str, facd:str, fdep:float, famn:float, 
                 famp:float, famk:float=None, famc:float=None, famo:float=None,
                 focd:str=None, fername:str=None):
        """
        Initializes a fertilizer application.

        Arguments
        ----------
        fdate: date
            Fertilizer application date
        fcmd: str
            Fertilizer material code
        facd: str
            Fertilizer application method
        fdep: float
            application depth, cm
        famn: float
            N amount, kg ha-1
        famp: float
            P amount, kg ha-1
        famk: float
            K amount, kg ha-1
        famc: float
            Ca amount, kg ha-1
        famo: float
            Other elements, kg ha-1
        focd: str
            Other element code
        fername: str
            Description
        """
        super().__init__()
        kwargs = {
            "fdate": fdate, "fmcd": fmcd, "facd": facd, "fdep": fdep, 
            "famn": famn, "famp": famp, "famk": famk, "famc": famc, 
            "famo": famo, "focd": focd, "fername": fername
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        return

class Fertilizer(TabularRecord):
    prefix = "c"
    dtypes = {}
    pars_fmt = {}
    table_dtype = FertilizerEvent
    def __init__(self, table=list[FertilizerEvent]):
        """
        Initializes a fertilizer section. It is formed by 

        Arguments
         ----------
        table: list of FertilizerEvent
            Fertilizer events
        """
        super().__init__()
        self.table = table


class SoilAnalysisLayer(Record):
    prefix = "a"
    dtypes = {
        "sabl": NumberType, "sadm": NumberType, "saoc": NumberType, 
        "sani": NumberType, "saphw": NumberType, "saphb": NumberType,
        "sapx": NumberType, "sake": NumberType, "sasc": NumberType
    }
    pars_fmt = {
        "sabl": ">4.0f", "sadm": ">5.1f", "saoc": ">5.2f", "sani": ">5.2f",
        "saphw": ">5.1f", "saphb": ">5.1f", "sapx": ">5.1f", "sake": ">5.1f",
        "sasc": ">5.2f"
    }
    table_index = "sabl" # Index when buliding table
    def __init__(self, sabl:float, sadm:float=None, saoc:float=None, 
                 sani:float=None, saphw:float=None, saphb:float=None,
                 sapx:float=None, sake:float=None, sasc:float=None):
        """
        Initializes a soil analysis for layer instance.

        Arguments
        ----------
        sabl: float
            Depth of base layer, cm
        sadm: float
            Bulk density, moist, g cm-3
        saoc: float
            Organic carbon, %
        sani: float
            Total nitrogen, %
        saphw: float
            pH in water
        saphb: float
            pH in buffer
        sapx: float
            Phosphorus extractable, mg kg-1
        sake: float
            Potassium exchangeable, cmol kg-1
        sasc: float
            Stable organic carbon, %
        """
        super().__init__()
        kwargs = {"sabl": sabl, "sadm": sadm, "saoc": saoc, "sani": sani,
                  "saphw": saphw, "saphb": saphb, "sapx": sapx, "sake": sake,
                  "sasc": sasc}
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        return

class SoilAnalysis(TabularRecord):
    prefix = "a"
    dtypes = {
        "sadat": DateType, "smhb": MethodType, "smpx": MethodType, 
        "smke": MethodType, "saname": DescriptionType
    }
    pars_fmt = {
        "sadat": ">5", "smhb": ">5", "smpx": ">5", "smke": ">5", 
        "saname": "<16"
    }
    table_dtype = SoilAnalysisLayer
    def __init__(self, sadat:date, table:list[SoilAnalysisLayer],
                smhb:str=None, smpx:str=None, smke:str=None, saname:str=None):
        """
        Initializes a soil analysis instance.

        Arguments
        ----------
        sadat: date
            Soil Analysis date
        table: list
            List of SoilAnalysisLayer instances
        smhb: str
            pH in buffer determination method
        smpx: str
            Phosphorus determination method
        smke: str
            Potassium determination method
        saname: str
            Soil Analysis name
        """
        super().__init__()
        kwargs = {
            "sadat": sadat, "smhb": smhb, "smpx": smpx, "smke": smke, 
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        self.table = table


class IrrigationEvent(Record):
    prefix = "i"
    dtypes = {
        "idate": DateType, "irop": MethodType, "irval": NumberType, 
    }
    pars_fmt = {
        "idate": ">5", "irop": ">5", "irval": ">5.1f"
    }
    table_index = "idate" # Index when buliding table
    def __init__(self, idate:date, irval:float, irop:str=None):
        """
        Initializes a irrigation event instance.

        Arguments
        ----------
        idate: date
            Irrigation date
        irval: float
            Irrigation amount, mm
        irop: str
            Operation method
        """
        super().__init__()
        kwargs = {"idate": idate, "irop": irop, "irval": irval}
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        return

class Irrigation(TabularRecord):
    prefix = "i"
    dtypes = {
        "efir": NumberType, "idep": NumberType, "ithr": NumberType,
        "iept": NumberType, "ioff": MethodType, "iame": MethodType,
        "iamt": NumberType, "irname": DescriptionType
    }
    pars_fmt = {
        "efir": ">5.2f", "idep": ">5.1f", "ithr": ">5.1f", "iept": ">5.1f",
        "ioff": ">5", "iame": ">5", "iamt": ">5.1f", "irname": "<16"
    }
    table_dtype = IrrigationEvent
    def __init__(self, table=list[IrrigationEvent], efir:float=1,
                    idep:float=None, ithr:float=None, iept:float=None,
                    ioff:str=None, iame:str=None, iamt:float=None, 
                    irname:str=None):
        """
        Initializes a Irrigation instance.

        Arguments
        ----------
        table: list
            List of IrrigationEvent
        efir: float
            Irrigation efficiency, 0-1
        idep: float
            Management depth for automatic application, cm
        ithr: float
            Threshold for automatic appl., % of max. available
        iept: float
            End point for automatic appl., % of max. available
        ioff: str
            End of automatic applications, growth stage
        iame: str
            Method for automatic applications, code
        iamt: float
            Amount per automatic irrigation if fixed, mm
        irname: str
            Irrigation treatment name
        """
        super().__init__()
        kwargs = {
            "efir": efir, "idep": idep, "ithr": ithr, "iept": iept,
            "ioff": ioff, "iame": iame, "iamt": iamt, 
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)
        self.table = table


class ResidueEvent(Record):
    prefix = "r"
    dtypes = {
        "rdate": DateType, "rcod": MethodType, "ramt": NumberType,
        "resn": NumberType, "resp": NumberType, "resk": NumberType,
        "rinp": NumberType, "rdep": NumberType, "rmet": MethodType,
        "rename": DescriptionType
    }
    pars_fmt = {
        "rdate": ">5", "rcod": ">5", "ramt": ">5.0f", "resn": ">5.2f",
        "resp": ">5.2f", "resk": ">5.2f", "rinp": ">5.0f", "rdep": ">5.0f",
        "rmet": ">5", "rename": "<16"
    }
    table_index = "rdate" # Index when buliding table
    def __init__(self, rdate:date, rcod:str, ramt:float, resn:float,
                 resp:float, resk:float, rinp:float, rdep:float, rmet:str,
                 rename:str=None):
        """
        Initializes a residue application.

        Arguments
        ----------
        rdate: date
            Residue application date
        rcod: str
            Residue material, code
        ramt: float
            Residue amount, kg ha-1
        resn: float
            Residue nitrogen concentration, %
        resp: float
            Residue phosph. concentration, %
        resk: float
            Residue potassium concentration, %
        rinp: float
            Residue incorporation, %
        rdep: float
            Incorporation depth, cm
        rmet: str
            Method of incorporation, code
        rename: str
            Description
        """
        super().__init__()
        kwargs = {
            "rdate": rdate, "rcod": rcod, "ramt": ramt, "resn": resn,
            "resp": resp, "resk": resk, "rinp": rinp, "rdep": rdep,
            "rmet": rmet, "rename": rename
        }
        for name, value in kwargs.items():
            super().__setitem__(name, value)

class Residue(TabularRecord):
    prefix = "r"
    dtypes = {}
    pars_fmt = {}
    table_dtype = ResidueEvent
    def __init__(self, table=list[ResidueEvent]):
        """
        Initializes a residue section. 

        Arguments
         ----------
        table: list of ResidueEvent
            Residue application events
        """
        super().__init__()
        self.table = table
    

class ChemicalsEvent(Record):
    def __init__(self):
        return
    
class Chemicals(TabularRecord):
    def __init__(self):
        return
    
class Tillage(TabularRecord):
    def __init__(self):
        return

def get_header_range(l, h, pars_fmt):
    """Get variable start and index in the header line"""
    h_fmt = pars_fmt[h]
    if h_fmt[0] == "<":
        start = l.lower().find(h)
        end = start + int(h_fmt[1:].split(".")[0])
    elif h_fmt[0] == ">":
        end = l.lower().find(h) + len(h)
        start = end - int(h_fmt[1:].split(".")[0])
    elif h_fmt[0] == "%":
        start = l.lower().find(h)
        end = start + 5 # Assuming all dates in FileX are a 5 character string
    else:
        raise ValueError("Variable format must be right or left justified")
    return (start, end)

def read_filex(filexpath):
    """
    Asumptions:
    Some of the assumptions are needed to deal with description fields 
    that can contain spaces, such as Cultivar name.
    - Values are below their header
    - Each column/header must be right or left justified
    - Treament number is always the first column
    - Treatment number is on the first two spaces
    """
    with open(filexpath, "r") as f:
        lines = f.readlines()
    lookup = "section"
    vals_dict = {}
    table_values = []
    experiment = {}
    for l in lines:
        l = l.replace("\n", "")
        if len(l.strip()) == 0:
            if lookup == "table values":
                if only_table:
                    for level, val in vals.items():
                        vals_dict[level] = cls(table= val)
                else:
                    vals["table"] = table_values
                    vals_dict[level] = cls(**vals)
                experiment[cls.__name__] = vals_dict
                vals_dict = {}
                table_values = []
                del level
            if lookup == "values":
                experiment[cls.__name__] = vals_dict
                vals_dict = {}
                del level
            lookup = "section"
            continue 
        elif lookup == "header":
            if l[0] == "@":
                header = l.lower().split()
                header_start_end = {
                    h: get_header_range(l, h, cls.pars_fmt) 
                    for h in header[1:]
                }
                lookup = "values"
                continue
        elif lookup == "table header":
            if l[0] == "@":
                table_header = l.lower().split()
                table_header_start_end = {
                    h: get_header_range(l, h, cls.table_dtype.pars_fmt) 
                    for h in table_header[1:]
                }
                lookup = "table values"
                continue
        elif lookup == "values":
            vals = {
                key: l[header_start_end[key][0]:header_start_end[key][1]]
                for key in header[1:]
            }
            level = int(l[:2])
            if hasattr(cls, "table_dtype"):
                lookup = "table header"
            else:
                vals_dict[level] = cls(**vals)
            continue
        elif lookup == "table values":
            if l[0] == "@":
                vals["table"] = table_values
                vals_dict[level] = cls(**vals)
                table_values = []
                lookup = "values"
                del level
                continue
            row = cls.table_dtype(**{
                key: l[table_header_start_end[key][0]:
                       table_header_start_end[key][1]]
                for key in table_header[1:]
            })
            if only_table:
                level = int(l[:2])
                vals[level] = vals.get(level, []) + [row]
            table_values.append(row)
        elif lookup == "section":
            if l[:6] == "*PLANT":
                cls = Planting
            elif l[:6] == "*CULTI":
                cls = Cultivars
            elif l[:6] == "*HARVE":
                cls = Harvest
            elif l[:6] == "*INITI":
                cls = InitialConditions
            elif l[:6] == "*FERTI":
                cls = Fertilizer
            elif l[:6] == "*SOIL ":
                cls = SoilAnalysis
            elif l[:6] == "*IRRIG":
                cls = Irrigation
            elif l[:6] == "*RESID":
                cls = Residue
            else:
                continue
            # Some sections are only tables, for those go directly to table
            # header
            only_table = len(cls.dtypes) == 0
            if only_table:
                lookup = "table header"
                vals = {}
            else:
                lookup = "header"
        else:
            raise ValueError
    return
    