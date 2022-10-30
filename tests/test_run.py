import pytest

from DSSATTools import (
    Crop, SoilProfile, WeatherData, WeatherStation,
    Management, DSSAT
    )
from DSSATTools.base.sections import TabularSubsection
from datetime import datetime
import pandas as pd
import numpy as np
import os

DATES = pd.date_range('2000-01-01', '2002-12-31')
N = len(DATES)
df = pd.DataFrame(
    {
    'tn': np.random.gamma(24, 1, N),
    'rad': np.random.gamma(15, 1.5, N),
    'prec': np.round(np.random.gamma(.4, 10, N), 1),
    'rh': 100 * np.random.beta(1.5, 1.15, N),
    },
    index=DATES,
)
df['TMAX'] = df.tn + np.random.gamma(5., .5, N)
# Create a WeatherData instance
WTH_DATA = WeatherData(
    df,
    variables={
        'tn': 'TMIN', 'TMAX': 'TMAX',
        'prec': 'RAIN', 'rad': 'SRAD',
        'rh': 'RHUM'
    }
)
# Create a WheaterStation instance
wth = WeatherStation(
    WTH_DATA, 
    {'ELEV': 33, 'LAT': 0, 'LON': 0, 'INSI': 'dpoes'}
)

soil = SoilProfile(default_class='SIL')

def test_no_setup():
    with pytest.raises(AssertionError) as excinfo:
        assert 'setup() method' in str(excinfo.value)

def test_run_maize():
    crop = Crop('maize')
    man = Management(
        cultivar='IB0001',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_mz')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_millet():
    soil = SoilProfile(default_class='SIL')
    crop = Crop('millet')
    man = Management(
        cultivar='999991',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_ml')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_sugarbeet():
    crop = Crop('sugarbeet')
    man = Management(
        cultivar='CR0001',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_bs')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_rice():
    crop = Crop('rice')
    man = Management(
        cultivar='IB0003',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_ri')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_sorghum():
    crop = Crop('sorghum')
    man = Management(
        cultivar='IB0001',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_sg')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_sweetcorn():
    crop = Crop('sweetcorn')
    man = Management(
        cultivar='SW0001',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_sw')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_alfalfa():
    crop = Crop('alfalfa')
    man = Management(
        cultivar='AL0001',
        planting_date=DATES[10],
    )
    man.mow['table'] = TabularSubsection({
        'DATE': [DATES[300].strftime('%y%j'), DATES[340].strftime('%y%j')], 
        'MOW': [1000, 1000], 'RSPLF': [20, 20], 'MVS': [2, 2], 'RSHT': [5, 5]
    })
    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_al')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_bermudagrass():
    crop = Crop('bermudagrass')
    man = Management(
        cultivar='UF0001',
        planting_date=DATES[10],
    )
    man.mow['table'] = TabularSubsection({
        'DATE': [DATES[300].strftime('%y%j'), DATES[340].strftime('%y%j')], 
        'MOW': [1000, 1000], 'RSPLF': [20, 20], 'MVS': [2, 2], 'RSHT': [5, 5]
    })
    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_bm')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
    # dssat.close()
    # assert not os.path.exists(dssat._RUN_PATH)

def test_run_soybean():
    crop = Crop('soybean')
    man = Management(
        cultivar='IB0011',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_sb')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))

def test_run_canola():
    crop = Crop('canola')
    man = Management(
        cultivar='CA0001',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_cn')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))

def test_run_sunflower():
    crop = Crop('sunflower')
    man = Management(
        cultivar='IB0009',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_su')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))


def test_run_potato():
    crop = Crop('potato')
    man = Management(
        cultivar='IB0001',
        planting_date=DATES[10],
    )

    dssat = DSSAT()
    dssat.setup(cwd='/tmp/test_su')
    dssat.run(
        soil=soil, weather=wth, crop=crop, management=man,
    )
    assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))


if __name__ == '__main__':
    test_run_alfalfa()